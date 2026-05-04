with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

patches = {
    420: '                            <svg class="w-4 h-4 shrink-0 text-[#d49813]" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a8 8 0 100 16A8 8 0 0010 2zm1 11H9V9h2v4zm0-6H9V5h2v2z"/></svg>\n                            <span>One-Off &amp; Site Clearance Works</span>\n',
    694: '                        Everything Your Outdoor Space Needs\n',
    774: '                            Professional herbicide applications for lawns and hard surfaces, plus one-off site clearance visits to restore overgrown properties.\n',
    954: '                                    Free Site Assessment</h3>\n',
    981: '                                    Receive a Clear, Fair Quote</h3>\n',
    1008: '                                    Consistent, Professional Results</h3>\n',
    1197: '                                            "Absolutely transformed our overgrown garden. Brilliant service from start to finish \u2014 Tim really knows his craft."\n',
    1317: '                                            "Green Seasons took on our long-neglected grounds and had them looking superb within a single visit. Exceptional work."\n',
    1400: '                                            "Tim went above and beyond with our full lawn renovation. The before and after comparison is truly remarkable."\n',
    1520: '                                            "Brilliant end-to-end service. The garden looks absolutely stunning now. Would recommend Green Seasons to anyone."\n',
    1691: '                                <span class="btn-bubble-text">Get a Free Quote</span>\n',
    1963: '                            Ready to Get Started?\n',
    1968: '                            Let\'s Transform Your Outdoor Space\n',
    1973: '                            Contact Green Seasons today for a free, no-obligation quote. Serving South Oxfordshire, Monday to Friday, 8\u202fAM\u20135\u202fPM.\n',
    1978: '                             <span class="btn-bubble-text font-bold tracking-wide">Request a Free Quote</span>\n',
}

# FAQ questions at lines 1713,1733,1753,1773,1793,1813,1833,1853
faq_qs = [
    'What areas do you cover?',
    'Do you offer one-off visits or only ongoing contracts?',
    'What types of clients do you work with?',
    'Are you fully insured?',
    'Can you carry out weed control on hard surfaces?',
    'How do I get a quote?',
    'What is included in a grounds maintenance contract?',
    'What hours do you operate?',
]
faq_q_lines = [1713, 1733, 1753, 1773, 1793, 1813, 1833, 1853]

for i, ln in enumerate(faq_q_lines):
    idx = ln - 1
    original = lines[idx]
    # Replace the [LONG_TEXT_PLACEHOLDER_DESCRIPTION] within the span
    lines[idx] = original.replace('[LONG_TEXT_PLACEHOLDER_DESCRIPTION]', faq_qs[i])

for ln, content in patches.items():
    lines[ln - 1] = content

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Patch complete.")
