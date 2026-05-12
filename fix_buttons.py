import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Replace the long tailwind string for dark buttons
    content = re.sub(
        r'class="inline-block border-\[1\.5px\] border-\[#1a3528\].*?rounded-\[1px\]"',
        r'class="btn-primary"',
        content
    )

    # 2. Replace the long tailwind string for light/white buttons (previously beige)
    content = re.sub(
        r'class="inline-block border-\[1\.5px\] border-\[#fff7e6\].*?rounded-\[1px\]"',
        r'class="btn-primary-white"',
        content
    )

    # 3. Find and replace btn-bubble
    # A btn bubble block looks like:
    # <a href="..." class="btn-bubble ...">
    #   <span class="btn-bubble-fill"></span>
    #   <span class="btn-bubble-text">Text</span>
    #   <span class="btn-bubble-icon-container">...</span>
    # </a>
    # We want to extract the href and text, and whether it's btn-dark-bg.
    
    # Regex to find the whole a tag or button tag that has btn-bubble
    pattern = re.compile(
        r'<a([^>]*?)class="([^"]*?btn-bubble[^"]*?)"([^>]*?)>(.*?)</a>',
        re.DOTALL
    )
    
    def replace_bubble(match):
        attrs_before = match.group(1)
        classes = match.group(2)
        attrs_after = match.group(3)
        inner_html = match.group(4)
        
        # Determine if it should be btn-primary or btn-primary-white
        # If it has btn-dark-bg, it was on a light background so it should be dark (btn-primary).
        # Wait, btn-dark-bg meant the button itself has a dark background. So it's a primary button.
        # If it doesn't have btn-dark-bg, maybe it was a light button on a dark background?
        # Let's check the classes.
        is_white = 'btn-light' in classes or 'border-white' in classes or 'text-white' in classes
        
        # In the original system:
        # btn-dark-bg = Forest Green #668e78 background. Used on light backgrounds. -> btn-primary
        # btn-light-bg = #fff7e6 background. Used on dark backgrounds. -> btn-primary-white
        # Let's default to btn-primary, unless we see indications it's on a dark background.
        
        btn_class = 'btn-primary-white' if ('btn-light' in classes or 'text-white' in classes or 'border-white' in classes) else 'btn-primary'
        
        # Sometimes it's hard to tell. We'll refine below based on text color or background.
        # In footer, it's on a dark green background, but it uses btn-dark-bg. Wait, the footer uses:
        # class="btn-bubble btn-dark-bg font-body" on a background #668e78 (which is forest green).
        # Actually, in footer it should be btn-primary-white. Let's force btn-primary-white for footer.html.
        
        # Extract the text from inner_html
        # We look for <span class="btn-bubble-text">Text</span>
        text_match = re.search(r'<span class="btn-bubble-text[^"]*">(.*?)</span>', inner_html, re.DOTALL)
        if text_match:
            text = text_match.group(1).strip()
        else:
            # strip tags
            text = re.sub(r'<[^>]+>', '', inner_html).strip()
            
        return f'<a{attrs_before}class="{btn_class}"{attrs_after}>{text}</a>'
        
    content = pattern.sub(replace_bubble, content)
    
    # same for <button>
    pattern_btn = re.compile(
        r'<button([^>]*?)class="([^"]*?btn-bubble[^"]*?)"([^>]*?)>(.*?)</button>',
        re.DOTALL
    )
    
    def replace_bubble_btn(match):
        attrs_before = match.group(1)
        classes = match.group(2)
        attrs_after = match.group(3)
        inner_html = match.group(4)
        
        btn_class = 'btn-primary-white' if ('btn-light' in classes or 'text-white' in classes) else 'btn-primary'
        
        text_match = re.search(r'<span class="btn-bubble-text[^"]*">(.*?)</span>', inner_html, re.DOTALL)
        if text_match:
            text = text_match.group(1).strip()
        else:
            text = re.sub(r'<[^>]+>', '', inner_html).strip()
            
        return f'<button{attrs_before}class="{btn_class}"{attrs_after}>{text}</button>'
        
    content = pattern_btn.sub(replace_bubble_btn, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def walk_dir(directory):
    changed_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if process_file(filepath):
                    changed_files.append(filepath)
    return changed_files

changed = walk_dir('.')
print("Changed files:")
for f in changed:
    print(f)
