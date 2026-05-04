with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find start and end of the scrolling banner inner groups
start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if '<div class="scrolling-track' in line:
        start_idx = i + 1
    if start_idx != -1 and '<!-- ABOUT / TRUST SECTION -->' in line:
        pass
    if start_idx != -1 and i > start_idx + 10:
        if '</div>' in line and lines[i+1].strip() == '</div>' and lines[i+2].strip() == '</div>':
            if '<section class="relative py-20 lg:py-32' in lines[i+4] or '<section class="relative py-20 lg:py-32' in lines[i+5]:
                end_idx = i
                break

if start_idx != -1 and end_idx != -1:
    group = """
                    <div class="flex items-center gap-12 md:gap-20 px-6 md:px-10">
                        <div class="flex items-center gap-3 hover-item">
                            <svg class="w-4 h-4 shrink-0 text-[#d49813]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                            <span>Grounds Maintenance</span>
                        </div>
                        <div class="flex items-center gap-3 hover-item">
                            <svg class="w-4 h-4 shrink-0 text-[#d49813]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                            <span>Lawn Care &amp; Renovation</span>
                        </div>
                        <div class="flex items-center gap-3 hover-item">
                            <svg class="w-4 h-4 shrink-0 text-[#d49813]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                            <span>Hedge Cutting</span>
                        </div>
                        <div class="flex items-center gap-3 hover-item">
                            <svg class="w-4 h-4 shrink-0 text-[#d49813]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                            <span>Weed Control</span>
                        </div>
                        <div class="flex items-center gap-3 hover-item">
                            <svg class="w-4 h-4 shrink-0 text-[#d49813]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                            <span>Site Clearance</span>
                        </div>
                    </div>\n"""
    
    new_content = group + group + group
    
    # replace lines[start_idx:end_idx] with new_content
    lines = lines[:start_idx] + [new_content] + lines[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("Replaced scrolling banner.")
else:
    print(f"Could not find bounds. start: {start_idx}, end: {end_idx}")
