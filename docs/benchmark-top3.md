# BENCHMARK-TOP3：缺口总排行（DAILY 每天从这里拿选题）

- **对标三家（@TOP3，2026-09-28 新命令锁定，28 天内不换）**：`geico.com` / `aspcapetinsurance.com` / `allstate.com`
- **核心词（@KEYWORD，不换）**：`pet insurance`
- **单站 10 页明细**：`docs/bench-geico.md`、`docs/bench-aspcapetinsurance.md`、`docs/bench-allstate.md`（各含「一、对标表 10 页 / 二、缺口 / 三、纪律声明」）
- **生成日期**：2026-09-28；三家均为**导流型**（GEICO→Embrace、Allstate→Embrace/Ivantage、ASPCA→Crum & Forster 自营），**0 张可比价格表**是三家共同结构位。
- **用途**：每天一篇 = 本表从上往下取第一个**未发布**的缺口，一篇一个缺口，不重、不并。

---

## A. 缺口排行（三家都没有 / 谁有谁没有标注清楚）

| # | 缺口（页面主题） | 三家各自的状况 | 独家料从哪取 | 状态 |
|---|---|---|---|---|
| N1 | **按疾病类型的等待期明细表**（意外 / 疾病 / 骨科 / 癌症 / 十字韧带 各多久，逐家） | GEICO：4 处提及但结论是"问 agent"，**零天数**；ASPCA：有"Waiting Period Health Assessment"落地页但要走评估；Allstate：仅一句"疾病等待期 2 周、因州而异" | 各家公开条款/SPD 逐条抄录（条款是公开原文，**标注条款版本与生效日**），不做任何推算 | 已发 + 2026-09-29 + https://furadvisor.com/pet-insurance-waiting-periods-by-condition （G2 已发的是"等待期是什么+我站口径"，**不是**逐家逐疾病天数表 → 不算重复，是 G2 的深化） |
| N2 | **同一只宠 3–5 家的真实报价对比表**（同品种/同年龄/同邮编，四列并排：保费·免赔·报销比·限额） | GEICO：狗 $35–65、猫 $15–45 两个口头区间，无拆分；ASPCA：价格锁在留资后，只有"低至 $X"；Allstate：狗 $20–70、猫 $10–30 + 6 行"from"示例（Embrace 口径） | 我方**自己跑报价**（同一宠物档案、同一邮编、公开截图口径与日期），输出分布而非区间 | 未发（#4 cost by brand 是"各家官方价目页"口径，非我方实跑报价 → 不同料） |
| N3 | **理赔真相层**：到账时效分布 / 常见拒赔理由 / 申诉路径 / 有无直付 | GEICO：只讲"按比例报销、$5,000 限额打满不再赔"，无时效无拒赔；ASPCA：只有"一般 30 天内"+4 步+3 个 2021 挑选案例；Allstate：FAQ 只到"按比例报销"为止 | 各家客服**实测提问并记录公开口径与日期**（不代答、不推断）+ 我方已发申诉页延伸 | 未发（`/pet-insurance-claim-denied` 已发申诉流程，**时效分布/拒赔理由清单/直付有无**是它没写的） |
| N4 | **"值不值"量化模型**（保费 vs 自付期望值 / breakeven / 涨价轨迹） | 三家每页都有 "Is it worth it" / "worth it" 却全定性；ASPCA 数据停在 2016/2017 NAPHIA；Allstate 成本文全是二手媒体区间无一手数据 | 我方用 N2 的实跑报价 + 自采兽医收费数据算，**公式与口径公开** | 未发（我站**没有**"值不值"页——已核 `site/*.html` 13 页里无同名/同意图页；`pet-insurance-cost` 只讲价格不讲期望值 → 本条是全新题） |
| N5 | **州级可用性与州级差异解读**（哪些州有/没有、同保单在不同州差在哪） | GEICO：完全无；ASPCA：**有** 51 州 × 4 样本保单、9 州披露文件、7 州等待期评估——但只当文件仓库、不解释；Allstate：无州清单（一句"因州而异"） | ASPCA 公开的州文件（披露原文，非我方编造）+ 各州 DOI 公开备案 | 未发（我站 13 页里**没有任何州页**——`pet-insurance-cost-by-state`、`best-pet-insurance-california` 均不存在，2026-09-28 已核；**50 州是整块空白长尾池，一篇一州或按区**） |
| N6 | **条款级承保矩阵**（保 / 不保 / 可加购 三栏 × 5 家，拉平对照） | GEICO：只有"不保清单"类别，无跨家区分；ASPCA：有 `whats-covered` 单家页；Allstate：列了 8 条覆盖 + 6 条不保（含 DNA 检测），**单家** | 各家公开条款原文逐条核验，**每格带 source_url + 复核日期** | 未发 |
| N7 | **品种 × 高发病 × 核保态度矩阵**（金毛/法斗/德牧… 加费还是拒保） | GEICO：零覆盖（导流方无核保数据）；Allstate：**有** cane-corso 品种页（寿命/常见病/末段接保险 CTA），但**不给该品种保费相对水平、不给哪些公司加费**；ASPCA：无 | 各家公开条款 breed exclusion + AKC/OFA 高发病种 + 我方实测问询 | 未发（Allstate cane-corso 是可学结构：**品种 SEO → 导流**，我方补上"保费影响"这一它不写的列） |
| N8 | **wellness 各档年度额度与"划算线"**（疫苗/体检单项在 保险 vs 自付 vs wellness 三种路径下的成本对比） | GEICO：只说"wellness 可选"；ASPCA：有 wellness 页但无年度额度表；Allstate：`vet-visits` 页讲三档层级，**无各档年度额度数字** | 我方采集的疫苗/体检/绝育/洗牙单项价格 × 是否可报 × 各家 wellness 年度额度 → 算"买 wellness 的划算线" | 未发（G3 wellness add-on 已发"是什么+怎么选" → **本条是"额度数字+划算线"，不同料**） |
| N9 | **急诊场景决策页**：热射病 / 误食防冻液 / 骨折 —— 算意外还是算疾病？（决定等待期与能否赔） | GEICO：`summer-pet-safety` 讲中暑处理**不讲可否赔**、`pet-winter` 讲防冻不讲误食；Allstate：`emergencies` 只给"3 类通常赔"，无费用量级无直付；ASPCA：无专题页 | 各家条款"意外 vs 疾病"定义逐条核验 + 我方自采急诊价目区间 | 未发 |
| N10 | **新宠时间线页**（0–8 周做什么 / 投保窗口 / 等待期怎么卡时间） | GEICO：`10-ways-to-prep` 第 8 条"选兽医"**不提费用与投保窗口**；ASPCA：无；Allstate：FAQ 提"最佳投保年龄 6–8 周"但无时间线 | 我方已发的 G2 等待期 + G4 索赔时限 + 各家投保年龄线实测 | 未发 |
| N11 | **组合决策页：租客险 + 宠物险**（该买什么组合、花多少） | GEICO：`does-renters-cover-dogs` 有"Pet Insurance vs. Renters Insurance"**正文小节**，但不给组合方案与成本；ASPCA：无；Allstate：无 | 各州租客险均价（公开数据）× 犬种限责情况 × 宠物险加费 | 未发 |
| N12 | **异宠保险**（兔子 / 蜥蜴 / 鸟 是否保、多少钱） | 三家全无（Allstate 异宠 wellness 仅一句"一般不保"）；GEICO cost-to-own 页倒是有**异宠养宠成本**（寄居蟹 $80+$180/年、豹纹守宫 $149+$290/年、鸟 $295+$185/年） | 各家公开条款"是否承保异宠"逐家核验 + GEICO 的异宠养宠成本可作**需求侧背景**（数字仅用于描述对方，引用须回源） | 已发 + 2026-09-30 + https://furadvisor.com/exotic-pet-insurance |


> **2026-09-30 补记（推进器）**：DAILY 当日 09:00 的 N2 实跑报价尝试以 `RuntimeError: Response truncated due to output length limit` 失败（09:55），daily-log 当日为空，故推进器按退路改发 **N12 异宠**（今日唯一一篇，已上线）。**N2 仍是 A 段第一个未发缺口**，明天 DAILY 继续从 N2 起；N2 需要我方自己跑 3–5 家报价，报价流通常在出价前索要姓名/邮箱/电话——写稿时如遇此墙，先做不需真人信息的部分，拿不到就按 NOFAKE 写「官方需留资后出价」，不许编报价。

---

## B. 已发布选题（**这些不要再写** —— 共 13 页，与 `docs/daily-log.md` 的 P1 行一致，已核磁盘）

`fetch-pet-insurance` ｜ `lemonade-pet-insurance` ｜ `spot-pet-insurance` ｜ `best-pet-insurance` ｜ `how-to-submit-a-pet-insurance-claim` ｜ `lemonade-vs-spot` ｜ `pet-insurance-claim-denied` ｜ `pet-insurance-cost` ｜ `pet-insurance-promo-code` ｜ `pet-insurance-waiting-periods` ｜ `pet-insurance-cost-by-brand` ｜ `pet-insurance-wellness-add-on` ｜ `pet-insurance-claim-filing-deadline`

（日期与 commit 见 `docs/daily-log.md`；**该文件由脚本从 git 实际入库记录生成，以它为准**。2026-09-28 曾有一版手写日志混入 10 个磁盘上不存在的页面名，已删除并改为脚本生成——引用前请以 daily-log 为准。）

> **A 段状态修正说明**：A 段里 N1/N2/N3/N4/N8 与已发 13 页存在主题相邻关系，**不是重复**：已发页是"概念/单口径"（等待期是什么、wellness 是什么、报销比例对比），A 段各条是"跨家数字表/实跑报价/时效分布/算式"。取题时若发现与已发页论点重叠，按 C-3 换角度。

---

## C. DAILY 取题规则（照抄执行）

1. 从 A 段**从上往下**取第一个「状态=未发」的缺口，**一篇一个缺口**；发完把该行状态改成 `已发 + YYYY-MM-DD + URL`。
2. 同一缺口**不写第二篇**；同一天已有条目 = 今天已完成（读 `docs/daily-log.md` 判断）。
3. **B 段里的选题不许重写**；若某条与已发页主题重叠，必须换角度（例：G2 已发"等待期是什么"，N1 写"逐家逐疾病天数表"，不可再写概念页）。
4. 每篇按第 8 步判据：**第一屏就是答案**、独家 ≥30%、每条事实带 source_url + 复核日期、缺来源构建失败、不用视频标题/频道名/中文原文痕迹。
5. 发布后：更新 sitemap → 线上验证 → 追加 `docs/daily-log.md` → 追加进度档案 LOG。
