# 07 · s2-our-selectors — "The same six selectors, on our own site"

**Deck:** Part 2 · **Indicator:** 2 · **Time:** 3 min
**start/** = `/stages/stage-6-block-1/` · **end/** = `/stages/stage-6-block-2/` byte for byte.
Line 1 of each file (the slide comment) is not typed live.

## Typed live — HTML first
1. Ctrl+Shift+H across the folder, Replace All:
   `<p><a href="index.html">Little Lemon</a></p>` → `<p id="site-name"><a href="index.html">Little Lemon</a></p>`
2. Same: `<p>Middle Eastern food in the Main District</p>` → `<p id="tagline">Middle Eastern food in the Main District</p>`
3. `index.html`: both `<div>` dish cards → `<div class="dish">`; both price lines → `<p class="price">`.
4. `class="current"` after the href of **this page's** nav link only:
   index → Menu · location → Location · book → Book a Table. Ctrl+K S.

## Typed live — style.css, after block 1
5. Block header `/* ===== 2. Selectors: id, class, descendant, child, :hover (§2) ===== */`, then
   seven rules, one declaration per line, saving after each so the room sees it land:
   `#site-name` font-size 32px, font-weight bold · `#tagline` color #5F7171, font-style italic ·
   `.price` font-weight bold, color #B86B00 · `header a` color #064E4F, text-decoration none ·
   `nav > ul > li > a` color #0067AC, text-decoration none · `nav a:hover` text-decoration
   underline · `a.current` font-weight bold.
   Copy the exact text from `end/style.css` if in doubt.

## Room sees
Large bold site name, grey italic tagline, amber prices, blue nav links with no underline
until hovered, and the current page's link in bold. Hover over a nav link to show `:hover`.

## Fault to expect
`class="current"` on Menu on all three pages (the deck notes say students do this).
Click through: Menu stays bold everywhere. One page, one current link.
The slide's title says "six selectors"; there are seven rules — six kinds plus `a.current`.
