// 用真实 Chrome 打开页面并读出「人眼能看到的文本」。
// 静态抓 HTML 时，很多品牌页的内容是前端渲染的（Next.js / Contentful），
// 直接搜标签只会得到一堆假阴性。
//
// 用法: node render_text.js <outJson> <url1> <url2> ...
const fs = require('fs');
const PORT = 9222;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

class CDP {
  constructor(ws) {
    this.ws = ws; this.id = 0; this.pending = new Map(); this.events = [];
    ws.addEventListener('message', (ev) => {
      const m = JSON.parse(ev.data);
      if (m.id && this.pending.has(m.id)) {
        const { resolve, reject } = this.pending.get(m.id);
        this.pending.delete(m.id);
        m.error ? reject(new Error(JSON.stringify(m.error))) : resolve(m.result);
      } else if (m.method) this.events.push(m);
    });
  }
  send(method, params = {}, sessionId) {
    const id = ++this.id; const p = { id, method, params };
    if (sessionId) p.sessionId = sessionId;
    this.ws.send(JSON.stringify(p));
    return new Promise((res, rej) => {
      this.pending.set(id, { resolve: res, reject: rej });
      setTimeout(() => { if (this.pending.has(id)) { this.pending.delete(id); rej(new Error('timeout ' + method)); } }, 60000);
    });
  }
  waitEvent(m, t = 45000) {
    const d = Date.now() + t;
    return new Promise((res, rej) => {
      const tick = () => {
        const i = this.events.findIndex((e) => e.method === m);
        if (i >= 0) return res(this.events.splice(i, 1)[0]);
        if (Date.now() > d) return rej(new Error('timeout ' + m));
        setTimeout(tick, 150);
      };
      tick();
    });
  }
}

async function connect() {
  const info = await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json();
  const ws = new WebSocket(info.webSocketDebuggerUrl);
  await new Promise((res, rej) => { ws.addEventListener('open', res); ws.addEventListener('error', rej); });
  return new CDP(ws);
}

(async () => {
  const out = process.argv[2];
  const urls = process.argv.slice(3);
  if (!urls.length) { console.error('no urls'); process.exit(1); }
  const cdp = await connect();
  const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
  await cdp.send('Page.enable', {}, sessionId);
  await cdp.send('Runtime.enable', {}, sessionId);
  await cdp.send('Network.enable', {}, sessionId);

  const result = {};
  for (const url of urls) {
    cdp.events.length = 0;
    try {
      await cdp.send('Page.navigate', { url }, sessionId);
      await cdp.waitEvent('Page.loadEventFired', 45000);
    } catch (e) { /* 继续，用下面的轮询兜底 */ }
    // 等文本长度稳定：SPA 会在 hydrate 之后再塞内容
    let prev = -1, stable = 0;
    for (let i = 0; i < 30; i++) {
      await sleep(700);
      const len = await cdp.send('Runtime.evaluate', {
        expression: 'document.body ? document.body.innerText.length : 0',
        returnByValue: true,
      }, sessionId).then((r) => r.result.value).catch(() => 0);
      if (len === prev && len > 0) { stable++; if (stable >= 3) break; } else stable = 0;
      prev = len;
    }
    const text = await cdp.send('Runtime.evaluate', {
      expression: 'document.body ? document.body.innerText : ""',
      returnByValue: true,
    }, sessionId).then((r) => r.result.value).catch(() => '');
    result[url] = { chars: text.length, text };
    console.log(`${String(text.length).padStart(7)} chars  ${url}`);
  }
  fs.writeFileSync(out, JSON.stringify(result, null, 1), 'utf8');
  await cdp.send('Target.closeTarget', { targetId }).catch(() => {});
  process.exit(0);
})().catch((e) => { console.error('FATAL ' + e.message); process.exit(1); });
