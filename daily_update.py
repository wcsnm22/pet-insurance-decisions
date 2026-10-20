#!/usr/bin/env python3
"""每天一次：核对来源页 → 重建 → 自检 → 部署 → 线上复核。

规则：
  1. 核对只把 checked 推到「今天真的读过、而且内容和上次一样」的来源页。
  2. 有任何来源页内容变了 → 停下来不部署，等人看过。自动把变了的事实连同旧文案
     一起发出去，等于把过时信息当新鲜信息卖。
  3. 自检不过 → 不部署。宁可今天不发，也不发一个坏页面。
  4. 站点内容跟上次部署时一模一样 → 不部署，不制造空部署。
     判断依据是 site/ 的指纹，不是「今天推进了几条日期」—— 后者在同一天里
     第二次跑时天然是 0，会造成「改好了却没发出去」。
  5. 部署后线上抽检，抽检不过就当失败报出来。

退出码：0 = 正常（含「无需部署」）；1 = 需要人处理（来源变了/自检失败/部署失败）。
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent
PY = sys.executable
WRANGLER = Path(os.environ["APPDATA"]) / "npm" / "wrangler.cmd"
ACCOUNT_ID = "a42087cd60e437c858761af03941e415"
PROJECT = "furwell"
BASE_URL = "https://furadvisor.com"
LOG = ROOT / "docs" / "daily-update.log"
STAMP = ROOT / "docs" / ".last_deploy_fingerprint"
SITE = ROOT / "site"

SPOT_CHECK = [
    "/",
    "/pet-insurance-cost",
    "/pet-insurance-waiting-periods",
    "/lemonade-cat-insurance",
    "/sitemap.xml",
]


def log(msg):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    # 控制台是 GBK，来源页文案里可能出现 GBK 编不出的字符。写日志不能因此中断：
    # 控制台把编不出的字符替换掉，日志文件按 UTF-8 原样写。
    try:
        print(line, flush=True)
    except UnicodeEncodeError:
        enc = sys.stdout.encoding or "utf-8"
        print(line.encode(enc, "replace").decode(enc, "replace"), flush=True)
    LOG.parent.mkdir(exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(cmd, env=None):
    log(f"$ {' '.join(str(c) for c in cmd)}")
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    out = ((p.stdout or "") + (p.stderr or "")).strip()
    for ln in out.splitlines()[-40:]:
        log(f"  | {ln}")
    return p.returncode, out


def site_fingerprint():
    """site/ 下所有文件的相对路径 + 内容哈希，顺序无关。"""
    h = hashlib.sha256()
    for p in sorted(SITE.rglob("*")):
        if p.is_file():
            h.update(p.relative_to(SITE).as_posix().encode("utf-8"))
            h.update(hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()[:16]


def parse_stat(out, key):
    for ln in out.splitlines():
        if ln.strip().startswith("STAT "):
            for tok in ln.split():
                if tok.startswith(key + "="):
                    try:
                        return int(tok.split("=", 1)[1])
                    except ValueError:
                        return 0
    return 0


def main():
    log("=" * 70)
    log("daily update start")

    # 1) 核对来源页；确认没变的那些，checked 推到今天
    code, out = run([PY, "daily_verify.py", "--apply"])
    if code != 0:
        log("ABORT: 有来源页内容变了或抓取异常，未部署。")
        log("       逐条看上面的 CHANGED 行，人工核对后用 "
            "`python daily_verify.py --apply --force` 推进。")
        return 1
    n_sources = parse_stat(out, "sources")
    n_ok = parse_stat(out, "fetch_ok")
    n_changed = parse_stat(out, "changed")
    n_applied = parse_stat(out, "applied")
    log(f"verify: sources={n_sources} fetch_ok={n_ok} changed={n_changed} applied={n_applied}")

    # 2) 重建
    code, _ = run([PY, "build.py"])
    if code != 0:
        log("ABORT: 构建失败，未部署。")
        return 1

    # 3) 自检；不过就不发
    code, out = run([PY, "selfcheck.py"])
    if code != 0 or "RESULT: PASS" not in out:
        log("ABORT: 自检未通过，未部署。")
        return 1
    log("selfcheck PASS")

    # 4) 站点没变就不部署
    fp = site_fingerprint()
    prev = STAMP.read_text(encoding="utf-8").strip() if STAMP.exists() else ""
    if fp == prev:
        log(f"SKIP DEPLOY: 站点指纹与上次部署相同（{fp}），没有可发的内容。")
        return 0
    log(f"site fingerprint {prev or '(none)'} -> {fp}")

    # 5) 本地留痕（push 仍坏着，只做本地提交）
    today = datetime.now().strftime("%Y-%m-%d")
    run(["git", "add", "-A"])
    code, out = run(["git", "commit", "-q", "-m",
                     f"daily: re-verify {n_ok}/{n_sources} sources on {today}"])
    if code != 0 and "nothing to commit" not in out:
        log("note: git commit 没成功，继续部署（部署不依赖提交）")

    # 6) 部署
    env = dict(os.environ, CLOUDFLARE_ACCOUNT_ID=ACCOUNT_ID)
    code, out = run([str(WRANGLER), "pages", "deploy", "site",
                     f"--project-name={PROJECT}", "--branch=main",
                     "--commit-dirty=true"], env=env)
    if code != 0:
        log("ABORT: 部署失败。")
        return 1

    # 7) 线上抽检。首次部署后边缘可能短暂 404/旧版，给 3 分钟重试窗口
    deadline = time.time() + 180
    failures = []
    for path in SPOT_CHECK:
        url = BASE_URL + path
        ok = False
        while time.time() < deadline:
            try:
                r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
                if r.status_code == 200 and (path != "/" or today in r.text):
                    log(f"  live {path}: 200 {len(r.content)}B")
                    ok = True
                    break
                log(f"  live {path}: {r.status_code}"
                    + ("（首页还没出现今天的日期，等边缘刷新）" if r.status_code == 200 else "")
                    + "，重试")
            except Exception as e:  # noqa: BLE001
                log(f"  live {path}: {type(e).__name__}，重试")
            time.sleep(10)
        if not ok:
            failures.append(path)

    if failures:
        log(f"DEPLOYED BUT NOT VERIFIED: {failures}（部署成功但线上没确认到，请手动看）")
        return 1

    STAMP.write_text(fp, encoding="utf-8")
    log("daily update done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
