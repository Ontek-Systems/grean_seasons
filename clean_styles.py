import os
import glob
import re

html_files = glob.glob('pages/**/*.html', recursive=True) + ['index.html']

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Remove simple .btn-bubble inline styles
    content = re.sub(r'^[ \t]*\.btn-bubble,\s*\.btn-bubble-fill,\s*\.btn-bubble-icon-container\s*\{\s*border-radius:\s*0\s*!important;\s*\}\s*\n', '', content, flags=re.MULTILINE)
    
    # Remove #about-parallax-section .btn-bubble etc
    content = re.sub(r'^[ \t]*#[a-zA-Z0-9_-]+ \.btn-bubble,\s*#[a-zA-Z0-9_-]+ \.btn-bubble-fill,\s*#[a-zA-Z0-9_-]+ \.btn-bubble-icon-container\s*\{[^}]*\}\s*\n', '', content, flags=re.MULTILINE)

    # Some might be multiline without ID
    content = re.sub(r'^[ \t]*\.btn-bubble,\s*\.btn-bubble-fill,\s*\.btn-bubble-icon-container\s*\{[^}]*\}\s*\n', '', content, flags=re.MULTILINE)
    
    with open(file, 'w') as f:
        f.write(content)

print("Styles cleaned.")
