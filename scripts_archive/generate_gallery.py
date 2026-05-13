import re

with open('pages/gallery.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', text, flags=re.DOTALL)
head = head_match.group(1) if head_match else ""

# Extract top of body
body_top_match = re.search(r'(<body.*?>\s*<div id="header-placeholder"></div>\s*<main>)', text, flags=re.DOTALL)
body_top = body_top_match.group(1) if body_top_match else ""

# Extract scripts at bottom
scripts_match = re.search(r'(<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?</body>\s*</html>)', text, flags=re.DOTALL)
scripts = scripts_match.group(1) if scripts_match else ""

# The gallery data for Green Seasons
categories = [
    {
        "id": "grounds-maintenance",
        "title": "Grounds & Garden Maintenance",
        "images": ["c3.jpeg", "c1.png", "c11.jpeg"]
    },
    {
        "id": "lawn-care",
        "title": "Lawn Care & Renovation",
        "images": ["Garden-turfing.jpg", "c8.jpeg", "c12.jpeg"]
    },
    {
        "id": "hedge-care",
        "title": "Hedge & Shrub Care",
        "images": ["c4.jpeg", "c6.jpg"]
    },
    {
        "id": "planting",
        "title": "Planting & Soft Landscaping",
        "images": ["c2.jpeg", "a1.jpeg", "a2.jpeg"]
    },
    {
        "id": "weed-control",
        "title": "Professional Weed Control",
        "images": ["c5.jpg"]
    },
    {
        "id": "specialist-treatments",
        "title": "Specialist Treatments",
        "images": ["c10.jpeg"]
    },
    {
        "id": "site-clearance",
        "title": "One-Off Site Clearance",
        "images": ["clearance and site prep.jpeg", "before.jpg", "after.jpg"]
    }
]

# Generate Hero and Filter Nav
html = """
        <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ImageGallery",
          "name": "Green Seasons Project Gallery",
          "description": "A portfolio of grounds and garden maintenance projects across South Oxfordshire by Green Seasons.",
          "url": "https://www.greenseasons.co.uk/gallery.html",
          "provider": {
            "@type": "HomeAndConstructionBusiness",
            "@id": "https://www.greenseasons.co.uk/",
            "name": "Green Seasons"
          }
        }
        </script>

        <section class="relative min-h-[100svh] pt-44 pb-16 md:pt-52 md:pb-24 flex flex-col items-center overflow-hidden" style="background:#F5F3EE;">
            <div class="w-full max-w-[98rem] mx-auto px-4 sm:px-6 lg:px-10 relative z-20 flex-grow flex flex-col">
                <div class="text-center mb-12 md:mb-16 reveal reveal-up flex flex-col items-center">
                    <span class="inline-block px-5 py-1.5 font-body font-bold text-sm tracking-widest uppercase rounded-full mb-6 cursor-default bg-[#caebd8] text-[#1a3528] hover:bg-[#825c3e] hover:text-white transition-colors duration-300" style="box-shadow: 0 4px 16px rgba(202, 235, 216, 0.30);">
                        Our Portfolio
                    </span>
                    <h1 class="group font-heading text-4xl md:text-5xl lg:text-6xl font-bold text-[#141229] leading-tight flex flex-col items-center cursor-default w-full">
                        Green Seasons Gallery
                    </h1>
                    <p class="font-body text-lg lg:text-xl mt-8 max-w-3xl mx-auto leading-relaxed" style="color:rgba(20,18,41,0.68);">
                        Explore our recent grounds and garden maintenance projects across South Oxfordshire. From lawn renovations to full site clearances, see the quality of our work.
                    </p>
                </div>

                <div class="w-full max-w-[98rem] mx-auto px-0 sm:px-6 lg:px-10 relative z-30 mb-16">
                    <div class="relative group/nav flex items-center">
                        <button id="scroll-left" class="absolute -left-4 sm:-left-6 lg:-left-12 z-40 w-10 h-10 bg-white rounded-full shadow-xl border border-[#141229]/10 hidden sm:flex items-center justify-center text-[#141229] transition-all duration-500 opacity-0 -translate-x-4 pointer-events-none group-hover/nav:opacity-100 group-hover/nav:translate-x-0 group-hover/nav:pointer-events-auto hover:bg-[#d49813] hover:text-white" aria-label="Scroll filter left">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/>
                            </svg>
                        </button>
                        <div id="nav-container" class="bg-white rounded-full shadow-md border mx-4 sm:mx-0 p-2 overflow-x-auto hide-scrollbar scroll-smooth" style="border-color:rgba(20,18,41,0.06); -webkit-overflow-scrolling: touch;">
                            <ul class="flex items-center gap-2 w-max px-4 sm:px-2 justify-start md:justify-center">
                                <li>
                                    <a href="#all" class="filter-btn block px-4 py-2 rounded-full font-body text-sm md:text-base font-bold transition-all duration-300 whitespace-nowrap bg-[#caebd8] text-[#1a3528]" style="box-shadow:0 4px 16px rgba(202, 235, 216, 0.30);" data-filter="all">All Projects</a>
                                </li>
"""

# Generate filter buttons
for cat in categories:
    html += f"""
                                <li>
                                    <a href="#{cat['id']}" class="filter-btn block px-4 py-2 rounded-full font-body text-sm md:text-base font-bold transition-all duration-300 whitespace-nowrap text-[#1a3528]/80 hover:bg-[#caebd8] hover:text-[#1a3528]" data-filter="{cat['id']}">{cat['title']}</a>
                                </li>
"""

html += """
                            </ul>
                        </div>
                        <button id="scroll-right" class="absolute -right-4 sm:-right-6 lg:-right-12 z-40 w-10 h-10 bg-white rounded-full shadow-xl border border-[#141229]/10 hidden sm:flex items-center justify-center text-[#141229] transition-all duration-500 opacity-0 translate-x-4 pointer-events-none group-hover/nav:opacity-100 group-hover/nav:translate-x-0 group-hover/nav:pointer-events-auto hover:bg-[#d49813] hover:text-white" aria-label="Scroll filter right">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/>
                            </svg>
                        </button>
                    </div>
                </div>

                <div class="w-full max-w-[98rem] mx-auto px-4 sm:px-6 lg:px-10 relative z-20 flex-grow">
                    <div id="all-projects-grid" class="mb-16" style="display:none;"></div>
"""

# Generate Gallery grids
for cat in categories:
    html += f"""
                    <div class="category-section reveal reveal-up mb-24" data-category="{cat['id']}" id="{cat['id']}">
                        <h3 class="font-heading text-3xl md:text-4xl font-bold text-[#141229] mb-8 text-center relative max-w-max mx-auto pb-4 group/h2 section-title-accent">
                            {cat['title']}
                        </h3>
                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 md:gap-10">
"""
    for i, img in enumerate(cat['images']):
        delay = i * 100
        html += f"""
                            <div class="reveal reveal-up block w-full h-full" style="transition-delay:{delay}ms;">
                                <button class="gallery-item w-full relative block rounded-[2rem] overflow-hidden shadow-xl border border-black/5 group cursor-pointer focus:outline-none" data-src="../assets/imgs/{img}" data-caption="{cat['title']} — South Oxfordshire">
                                    <img src="../assets/imgs/{img}" alt="{cat['title']}" loading="lazy" decoding="async" class="w-full h-auto object-cover transition-transform duration-700 group-hover:scale-110">
                                    <div class="absolute inset-0 bg-gradient-to-t from-[#141229]/90 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex flex-col justify-end p-6">
                                        <h4 class="text-white font-heading text-xl font-bold translate-y-2 group-hover:translate-y-0 transition-transform duration-500 text-left">{cat['title']}</h4>
                                    </div>
                                </button>
                            </div>
"""
    html += """
                        </div>
                    </div>
"""

# Close section
html += """
                </div>
            </div>
        </section>

        <!-- Lightbox -->
        <div id="lightbox" class="fixed inset-0 z-50 bg-[#141229]/95 hidden opacity-0 transition-opacity duration-300 backdrop-blur-sm flex items-center justify-center">
            <button id="lightbox-close" class="absolute top-6 right-6 w-12 h-12 flex items-center justify-center bg-white/10 hover:bg-[#d49813] text-white rounded-full transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-[#d49813]/50">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <button id="lightbox-prev" class="absolute left-4 sm:left-10 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-16 sm:h-16 flex items-center justify-center bg-white/10 hover:bg-[#d49813] text-white rounded-full transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-[#d49813]/50">
                <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7"/></svg>
            </button>
            <button id="lightbox-next" class="absolute right-4 sm:right-10 top-1/2 -translate-y-1/2 w-12 h-12 sm:w-16 sm:h-16 flex items-center justify-center bg-white/10 hover:bg-[#d49813] text-white rounded-full transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-[#d49813]/50">
                <svg class="w-6 h-6 sm:w-8 sm:h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7"/></svg>
            </button>
            <div class="relative w-full max-w-5xl px-4 sm:px-12 flex flex-col items-center" onclick="event.stopPropagation()">
                <img id="lightbox-img" src="" alt="" class="max-h-[80vh] w-auto max-w-full rounded-2xl shadow-2xl object-contain">
                <p id="lightbox-caption" class="text-white/80 font-body text-sm sm:text-base mt-6 text-center tracking-wide"></p>
            </div>
        </div>
    </main>
"""

# Modify scripts to update filter colors logic
scripts = re.sub(
    r'btn\.style\.background.*?btn\.style\.color = \'#141229\'',
    "btn.classList.add('bg-[#caebd8]', 'text-[#1a3528]'); btn.classList.remove('text-[#1a3528]/80'); btn.style.boxShadow = '0 4px 16px rgba(202, 235, 216, 0.30)'",
    scripts, flags=re.DOTALL
)
scripts = re.sub(
    r'btn\.style\.background.*?btn\.style\.color = \'rgba\(20,18,41,0\.80\)\'',
    "btn.classList.remove('bg-[#caebd8]', 'text-[#1a3528]'); btn.classList.add('text-[#1a3528]/80'); btn.style.boxShadow = 'none'",
    scripts, flags=re.DOTALL
)

final_html = head + "\n" + body_top + "\n" + html + "\n" + scripts

with open('pages/gallery.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Gallery generated successfully!")
