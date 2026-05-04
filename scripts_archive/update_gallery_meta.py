import re
import os

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace <style type="text/tailwindcss"> block colors
style_block = """        @theme {
            --color-brand-dark:   #668e78;
            --color-brand-ocean:  #668e78;
            --color-brand-bronze: #d49813;
            --color-brand-alice:  #caebd8;
            --color-brand-beige:  #caebd8;
            --color-brand-text:   #1a3528;
            --font-heading: 'Marcus Traianus', 'Cinzel', Georgia, serif;
            --font-body:    'DM Sans', sans-serif;
        }"""
text = re.sub(r'@theme \{.*?(?=\})\}', style_block, text, flags=re.DOTALL)

# Replace placeholders
text = text.replace('<title>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</title>', '<title>Project Gallery | Green Seasons – Professional Grounds & Garden Maintenance</title>')
text = text.replace('https://www.jboutdoorservices.co.uk/', 'https://www.greenseasons.co.uk/')
text = text.replace('JB Outdoor Services Ltd', 'Green Seasons')
text = text.replace('JB Outdoor Services', 'Green Seasons')
text = text.replace('Wincanton and Somerset', 'South Oxfordshire')
text = text.replace('Somerset', 'South Oxfordshire')

# The hero text placeholders
text = text.replace('[TEXT_PLACEHOLDER]', 'Our Portfolio', 1)
text = text.replace('[TEXT_PLACEHOLDER]', 'Green Seasons Gallery', 1)
text = text.replace('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 'Explore our recent grounds and garden maintenance projects across South Oxfordshire. From lawn renovations to full site clearances, see the quality of our work.')

# Write updated text back
with open('pages/gallery.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated gallery.html metadata and theme")
