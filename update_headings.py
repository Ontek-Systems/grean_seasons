import os
import glob
import re

html_files = glob.glob('pages/**/*.html', recursive=True) + ['index.html']

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. Remove gold accent line INSIDE headings
    def heading_replacer(match):
        tag = match.group(1) # h2 or h3
        classes = match.group(2)
        inner = match.group(3)
        
        inner = re.sub(r'\s*<span class="(?:title-underline-anim )?block[^>]*bg-\[\#(?:db9f1b|d49813)\][^>]*></span>\s*\n?', '', inner)
        
        classes = re.sub(r'\bfont-(semibold|bold)\b', 'font-black', classes)
        if 'font-black' not in classes:
            classes += ' font-black'
            
        classes = re.sub(r'\btext-\d+xl\b', '', classes)
        classes = re.sub(r'\b(?:sm|md|lg|xl|2xl):text-\d+xl\b', '', classes)
        classes = re.sub(r'\b(?:sm|md|lg|xl|2xl):text-\[.*?\]\b', '', classes)
        classes += ' text-4xl sm:text-5xl'
        
        classes = re.sub(r'\bleading-\S+\b', 'leading-[1.15]', classes)
        if 'leading-[1.15]' not in classes:
            classes += ' leading-[1.15]'
            
        classes = re.sub(r'\bmb-\d+\b', 'mb-[22px]', classes)
        if 'mb-[22px]' not in classes:
            classes += ' mb-[22px]'
            
        if 'hover:text-[#db9f1b]' not in classes:
            classes += ' hover:text-[#db9f1b]'
        if 'transition-colors' not in classes:
            classes += ' transition-colors'
        if 'duration-500' not in classes:
            classes += ' duration-500'
            
        classes = re.sub(r'\s+', ' ', classes).strip()
        
        return f'<{tag} class="{classes}">{inner}</{tag}>'

    content = re.sub(r'<(h[23])([^>]*)>((?:(?!</\1>).)*?<span class="(?:title-underline-anim )?block[^>]*bg-\[\#(?:db9f1b|d49813)\][^>]*></span>(?:(?!</\1>).)*?)</\1>', heading_replacer, content, flags=re.DOTALL)

    # 3. Remove freestanding gold lines
    content = re.sub(r'\s*<div class="w-12 h-1 md:h-\[2px\] bg-\[\#(?:db9f1b|d49813)\][^>]*></div>\s*\n?', '', content)
    content = re.sub(r'\s*<div class="w-12 h-1 bg-\[\#(?:db9f1b|d49813)\][^>]*></div>\s*\n?', '', content)

    # 4. Replace Taglines
    tagline_counter = 1
    def tagline_replacer(match):
        global tagline_counter
        num_str = f"{tagline_counter:02d}"
        tagline_counter += 1
        
        return f'<span class="word-mask-inner inline-block font-body font-extrabold text-xl tracking-widest uppercase mb-8 cursor-default text-[#1a3528] hover:text-[#db9f1b] transition-colors duration-300" style="transition-delay: 50ms;">\n                            <span class="border-b-[1.5px] border-current pb-0.5">{num_str}</span>\n                        </span>'

    # Pattern matches old taglines
    p_old = r'<span\s+class="[^"]*inline-block[^"]*tracking-widest[^"]*uppercase[^"]*"[^>]*>[\s\S]*?</span>'
    content = re.sub(p_old, tagline_replacer, content)
    
    with open(file, 'w') as f:
        f.write(content)

print("Headings and taglines updated.")
