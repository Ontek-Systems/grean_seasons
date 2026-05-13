# Green Seasons — UI Component Library

## How the token system works

Every section on the site is either **light** or **dark**.

| Section type | What to do | Button to use |
|---|---|---|
| White / cream background | Nothing extra | `.btn-primary` or `.btn-adaptive` |
| Dark green / image background | Add `section-dark` class to the `<section>` tag | `.btn-ghost` or `.btn-adaptive` |

Adding `class="section-dark"` to a section automatically changes:
- All `--gs-fg` tokens → white
- All `--gs-fg-muted` tokens → white at 90%  
- All `--gs-fg-subtle` tokens → white at 60%
- `.btn-adaptive` → transparent ghost with white border (gold on hover)

You never need to set text colours per-element.

---

## Components

### 1. Tagline (eyebrow label)

The numbered label above every section heading.

**File:** `components/ui/tagline.html`

```html
<span class="gs-tagline word-mask-inner" style="transition-delay: 50ms;">
    <span class="border-b-[1.5px] border-current pb-0.5">01</span>
</span>
```

**Usage rules:**
- Change the number to match the section sequence
- Works on light and dark backgrounds with no class changes
- The `word-mask-inner` class adds the scroll-reveal animation

---

### 2. Section heading (h2)

The large animated title used in every major section.

**File:** `components/ui/section-heading.html`

```html
<h2 class="gs-heading group mb-6 flex flex-col items-center lg:items-start">
    <span class="flex flex-wrap justify-center lg:justify-start gap-x-3 lg:gap-x-4 leading-tight">
        <span class="word-mask"><span class="word-mask-inner" style="transition-delay: 100ms;">Your</span></span>
        <span class="word-mask"><span class="word-mask-inner" style="transition-delay: 200ms;">Heading</span></span>
        <span class="word-mask"><span class="word-mask-inner" style="transition-delay: 300ms;">Here</span></span>
    </span>
</h2>
```

**Usage rules:**
- Add one `<span class="word-mask">` per word (or per short phrase)
- Stagger `transition-delay` by 100ms per word
- `gs-heading` handles colour and hover-gold automatically
- Add `text-center` or `items-center` for centred layouts

---

### 3. Body / subtitle text

The descriptive paragraph below the heading.

**File:** `components/ui/section-body.html`

```html
<p class="gs-body mb-8 max-w-xl">
    Your body copy goes here. Describe the section content in one or two sentences.
</p>
```

**Usage rules:**
- `gs-body` handles colour automatically (dark green on light, white/90 on dark)
- Adjust `max-w-*` to control line length (xl = ~576px, 2xl = ~672px)
- Add `mx-auto` for centred layouts

---

### 4. Adaptive button

Automatically gold-solid on light sections, ghost/outline on dark sections.

**File:** `components/ui/button-adaptive.html`

```html
<a href="pages/your-page.html" class="btn-adaptive">Button Label</a>
```

**Usage rules:**
- Inside a `.section-dark` wrapper → renders as transparent white-outline ghost
- Outside (on white/cream bg) → renders as gold solid with green hover
- For an always-gold button regardless of context: use `btn-primary`
- For an always-ghost button regardless of context: use `btn-ghost`

---

## Full section template

Copy this entire block for any new section. Add `section-dark` to the `<section>` for dark mode.

**File:** `components/ui/section-template.html`

```html
<!-- 
  LIGHT SECTION: remove "section-dark" for white/cream bg
  DARK SECTION:  keep "section-dark" and add style="background:#1a3528;" 
-->
<section class="section-dark py-20 lg:py-32" style="background: #1a3528;">
    <div class="w-full max-w-[96rem] mx-auto px-4 sm:px-8 lg:px-12">
        <div class="flex flex-col items-center text-center reveal">

            <!-- 1. Tagline -->
            <span class="gs-tagline word-mask-inner" style="transition-delay: 50ms;">
                <span class="border-b-[1.5px] border-current pb-0.5">XX</span>
            </span>

            <!-- 2. Heading -->
            <h2 class="gs-heading group mb-6 flex flex-col items-center">
                <span class="flex flex-wrap justify-center gap-x-3 lg:gap-x-4 leading-tight">
                    <span class="word-mask"><span class="word-mask-inner" style="transition-delay: 100ms;">Section</span></span>
                    <span class="word-mask"><span class="word-mask-inner" style="transition-delay: 200ms;">Title</span></span>
                    <span class="word-mask"><span class="word-mask-inner" style="transition-delay: 300ms;">Here</span></span>
                </span>
            </h2>

            <!-- 3. Body text -->
            <p class="gs-body mb-10 max-w-2xl mx-auto">
                Subtitle or descriptive text goes here.
            </p>

            <!-- 4. Button (auto-adapts to light/dark) -->
            <a href="pages/your-page.html" class="btn-adaptive">
                Call to Action
            </a>

        </div>
    </div>
</section>
```

---

## Refactoring an existing section

Use this prompt for any section you want to migrate to the token system:

> "Refactor the [SECTION NAME] section in index.html to use the Green Seasons design token system. Replace hardcoded colour classes on the tagline, h2, body text, and button with `gs-tagline`, `gs-heading`, `gs-body`, and `btn-adaptive`. If the section has a dark background, add `section-dark` to the `<section>` tag. Do not change any other section. After refactoring, the section must look pixel-identical to before."
