import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Scrolling Banner Icons
# Find the scrolling banner section
banner_start = text.find('<div class="scrolling-track')
banner_end = text.find('<!-- ABOUT / TRUST SECTION -->')
if banner_start != -1 and banner_end != -1:
    banner_section = text[banner_start:banner_end]
    banner_section = banner_section.replace('text-[#d49813]', 'text-[#825c3e]')
    text = text[:banner_start] + banner_section + text[banner_end:]

# 2. Section Pill Tags
# They currently have: bg-[#caebd8] text-[#1a3528]
# The user wants them to be Earth Brown text: text-[#825c3e]
text = text.replace('bg-[#caebd8] text-[#1a3528]', 'bg-[#caebd8] text-[#825c3e]')

# 3. Process/Review Card Borders
# "How It Works" section
# The cards probably have border-white/5. Let's find the section.
process_start = text.find('How It Works')
if process_start != -1:
    # Look back to the start of the section
    sec_start = text.rfind('<section', 0, process_start)
    sec_end = text.find('</section>', process_start)
    if sec_start != -1 and sec_end != -1:
        process_sec = text[sec_start:sec_end]
        process_sec = process_sec.replace('border-white/5', 'border-[#825c3e]/15')
        text = text[:sec_start] + process_sec + text[sec_end:]

# Reviews section
# Review cards need "border border-[#825c3e]/15" added.
# They are currently something like: class="... rounded-3xl ... shadow-lg hover:shadow-xl"
# Let's find the reviews section
reviews_start = text.find('REVIEWS SECTION')
if reviews_start != -1:
    sec_end = text.find('</section>', reviews_start)
    if sec_end != -1:
        reviews_sec = text[reviews_start:sec_end]
        # The review cards have class="group relative p-6 sm:p-6 lg:p-8 rounded-3xl h-full flex flex-col justify-between transition-all duration-500 hover:-translate-y-2 shadow-lg hover:shadow-xl"
        # We need to add "border border-[#825c3e]/15"
        reviews_sec = reviews_sec.replace('shadow-lg hover:shadow-xl"', 'shadow-lg hover:shadow-xl border border-[#825c3e]/15"')
        text = text[:reviews_start] + reviews_sec + text[sec_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Earth Brown accents applied.")
