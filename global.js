document.addEventListener('DOMContentLoaded', async () => {

    await loadComponents();

    // Set mega menu top to bottom edge of header (runs after layout is complete)
    function updateMegaTop() {
        const h = document.getElementById('site-header');
        if (h) document.documentElement.style.setProperty('--header-bottom', h.getBoundingClientRect().bottom + 'px');
    }
    requestAnimationFrame(() => { requestAnimationFrame(updateMegaTop); });
    window.addEventListener('scroll', updateMegaTop, { passive: true });
    window.addEventListener('resize', updateMegaTop, { passive: true });

    // ==========================================
    // 1. MOBILE MENU LOGIC (Smooth Animation)
    // ==========================================
    const menuBtn = document.getElementById('menuBtn');
    const mobileNav = document.getElementById('mobileNav');

    if (menuBtn && mobileNav) {
        menuBtn.addEventListener('click', () => {
            // Toggle the smooth animation classes instead of 'hidden'
            mobileNav.classList.toggle('opacity-0');
            mobileNav.classList.toggle('invisible');
            mobileNav.classList.toggle('-translate-y-4');
            mobileNav.classList.toggle('pointer-events-none');

            // Toggle the hamburger icon to an 'X' icon
            const svg = menuBtn.querySelector('svg');
            if (mobileNav.classList.contains('opacity-0')) {
                // Hamburger icon (Menu Closed)
                svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>';
            } else {
                // X icon (Menu Open)
                svg.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>';
            }
        });
    }

    initHeaderScroll();
    setActiveNav();
    initServicesMegaMenu();

    // ==========================================
    // 2. SCROLL REVEAL ANIMATIONS
    // ==========================================
    const revealElements = document.querySelectorAll('.reveal');

    // Create an observer that triggers when elements are 10% visible
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active'); // Triggers CSS transition
                observer.unobserve(entry.target);     // Only animate once per load
            }
        });
    }, {
        root: null,
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px" // Triggers slightly before hitting the bottom of viewport
    });

    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            // Already in viewport on load — activate immediately, no observer needed
            el.classList.add('active');
        } else {
            revealObserver.observe(el);
        }
    });

});

async function loadComponents() {
    const path = window.location.pathname;
    const isPagesLocationsDir = path.includes('/pages/locations/');
    const isPagesServiceDir = !isPagesLocationsDir && path.includes('/pages/services/');
    const isPagesDir = !isPagesServiceDir && !isPagesLocationsDir && path.includes('/pages/');
    let basePath = '';
    if (isPagesServiceDir || isPagesLocationsDir) basePath = '../../';
    else if (isPagesDir) basePath = '../';

    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
        try {
            const resp = await fetch(basePath + 'components/header.html');
            let html = await resp.text();
            if (basePath) {
                html = html.replace(/(href|src)="([^"]*)"/g, (match, p1, p2) => {
                    if (p2.startsWith('http') || p2.startsWith('mailto:') || p2.startsWith('tel:') || p2.startsWith('#') || p2.startsWith('/')) return match;
                    return `${p1}="${basePath + p2}"`;
                });
            }
            headerPlaceholder.outerHTML = html;
        } catch (e) {
            console.error('Error loading header:', e);
        }
    }

    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
        try {
            const resp = await fetch(basePath + 'components/footer.html');
            let html = await resp.text();
            if (basePath) {
                html = html.replace(/(href|src)="([^"]*)"/g, (match, p1, p2) => {
                    if (p2.startsWith('http') || p2.startsWith('mailto:') || p2.startsWith('tel:') || p2.startsWith('#') || p2.startsWith('/')) return match;
                    return `${p1}="${basePath + p2}"`;
                });
            }
            if (document.body.hasAttribute('data-suppress-footer-cta')) {
                const footerStart = html.indexOf('<footer');
                if (footerStart !== -1) html = html.slice(footerStart);
            }
            footerPlaceholder.outerHTML = html;
        } catch (e) {
            console.error('Error loading footer:', e);
        }
    }
}

function initServicesMegaMenu() {
    const trigger = document.querySelector('.group\\/nav');
    const menu = document.getElementById('services-mega-wrapper');
    if (!trigger || !menu) return;
    let hideTimer;

    function openMenu() {
        clearTimeout(hideTimer);
        menu.classList.add('open');
    }
    function scheduleClose() {
        hideTimer = setTimeout(() => menu.classList.remove('open'), 200);
    }

    trigger.addEventListener('mouseenter', openMenu);
    trigger.addEventListener('mouseleave', scheduleClose);
    menu.addEventListener('mouseenter', openMenu);
    menu.addEventListener('mouseleave', scheduleClose);
}

function initHeaderScroll() {
    const header = document.getElementById('site-header');
    const container = document.getElementById('header-container');
    const isServicePage = window.location.pathname.match(/\/pages\/services\/.+\.html/);

    if (header && container) {
        if (isServicePage) {
            header.classList.add('scrolled');
            return;
        }

        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
                header.classList.remove('bg-transparent', 'border-transparent');
                header.classList.add('bg-brand-dark/95', 'backdrop-blur-md', 'shadow-md', 'border-white/10');
                container.classList.remove('py-5', 'md:py-6');
                container.classList.add('py-2', 'md:py-3');
            } else {
                header.classList.remove('scrolled');
                header.classList.add('bg-transparent', 'border-transparent');
                header.classList.remove('bg-brand-dark/95', 'backdrop-blur-md', 'shadow-md', 'border-white/10');
                container.classList.add('py-5', 'md:py-6');
                container.classList.remove('py-2', 'md:py-3');
            }
        };

        window.addEventListener('scroll', handleScroll);
        // call once
        handleScroll();
    }
}

function setActiveNav() {
    const path = window.location.pathname;

    // Map page segments to nav link labels
    const matchers = [
        { test: p => p === '/' || p.endsWith('index.html'), label: 'Home' },
        { test: p => p.includes('/pages/services'), label: 'Services' },
        { test: p => p.includes('/pages/about'), label: 'About' },
        { test: p => p.includes('/pages/gallery'), label: 'Gallery' },
        { test: p => p.includes('/pages/contact'), label: 'Contact' },
        { test: p => p.includes('/pages/locations/'), label: 'Where We Serve' },
    ];

    let activeLabel = null;
    for (const m of matchers) {
        if (m.test(path)) { activeLabel = m.label; break; }
    }

    if (!activeLabel) return;

    // Only target desktop nav links (inside <nav>), not mobile menu links
    document.querySelectorAll('nav .nav-link').forEach(el => {
        const text = el.textContent.trim();
        if (text === activeLabel) {
            el.classList.add('active-nav');
        }
    });
}