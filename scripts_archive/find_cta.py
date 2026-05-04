import re

with open('pages/contact.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'(<section[^>]*>.*?<\/section>)', text, flags=re.DOTALL)
for i, m in enumerate(matches):
    if "CTA" in m or "Call" in m or "contact" in m.lower():
        print(f"Section {i} looks like CTA. Length: {len(m)}")
        print(m[:200])

