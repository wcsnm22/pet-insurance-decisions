# Insert the "pet insurance claim denied" article into data/articles.json (idempotent).
import json, io, sys

PATH = 'data/articles.json'
Lemonade_howto = 'https://www.lemonade.com/pet/explained/how-to-file-a-pet-insurance-claim'
Lemonade_denials = 'https://www.lemonade.com/pet/insurance-guide/pet-claim-denials/'
Spot_claims = 'https://spotpet.com/submitting-a-claim'
Fetch_pdf = 'https://www.fetchpet.com/PORTALDOCS/FORMS/2016_04/TermsConditions/GPTM_050-XX_0316.pdf'
Fetch_claims = 'https://www.fetchpet.com/claims'
D = '2026-09-25'

article = {
    'slug': 'pet-insurance-claim-denied',
    'nav_label': 'Denied Claim',
    'type': 'tutorial',
    'keyword': 'pet insurance claim denied',
    'title': 'Pet Insurance Claim Denied? How to Appeal with Lemonade, Spot and Fetch',
    'description': 'Pet insurance claim denied - the three official appeal routes side by side: Lemonade in the app with extra vet documents, Spot by email with an around-30-day review, Fetch in writing within 90 days of the denial. Every route, deadline and denial reason from the brands\' own pages, checked 2026-09-25.',
    'h1': 'Pet insurance claim denied: how to appeal it',
    'lede': (
        'Quick answer: yes, you can appeal, and each brand publishes a different route. '
        'Spot wants the appeal by email to service@customer.spotpetins.com - in writing, clearly stating why you or your vet disagree with the initial determination, plus supporting documentation - and says appeals take around 30 days to be reviewed. '
        'Fetch\'s policy terms give you 90 days from the denial to file a written appeal, which triggers an Internal Review by a claims specialist working with a claims manager and, when applicable, Fetch\'s veterinarian, with a written notice of the outcome. '
        'Lemonade tells you to read the denial explanation in its app first, then appeal through the app with additional documentation from your vet. '
        'Whatever the route, your first move is identical: read the stated reason, then get your vet\'s records that answer it.'
    ),
    'stats': [
        {'value': '90 days', 'label': 'Fetch\'s written deadline to appeal after a denial'},
        {'value': '~30 days', 'label': 'Spot\'s published appeal review time'},
        {'value': D, 'label': 'every route and figure rechecked'},
    ],
    'columns': [
        {'name': 'Lemonade', 'url': '/lemonade-pet-insurance'},
        {'name': 'Spot', 'url': '/spot-pet-insurance'},
        {'name': 'Fetch', 'url': '/fetch-pet-insurance'},
    ],
    'rows': [
        {
            'label': 'How to file the appeal',
            'cells': [
                'Read the denial explanation in the Lemonade app, then appeal through the app with additional documentation from your vet; Lemonade adds that its customer support team can help clarify coverage questions',
                'Email your request and supporting documentation to service@customer.spotpetins.com; every appeal must be in writing and clearly state why you or your vet disagree with the initial determination',
                'File the appeal in writing - your policy terms require it and spell out an Internal Review; note that Fetch\'s public help pages do not publish a step-by-step appeal walkthrough (checked 2026-09-25)',
            ],
            'sources': [Lemonade_howto, Spot_claims, Fetch_pdf],
        },
        {
            'label': 'Deadline to appeal after the denial',
            'cells': [
                'No appeal deadline is published on the two Lemonade pages cited here (checked 2026-09-25)',
                'No appeal deadline is published on Spot\'s claims page (checked 2026-09-25)',
                'Within 90 days of the denial, in writing (policy section 2, APPEALS)',
            ],
            'sources': [Lemonade_howto, Spot_claims, Fetch_pdf],
        },
        {
            'label': 'How long the appeal review takes',
            'cells': [
                'Not published on the cited pages (checked 2026-09-25)',
                'Around 30 days to be reviewed; Spot emails you a confirmation once the appeal is received',
                'The policy promises a written notice of the outcome but states no duration (checked 2026-09-25)',
            ],
            'sources': [Lemonade_denials, Spot_claims, Fetch_pdf],
        },
        {
            'label': 'What the appeal must contain',
            'cells': [
                'Additional documentation from your vet, uploaded inside the app',
                'Your written disagreement with the initial determination plus any supporting documentation',
                'A written statement of why you or your vet disagree with the initial determination, plus supporting documentation',
            ],
            'sources': [Lemonade_howto, Spot_claims, Fetch_pdf],
        },
    ],
    'facts': [
        {
            'fact': 'A written appeal within 90 days of the denial triggers an Internal Review',
            'condition': 'Fetch pet health insurance policy, section 2 APPEALS (form GPTM 050 0316, copyright 2016, hosted on fetchpet.com): reviewed by a claims specialist with a claims manager and Fetch\'s veterinarian when applicable; a written notice reports the outcome, and if the original decision is upheld that notice cites the specific reasons and the policy sections relied on',
            'source_url': Fetch_pdf,
            'checked': D,
        },
        {
            'fact': 'Appeals take around 30 days to be reviewed',
            'condition': 'Spot: appeal emailed to service@customer.spotpetins.com with supporting documents; an email confirmation is sent once the appeal is received',
            'source_url': Spot_claims,
            'checked': D,
        },
        {
            'fact': 'The appeal goes through the app with extra vet documents',
            'condition': 'Lemonade: read the denial explanation in the app first - the page lists the common reasons as pre-existing conditions, waiting periods or excluded treatments - then appeal in the app',
            'source_url': Lemonade_howto,
            'checked': D,
        },
        {
            'fact': 'Waiting periods: 14 days for illnesses, 30 days for orthopedic conditions',
            'condition': 'Lemonade denial reason: a claim filed before the relevant waiting period has passed is not eligible; the same page warns that cancelling and reapplying resets the waiting periods',
            'source_url': Lemonade_denials,
            'checked': D,
        },
        {
            'fact': 'Claims submitted after 90 days are not covered',
            'condition': 'Fetch: the claim itself must reach Fetch within 90 days of the vet visit to be eligible for reimbursement',
            'source_url': Fetch_claims,
            'checked': D,
        },
        {
            'fact': 'Preventive care is not covered unless Fetch Wellness is added - with 30 days from enrollment to add it',
            'condition': 'Fetch claims page: annual exams, dental cleanings, vaccinations, heartworm/flea/tick prevention, spaying/neutering and microchipping are preventive-care examples that need Fetch Wellness',
            'source_url': Fetch_claims,
            'checked': D,
        },
        {
            'fact': 'Pre-existing conditions are not covered - except curable pre-existing conditions',
            'condition': 'Fetch: a condition whose signs or symptoms appear before enrollment or during the waiting period of up to 15 days; claims tied to it are not covered unless it is curable',
            'source_url': Fetch_claims,
            'checked': D,
        },
    ],
    'faqs': [
        {
            'q': 'How do I appeal a denied Lemonade pet insurance claim?',
            'a': 'Lemonade\'s own instructions: first review the explanation in your app to understand why the claim was denied - the common reasons it lists are pre-existing conditions, waiting periods or excluded treatments - then appeal through the app with additional documentation from your vet. Its customer support team can also help clarify coverage questions. The cited page publishes no appeal deadline (checked 2026-09-25).',
            'source_url': Lemonade_howto,
            'checked': D,
        },
        {
            'q': 'How do I appeal a denied Spot pet insurance claim?',
            'a': 'Email your request and supporting documentation to service@customer.spotpetins.com. Spot says every appeal must be sent in writing and must clearly state why you or your vet disagree with the initial determination, and that you will receive an email confirmation once it arrives. Spot publishes the review time as around 30 days (checked 2026-09-25).',
            'source_url': Spot_claims,
            'checked': D,
        },
        {
            'q': 'How do I appeal a denied Fetch pet insurance claim?',
            'a': 'Under your policy\'s section 2 (APPEALS), you may appeal to have the claim undergo an Internal Review. The request must be in writing within 90 days of the denial and should state clearly why you or your vet disagree with the initial determination, with supporting documentation. A claims specialist reviews it with a claims manager and, when applicable, Fetch\'s veterinarian, and you get a written notice of the outcome; if the original decision is upheld, that notice cites the specific reasons and the policy sections relied on (checked 2026-09-25).',
            'source_url': Fetch_pdf,
            'checked': D,
        },
        {
            'q': 'Why was my Lemonade pet insurance claim denied?',
            'a': 'Lemonade\'s denial guide names the usual causes: the condition was considered pre-existing or bilateral; the relevant waiting period (14 days for illnesses, 30 days for orthopedic conditions) had not passed; or you went beyond the per-item limits in your Preventative Care package. It also warns that cancelling and reapplying later resets waiting periods and can enlarge the list of conditions treated as pre-existing (checked 2026-09-25).',
            'source_url': Lemonade_denials,
            'checked': D,
        },
        {
            'q': 'What reasons does Fetch give for not approving claims?',
            'a': 'Fetch\'s claims page lists them: preventive care without Fetch Wellness added, pre-existing conditions (unless curable), and claims submitted after the 90-day window - plus its note that a pre-existing condition is one with signs or symptoms before enrollment or during the waiting period of up to 15 days. Fetch states it has paid back $500 million+ in claims since 2021 and that only a small percentage of claims are not approved (checked 2026-09-25).',
            'source_url': Fetch_claims,
            'checked': D,
        },
        {
            'q': 'If my claim was denied as pre-existing, will another insurer cover it?',
            'a': 'Lemonade\'s denial guide addresses this directly: chances are the new carrier would not cover those conditions either, and any new conditions or injuries your pet experiences while insured with Lemonade would be considered pre-existing by a new carrier. In other words, switching insurers rarely rescues a denied pre-existing condition (checked 2026-09-25).',
            'source_url': Lemonade_denials,
            'checked': D,
        },
    ],
    'disclaimer': (
        'This page is not affiliated with Lemonade, Spot or Fetch. It repeats only what each brand publishes on its own '
        'claim pages, help pages and policy wording, with the source and check date attached to every figure; policy terms '
        'always govern and your own appeal timeline will differ. Facts last checked 2026-09-25.'
    ),
    'blocks': [
        {
            'type': 'section',
            'h2': 'What to do in the first 24 hours',
            'html': (
                '<p>The denial notice tells you which category of problem the brand thinks it has. Before you write anything, do these four things:</p>'
                '<ol>'
                '<li><strong>Read the stated reason.</strong> Match it to one of the categories the brands themselves publish - pre-existing condition, waiting period, exclusion or paperwork - because each one needs a different kind of answer.</li>'
                '<li><strong>Pull your pet\'s complete records.</strong> Ask your vet for the full file, including the date symptoms were first noted; pre-existing decisions turn on those dates, not on opinion.</li>'
                '<li><strong>Write the disagreement as facts.</strong> Say why you or your vet disagree with the initial determination - that is the exact wording both Spot and Fetch require - and attach the records that back it up.</li>'
                '<li><strong>Send it on the official route for your brand</strong> - in the Lemonade app, by email to Spot, or in writing within Fetch\'s 90-day window.</li>'
                '</ol>'
                '<img src="/assets/appeal-flow.svg" alt="Appeal flow: read the denial reason, collect vet records, write the disagreement with documents, send it through the brand\'s official route" width="100%">'
            ),
        },
        {'type': 'compare'},
        {
            'type': 'section',
            'h2': 'Why claims get denied - the brands\' own list',
            'html': (
                '<p><strong>Lemonade</strong> publishes a dedicated denials page. Its usual causes: a condition considered pre-existing or bilateral; a waiting period that had not passed (14 days for illnesses, 30 days for orthopedic conditions); or per-item limits exceeded in a Preventative Care package. It also says plainly that moving to another carrier would likely not cover those same conditions, and that any new condition appearing while you are insured would be pre-existing at the next carrier.</p>'
                '<p><strong>Fetch</strong> lists its non-approval reasons on the claims page: preventive care without Fetch Wellness (you have 30 days from enrollment to add it), pre-existing conditions unless curable, and claims filed after 90 days from the vet visit.</p>'
                '<p><strong>Spot</strong> does not publish a denial-reason list on its claims page; what it does publish is the appeal route itself - and an initial determination you are explicitly allowed to contest in writing.</p>'
                '<p class="muted">Every sentence above is linked to the brand page it came from in the tables below; nothing here is guesswork about how any company decides individual claims.</p>'
            ),
        },
        {'type': 'facts'},
        {'type': 'faqs'},
        {'type': 'cards'},
    ],
}

data = json.loads(io.open(PATH, encoding='utf-8').read())
slugs = [a['slug'] for a in data['articles']]
if article['slug'] in slugs:
    print('already present, no change')
    sys.exit(0)
data['articles'].append(article)
io.open(PATH, 'w', encoding='utf-8', newline='\n').write(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
print('inserted, total articles:', len(data['articles']))
