import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<span[^>]*style="background:#caebd8; color:#1a3528;"[^>]*>', text)
for m in matches:
    print(m.group(0))
