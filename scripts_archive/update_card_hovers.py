import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace inline JS hover states
# Case 1: onmouseenter="this.style.background='#d49813'"
text = text.replace("this.style.background='#d49813'", "this.style.background='#825c3e'")

# Case 2: onmouseenter='this.style.background="#d49813"' (if any)
text = text.replace('this.style.background="#d49813"', 'this.style.background="#825c3e"')

# Replace Tailwind hover background classes if any are used for bronze on cards
text = text.replace("hover:bg-[#d49813]", "hover:bg-[#825c3e]")

# Also check for bronze decorative elements like lines (they are not clickable)
# The user said "all the card hover", so I'll focus on backgrounds for now.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Card hover colors updated to Earth Brown.")
