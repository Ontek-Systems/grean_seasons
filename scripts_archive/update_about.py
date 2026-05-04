import re

with open('pages/about.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace pill buttons
pill_regex = r'<span\s+class="inline-block\s+px-5\s+py-1\.5\s+font-body\s+font-semibold\s+text-sm\s+tracking-widest\s+uppercase\s+rounded-full\s+mb-6\s+cursor-default.*?"\s*style=".*?".*?>\s*(.*?)\s*</span>'

replacement_pill = r'<span class="inline-block px-5 py-1.5 font-body font-bold text-sm tracking-widest uppercase rounded-full mb-6 cursor-default bg-[#caebd8] text-[#1a3528] hover:bg-[#825c3e] hover:text-white transition-colors duration-300" style="box-shadow: 0 4px 16px rgba(202, 235, 216, 0.30);">\n                            \1\n                        </span>'

# Because of indentation differences, we might have to use a function
def pill_sub(match):
    content = match.group(1).strip()
    return f'<span class="inline-block px-5 py-1.5 font-body font-bold text-sm tracking-widest uppercase rounded-full mb-6 cursor-default bg-[#caebd8] text-[#1a3528] hover:bg-[#825c3e] hover:text-white transition-colors duration-300" style="box-shadow: 0 4px 16px rgba(202, 235, 216, 0.30);">{content}</span>'

text = re.sub(pill_regex, pill_sub, text, flags=re.DOTALL)


# Replace Cards
# <div class="group flex flex-col items-center text-center p-8 md:p-12 rounded-3xl hover:-translate-y-2 cursor-default border border-transparent w-[280px] md:w-[320px] shrink-0 transition-all duration-500"
#     style="background:#1a3528;"
#     onmouseenter="this.style.background='#d49813';" onmouseleave="this.style.background='#1a3528';">
card_class_regex = r'class="group flex flex-col items-center text-center p-8 md:p-12 rounded-3xl hover:-translate-y-2 cursor-default border border-transparent w-\[280px\] md:w-\[320px\] shrink-0 transition-all duration-500"'
new_card_class = r'class="group flex flex-col items-center text-center p-8 md:p-12 rounded-3xl hover:-translate-y-2 shadow-lg hover:shadow-xl border border-[#825c3e]/15 cursor-default w-[280px] md:w-[320px] shrink-0 transition-all duration-500"'
text = text.replace(
    'class="group flex flex-col items-center text-center p-8 md:p-12 rounded-3xl hover:-translate-y-2 cursor-default border border-transparent w-[280px] md:w-[320px] shrink-0 transition-all duration-500"',
    'class="group flex flex-col items-center text-center p-8 md:p-12 rounded-3xl hover:-translate-y-2 shadow-lg hover:shadow-xl border border-[#825c3e]/15 cursor-default w-[280px] md:w-[320px] shrink-0 transition-all duration-500"'
)

text = text.replace("style=\"background:#1a3528;\"", "style=\"background:#668e78;\"")
text = text.replace("onmouseenter=\"this.style.background='#d49813';\" onmouseleave=\"this.style.background='#1a3528';\"", "onmouseenter=\"this.style.background='#825c3e';\" onmouseleave=\"this.style.background='#668e78';\"")

# Card Icon Colors
# <div class="flex items-center justify-center mb-6 md:mb-8 group-hover:-translate-y-2 transition-all duration-400 text-[#d49813] group-hover:text-[#1a3528]">
text = text.replace('text-[#d49813] group-hover:text-[#1a3528]', 'text-[#d49813] group-hover:text-white')

# Card Headings
# <h3 class="font-heading text-2xl md:text-3xl font-bold text-white group-hover:text-[#1a3528] transition-colors duration-400 mb-4">
text = text.replace('text-white group-hover:text-[#1a3528]', 'text-white')

# Card Paragraphs
# <p class="font-body text-white/90 group-hover:text-[#1a3528]/90 transition-colors duration-400 leading-relaxed text-base md:text-lg">
text = text.replace('text-white/90 group-hover:text-[#1a3528]/90', 'text-white/80 group-hover:text-white')

with open('pages/about.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated about.html pills and cards")
