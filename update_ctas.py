import re

def update_cta(file_path, number, title_words, subtitle, href_prefix=""):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(r'<section[^>]*style="background:#1a3528;"[^>]*>.*?</section>', re.DOTALL)
    
    if not pattern.search(content):
        print(f"Could not find CTA section in {file_path}")
        return
            
    title_spans = []
    for i, word in enumerate(title_words):
        delay = (i + 1) * 100
        title_spans.append(f'<span class="word-mask"><span class="word-mask-inner" style="transition-delay: {delay}ms;">{word}</span></span>')
        
    title_html = '\n                                '.join(title_spans)
    
    link_href = "pages/contact.html" if href_prefix == "" else "contact.html"
    
    cta_html = f'''<section class="section-dark relative py-20 flex items-center justify-center text-white overflow-hidden border-t border-white/5" style="background:#1a3528;">
            <div class="w-full max-w-[96rem] mx-auto px-4 sm:px-8 lg:px-12 relative z-20">
                <div class="flex flex-col lg:flex-row items-center justify-between gap-12 lg:gap-8 w-full">

                    <div class="w-full lg:w-3/12 reveal order-2 lg:order-1 flex justify-center lg:justify-start">
                        <div class="relative w-full max-w-sm lg:max-w-none h-[300px] lg:h-[400px] rounded-none overflow-hidden shadow-2xl group">
                            <img src="{href_prefix}assets/imgs/footer1.png"
                                alt="Green Seasons team maintaining a residential garden in Oxfordshire" loading="lazy"
                                class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        </div>
                    </div>

                    <div class="w-full lg:w-6/12 text-center reveal order-1 lg:order-2 flex flex-col items-center">

                        <span class="word-mask-inner inline-block font-body font-extrabold text-xl tracking-widest uppercase mb-8 cursor-default text-white hover:text-[#db9f1b] transition-colors duration-300" style="transition-delay: 50ms;">
                            <span class="border-b-[1.5px] border-current pb-0.5">{number}</span>
                        </span>

                        <h2 class="group font-heading font-black text-white leading-[1.15] mb-[22px] flex flex-col items-center text-4xl text-5xl hover:text-[#db9f1b] transition-colors duration-500">
                            <span class="flex flex-wrap justify-center gap-x-3 lg:gap-x-4 leading-tight">
                                {title_html}
                            </span></h2>

                        <p class="title-underline-anim font-body text-base sm:text-lg md:text-xl mb-10 max-w-md mx-auto leading-relaxed mt-2" style="color:rgba(255,255,255,0.80); animation-delay: 800ms;">
                            {subtitle}
                        </p>

                        <div class="title-underline-anim" style="animation-delay: 900ms;">
                            <a href="{link_href}"
                                 class="btn-adaptive">Get in Touch</a>
                        </div>
                    </div>

                    <div class="hidden lg:flex w-full lg:w-3/12 reveal order-3 justify-center lg:justify-end mt-0 lg:mt-16" style="transition-delay:200ms;">
                        <div class="relative w-full max-w-sm lg:max-w-none h-[300px] lg:h-[400px] rounded-none overflow-hidden shadow-2xl group">
                            <img src="{href_prefix}assets/imgs/footer2.png"
                                alt="Freshly turfed lawn by Green Seasons in Oxfordshire" loading="lazy"
                                class="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110">
                        </div>
                    </div>

                </div>
            </div>
        </section>'''
        
    new_content = pattern.sub(cta_html, content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {file_path}")

# index.html
update_cta(
    "index.html", 
    "16", 
    ["Ready", "to", "Elevate", "Your", "Space?"], 
    "Whether it's a one-off project or regular care, we have the expertise to bring your vision to life. Contact Tim today for a free, no-obligation quote.",
    ""
)

# services.html
update_cta(
    "pages/services.html", 
    "02", 
    ["Let's", "Transform", "Your", "Outdoors"], 
    "From comprehensive maintenance to specialized treatments, our expert team guarantees stunning results. Contact Tim today for a free, no-obligation quote.",
    "../"
)

# gallery.html
update_cta(
    "pages/gallery.html", 
    "02", 
    ["Inspired", "by", "Our", "Work?"], 
    "Let us create a beautiful, lasting outdoor environment tailored to your needs. Contact Tim today for a free, no-obligation quote.",
    "../"
)

