# 对标缺口表（MODULE BENCH · pet insurance · 28 天周期线二）

- 读取日期：**2026-09-27**（本机时间 21:29–21:53 CST）
- 对标三家（28 天冻结，不换）：petinsurance.com（Nationwide）/ lemonade.com / pawlicy.com（Pawlicy Advisor）
- 选页口径：每站从 robots.txt + sitemap 里挑与 pet insurance 最直接相关的**前 10 页**（按导航显著度与 sitemap 权重），逐页读
- 抓取方式（可复现）：
  - petinsurance.com、lemonade.com：本机直抓（curl/urllib）拿到原始 HTML 再解析
  - pawlicy.com：curl 返回 403、直连触发 Cloudflare 挑战 → 用本机真实 Chrome（CDP 9222）取回原始 HTML 再解析
  - petinsurance.com 的 `/comparison/*` 对比页是 **JS 渲染**：原始 HTML 只有导航与免责声明（可见正文 2,358 字符、无表格），必须浏览器渲染后才看到对比表 → 抓这类页一律走 Chrome DOM
- 纪律：**只学结构和角度，原文一个字不抄**；下表里的数字只用来判断"它讲了什么"，进我站正文必须回品牌官网/官方条款页重新现抓并带 URL + 复核日期（NOFAKE）

---

## A. 总排行（缺口从大到小，DAILY 选题按这个顺序拿）

| # | 缺口 | 三家为什么都没有（2026-09-27 实测证据） | 我能补的独家料从哪取 | 可写选题 |
|---|---|---|---|---|
| G1 | **跨品牌价格表没有"抓价日期 + 官方来源 + 报价假设"** | lemonade.com `/pet/insurance-guide/pet-insurance-cost/` 印了同行均价表（Trupanion $336 / Fetch $99 / Healthy Paws $85 / Pets Best $77 / ManyPets $73 / Lemonade $61），只注明 "Based on rates for a 4-year-old Goldendoodle in Chicago"，**无抓价日期、无官方来源链接、只有单一犬种单一城市**；petinsurance.com `/comparison/lemonade/` 印 $77.34 vs $90.63 与全套条款，但是**自家 vs 对手**（利害关系方）且页面对非浏览器抓取是空壳；pawlicy.com 的价格格子一律 "Compare quotes →" 要留资才给，"Lifetime Cost" 格子写 "we use the data you entered…" | 我站 #4 `pet-insurance-cost` 已有的三家官方价目 + 各家 FAQ 现抓口径（写稿当天重抓），扩展成"三家官方已发布价格 + 每格标官方 URL + 复核日期 + 报价假设" | 《Pet Insurance Cost by Brand: Published Prices From Each Official Site (Date-Stamped)》 |
| G2 | **等待期 × 州的可查对照** | pawlicy.com `/insurance-company/lemonade/` 印了按州不同（意外 0 天 vs 2 天、髋发育不良 14/30 天、十字韧带 30/180 天），但只覆盖一家；petinsurance.com 有 50 州 `/whats-covered/<state>/` 页但只是本家；lemonade.com 无跨家等待期表 | 三家官方条款/FAQ 页的等待期原文（Lemonade FAQ、Spot 样例保单、Fetch 条款），落页前逐条现抓 | 《Pet Insurance Waiting Periods Compared: Accident, Illness, Cruciate, Hip Dysplasia — and Which States Change Them》 |
| G3 | **wellness 附加计划的"每项额度"跨家对照** | petinsurance.com `/petwellness/` 单家印了完整福利额度表（最高年额度 $450 / $800，体检 $80 与 $40 上限、疫苗 $80、心丝虫 $35、粪检 $30、驱虫 $25、芯片 $50、健康证 $50、跳蚤/心丝虫预防 $100、影像/血检/EKG $100、绝育或洗牙 $250，90 天等待）；lemonade.com 只有 Preventative Care 套餐描述、pawlicy.com 只有 "Wellness Plan add-on" 入口，**三家都没有并排的每项额度表** | Nationwide 官方 wellness 表（已抓）+ Lemonade Preventative Care 官方页 + Spot/Fetch 官方 wellness/wellness rider 页 | 《Wellness Add-On Comparison: What Each Official Benefit Schedule Actually Pays》 |
| G4 | **理赔时效与索赔窗口的口径与出处** | pawlicy.com `/insurance-company/lemonade-vs-spot/` 印 "Average Days To Reimburse 4 Days / 3 Days" 与 "Days To Submit Claim 180 / 270"，**未给统计窗口与来源**；lemonade.com `/pet` 用自选真实案例（Simba Vet Bill $2,898 / Saved $2,163 等）当证据；petinsurance.com 只讲流程不给天数 | 我站 #6 `how-to-submit-a-pet-insurance-claim` 已现抓的三家官方索赔窗口（Lemonade 180 天 / Spot 270 天 / Fetch 90 天）+ 各家官方直付条款 | 《How Long Do You Have to File a Pet Insurance Claim? Official Windows Side by Side》 |
| G5 | **异宠（鸟/兔/豚鼠/爬行）是 Nationwide 独有、另两家没有** | petinsurance.com `/pet-insurance/` 明说 "the only pet insurer to offer coverage for birds and exotic pets"，并有 `/exotics/` 子站；lemonade.com 只有猫狗；pawlicy.com 无异宠页 | Nationwide 官方 `/exotics/` 各页（rabbits/birds/guinea pigs/lizards/pigs-and-goats/ferrets）现抓价格与限制 | 《Exotic Pet Insurance: Who Actually Covers Birds, Rabbits and Reptiles》——**已发 2026-09-30 https://furadvisor.com/exotic-pet-insurance** |
| G6 | **疑问句长尾（线四 GEO）** | pawlicy.com 博客有一整排疑问句文章（Does Pet Insurance Cover Neutering / Does Pet Insurance with No Deductible Exist / Pet Insurance That Pays the Vet Directly / What Pet Insurance Do Vets Recommend…）；lemonade.com 用 "Reddit Asked, So We Answered" 段落吃社媒问句（cost 页、what-is 页各一段） | 题目只当线索；每题的**答案**必须回 Lemonade/Spot/Fetch 官方页与官方条款抓 | 一问一篇（从 ammo-list Questions 表拿，或从这两家的题目里挑我们没写的） |
| G7 | **每条事实带 source URL + 复核日期，三家都没有** | 更新日期口径不一：pawlicy 品牌页写 "Updated May 2026" 而标题写 "Review 2025"/"September 2026"，lemonade co-insurance 页写 "Last Updated: Oct 30, 2025"，petinsurance.com 页面无更新日期；三家都不逐条标来源 URL | 我站现有 build/selfcheck 强制（缺 source_url 即构建失败）—— 这是**结构性优势**，继续保持，不用另开选题 | 不开题，作为写稿标准 |
| G8 | **诚实空格（"not published on the official site"）** | 三家都只显示有数的格子，缺数就留白或藏进留资后 | 我站规则已强制 | 不开题，作为写稿标准 |

---

## B. petinsurance.com（Nationwide）· 10 页

| URL | 页面主题 | 它们讲了什么（结构/角度） | 它们全都没有的 | 我能补的独家料从哪取 |
|---|---|---|---|---|
| `/` | 首页 | "Best. Pet insurance. Ever." 情绪化首屏 + 起步价 + 三步流程（看兽医→交材料→收报销）+ 11 条 FAQ | 无价格表、无更新日期 | 首页口径 `premiums starting at $12/mo`，而 `/pet-insurance-reviews/` 同页写 `$13/mo`、`/dog-insurance/` 写 `$13/mo`、`/cat-insurance/` 写 `$6/mo` —— 同站不同起步价，写稿前回官方页核当天口径 |
| `/pet-insurance/` | 产品总览 | 8 组自问自答（该不该买/怎么选/保什么/异宠/理赔/多人多宠）+ 五大保障块（意外/疾病/预防/急救/手术） | 无价格、无跨家对比 | `/exotics/` 各页（异宠独家，见 G5） |
| `/dog-insurance/` | 犬险 | 按年龄分档（puppy 0-1 / adult 2-7 / older 8+）+ 起步价 + 兽医账单常识（耳感染均值 $250、骨折 $200–$5,000、吞异物手术至多 $2,000）+ 12 条 FAQ + 1 张表；JSON-LD 含 FAQPage/ItemList/Product | 无分犬种价格表、无等待期明细 | 账单区间是 Nationwide 2024 数据（页脚脚注），可作为"兽医账单有多贵"的官方引子（引用要带脚注出处） |
| `/cat-insurance/` | 猫险 | 与犬险同构；起步价 $6/mo；绝育/阉割问题进 FAQ | 同上 | 同上 |
| `/whats-covered/` | 保障总览 + 50 州入口 | 州下拉框 → 50 个 `/whats-covered/<state>/` 页；列出四类不保（既往症、尸体处理、寄养/美容、税） | 州页只是本家条款，无跨家 | 州级差异是 G2 的一半，另一半（等待期）要从各家条款页拿 |
| `/whats-not-covered/` | 除外责任 | 逐条讲：既往症（**治愈满 6 个月可能可保**）、美容、等待期内十字韧带、先天/遗传、非兽医费用、非 wellness 项目 | 无对照、无表格 | "cured for at least six months" 这条口径是少见的细料，可与 Lemonade「curable pre-existing」官方口径并排写 |
| `/petwellness/` | Wellness 计划 | 单家完整额度表（$450/$800 两档 + 逐项上限，见 G3）+ 8 条 FAQ | 无跨家每项额度 | G3 选题的主料 |
| `/comparison/` | 对比 hub | 只有 Trust/Value/Experience 三段自夸 + "pro tip"（换公司后既往症可能不保） | hub 页本身无数据（对比表在 `/comparison/<brand>/` 子页） | 换保司的既往症断档是真问题 → 可写《Switching Pet Insurance: What Resets》（三家官方条款现抓） |
| `/comparison/lemonade/` | 自家 vs Lemonade（JS 渲染） | 浏览器渲染后是完整对照表：计划名、免赔额 $250、年度限额 $5,000、报销比例 70%、月费 $77.34 vs $90.63、手续费 $3.25 vs $2、24 项勾叉、理赔算例（肠道异物手术 $3,158 → $2,035.60） | **对非浏览器抓取是空壳**（原始 HTML 无表格）；没有抓价日期与报价假设；是自家利害方 | 学它"把条款拆成 24 个勾叉格子"的结构；数字全部要回各家官方页重取 |
| `/faq/` | 全站 FAQ | 4 组共 35 问（保障 14 / 价格 6 / 使用 7 / 选购 6 / 资格 2），FAQPage JSON-LD | 无更新日期、无逐问来源 | 35 问的题目清单可当线四 GEO 选题池（答案自己回官方源写） |

补充：`/pet-insurance-reviews/` 只有 544 字符可见正文（Trustpilot 转载 + 一句起步价）——**评价页是它家最薄的页面**，可写《Where Pet Insurance Reviews Come From》角度（不动 Trustpilot 数据口径）。

## C. lemonade.com · 10 页

| URL | 页面主题 | 它们讲了什么（结构/角度） | 它们全都没有的 | 我能补的独家料从哪取 |
|---|---|---|---|---|
| `/pet` | 产品页 | 极速理赔主张 + 5 个真实理赔案例卡（病名 / 兽医账单 / Saved With Lemonade：$2,898→$2,163、$632→$426、$15,259→$14,143、$5,391→$4,248…）+ 13 条 FAQ（waiting periods / pre-existing / 值不值 / 多少钱 / 换公司比较） | 案例是自选、无核验口径；无表格；无更新日期 | 案例结构（bill vs saved）值得学；数字不能用 |
| `/pet/insurance-guide/` | 指南 hub（`/pet/explained/` 301 到这里） | 22 篇指南的卡片目录，一屏一答的短摘要（deductible / euthanasia / vet visits / emergency / medication / dental / waiting period / pre-existing…） | 无表格、无来源 | 这是"一问一答卡片 → 深页"的结构范式，学结构 |
| `/pet/insurance-guide/pet-insurance/` | 什么是宠物险 | 长文（可见正文 28,227 字符）+ 1 张表 + FAQPage/VideoObject；后面挂 **27 条深问**（Apoquel/Cytopoint、双侧性疾病、行为性疾病、安乐死与火化、针灸水疗、牙科、住院、急诊吞异物…）+ "Reddit Asked, So We Answered" 段 | 无逐条来源、无复核日期 | 27 条深问 = 线四 GEO 选题池（我按 Lemonade/Spot/Fetch 官方口径自己答） |
| `/pet/insurance-guide/pet-insurance-cost/` | 多少钱 | 3 张表：分州均价（$30–$49 区间数字成片）、犬猫对比、**同行均价表**（Trupanion $336 / Fetch $99 / Healthy Paws $85 / Pets Best $77 / ManyPets $73 / Lemonade $61，注 "4-year-old Goldendoodle in Chicago"）+ 降保费四杠杆（co-insurance / deductible / annual limits） | 同行数字无日期、无官方来源链接、单犬种单城市（见 G1）；无"各家官方价目页"链接 | G1 选题主料（我方每格带官方 URL + 抓取日期） |
| `/pet/insurance-guide/pet-insurance-coverage/` | 保什么 | 与 what-is 页同 URL（301 到 `…/pet-insurance/`） | — | 记下来：Lemonade 把同意图页合并，符合我们"一页吃整族"规则 |
| `/pet/insurance-guide/lemonade-pet-insurance-faq/` | 自家 FAQ | 34+ 问的超长 FAQ（申请/等待期/十字韧带/共付比例/改保/既往症可否治愈后保/电话客服/涨价原因/取消/理赔时限/Chewy、Costco 药品能否报/被偷被丢/领养前能否报价…）+ 3 个故事化算例（十字韧带 Max、癌症 Luna、等待期 Charlie） | 只讲自家、无跨家 | 故事化算例（症状→账单→报销）是可学结构；数字不抄 |
| `/pet/dogs` | 犬险 | 情绪化卖点 + 20 项保障词云（bloodwork/MRI/CT/cancer/…）+ 7 条 FAQ | 无价格表 | 词云式保障清单可比对官方条款做"真保 vs 只是词"的核验稿 |
| `/pet/cats` | 猫险 | 同犬险（词云里多 diabetes / urinary tract infections） | 同上 | 同上 |
| `/pet/compare` | 自家对比工具 | 三问选型（customization / claims / price）+ 一张与同行的勾叉表（App Store 评分列：N/A、4.7、4.5、4.8、4.6…，**不写对手名**，只给 "Full review" 链接） | 勾叉表不标对手名、无口径 | 学"评分列 + 勾叉列"结构；我方必须标名字与口径 |
| `/pet/insurance-guide/co-insurance/` | 名词解释 | 单概念页：定义 + 与 copay 区别 + 算式 `(cost × co-insurance) – deductible = claim payment` + "该选多少" + HowTo JSON-LD；标注 "Last Updated: Oct 30, 2025" | 单概念、无跨家 | 算式与我们 #4 的报销算例同源思路，可用官方政策条款做我方版本 |

URL 结构学习：Lemonade 的内容层是 `/pet/insurance-guide/<slug>/`（hub + slug），`/pet/explained/*` 与 `/pet-insurance-coverage` 都 301 到它 —— **同意图不拆多页**，与我站规则一致。

## D. pawlicy.com（Pawlicy Advisor）· 10 页

| URL | 页面主题 | 它们讲了什么（结构/角度） | 它们全都没有的 | 我能补的独家料从哪取 |
|---|---|---|---|---|
| `/` | 首页（marketplace） | 报价匹配器 + 11 家 "Policy Overview" 卡片 + 4.9 星 + 7 条 FAQ（含"你们怎么赚钱"） | 价格格子要留资才给 | 商业模式透明是它强项；我方不涉及佣金入正文 |
| `/dog-insurance/` | 犬险落地页 | 报价器 + 11 家评分/免赔/报销天数卡（如 3.8 (6,234)、$100–$1,000、10–30 天）+ **"Example monthly premium … for different dogs"（按犬种查价）** + "Dog owners save 24% on average when comparing" 脚注 + 11 条 FAQ | 具体价格要进漏斗才显示；24% 那句未标来源 | 按犬种查价的结构可学；价格必须回各家官方页 |
| `/cat-insurance/` | 猫险落地页 | 同犬险同构（表 2 张） | 同上 | 同上 |
| `/methodology/` | 方法论 | 长文：推荐算法 = Lifetime Cost Score + 个性化匹配；"Best" 定义、用到的数据类型、**Calculating Average Cost** 章节、AAHA 认可、可下载 PDF 报告 | 未披露具体数据采集日期与样本量 | 这是它可信度的支柱；我方对应物 = 逐条 source URL + 复核日期，可写成我站 how-we-rate 页 |
| `/dictionary/pet-insurance-terms/` | 术语表 | 70+ 条术语锚点列表（Accident-Illness…Zero Fee Service，含自家口径 Lifetime Pricing Score / Coverage Score / Average Days to Reimburse） | 列表页不给解释（进词条页） | 术语清单 = FAQ/结构参考；解释要按官方条款写 |
| `/pet-insurance-usa/` | 全美总览 + 50 州入口 | 州选择器 → `/pet-insurance-usa/<state>/`；三段卖点（老牌/快赔/终身价值）+ FAQPage | 无跨家价格 | 州页结构可学，州级事实回各家官方条款 |
| `/insurance-company/lemonade/` | 单家品牌 review | **固定模板**：Reviewer 署名（Licensed Insurance Producer）+ Updated 日期 + FACT CHECKED 徽章 → Pricing 面板（犬 $10/月*、猫 $10/月*、免赔 $100/$250/$500/$750、报销 70/80/90%、限额 $5,000–$100,000）→ **按州等待期**（意外 2 天，AL/AR/CT/DC/GA/IL/IN/IA/MD/MS/NE/NH/NM/OH/SC/TX/UT/WA 为 0 天；疾病 14 天；髋发育不良 14 或 30 天；十字韧带 30 或 180 天）→ Pros/Cons → 覆盖矩阵 → 理赔/价格/折扣/客服/取消/评价 → 8 条 FAQ | 价格是"from"口径且写 $10 起（与官方页口径需核）；等待期数据未标来源 URL | 这套模板是我们品牌页该对齐的结构；所有数字回 lemonade.com 官方页重取 |
| `/insurance-company/trupanion/` | 单家品牌 review | 同模板（4 张表、可见正文 64,429 字符），标题写 "Review 2025" 而站内其他处写 2026 —— **日期口径不一致** | 同上 | 日期口径不一致是它家弱点，我方以 selfcheck 逐条日期校验对打 |
| `/insurance-company/lemonade-vs-spot/` | 双家对比 | 月度标题（"September 2026 Comparison Chart"）+ TrustPilot 评分带日期（4.1/5,432 与 4.7/10,979）+ 平均报销天数（4 天 / 3 天）+ 索赔窗口（180 / 270 天）+ 24 行覆盖矩阵（每行带一句解释 + tooltip）+ "Policy Score / Lifetime Cost Score" 要留资 | 报销天数无统计口径与来源；评分来自第三方平台；分值不公开 | 与我方 `#5 lemonade-vs-spot` 直接同题 —— 我方差异点=每格带官方来源与日期、不靠留资 |
| `/blog/` | 博客 hub | 精选 4 篇（How to Choose / Is It Worth It in 2026 vet 视角 / Best Companies 2026 / What Is Pet Insurance）+ **60+ 组 "A vs B (Comparison Chart)"**（ASPCA/Embrace/Fetch/Figo/Hartville/Healthy Paws/Lemonade/MetLife/Pets Best/Prudent Pet/Pumpkin/Spot/Trupanion…全组合）+ 一排疑问句文章 | 对比图表是模板化、无逐格来源 | 组合覆盖面是它的护城河；我方按不拆页规则只做已有品牌的对位页，别照抄全组合 |

（`/review-insurance/` 实测是 UGC 提交表单，可见正文 784 字符，不计入前 10 页正选。）

---

## E. 与我站（furadvisor.com / S1）对照

- 已覆盖：跨家价格（#4）、报销算例与流程（#6）、折扣官方口径（#7）、双家对比（#5）、全站 best（#1）、申诉流程（`/pet-insurance-claim-denied`，线上 200）、三家品牌页（Lemonade/Spot/Fetch）
- 结构性优势（三家都没有）：每条事实带 source_url + checked 日期，缺来源构建失败；"not published on the official site" 诚实空格；首屏直接给答案
- 未覆盖（按 A 段缺口顺序）：G1 价格表加"抓价日期+官方链接+报价假设"、G2 等待期×州、G3 wellness 额度跨家、G4 索赔窗口三家对照（#6 已有部分，可做独立页）、G5 异宠、G6 疑问句一问一篇

## F. DAILY 用法（线二/线四）

1. 每天那篇的选题从 A 段排行拿：**一个缺口一篇**，缺口大优先
2. 发之前先查我站 sitemap（`https://furadvisor.com/sitemap.xml`）没有同词或同角度的页，有就换下一个缺口
3. 题目可以从 B/C/D 的"它讲了什么"里找灵感，**结构学、句子不抄**；每个数字回品牌官网/官方条款页现抓，带 URL + 复核日期
4. 三家对标 28 天内不换；下一轮重读三家时刷新本表（改动写在本文件末尾）
