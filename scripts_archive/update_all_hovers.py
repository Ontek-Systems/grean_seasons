import os

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("this.style.background='#d49813'", "this.style.background='#825c3e'")
    new_content = new_content.replace('this.style.background="#d49813"', 'this.style.background="#825c3e"')
    new_content = new_content.replace("hover:bg-[#d49813]", "hover:bg-[#825c3e]")
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def walk_and_replace(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                replace_in_file(os.path.join(root, file))

walk_and_replace(".")
