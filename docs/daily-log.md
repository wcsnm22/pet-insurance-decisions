# Daily log — 发布日志（DAILY 任务与推进器共用的唯一去重依据）

格式：`日期 | 站 | 页面 slug | URL | 用了哪个缺口 | 当时的 commit 标题`
去重规则：**同一个缺口不许写第二篇；同一天已有条目 = 今天主线已完成。**

> **生成方式（2026-09-28）**：本文件由脚本 `gen_daily_log.py` 从四个仓库的 `site/*.html` 实际存在文件 + `git log --diff-filter=A` 首次入库日期自动生成，**不是手写的**。
> 每行都能追溯到一次 git 提交；表中不存在任何磁盘上找不到的页面。
> 页面首次入库日期 = 该页在本仓库的首次出现日期，即发布日期口径（构建产物随源文件同次入库）。


## 2026-09-24

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| P1 | fetch-pet-insurance | https://furadvisor.com/fetch-pet-insurance | — | v1: home + 3 brand pages + about/privacy/contact, facts sourced to official sites (checked 2026-09-24) |
| P1 | lemonade-pet-insurance | https://furadvisor.com/lemonade-pet-insurance | — | v1: home + 3 brand pages + about/privacy/contact, facts sourced to official sites (checked 2026-09-24) |
| P1 | spot-pet-insurance | https://furadvisor.com/spot-pet-insurance | — | v1: home + 3 brand pages + about/privacy/contact, facts sourced to official sites (checked 2026-09-24) |

## 2026-09-25

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| P1 | best-pet-insurance | https://furadvisor.com/best-pet-insurance | — | feat: guides layer (data/articles.json) + #1 Best Pet Insurance 2026 comparison |
| P1 | how-to-submit-a-pet-insurance-claim | https://furadvisor.com/how-to-submit-a-pet-insurance-claim | S1 | feat: guides #6 how to submit a claim + #7 promo code & discount guide; publish S1 schedule rows |
| P1 | lemonade-vs-spot | https://furadvisor.com/lemonade-vs-spot | — | feat: guides #4 pet insurance cost + #5 Lemonade vs Spot; recheck all sources 2026-09-25 |
| P1 | pet-insurance-claim-denied | https://furadvisor.com/pet-insurance-claim-denied | — | content: claim-denied appeal guide (Lemonade/Spot/Fetch, official sources); BreadcrumbList schema; appeal-flow SVG |
| P1 | pet-insurance-cost | https://furadvisor.com/pet-insurance-cost | — | feat: guides #4 pet insurance cost + #5 Lemonade vs Spot; recheck all sources 2026-09-25 |
| P1 | pet-insurance-promo-code | https://furadvisor.com/pet-insurance-promo-code | S1 | feat: guides #6 how to submit a claim + #7 promo code & discount guide; publish S1 schedule rows |
| S1b | 1800petmeds-online-pharmacy | site:pet-health/1800petmeds-online-pharmacy | S1b | feat: S1b pet health site skeleton - 4 brand pages (Vetster, 1-800-PetMeds, Cosequin, Embark), sourced facts, build/selfcheck with official-host white |
| S1b | cosequin-joint-supplement | site:pet-health/cosequin-joint-supplement | S1b | feat: S1b pet health site skeleton - 4 brand pages (Vetster, 1-800-PetMeds, Cosequin, Embark), sourced facts, build/selfcheck with official-host white |
| S1b | embark-dna-test | site:pet-health/embark-dna-test | S1b | feat: S1b pet health site skeleton - 4 brand pages (Vetster, 1-800-PetMeds, Cosequin, Embark), sourced facts, build/selfcheck with official-host white |
| S1b | vetster-online-vet | site:pet-health/vetster-online-vet | S1b | feat: S1b pet health site skeleton - 4 brand pages (Vetster, 1-800-PetMeds, Cosequin, Embark), sourced facts, build/selfcheck with official-host white |

## 2026-09-26

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| S1b | best-joint-supplement-for-dogs | site:pet-health/best-joint-supplement-for-dogs | — | content: schedule #10 buy pet prescription meds online + #11 best joint supplements for dogs; official sources re-read 2026-09-26; two SVG infographic |
| S1b | buy-pet-prescription-meds-online | site:pet-health/buy-pet-prescription-meds-online | — | content: schedule #10 buy pet prescription meds online + #11 best joint supplements for dogs; official sources re-read 2026-09-26; two SVG infographic |
| S1b | embark-discount-code | site:pet-health/embark-discount-code | — | content: schedule #12 Embark DNA test review + #13 Embark discount code; official sources re-read 2026-09-26 (embarkvet.com product/feature pages + he |
| S1b | embark-dna-test-review | site:pet-health/embark-dna-test-review | — | content: schedule #12 Embark DNA test review + #13 Embark discount code; official sources re-read 2026-09-26 (embarkvet.com product/feature pages + he |
| S1b | online-vet-vs-in-person | site:pet-health/online-vet-vs-in-person | — | content: schedule #8 Vetster review + #9 online vet vs in-person; official-source facts checked 2026-09-26; two SVG infographics; selfcheck per-item d |
| S1b | vetster-review | site:pet-health/vetster-review | — | content: schedule #8 Vetster review + #9 online vet vs in-person; official-source facts checked 2026-09-26; two SVG infographics; selfcheck per-item d |
| S2 | justfoodfordogs-fresh-food | site:pet-fresh-food/justfoodfordogs-fresh-food | S2 | S2 fresh food site skeleton: 3 brand pages, 45 sourced facts, build+selfcheck PASS |
| S2 | ollie-cost-per-day | site:pet-fresh-food/ollie-cost-per-day | S2 | S2 articles #14 ollie-vs-the-farmers-dog and #15 ollie-cost-per-day: 34 facts + 20 FAQs from ollie.com/thefarmersdog.com reads of 2026-09-26, 2 self-d |
| S2 | ollie-fresh-dog-food | site:pet-fresh-food/ollie-fresh-dog-food | S2 | S2 fresh food site skeleton: 3 brand pages, 45 sourced facts, build+selfcheck PASS |
| S2 | ollie-vs-the-farmers-dog | site:pet-fresh-food/ollie-vs-the-farmers-dog | S2 | S2 articles #14 ollie-vs-the-farmers-dog and #15 ollie-cost-per-day: 34 facts + 20 FAQs from ollie.com/thefarmersdog.com reads of 2026-09-26, 2 self-d |
| S2 | the-farmers-dog | site:pet-fresh-food/the-farmers-dog | S2 | S2 fresh food site skeleton: 3 brand pages, 45 sourced facts, build+selfcheck PASS |

## 2026-09-27

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| S2 | best-fresh-dog-food-subscriptions | site:pet-fresh-food/best-fresh-dog-food-subscriptions | S2 | S2 article #16 best-fresh-dog-food-subscriptions: 28 facts + 10 FAQs from ollie.com/thefarmersdog.com/justfoodfordogs.com reads of 2026-09-27, 1 self- |
| S2 | best-raw-dog-food-delivery | site:pet-fresh-food/best-raw-dog-food-delivery | S2 | S2 article #18 best-raw-dog-food-delivery: 20 facts + 10 FAQs from wefeedraw.com, darwinspet.com and meetmaev.com pages read 2026-09-27, 1 self-drawn  |
| S2 | justfoodfordogs-review | site:pet-fresh-food/justfoodfordogs-review | S2 | S2 article #17 justfoodfordogs-review: 15 facts + 10 FAQs from justfoodfordogs.com product pages, FAQ, promo terms and ToS read 2026-09-27, 1 self-dra |
| S3 | best-automatic-litter-box | site:smart-pet-device/best-automatic-litter-box | S3 | S3 article #19 best-automatic-litter-box: 4-way comparison of Litter-Robot, CatGenie, PETKIT and Meowant with 24 facts + 10 FAQs read from the four of |
| S3 | furbo | site:smart-pet-device/furbo | — | track built site/ like the sibling repos (10 pages, canonical host smart-pet-device-decisions.pages.dev) |
| S3 | litter-robot | site:smart-pet-device/litter-robot | — | track built site/ like the sibling repos (10 pages, canonical host smart-pet-device-decisions.pages.dev) |
| S3 | pawfit | site:smart-pet-device/pawfit | — | track built site/ like the sibling repos (10 pages, canonical host smart-pet-device-decisions.pages.dev) |
| S3 | petcube | site:smart-pet-device/petcube | — | track built site/ like the sibling repos (10 pages, canonical host smart-pet-device-decisions.pages.dev) |
| S3 | tractive | site:smart-pet-device/tractive | — | track built site/ like the sibling repos (10 pages, canonical host smart-pet-device-decisions.pages.dev) |

## 2026-09-28

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| P1 | pet-insurance-claim-filing-deadline | https://furadvisor.com/pet-insurance-claim-filing-deadline | G4 | content: pet-insurance-claim-filing-deadline (gap G4) - official filing windows side by side: Spot 270 days (FAQ + CA/AZ sample policy contract senten |
| P1 | pet-insurance-cost-by-brand | https://furadvisor.com/pet-insurance-cost-by-brand | G1 | content: pet-insurance-cost-by-brand (gap G1) - every published price from Lemonade/Spot/Fetch with assumption + brand date stamp + read date; 19 fact |
| P1 | pet-insurance-waiting-periods | https://furadvisor.com/pet-insurance-waiting-periods | — | content: pet-insurance-waiting-periods (G2) - 17 facts / 9 FAQ / 9-row state-aware comparison + SVG chart, all sources rechecked 2026-09-28; selfcheck |
| P1 | pet-insurance-wellness-add-on | https://furadvisor.com/pet-insurance-wellness-add-on | G3 | content: pet-insurance-wellness-add-on (gap G3) - four official wellness benefit schedules compared item by item: Lemonade counts, Spot Gold/Platinum  |
## 2026-09-29

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| P1 | pet-insurance-waiting-periods-by-condition | https://furadvisor.com/pet-insurance-waiting-periods-by-condition | N1 | content: pet-insurance-waiting-periods-by-condition (gap N1) - per-condition waiting-period day counts for GEICO, ASPCA and Allstate read from the bra |


## 2026-09-30

| 站 | 页面 | URL | 缺口 | commit 标题（截断） |
|---|---|---|---|---|
| P1 | exotic-pet-insurance | https://furadvisor.com/exotic-pet-insurance | N12 | content: exotic-pet-insurance (gap N12/old G5) - who actually covers birds, rabbits and reptiles: Nationwide's own exotic page vs GEICO/Allstate/ASPCA dog-and-cat-only pages, 17 facts + 11 FAQs read 2026-09-30 |
| S3 | furbo-vs-petcube | site:smart-pet-device/furbo-vs-petcube | S3 | S3 article #21 furbo-vs-petcube: two-store comparison of camera prices, Nanny/Care plan rates and return/warranty terms, |
| S3 | litter-robot-alternatives | site:smart-pet-device/litter-robot-alternatives | S3 | S3 article #20 litter-robot-alternatives: 4-way cheaper-alternative comparison with 27 facts + 10 FAQs read from litter- |
---

## 统计

- 总页数（四个站，磁盘上实际存在且已入库）：**41**
- P1=15，S1b=10，S2=8，S3=8
- P1（furadvisor.com，本命令主站）：**15 篇**
- 按日：**2026-09-24:3，2026-09-25:10，2026-09-26:11，2026-09-27:9，2026-09-28:4，2026-09-29:1，2026-09-30:3**
- git 历史中曾出现但磁盘上已不存在的页面（孤儿）：**0**（脚本已核）
