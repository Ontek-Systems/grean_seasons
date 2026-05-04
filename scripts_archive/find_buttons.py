import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all buttons with btn-bubble
matches = re.finditer(r'<a[^>]*class="[^"]*btn-bubble[^"]*"[^>]*>.*?</a>', text, re.DOTALL)
for m in matches:
    print("MATCH START")
    print(m.group(0))
    print("MATCH END\n")
