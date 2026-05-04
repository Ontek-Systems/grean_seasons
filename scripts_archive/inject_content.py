import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── COLOUR SWAP (inline styles & Tailwind arbitrary values) ──────────────────
html = html.replace('#141229', '#668e78')
html = html.replace('#F5F3EE', '#caebd8')
html = html.replace('#e8b01e', '#d49813')
html = html.replace('FAFAFA', 'f5fef8')   # services section bg
html = html.replace('bg-white', 'bg-[#f5fef8]')  # only affects section bg whites - safe enough
# restore btn fill colours that must stay white
html = html.replace('bg-[#f5fef8] flex items-center justify-center text-[#668e78]',
                    'bg-white flex items-center justify-center text-[#668e78]')

# ── ABOUT SECTION ────────────────────────────────────────────────────────────
# Pill
html = html.replace(
    'style="background:#e8b01e; color:#668e78;">\r\n                    [TEXT_PLACEHOLDER]\r\n                </span>\r\n\r\n                <h2\r\n                    class="group font-heading text-4xl',
    'style="background:#d49813; color:#1a3528;">\r\n                    About Green Seasons\r\n                </span>\r\n\r\n                <h2\r\n                    class="group font-heading text-4xl'
)

replacements = [
    # About H2
    (
        'style="background:#d49813; color:#1a3528;">\r\n                    About Green Seasons\r\n                </span>\r\n\r\n                <h2\r\n                    class="group font-heading text-4xl sm:text-5xl md:text-6xl font-bold text-[#668e78] mb-6 leading-tight flex flex-col items-center cursor-default w-full text-center">\r\n                    [TEXT_PLACEHOLDER]',
        'style="background:#d49813; color:#1a3528;">\r\n                    About Green Seasons\r\n                </span>\r\n\r\n                <h2\r\n                    class="group font-heading text-4xl sm:text-5xl md:text-6xl font-bold text-[#668e78] mb-6 leading-tight flex flex-col items-center cursor-default w-full text-center">\r\n                    A Second-Generation Gardener You Can Trust'
    ),
]

for old, new in replacements:
    html = html.replace(old, new)

# ── BULK LOREM IPSUM → GREEN SEASONS COPY ───────────────────────────────────
# We iterate through occurrences and replace them one by one with context-specific copy.
# Use a state counter approach via re.sub with a function.

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'

copy_pool = [
    # About para 1
    'Green Seasons is run by Tim Harris — a second-generation gardener with a deep horticultural background and years of hands-on experience. Based in Kingston Bagpuize, we serve private estates, housing developments, business parks, and local authority spaces across South Oxfordshire.',
    # About para 2
    'Whether you need a one-off site clearance or a long-term maintenance contract, Tim provides a genuinely personal service backed by professional-grade equipment and an unwavering commitment to high standards.',
    # Services intro
    'From weekly maintenance contracts to one-off site clearances, Green Seasons offers a comprehensive range of garden and grounds services tailored to both residential and commercial clients across South Oxfordshire.',
    # Service card 1 body
    'Regular grass cutting, strimming, edging, and comprehensive site presentation to keep your property looking its best year-round.',
    # Service card 1 footer
    'Ideal for residential estates, business parks, and housing developments requiring consistent upkeep.',
    # Service card 2 body
    'Full lawn overhauls, seasonal fertiliser programmes, targeted weed and moss control — designed to improve long-term turf health.',
    # Service card 2 footer
    'Includes aeration, scarification, slow-release fertiliser, and wetting agent applications.',
    # Service card 3 body (digger hire → hedge cutting)
    'Regular trimming, shaping, and dedicated plant care to ensure hedges and shrubs remain tidy, healthy, and well-structured throughout the season.',
    # Service card 3 footer
    'Scheduled visits tailored to your hedge species and growth rate for the best results.',
    # Service card 4 body
    'Safe and professional herbicide applications for lawns and hard surfaces, plus initial site clearance visits to restore overgrown or neglected spaces.',
    # Service card 4 footer
    'All treatments are carried out with certified equipment by a qualified applicator.',
    # Gallery section para
    'Browse our project gallery to see the quality of finish Green Seasons delivers — from lawn renovations and hedge transformations to full garden clearances. The results speak for themselves.',
    # Process step 1 body
    'Call or email Tim and tell us what your outdoor space needs. We\'ll arrange a convenient time for a site visit at no obligation.',
    # Process step 2 body
    'Tim visits your property to assess the current condition, understand the scope of work, and discuss your specific requirements in detail.',
    # Process step 3 body
    'We provide a clear, fair quote covering all agreed works. No hidden charges — just straightforward, transparent pricing.',
    # Process step 4 body
    'Once work begins, expect punctual, professional service on every visit — with consistently high standards maintained throughout the contract.',
    # Process right-panel para
    'We keep things simple so you can focus on enjoying your outdoor space. From first contact to ongoing maintenance, Green Seasons makes the process effortless.',
    # Reviews para
    'Don\'t just take our word for it. Here\'s what our clients across South Oxfordshire say about the Green Seasons service.',
    # Review 1
    '"Tim and his team have been looking after our grounds for over a year now. Consistently immaculate — we couldn\'t be happier with the results."',
    # Review 3
    '"Very professional and thorough. Our lawn has never looked better since Green Seasons took over the maintenance."',
    # Review 4
    '"Reliable, tidy, and always on time. Highly recommended for any garden or grounds work in Oxfordshire."',
    # Review 5
    '"Tim noticed issues with our lawn we hadn\'t even spotted and sorted them quickly. Real expertise and a great attitude."',
    # Review 6
    '"Outstanding grounds maintenance for our business park. Always presentable and professional every single visit."',
    # Review 7
    '"We\'ve used Green Seasons for seasonal treatments and lawn care programmes — the improvement has been remarkable."',
    # Review 8
    '"Cleared our completely neglected garden in a single day. Superb work ethic and a fantastic end result."',
    # Review 9
    '"Green Seasons are our go-to for all garden maintenance. Highly professional, trustworthy, and great value."',
    # Review 10
    '"Punctual, pleasant to deal with, and the quality of work is second to none. Very happy customer!"',
    # Review 11
    '"Tim went above and beyond with our lawn renovation — the before and after difference is remarkable."',
    # Review 12
    '"Brilliant service all round — the garden looks amazing. Would recommend to anyone in South Oxfordshire."',
    # Review request para
    'Happy with your Green Seasons experience? Leave us a review on Google and help other South Oxfordshire residents find a gardener they can trust.',
    # FAQ para
    'Have a question about our services? Here are answers to the questions we\'re asked most often. Can\'t find what you need? Get in touch directly.',
    # Bottom CTA para
    'Contact Green Seasons today for a free, no-obligation quote. We serve South Oxfordshire and surrounding areas — Monday to Friday, 8 AM–5 PM.',
    # Form fallback alert
    'Something went wrong. Please call Tim on 07545 285408.',
]

idx = [0]
def replace_lorem(m):
    if idx[0] < len(copy_pool):
        result = copy_pool[idx[0]]
        idx[0] += 1
        return result
    return m.group(0)

html = re.sub(re.escape(lorem), replace_lorem, html)

# ── [TEXT_PLACEHOLDER] replacements ─────────────────────────────────────────
tp = '[TEXT_PLACEHOLDER]'
text_pool = [
    'About Green Seasons',      # about pill (already replaced above - skip by inserting dummy)
    'A Second-Generation Gardener You Can Trust',   # about h2
    'Years of Experience',      # stat 1 label
    'Google Rating',            # stat 2 label
    'Owner-Led Service',        # stat 3 label
    'Our Story',                # about button
    'Our Services',             # services pill
    'Grounds &amp; Garden Maintenance',  # card 1 h3
    'Included Services',        # card 1 footer label
    'Lawn Care &amp; Renovation',        # card 2 h3
    'What\'s Included',         # card 2 footer label
    'Hedge Cutting &amp; Shrub Maintenance', # card 3 h3
    'Our Approach',             # card 3 footer label
    'Weed Control &amp; Site Clearance', # card 4 h3
    'Certified Applications',   # card 4 footer label
    'View All Services',        # services button
    'Our Work',                 # gallery pill
    'See the Difference We Make', # gallery h2
    'View Our Gallery',         # gallery button
    'Before',                   # ba before label
    'After',                    # ba after label
    'How It Works',             # process pill
    'Simple. Reliable. Professional.', # process h2
    'Request a Quote',          # process button
    'Get in Touch',             # step 1 h3
    'Free Site Assessment',     # step 2 h3 - already handled by LONG_TEXT
    'Transparent Quotation',    # step 3 h3
    'Ongoing Excellence',       # step 4 h3
    'Client Reviews',           # reviews pill
    'Trusted Across South Oxfordshire', # reviews h2
    'Sarah M. — South Oxfordshire',    # review 1 name
    'James R. — Kingston Bagpuize',    # review 2 name
    'Helen T. — Abingdon',            # review 3 name
    'David K. — Wantage',             # review 4 name
    'Rachel P. — Faringdon',          # review 5 name
    'Claire S. — Didcot',             # review 6 name
    'Tom W. — Grove',                 # review 7 name
    'Emma L. — Steventon',            # review 8 name
    'Andrew H. — Abingdon',           # review 9 name
    'Jenny C. — Oxfordshire',         # review 10 name
    'Paul D. — Carterton',            # review 11 name
    'Lisa F. — Wantage',              # review 12 name
    'Mike B. — Witney',               # review 13 name
    'Share Your Experience',          # review request pill
    'Happy With Our Service?',        # review request h2
    'Leave a Google Review',          # review request button
    'Green Seasons',                  # google text
    'FAQs',                           # faq pill
    'Common Questions',               # faq h2
    'Get a Free Quote',               # faq button
    'Ready to Get Started?',          # cta pill (LONG_TEXT type but short)
    'Let\'s Transform Your Outdoor Space', # cta h2
    'Request a Free Quote',           # cta button
]

tidx = [0]
def replace_tp(m):
    if tidx[0] < len(text_pool):
        result = text_pool[tidx[0]]
        tidx[0] += 1
        return result
    return m.group(0)

html = re.sub(re.escape(tp), replace_tp, html)

# ── LONG_TEXT_PLACEHOLDER_DESCRIPTION ───────────────────────────────────────
ltp = '[LONG_TEXT_PLACEHOLDER_DESCRIPTION]'
long_pool = [
    # Services section H2
    'Everything Your Outdoor Space Needs',
    # Gallery H2
    'See the Difference We Make',
    # Process step 2 h3
    'Free Site Assessment',
    # Process step 3 h3
    'Receive a Clear, Fair Quote',
    # Process step 4 h3
    'Consistent, Professional Results',
    # Review 2 text (FB)
    '"Absolutely transformed our overgrown garden. Brilliant service from start to finish — Tim really knows his craft."',
    # Review 8 text (FB)
    '"Green Seasons took on our long-neglected grounds and had them looking superb within a single visit. Exceptional work."',
    # Review 12 text (Google)
    '"Tim went above and beyond with our full lawn renovation. The before and after comparison is truly remarkable."',
    # FAQ Q1
    'What areas do you cover?',
    # FAQ Q2
    'Do you offer one-off visits or only ongoing contracts?',
    # FAQ Q3
    'What types of clients do you work with?',
    # FAQ Q5
    'Can you carry out weed control on hard surfaces such as driveways and paths?',
    # FAQ Q6
    'How do I get a quote?',
    # FAQ Q8
    'What hours do you operate?',
    # Bottom CTA pill
    'Ready to Get Started?',
]

lidx = [0]
def replace_ltp(m):
    if lidx[0] < len(long_pool):
        result = long_pool[lidx[0]]
        lidx[0] += 1
        return result
    return m.group(0)

html = re.sub(re.escape(ltp), replace_ltp, html)

# ── IMAGE ALT TEXTS ──────────────────────────────────────────────────────────
alts = [
    ('alt="[IMAGE_DESCRIPTION]"\r\n                        decoding="async" class="slide absolute', 'alt="Green Seasons garden maintenance work"\r\n                        decoding="async" class="slide absolute'),
    ('alt="[IMAGE_DESCRIPTION]" loading="lazy"\r\n                        decoding="async" class="slide absolute', 'alt="Lawn care and grounds maintenance Oxfordshire"\r\n                        decoding="async" class="slide absolute'),
]
for old, new in alts:
    html = html.replace(old, new)
html = html.replace('alt="[IMAGE_DESCRIPTION]"', 'alt="Green Seasons professional garden and grounds maintenance"')

# ── FAQ ANSWERS ──────────────────────────────────────────────────────────────
# The FAQ answers are still Lorem ipsum — replace sequentially
faq_answers_lorem = '<span itemprop="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</span>'
faq_answers = [
    'Green Seasons is based in Kingston Bagpuize and covers South Oxfordshire and surrounding areas. If you\'re unsure whether we cover your location, please call or email and we\'ll confirm.',
    'We offer both. Whether you need a single clearance visit to restore a neglected garden or an ongoing maintenance contract, we can accommodate your requirements.',
    'We work with a wide range of clients including private homeowners, landlords, housing developers, business parks, and local authority spaces. No job is too big or too small.',
    'Yes, Green Seasons is fully insured. We carry appropriate public liability insurance for all residential and commercial work.',
    'Yes. We provide professional herbicide treatments on both lawns and hard surfaces including driveways, paths, and patios — all carried out with certified equipment.',
    'Simply call Tim on 07545 285408, email green-seasons@hotmail.com, or use the contact form on this website. We\'ll arrange a free site visit and provide a no-obligation quote.',
    'A grounds maintenance contract typically includes regular grass cutting, strimming, edging, litter clearance, and general site presentation. We tailor the scope to your specific requirements.',
    'We operate Monday to Friday, 8:00 AM – 5:00 PM. Feel free to leave a message outside of these hours and Tim will get back to you as soon as possible.',
]
faidx = [0]
def replace_faq(m):
    if faidx[0] < len(faq_answers):
        result = f'<span itemprop="text">{faq_answers[faidx[0]]}</span>'
        faidx[0] += 1
        return result
    return m.group(0)

html = re.sub(re.escape(faq_answers_lorem), replace_faq, html)

# ── FAQ QUESTION 4 & 7 (were Lorem ipsum in summary, not itemprop) ──────────
lorem_q = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
faq_questions_lorem_idx = [0]
faq_q_replacements = ['Are you fully insured?', 'What is included in a grounds maintenance contract?']
def replace_faq_q(m):
    if faq_questions_lorem_idx[0] < len(faq_q_replacements):
        result = faq_q_replacements[faq_questions_lorem_idx[0]]
        faq_questions_lorem_idx[0] += 1
        return result
    return m.group(0)

html = re.sub(re.escape(lorem_q), replace_faq_q, html)

# ── FORM THANK-YOU MESSAGE ───────────────────────────────────────────────────
html = html.replace(
    "alert('Thank you! Jack will be in touch shortly.');",
    "alert('Thank you! Tim will be in touch shortly.');"
)
html = html.replace(
    "alert('Something went wrong. Please call Jack on +44 7445 064666.');",
    "alert('Something went wrong. Please call Tim on 07545 285408.');"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done. Replacements applied.")
