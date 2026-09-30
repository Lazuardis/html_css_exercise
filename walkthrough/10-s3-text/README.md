# 10 · s3-text — "Four text properties, and why a font is a list"

**Deck:** Part 3 · **Indicator:** 4 · **Time:** 3 min
**start/** = `/stages/stage-6-block-2/` · **end/** = `/stages/stage-6-block-3/` byte for byte.
Line 1 of each file (the slide comment) is not typed live.

## Open when the slide appears
Working copy of `start/`; `style.css` scrolled to the bottom; `index.html` in the browser.

## Typed live — style.css, after block 2
1. Block header: `/* ===== 3. Colour and text (§3) ===== */`
2. ```
   h1 {
     font-size: 40px;
     text-transform: uppercase;
   }
   ```
   Ctrl+S. Then Ctrl+U (view source): the HTML still says "Our Menu".
3. ```
   footer {
     color: #FCFDFC;
     background-color: #064E4F;
     font-size: 14px;
   }
   ```
   Save after typing `color` alone first — see the fault below — then add the other two.

## Room sees
OUR MENU in capitals (on every page, every h1), and a teal footer band with light text.

## Not typed
The slide's code panel also shows `body { font-family … }` and `nav a:hover { … }` to
explain lines 2 and 9. Both already exist from blocks 1 and 2; do not type them again.

## Fault to expect (use it)
`color: #FCFDFC` saved without the background: the footer text vanishes, near-white on
near-white. "Colour plus background colour, always together."
