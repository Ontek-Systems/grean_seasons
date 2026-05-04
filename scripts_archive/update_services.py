import re

with open('pages/services.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract <head>
head_match = re.search(r'(<head>.*?</head>)', text, flags=re.DOTALL)
head = head_match.group(1) if head_match else ""

# Extract top of body (including header placeholder)
body_top_match = re.search(r'(<body.*?>\s*<div id="header-placeholder"></div>\s*<main>)', text, flags=re.DOTALL)
body_top = body_top_match.group(1) if body_top_match else ""

# Extract bottom of body (from <div id="footer-placeholder"></div> to </html>)
body_bottom_match = re.search(r'(<div id="footer-placeholder"></div>.*</html>)', text, flags=re.DOTALL)
body_bottom = body_bottom_match.group(1) if body_bottom_match else ""

# Extract the CTA section from contact.html
with open('pages/contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

contact_cta_match = re.search(r'(<section[^>]*id="contact-form".*?</section>)', contact_html, flags=re.DOTALL)
contact_cta = contact_cta_match.group(1) if contact_cta_match else ""

services_data = [
    {
        "title": "Grounds & Garden Maintenance",
        "image": "../assets/imgs/c3.jpeg",
        "tasks": ["Routine grass cutting", "Strimming and edging", "Comprehensive site presentation"]
    },
    {
        "title": "Lawn Care & Renovation",
        "image": "../assets/imgs/Garden-turfing.jpg",
        "tasks": ["Seasonal fertiliser programmes", "Targeted weed and moss control", "Aeration and scarification", "Full lawn renovations"]
    },
    {
        "title": "Hedge & Shrub Care",
        "image": "../assets/imgs/c4.jpeg",
        "tasks": ["Regular trimming", "Expert shaping", "Plant health care"]
    },
    {
        "title": "Planting & Soft Landscaping",
        "image": "../assets/imgs/c2.jpeg",
        "tasks": ["Plant supply and sourcing", "Custom planting schemes", "Bespoke border design"]
    },
    {
        "title": "Professional Weed Control",
        "image": "../assets/imgs/c5.jpg",
        "tasks": ["Certified herbicide applications", "Lawn weed management", "Hard surface weed control"]
    },
    {
        "title": "Specialist Treatments",
        "image": "../assets/imgs/c10.jpeg",
        "tasks": ["Wetting agent applications", "Slow-release fertiliser programmes", "Soil resilience improvement"]
    },
    {
        "title": "One-Off Site Clearance",
        "image": "../assets/imgs/clearance and site prep.jpeg",
        "tasks": ["Initial \"reset\" visits", "Full site clearance works", "Overgrown area recovery"]
    }
]

sectors_data = [
    {"name": "Residential Developments", "icon": "fa-house-chimney"},
    {"name": "Property Management", "icon": "fa-building-user"},
    {"name": "Parish Councils", "icon": "fa-landmark-dome"},
    {"name": "Commercial Buildings", "icon": "fa-building"},
    {"name": "Retail Developments", "icon": "fa-store"},
    {"name": "Private Estates", "icon": "fa-tree-city"},
    {"name": "Educational Facilities", "icon": "fa-school"},
    {"name": "Industrial Sites", "icon": "fa-industry"}
]

# Generate Hero Section
hero_html = """
        <section class="relative pt-44 pb-16 md:pt-52 md:pb-24 flex flex-col items-center overflow-hidden"
            style="background:#F5F3EE;">
            <div class="w-full max-w-[98rem] mx-auto px-4 sm:px-6 lg:px-10 relative z-20 flex-grow flex flex-col">
                <div class="text-center mb-12 md:mb-16 reveal reveal-up flex flex-col items-center">
                    <span
                        class="inline-block px-5 py-1.5 font-body font-semibold text-sm tracking-widest uppercase rounded-full mb-6 cursor-default"
                        style="background:#eab308; color:#141229; transition: background 0.3s ease, color 0.3s ease, box-shadow 0.3s ease;">
                        Our Services
                    </span>
                    <h1 class="group font-heading text-4xl md:text-5xl lg:text-6xl font-bold text-[#141229] leading-tight flex flex-col items-center cursor-default w-full">
                        Everything Your Outdoor Space Needs
                        <span class="block w-12 md:w-16 h-0.5 md:h-[2px] bg-[#eab308] mt-4 lg:mt-6 rounded-full transition-all duration-300 ease-in-out group-hover:w-24 md:group-hover:w-32 group-hover:bg-[#eab308]/80"></span>
                    </h1>
                    <p class="font-body text-lg lg:text-xl mt-8 max-w-3xl mx-auto leading-relaxed" style="color:rgba(20,18,41,0.68);">
                        At Green Seasons we provide professional grounds and garden maintenance tailored to commercial and residential clients — helping protect and enhance the value of your property.
                    </p>
                </div>

                <div id="catalog-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 w-full pb-20">
"""

for s in services_data:
    tasks_html = "".join([f'<li class="flex items-start gap-2"><svg class="w-5 h-5 text-[#eab308] mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span class="text-[#141229]/80 font-body text-base">{task}</span></li>' for task in s["tasks"]])
    
    card = f"""
                    <div class="service-card relative bg-white rounded-[2rem] shadow-xl border border-black/5 overflow-hidden group flex flex-col h-full transform transition-all duration-500 hover:-translate-y-2 hover:shadow-2xl">
                        <div class="relative w-full h-64 md:h-72 overflow-hidden">
                            <img src="{s['image']}" alt="{s['title']}" loading="lazy" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                            <div class="absolute inset-0 bg-gradient-to-t from-[#141229]/90 via-[#141229]/20 to-transparent opacity-70 group-hover:opacity-90 transition-opacity duration-300"></div>
                            <h3 class="absolute bottom-6 left-6 right-6 font-heading text-2xl md:text-3xl font-bold text-white z-10 leading-tight drop-shadow-md">{s['title']}</h3>
                        </div>
                        <div class="p-6 md:p-8 flex flex-col flex-grow bg-white relative z-20">
                            <ul class="flex flex-col gap-3 mb-8 flex-grow">
                                {tasks_html}
                            </ul>
                            <div class="mt-auto flex flex-col gap-3 items-center">
                                <a href="contact.html" class="btn-bubble btn-primary font-body w-full">
                                    <span class="btn-bubble-fill"></span>
                                    <span class="btn-bubble-text text-base">Book a Site Visit</span>
                                    <span class="btn-bubble-icon-container">
                                        <svg class="btn-bubble-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 12h14m-6-6l6 6-6 6"></path></svg>
                                    </span>
                                </a>
                            </div>
                        </div>
                    </div>
"""
    hero_html += card

hero_html += """
                </div>
            </div>
        </section>
"""

# Sectors Section
sectors_cards = ""
for sec in sectors_data:
    sectors_cards += f"""
                    <div class="bg-white rounded-2xl p-6 shadow-md border border-[#141229]/5 flex flex-col items-center text-center hover:shadow-lg transition-shadow duration-300">
                        <i class="fa-solid {sec['icon']} text-4xl text-[#eab308] mb-4"></i>
                        <h4 class="font-heading text-xl font-bold text-[#141229]">{sec['name']}</h4>
                    </div>
"""

sectors_html = f"""
        <section class="relative py-20 bg-white">
            <div class="w-full max-w-[98rem] mx-auto px-4 sm:px-6 lg:px-10 relative z-20">
                <div class="text-center mb-16 reveal reveal-up flex flex-col items-center">
                    <h2 class="group font-heading text-3xl md:text-4xl lg:text-5xl font-bold text-[#141229] leading-tight flex flex-col items-center cursor-default w-full">
                        Who We Serve
                        <span class="block w-12 md:w-16 h-0.5 md:h-[2px] bg-[#eab308] mt-4 lg:mt-6 rounded-full transition-all duration-300 ease-in-out group-hover:w-24 md:group-hover:w-32 group-hover:bg-[#eab308]/80"></span>
                    </h2>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 lg:gap-8 reveal reveal-up" style="transition-delay: 100ms;">
                    {sectors_cards}
                </div>
            </div>
        </section>
"""

# Now write the final output
if not head:
    print("Could not parse head")
    
# We need to add fontawesome to <head> if not there
if "font-awesome" not in head:
    head = head.replace("</head>", '    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n</head>')

# Update title and meta
head = re.sub(r'<title>.*?</title>', '<title>Our Services | Green Seasons – Professional Grounds & Garden Maintenance</title>', head, flags=re.DOTALL)
head = re.sub(r'<meta name="description" content="\[META_DESCRIPTION_PLACEHOLDER\]" />', '<meta name="description" content="Green Seasons offers professional grounds maintenance, lawn care, hedge cutting, weed control, planting and site clearance across South Oxfordshire." />', head)
head = re.sub(r'<meta property="og:title" content="\[META_TITLE_PLACEHOLDER\]" />', '<meta property="og:title" content="Our Services | Green Seasons" />', head)
head = re.sub(r'<meta property="og:description" content="\[META_DESCRIPTION_PLACEHOLDER\]" />', '<meta property="og:description" content="Green Seasons offers professional grounds maintenance, lawn care, hedge cutting, weed control, planting and site clearance across South Oxfordshire." />', head)
head = re.sub(r'<meta name="twitter:title" content="\[META_TITLE_PLACEHOLDER\]" />', '<meta name="twitter:title" content="Our Services | Green Seasons" />', head)
head = re.sub(r'<meta name="twitter:description" content="\[META_DESCRIPTION_PLACEHOLDER\]" />', '<meta name="twitter:description" content="Green Seasons offers professional grounds maintenance, lawn care, hedge cutting, weed control, planting and site clearance across South Oxfordshire." />', head)

# Also ensure colors in style block are correct (Bronze to #eab308)
head = re.sub(r'--color-brand-bronze:\s*#[a-fA-F0-9]+;', '--color-brand-bronze: #eab308;', head)

final_html = head + "\n" + body_top + "\n" + hero_html + "\n" + sectors_html + "\n" + contact_cta + "\n    </main>\n" + body_bottom

with open('pages/services.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Updated services.html successfully")
