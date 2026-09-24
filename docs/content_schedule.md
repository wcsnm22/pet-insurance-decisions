# 首批内容排期表（M1，28 篇）

生成日期：2026-09-24。状态字段：todo / draft / published。
规则：英文页面；每条事实来自品牌官网/官方条款页，附来源 URL + 复核日期；一个品牌一页吃整族意图（name + review/quote/cost/promo code 进 title/H1/FAQ/JSON-LD）；不编价格、条款、折扣；不抄比价站。

## 站点映射

| 站 | 域名（Cloudflare Pages） | 覆盖 | 状态 |
|---|---|---|---|
| S1 保险 | pet-insurance-decisions.pages.dev | 支柱1·保险 | ✅ 已上线 |
| S1b 健康 | pet-health-decisions（待建） | 支柱1·远程兽医/在线药房/保健品/DNA | 待建 |
| S2 鲜粮 | pet-fresh-food-decisions（待建） | 支柱2 | 待建 |
| S3 智能设备 | smart-pet-device-decisions（待建） | 支柱3 | 待建 |
| S4 美容 | pet-grooming-decisions（待建） | 支柱4 | 待建 |
| S5 B2B | pet-software-decisions（待建） | 支柱5 | 待建 |

排期顺序：S1 → S1b → S2 → S3 → S4 → S5（支柱1+2 先发，S3 有站点权重后再申请高门槛项目，S5 收尾）。

## 排期表（28 篇）

| # | 支柱 | 站 | 类型 | 英文标题（title/H1 基准） | 主搜索词 | 状态 |
|---|---|---|---|---|---|---|
| 1 | 1 | S1 | best | Best Pet Insurance in 2026: Plans Compared Side by Side | best pet insurance | todo |
| 2 | 1 | S1 | review | Lemonade Pet Insurance Review: Coverage, Quotes & Claim Speed | lemonade pet insurance review | todo |
| 3 | 1 | S1 | review | Spot Pet Insurance Review: Is It Worth It for Dogs and Cats? | spot pet insurance review | todo |
| 4 | 1 | S1 | pricing | How Much Does Pet Insurance Cost? Real Quote Breakdown | pet insurance cost per month | todo |
| 5 | 1 | S1 | vs | Lemonade vs Spot Pet Insurance: Which One Should You Pick? | lemonade vs spot pet insurance | todo |
| 6 | 1 | S1 | tutorial | How to Submit a Pet Insurance Claim (Step by Step) | how to submit a pet insurance claim | todo |
| 7 | 1 | S1 | coupon | Pet Insurance Promo Codes & Discount Guide (Official Offers Only) | pet insurance promo code | todo |
| 8 | 1 | S1b | review | Vetster Review: Online Vet Appointments Tested | vetster review | todo |
| 9 | 1 | S1b | vs | Online Vet vs In-Person Vet: When Each Makes Sense | online vet vs in person vet | todo |
| 10 | 1 | S1b | tutorial | How to Buy Pet Prescription Meds Online Legally (Chewy, 1800PetMeds) | buy pet medication online | todo |
| 11 | 1 | S1b | best | Best Joint Supplements for Dogs: Vet-Backed Picks | best joint supplement for dogs | todo |
| 12 | 1 | S1b | review | Embark Dog DNA Test Review: Breed + Health Results Explained | embark dna test review | todo |
| 13 | 1 | S1b | coupon | Embark Dog DNA Test Discount Code (Verified Offers) | embark discount code | todo |
| 14 | 2 | S2 | vs | Ollie vs The Farmer's Dog: Fresh Dog Food Compared | ollie vs the farmer's dog | todo |
| 15 | 2 | S2 | pricing | How Much Does Ollie Cost Per Day? Plan Pricing Explained | ollie cost per day | todo |
| 16 | 2 | S2 | best | Best Fresh Dog Food Subscriptions in 2026 | best fresh dog food subscription | todo |
| 17 | 2 | S2 | review | JustFoodForDogs Review: Fresh Food, Pantry & Meals | justfoodfordogs review | todo |
| 18 | 2 | S2 | best | Best Raw Dog Food Delivery Services for 2026 | best raw dog food delivery | todo |
| 19 | 3 | S3 | best | Best Automatic Litter Boxes in 2026: Litter-Robot vs the Rest | best automatic litter box | todo |
| 20 | 3 | S3 | alternatives | Best Litter-Robot Alternatives (Cheaper Fully-Auto Boxes) | litter-robot alternatives | todo |
| 21 | 3 | S3 | vs | Furbo vs Petcube: Which Pet Camera Is Worth Buying? | furbo vs petcube | todo |
| 22 | 3 | S3 | best | Best Dog GPS Trackers: Tractive vs Pawfit vs Whistle | best dog gps tracker | todo |
| 23 | 4 | S4 | best | Best Dog Grooming Clippers for Home Use (Wahl & More) | best dog clippers for home | todo |
| 24 | 4 | S4 | tutorial | How to Deshed a Double-Coat Dog at Home (Tools Included) | how to deshed a dog | todo |
| 25 | 4 | S4 | best | Best Dog Grooming Kits: Slicker Brushes, Nail Grinders & More | best dog grooming kit | todo |
| 26 | 5 | S5 | pricing | Veterinary Software Pricing Compared: Gingr vs MoeGo vs DaySmart | veterinary software pricing | todo |
| 27 | 5 | S5 | alternatives | Best PetDesk Alternatives for Small Vet Clinics | petdesk alternatives | todo |
| 28 | 5 | S5 | review | VetRec AI Scribe Review: Automated SOAP Notes Tested | vetrec review | todo |

类型覆盖：best×8、review×8、vs×3、pricing×3、alternatives×2、tutorial×2、coupon×2 = 28。

## 起草顺序（每轮 1-2 篇）

1. #1–#7（S1，直接用现有 build.py/brands.json 架构扩）
2. #8–#13（S1b，需新站骨架：复制 S1 架构，改品牌数据）
3. #14–#18（S2）
4. #19–#22（S3）
5. #23–#25（S4）
6. #26–#28（S5）

## 事实来源要求（每篇执行）

- 价格/条款/折扣：只引用品牌官网、官方条款页、官方帮助中心；标注 URL + 复核日期。
- 官方页没写的一律写 "not published on the official site"，不估算。
- 联盟佣金等内部信息不进页面正文。
