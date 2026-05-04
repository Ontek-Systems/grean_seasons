import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Hero: "Get a Free Quote"
text = text.replace(
    'class="btn-bubble btn-primary font-body w-full sm:w-auto text-center shrink-0"',
    'class="btn-bubble btn-light-section font-body w-full sm:w-auto text-center shrink-0"'
)

# 2. About: "Our Story"
text = text.replace(
    '<a href="pages/about.html" class="btn-bubble btn-primary font-body">',
    '<a href="pages/about.html" class="btn-bubble btn-light-section font-body">'
)

# 3. Services: "View All Services"
text = text.replace(
    '<a href="pages/services.html" class="btn-bubble btn-primary font-body">',
    '<a href="pages/services.html" class="btn-bubble btn-light-section font-body">'
)

# 5. "Get in Touch"
text = text.replace(
    '<a href="pages/contact.html" class="btn-bubble btn-primary font-body">\n                            <span class="btn-bubble-fill"></span>\n                            <span class="btn-bubble-text">Get in Touch</span>',
    '<a href="pages/contact.html" class="btn-bubble btn-light-section font-body">\n                            <span class="btn-bubble-fill"></span>\n                            <span class="btn-bubble-text">Get in Touch</span>'
)

# 6. Google Maps: "Get a Free Quote" (wait, text is 'Get a Free Quote', let's check the block)
text = text.replace(
    'class="btn-bubble btn-primary font-body">\n                            <span class="btn-bubble-fill"></span>\n                            <span class="btn-bubble-text">Get a Free Quote</span>',
    'class="btn-bubble btn-light-section font-body">\n                            <span class="btn-bubble-fill"></span>\n                            <span class="btn-bubble-text">Get a Free Quote</span>'
)

# 7. Contact (FAQ section?): "Get a Free Quote"
text = text.replace(
    'class="btn-bubble btn-primary font-body">\n                                <span class="btn-bubble-fill"></span>\n                                <span class="btn-bubble-text">Get a Free Quote</span>',
    'class="btn-bubble btn-light-section font-body">\n                                <span class="btn-bubble-fill"></span>\n                                <span class="btn-bubble-text">Get a Free Quote</span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Buttons replaced.")
