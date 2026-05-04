import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The pills currently have:
# class="... transition-colors duration-300"
# style="background:#caebd8; color:#1a3528;"

# We need to replace style="background:#caebd8; color:#1a3528;" with empty string
# and inject the tailwind classes into the class attribute.

# regex to find the spans
pattern = r'(<span\s+class="[^"]*)(cursor-default)([^"]*")\s*style="background:#caebd8;\s*color:#1a3528;">'

def replacer(match):
    # match.group(1) is up to the class name before cursor-default
    # match.group(2) is cursor-default
    # match.group(3) is the rest of the class attribute
    return match.group(1) + 'cursor-pointer bg-[#caebd8] text-[#1a3528] hover:bg-[#1a3528] hover:text-[#caebd8]' + match.group(3) + '>'

new_html = re.sub(pattern, replacer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Pill tags updated to be hoverable via Tailwind classes.")
