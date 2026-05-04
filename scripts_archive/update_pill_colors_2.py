import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the current classes for pill tags
# Current: bg-[#caebd8] text-white hover:bg-[#825c3e] hover:text-white
# New: bg-[#caebd8] text-[#1a3528] hover:bg-[#825c3e] hover:text-white
old_classes = "bg-[#caebd8] text-white hover:bg-[#825c3e] hover:text-white"
new_classes = "bg-[#caebd8] text-[#1a3528] hover:bg-[#825c3e] hover:text-white"

if old_classes in html:
    html = html.replace(old_classes, new_classes)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced successfully.")
else:
    print("Could not find the old classes in index.html.")
