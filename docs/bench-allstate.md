# BENCH 对标缺口分析：allstate.com（核心词 pet insurance）

- **读取/抓取日期**：2026-09-28
- **抓取方式**：
  1. `curl https://www.allstate.com/robots.txt` + `https://www.allstate.com/sitemap.xml`（sitemap 为单文件 urlset，1.9 MB，含 lastmod）；
  2. `curl` 直取 HTML（Chrome UA）→ Python 正文抽取（去 script/style/nav/footer）；**全部页面为服务端渲染，10/10 抓取成功，无 403、无需浏览器兜底**；
  3. `web_search site:allstate.com pet insurance` 交叉校验 URL 是否遗漏。
- **范围说明**：
  - 域内 `/tests/pet-insurance*`（3 条）被 robots.txt `Disallow: /tests*`，属测试副本，已排除；
  - `/es/pet-insurance*` 为西语重复页，已排除；
  - 产品页「Get a Quote」点击后**跳出 allstate.com 前往 quote.embracepetinsurance.com**（合作方 Embrace 落地页）——页面本体仍在 allstate.com，落地页仅作记录，不计入 10 页。
- **承保结构（影响其内容立场）**：Allstate 自己不卖宠物险，属 Expanded Market Program，由 Ivantage Select Agency（Allstate 关联方）转介给 Embrace Pet Insurance Agency 报价，American Modern / American Southern 承保；页脚长免责声明反复声明「Pet Health Insurance is not an Allstate product」。**这决定了它只能做“教育+导流”，不能做“对比”。**

---

## 一、对标表（10 页）

| URL | 页面主题 | 它们讲了什么（结构/角度，列要点、小节、有没有表格/价格/FAQ/更新日期） | 它们全都没有的（缺口） | 我能补的独家料从哪取 |
|---|---|---|---|---|
| https://www.allstate.com/pet-insurance | 主落地页（H1「Pet health insurance」，导流枢纽） | 结构：Summary(带价) → What is → Cost → How it works(3步) → What covers / What doesn't cover → Is it worth it → dog vs cat 对比表 → Eligibility → Wellness plans → FAQ×7。**有价格区间**（狗 $20–70/月、猫 $10–30/月，脚注注明“2026 现有保单持有人数据”）、**有 1 个 dogs vs cats 对比表**、**有报销演算示例**（$1,200 急诊 + $250 免赔 + 80% 报销 → 自付 $440）、**有 FAQ**；**无页面更新日期**（sitemap lastmod 2026-09-04）。资格线：6 周–15 岁全险，15 岁以上仅意外险；疾病等待期 2 周；多宠最多 10% 折扣、军人家庭再 5%。 | ①只讲自己一家（Embrace 承保）的“区间价”，没有**任一具体计划/免赔/报销比例的价格表**；②没有**州级可用性**清单；③没有**等待期逐项明细表**（仅一句“因州而异”）；④“worth it”纯定性，**无赔付概率/期望值测算**；⑤无任何第三方计划对比、无用户评价/理赔数据。 | 州级可用性与等待期：抓 Embrace 条款 PDF（embracepetinsurance.com/coverage/embrace-terms）+ 各州 DOI 备案；期望值测算：自建“保费 vs 自付风险”计算器，用我们自己采集的报价跑数。 |
| https://www.allstate.com/pet-insurance/dog-insurance | 狗险产品子页（子导航 Overview/Cat/Dog） | 结构：What is → Why need → What is covered(8 条清单，含假肢、牙科意外、行为治疗) → How it works(3 步) → **保费示例表**（品种/年龄/州/邮编/预估保费，6 行如“Mixed Breed Toy, 5y, Evansville IN, from $13.88”，脚注 Embrace 2025 数据） → Is it worth it → How do I get(报价 4 项配置项解释) → FAQ×5 → **不保清单(6 条，含 DNA 检测)**。**有价格表、有 FAQ，无更新日期**（lastmod 2026-08-06）。 | ①示例表是**给定邮编的“from”起价**，不是同条件下的可比报价，且无覆盖/免赔对照，**无法横向比价**；②FAQ 不回答“申请要多久/怎么赔/多久到账”；③没有按品种的**高发病种 × 是否易被加费/拒保**对照；④无幼犬 vs 成犬投保时点的量化建议。 | 品种×理赔：把 Embrace/其它家条款里的 breed exclusion 与 AKC/OFА 高发病种做成对照矩阵；报价可比性：用同一宠物档案在 3–5 家各跑一次真实报价并公开截图口径（我们自己跑，不引对方数字）。 |
| https://www.allstate.com/pet-insurance/cat-insurance | 猫险产品子页 | 结构与狗险页**几乎模板复用**：What is → Why → Covered(同一 8 条) → 3 步流程 → **保费示例表**（Domestic Shorthair/Bengal 等 6 行，from $13.76–$19.38，脚注 Embrace 2025 数据） → Worth it → How do I get → FAQ×6（含“最佳投保年龄 6–8 周”） → 不保 6 条。**有价格表、有 FAQ，无更新日期**（lastmod 2026-08-06）。 | ①与狗险页**正文大段重复**，猫特有内容只有“6–8 周投保”一条，**没有猫特有高发病（尿路梗阻、肾病、牙病）与保费/核保关系**；②无室内猫/户外猫、绝育与否对核保的影响；③同上缺可比价格与到账时效。 | 猫特有风险：用我们自己整理的猫病种就诊成本 + 各家条款里的既往症/等待期规则做“猫家长决策表”；绝育状态、饲养环境对核保的影响需实测问询，不引对方数字。 |
| https://www.allstate.com/resources/pet-insurance | 资源中心 hub（分类页） | 结构极薄：H1「Pet insurance resources」→ 短横幅 → Recommended resources×5（其中 3 条其实是安全/搬家/旅行类泛宠物文）→ Pet insurance basics×3 → 中部 Quote CTA → 页脚长免责。**无更新日期、无列表分页、无文章总数**（sitemap lastmod 2026-07-29）。 | ①hub 只挂 8 篇，**未收录其站内全部宠物文章**（如绝育、品种、危险物等散落未聚合）；②无“按阶段”组织（买前比价 / 投保 / 索赔 / 理赔争议）；③无站内搜索/筛选、无作者署名（一律 Published By: Allstate）。 | 我方 hub 按**用户决策阶段**（选计划→算钱→投保→索赔→争议）重建信息架构，并公开每篇的方法论与更新日志。 |
| https://www.allstate.com/resources/pet-insurance/what-does-pet-insurance-cover | 承保范围教育文 | 结构：**Last Updated: October 2023** + Published By: Allstate → 可保 3 类 → 加购(wellness 分档、处方药) → What is → How it works（引 III） → 不保 4 条（既往症、食物维生素、怀孕繁殖、行为治疗） → 选计划 3 条 AVMA 指引 → 结语 CTA。**无表格、无价格、无 FAQ、更新日期偏旧（2023-10）**。 | ①**没有逐项“保/不保/可加购”三栏对照表**，用户要自己拼；②不含等待期、限额、报销方式这些真正决定“保什么”的参数；③内容更新滞后（2023 年），与主站 2026 口径可能不一致，**无人指出这种不一致**。 | 做“条款级”承保矩阵：把 Embrace 及同类 4–5 家条款的 cover/exclude/add-on 拉平成一张表，标注各家条款版本与生效日；并做“站内旧文 vs 现行条款”一致性核查。 |
| https://www.allstate.com/resources/pet-insurance/how-much-does-pet-insurance-cost | 成本教育文（其站内信息密度最高的一篇） | 结构：**Last Updated: April 2026** → **Key points 摘要 4 条** → How it works → 5 个影响因素（宠物类型/品种年龄/地区/保障/免赔） → 各因素分节（引 CBS、Forbes、III、NAPHIA） → 狗价区间、猫价、兽医均价 → Worth it → 三档保障(basic/comprehensive/wellness) → 如何选免赔额+**年度限额示例**（$250 保费/$100 免赔/$1,500 上限）。**有价格、有结构化 key points，无表格、无 FAQ、无本页数据源（全是二手媒体引用）**。 | ①价格全是**二手媒体区间**（如“约 $25–280/月”一类），**没有一手报价数据、没有分布（中位数/分位）**；②无**州级价格表**、无**涨价历史**（renewal 涨幅只在页脚免责里提一句“可能涨”）；③无“同一只宠在不同公司多少钱”的可比数据；④无成本敏感度表（免赔/报销比/限额三因子如何联动月保费）。 | 一手价格：我们自己在同一宠物档案/同一邮编下跑多家报价，输出**分布而非区间**；涨价：连续季度跟价 + 收集 renewal notice；免赔/报销/限额三因子敏感度表用我们的报价数据画。 |
| https://www.allstate.com/resources/pet-insurance/dog-insurance | “狗险如何运作”教育文 | 结构：**Last Updated: October 2025** → 4 类保障（意外疾病/wellness/处方/comprehensive） → 保单要素（保费、免赔、限额、等待期） → **3 种报销方式**（按账单百分比 / 按项目价目表 / 按当地常规合理收费，引 NAIC）并提醒“看细则” → Quote CTA → 成本因子(NAIC 5 条) → 结语。**无表格、无价格数字、无 FAQ。** | ①讲了有 3 种报销方式却**不告诉读者自己那份属于哪种、差异会让到账差多少**；②没有**等待期逐类明细**（意外/疾病/骨科/癌症通常各不同）；③“看细则”式收尾，**无一步步教人从哪里找到自己保单里的这几个字段**。 | 报销方式实测：拿同一笔模拟账单在三种算法下算出差额（我们自算）；等待期明细表从各家公开条款/SPD 逐条抄录并注明条款版本（条款是公开原文，不属我方编造）。 |
| https://www.allstate.com/resources/pet-insurance/vet-visits | “常规就诊是否赔”专题 | 结构：**Last Updated: September 2025** → 直接回答“含 wellness 才赔常规” → wellness 覆盖清单（体检、驱虫、疫苗） → 三档保障层级（引 III） → Quote CTA → 报销比例示例（“Max 看诊先自付再报销”文字例） → **不保项**（既往症、美容/剪甲，引 NAPHIA） + **30 天等待期**（引 NAPHIA） + 异宠 wellness 一般不保。**无表格、无价格、无 FAQ。** | ①**没有 wellness 各档每年额度与实际可报多少的数字**（“分档”只有描述）；②没有“疫苗/体检单项在保险 vs 自付 vs wellness add-on 三种路径下的成本对比表”；③常规就诊与“意外疾病”边界的**具体病种归属清单**缺失。 | 做一张“常规护理三路径成本表”：我们采集的疫苗/体检/绝育/洗牙单项价格 × 是否可报销 × wellness 年度额度，跑出“买 wellness 划算线”。 |
| https://www.allstate.com/resources/pet-insurance/emergencies | “急诊是否赔”专题 | 结构：**Last Updated: January 2025** → 引 III 列出通常赔的 3 类（意外受伤、疾病、误食中毒） → 急诊手术是否赔（骨折、肿瘤切除例子） → 既往症不赔（引 NAPHIA） → Quote CTA → 报销金额取决于计划（自付→按比例报，含免赔与限额） → 基本 vs 综合档差异。**无表格、无价格、无 FAQ、无急诊/异宠 24 小时价目数据。** | ①**完全没有急诊价格现实**（一次急诊实际花多少、常见项目费用区间）；②不回答“急诊当晚能否先赔/直付”（全行业是先自付，但**没有一家讲清直付有无**）；③无“急诊 vs 普通门诊 vs 二次诊疗意见”的决策路径。 | 急诊账单：收集（我们自建）真实公开账单样本与兽医收费表做区间；直付/快赔：向各家客服实测提问并公开记录（口径注明实测日期）。 |
| https://www.allstate.com/resources/pet-insurance/cane-corso | 品种页（含保险转化段，展示其“品种 SEO → 导流”打法） | 结构：**Last Updated: June 2024** → 寿命 8–12 年（引 Open Veterinary Journal） → 体型 → 行为/训练/美容 → **常见病分节**（髋关节发育不良、心肌病 DCM、肥胖、内翻睫、胃扩张扭转 bloat） → 预防养护 → **末段“Consider pet insurance for your cane corso”**（泛化话术+CTA，引 Embrace 说每年至少体检一次）。**无价格、无 FAQ、无“该品种保费比均值高多少”数据。** | ①列了品种高发病却**不给这些病的治疗费用量级、也不给该品种保费相对水平**，保险段与正文健康信息完全脱钩；②无“哪些公司对该品种加费/拒保”的对照；③典型大品种（金法斗、德牧、拉布拉多等）无同款页，覆盖面窄。 | 品种页做成“健康风险 × 治疗费用区间 × 各家核保态度”三合一（治疗费用取自我们采集的公开价目/账单，核保态度靠我们实测问询）；把我方品种页批量铺开，这是他们用一条模板就能复制的打法。 |

> 旁注（已读但排第 11，未计入表格）：`/resources/pet-insurance/cat-neutered`（Last Updated August 2025，讲绝育指征/术前术后准备/费用 $300–500 区间（引 petMD），仅中部一个报价 CTA，与保险决策关联弱）；另 `/tests/pet-insurance*` 为 robots 禁抓的测试副本。

---

## 二、该站整体可补缺口（按缺口从大到小）

1. **中立横向对比（最大缺口）**：全站 10 页只推 Embrace 一家承保，连“怎么和其他公司比”都不设章节——因为它是转介销售渠道，对比会直接自伤，而 furadvisor 是决策站，做对比天然正当。
2. **一手价格数据而非二手区间**：它给的只是“$20–70 之类”的区间与 6 行“from”示例，价格全部来自自家保单数据或媒体二手引用，无分布、无州级表、无涨价轨迹——保险公司视报价为商业敏感且动态生成，不公开就等于把数据位留给了我们。
3. **理赔真相层（赔付率、到账时效、常见拒赔理由、直付有无）**：一个把用户送去投保的品牌页不可能讲拒赔与争议，其 FAQ 只回答到“按比例报销”为止——这是品牌方结构性缺位。
4. **量化“值不值”模型**：它每页都有 “Is it worth it?” 却全是定性说辞，没有期望值、储蓄替代、breakeven 分析——因为营销页只需要结论，不需要算式。
5. **条款级明细的对齐呈现**（等待期逐项表、报销方式差异的实际金额影响、wellness 各档年度额度、州级可用性）：它反复让读者“read your policy / see terms on embracepetinsurance.com”，把核对成本甩给用户——把公开条款拉平成一张可比表，就是我们能补的结构差。

---

## 三、纪律声明

- 本文所有数字仅用于**描述对方页面讲了什么**，不得作为 furadvisor 可直接引用的事实；我方发布前须用自有采集数据或公开条款原文重新核验。
- 上述“它们全都没有的”基于 2026-09-28 抓取的 10 页正文逐页阅读，未覆盖其 JS 交互组件（报价器在 Embrace 域名侧）与未收录页面；抓取全部成功，无“抓不到”的页。
- 结构与角度的学习限于信息架构与选题，正文表述零复制。
