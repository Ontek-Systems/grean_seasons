import re

with open('components/header.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix \r\n rendering issue
text = text.replace('\\r\\n', '')

# Fix closing divs correctly
# Find the exact sequence of 4 closing divs and replace with 3
bad_divs = """                        </div>

                    </div>
                    </div>
                </div>
            </div>

            <a href="pages/about.html\""""

good_divs = """                        </div>

                    </div>
                </div>
            </div>

            <a href="pages/about.html\""""

if bad_divs in text:
    text = text.replace(bad_divs, good_divs)

with open('components/header.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Header cleaned.")
