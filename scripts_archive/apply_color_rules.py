import re

def update_colors():
    # 1. Update style.css
    with open('style.css', 'r', encoding='utf-8') as f:
        css = f.read()
    
    css = css.replace('background-color: #caebd8;', 'background-color: #ffffff;')
    
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    
    # 2. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Full-width backgrounds -> #ffffff
    # Hero
    html = html.replace('class="relative bg-[#caebd8]', 'class="relative bg-[#ffffff]')
    # About
    html = html.replace('<section class="relative py-20 lg:py-32 flex flex-col items-center justify-center overflow-hidden"\n            style="background:#caebd8;">', 
                        '<section class="relative py-20 lg:py-32 flex flex-col items-center justify-center overflow-hidden"\n            style="background:#ffffff;">')
    html = html.replace('<section class="relative py-20 lg:py-32 flex flex-col items-center justify-center overflow-hidden" style="background:#caebd8;">', 
                        '<section class="relative py-20 lg:py-32 flex flex-col items-center justify-center overflow-hidden" style="background:#ffffff;">')
    
    # Services
    html = html.replace('style="background:#f5fef8;"', 'style="background:#ffffff;"')
    
    # Reviews
    html = html.replace('<section class="relative py-16 md:py-24 overflow-hidden" style="background:#caebd8;">',
                        '<section class="relative py-16 md:py-24 overflow-hidden" style="background:#ffffff;">')

    # Body copy text colors -> #1a3528
    html = html.replace('text-[#668e78]/70', 'text-[#1a3528]/80')
    html = html.replace('text-[#668e78]/80', 'text-[#1a3528]/80')

    # Pill tags -> Mint Green (#caebd8) background with Forest Green text
    html = html.replace('style="background:#d49813; color:#668e78;"', 'style="background:#caebd8; color:#1a3528;"')
    html = html.replace('style="background:#ffffff; color:#668e78;"', 'style="background:#caebd8; color:#1a3528;"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Color updates applied to style.css and index.html")

update_colors()
