import re

def update_colors_and_info(text):
    text = text.replace('#141229', '#668e78')
    text = text.replace('#e8b01e', '#d49813')
    
    # Specific color fix for dark text on buttons
    text = text.replace("this.style.color='#668e78';", "this.style.color='#1a3528';")
    text = text.replace('style="color:#668e78;"', 'style="color:#1a3528;"')
    
    text = text.replace('jboutdoorservicesltd@gmail.com', 'green-seasons@hotmail.com')
    text = text.replace('+44 7445 064666', '07545 285408')
    text = text.replace('tel:+447445064666', 'tel:+447545285408')
    text = text.replace('Wincanton, Somerset', 'Kingston Bagpuize')
    text = text.replace('Mon-Fri: 8am-6pm, Sat: 8am-1pm', 'Mon-Fri: 8am-5pm')
    text = text.replace('Mon-Fri: 8am–6pm, Sat: 8am–1pm', 'Mon-Fri: 8am–5pm')
    text = text.replace('https://www.facebook.com/jbw1999', 'https://www.facebook.com/GreenSeasonsOxfordshire')
    text = text.replace('https://web.facebook.com/jbw1999/', 'https://www.facebook.com/GreenSeasonsOxfordshire')
    text = text.replace('https://www.google.com/search?q=JB+Outdoor+Services+Ltd+Wincanton#lrd=0x48722c1598f6d7ab:0xf51fa904c6436ec,1,,,', '#')
    text = text.replace('[IMAGE_DESCRIPTION]', 'Green Seasons')
    return text

# --- HEADER.HTML ---
with open('components/header.html', 'r', encoding='utf-8') as f:
    header = f.read()

header = update_colors_and_info(header)

# Mega Menu Replace
mega_menu_old = r'<div\s+class="bg-\[#668e78\] border border-white/10 shadow-2xl rounded-2xl p-8 w-\[900px\] flex gap-8 text-white">.*?</div>\s+</div>\s+</div>'
mega_menu_new = """<div
                        class="bg-[#668e78] border border-white/10 shadow-2xl rounded-2xl p-8 w-[900px] flex gap-8 text-white">

                        <!-- Col 1: Grounds Maintenance -->
                        <div class="flex-1">
                            <a href="pages/services.html#grounds-maintenance"
                                class="block text-[#d49813] font-heading font-bold text-[13px] tracking-widest uppercase mb-3 border-b border-white/10 pb-2 hover:opacity-75 transition-opacity">Grounds &amp; Garden Maintenance</a>
                            <ul class="flex flex-col gap-2 text-[13px] font-medium">
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Grass Cutting</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Strimming &amp; Edging</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Litter Clearance</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">General Presentation</a></li>
                            </ul>
                        </div>

                        <!-- Col 2: Lawn Care -->
                        <div class="flex-1">
                            <a href="pages/services.html#lawn-care"
                                class="block text-[#d49813] font-heading font-bold text-[13px] tracking-widest uppercase mb-3 border-b border-white/10 pb-2 hover:opacity-75 transition-opacity">Lawn Care &amp; Renovation</a>
                            <ul class="flex flex-col gap-2 text-[13px] font-medium">
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Lawn Overhauls</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Seasonal Fertiliser</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Scarification</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Aeration</a></li>
                            </ul>
                        </div>

                        <!-- Col 3: Hedge Cutting -->
                        <div class="flex-1">
                            <a href="pages/services.html#hedge-cutting"
                                class="block text-[#d49813] font-heading font-bold text-[13px] tracking-widest uppercase mb-3 border-b border-white/10 pb-2 hover:opacity-75 transition-opacity">Hedge Cutting</a>
                            <ul class="flex flex-col gap-2 text-[13px] font-medium">
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Regular Trimming</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Shaping</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Shrub Maintenance</a></li>
                            </ul>
                        </div>

                        <!-- Col 4: Weed Control -->
                        <div class="flex-1">
                            <a href="pages/services.html#weed-control"
                                class="block text-[#d49813] font-heading font-bold text-[13px] tracking-widest uppercase mb-3 border-b border-white/10 pb-2 hover:opacity-75 transition-opacity">Weed Control &amp; Site Clearance</a>
                            <ul class="flex flex-col gap-2 text-[13px] font-medium">
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Herbicide Applications</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Hard Surface Treatment</a></li>
                                <li><a href="pages/services/service-template.html"
                                        class="hover:text-[#d49813] transition-colors block py-0.5">Overgrown Garden Clearance</a></li>
                            </ul>
                        </div>

                    </div>
                </div>
            </div>"""

header = re.sub(mega_menu_old, mega_menu_new, header, flags=re.DOTALL)

# Mobile services panel
mobile_panel_old = r'<div id="mobileServicesPanel" class="hidden mt-3 space-y-4">.*?<a href="pages/services.html"\s+class="inline-block mt-1 text-xs uppercase tracking-widest text-\[#d49813\] font-bold hover:opacity-70 transition-opacity">View All Services</a>\s+</div>'
mobile_panel_new = """<div id="mobileServicesPanel" class="hidden mt-3 space-y-4">

                        <!-- Grounds Maintenance -->
                        <div>
                            <a href="pages/services.html#grounds-maintenance"
                                class="block text-[13px] font-heading font-bold tracking-widest uppercase text-[#d49813] mb-2">Grounds &amp; Garden Maintenance</a>
                            <div class="flex flex-col gap-1.5 text-sm text-white/80 pl-2">
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Grass Cutting</a>
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Strimming &amp; Edging</a>
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Litter Clearance</a>
                            </div>
                        </div>

                        <!-- Lawn Care -->
                        <div>
                            <a href="pages/services.html#lawn-care"
                                class="block text-[13px] font-heading font-bold tracking-widest uppercase text-[#d49813] mb-2">Lawn Care &amp; Renovation</a>
                            <div class="flex flex-col gap-1.5 text-sm text-white/80 pl-2">
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Lawn Overhauls</a>
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Seasonal Fertiliser</a>
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Scarification &amp; Aeration</a>
                            </div>
                        </div>

                        <!-- Hedge Cutting -->
                        <div>
                            <a href="pages/services.html#hedge-cutting"
                                class="block text-[13px] font-heading font-bold tracking-widest uppercase text-[#d49813] mb-2">Hedge Cutting</a>
                            <div class="flex flex-col gap-1.5 text-sm text-white/80 pl-2">
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Regular Trimming</a>
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Shaping &amp; Shrub Care</a>
                            </div>
                        </div>

                        <!-- Weed Control -->
                        <div>
                            <a href="pages/services.html#weed-control"
                                class="block text-[13px] font-heading font-bold tracking-widest uppercase text-[#d49813] mb-2">Weed Control &amp; Site Clearance</a>
                            <div class="flex flex-col gap-1.5 text-sm text-white/80 pl-2">
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Herbicide Applications</a>
                                <a href="pages/services/service-template.html"
                                    class="block py-0.5 hover:text-[#d49813] transition-colors">Overgrown Garden Clearance</a>
                            </div>
                        </div>

                        <a href="pages/services.html"
                            class="inline-block mt-1 text-xs uppercase tracking-widest text-[#d49813] font-bold hover:opacity-70 transition-opacity">View All Services</a>
                    </div>"""

header = re.sub(mobile_panel_old, mobile_panel_new, header, flags=re.DOTALL)

with open('components/header.html', 'w', encoding='utf-8') as f:
    f.write(header)

# --- FOOTER.HTML ---
with open('components/footer.html', 'r', encoding='utf-8') as f:
    footer = f.read()

footer = update_colors_and_info(footer)

# Fix placeholders using regex sequentially
text_replacements = [
    'Get a Free Quote', # btn text
    'Contact Us', # h3
    'Location', # label
    'Kingston Bagpuize, South Oxfordshire', # text
    'green-seasons@hotmail.com', # text (email)
    'Quick Links', # h3
    'Home', 'Services', 'About', 'FAQ', 'Gallery', 'Contact', # links
    'Privacy Policy', 'Website by', 'Ontek Systems'
]
for r in text_replacements:
    footer = footer.replace('[TEXT_PLACEHOLDER]', r, 1)

long_text_replacements = [
    'Serving South Oxfordshire and surrounding areas', # location description
    'Call Us', # phone label
    'Email Us', # email label
    '&copy; 2026 Green Seasons. All rights reserved.' # copyright
]
for r in long_text_replacements:
    footer = footer.replace('[LONG_TEXT_PLACEHOLDER_DESCRIPTION]', r, 1)

with open('components/footer.html', 'w', encoding='utf-8') as f:
    f.write(footer)

print('Updated header and footer.')
