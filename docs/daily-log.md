# Daily log — 发布日志（DAILY 任务与推进器共用的唯一去重依据）

格式：`日期 | 标题/页面 | URL | 用了哪个缺口 | 主要来源`
去重规则：**同一个缺口不许写第二篇；同一天已有条目 = 今天主线已完成。**
回填说明：2026-09-28 主会话用各仓库 `git log --diff-filter=A -- site/*.html`（页面文件首次入库日期）回填，与当日 content 提交记录核对一致。09-28 之前的「主要来源」列留空表示未回溯记录，不代表没带来源（站点 selfcheck 强制缺来源即构建失败）。

## 2026-09-28（4 篇，主线达标）
| 日期 | 标题/页面 | URL | 缺口 | 主要来源 |
|---|---|---|---|---|
| 2026-09-28 | Pet Insurance Waiting Periods | https://furadvisor.com/pet-insurance-waiting-periods | G2 | lemonade.com 等待期指南 + spotpet.com/sample-policy 六州 PDF + fetchpet.com FAQ（均 2026-09-28 现抓） |
| 2026-09-28 | Pet Insurance Cost by Brand | https://furadvisor.com/pet-insurance-cost-by-brand | G1 | 三家官网价格页与脚注（Lemonade/Spot/Fetch，见 ammo fill #14，2026-09-28 现抓） |
| 2026-09-28 | Pet Insurance Wellness Add-On | https://furadvisor.com/pet-insurance-wellness-add-on | G3 | Lemonade/Spot/Fetch/Nationwide 官方 wellness 额度表（ammo fill #15，2026-09-28 现抓） |
| 2026-09-28 | Pet Insurance Claim Filing Deadline | https://furadvisor.com/pet-insurance-claim-filing-deadline | G4 | Spot 270 天 FAQ+样例保单、Lemonade 180 天（德州 90）、Fetch 90 天（ammo fill #16，2026-09-28 现抓） |

## 2026-09-27（S2 三篇 + S3 一篇）
| 日期 | 标题/页面 | URL | 缺口 | 主要来源 |
|---|---|---|---|---|
| 2026-09-27 | Best Fresh Dog Food Subscriptions | https://pet-fresh-food-decisions.pages.dev/best-fresh-dog-food-subscriptions | S2 #17 | （未回溯） |
| 2026-09-27 | Best Raw Dog Food Delivery | https://pet-fresh-food-decisions.pages.dev/best-raw-dog-food-delivery | S2 #18 | wefeedraw/darwins/meetmaev 官方页（ammo fill #9） |
| 2026-09-27 | JustFoodForDogs Review | https://pet-fresh-food-decisions.pages.dev/justfoodfordogs-review | S2 #19 附近 | （未回溯） |
| 2026-09-27 | Best Automatic Litter Box | https://smart-pet-device-decisions.pages.dev/best-automatic-litter-box | S3 #19 | 四品牌官方页（ammo fill #11） |

## 2026-09-26（S1b 四篇 + S2 六篇）
| 日期 | 标题/页面 | URL | 缺口 | 主要来源 |
|---|---|---|---|---|
| 2026-09-26 | Vetster Review | https://pet-health-decisions.pages.dev/vetster-review | S1b #8 | vetster.com（2026-09-26 现抓） |
| 2026-09-26 | Online Vet vs In-Person Vet | https://pet-health-decisions.pages.dev/online-vet-vs-in-person | S1b #9 | vetster.com 官方指引 |
| 2026-09-26 | Best Joint Supplement for Dogs | https://pet-health-decisions.pages.dev/best-joint-supplement-for-dogs | S1b | 官方页 |
| 2026-09-26 | Buy Pet Prescription Meds Online | https://pet-health-decisions.pages.dev/buy-pet-prescription-meds-online | S1b | 1800petmeds 官方页 |
| 2026-09-26 | Embark Discount Code | https://pet-health-decisions.pages.dev/embark-discount-code | S1b | embarkvet.com 官方页 |
| 2026-09-26 | Embark DNA Test Review | https://pet-health-decisions.pages.dev/embark-dna-test-review | S1b | embarkvet.com |
| 2026-09-26 | Ollie Fresh Dog Food / Ollie Cost Per Day / Ollie vs The Farmer's Dog / JustFoodForDogs Fresh Food / The Farmer's Dog（S2 五篇品牌与对比页） | https://pet-fresh-food-decisions.pages.dev/ | S2 #14 #15 | 各家官网（ammo fill #7，2026-09-26 现抓） |

## 2026-09-25（P1 五篇 + S1b 四篇）
| 日期 | 标题/页面 | URL | 缺口 | 主要来源 |
|---|---|---|---|---|
| 2026-09-25 | Best Pet Insurance in 2026 | https://furadvisor.com/best-pet-insurance | S1 #1 | 三家官网 |
| 2026-09-25 | How Much Does Pet Insurance Cost | https://furadvisor.com/pet-insurance-cost | S1 #4 | 三家官网价格页 |
| 2026-09-25 | Lemonade vs Spot | https://furadvisor.com/lemonade-vs-spot | S1 #5 | 两家官网 |
| 2026-09-25 | How to Submit a Pet Insurance Claim | https://furadvisor.com/how-to-submit-a-pet-insurance-claim | S1 #6 | 三家官网理赔页 |
| 2026-09-25 | Pet Insurance Promo Codes | https://furadvisor.com/pet-insurance-promo-code | S1 #7 | 三家官方 offer |
| 2026-09-25 | Pet Insurance Claim Denied（appeal） | https://furadvisor.com/pet-insurance-claim-denied | G（claim denied） | Lemonade/Spot/Fetch 官方条款 |
| 2026-09-25 | Vetster Online Vet / 1800petmeds / Cosequin / Embark DNA Test（S1b 四个品牌页） | https://pet-health-decisions.pages.dev/ | S1b 骨架 | 各家官网当日现抓 |

## 2026-09-24（P1 骨架 + 三个品牌页）
- https://furadvisor.com/lemonade-pet-insurance 、/spot-pet-insurance 、/fetch-pet-insurance （品牌页，一品牌一页）

---
累计（按页面文件首次入库日期统计）：P1 furadvisor 14 篇内容页（不含 about/privacy/contact/404）、S1b 11、S2 9、S3 5。
