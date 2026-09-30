# 06 · s2-first-rules — "Three element selectors, and the site has a voice"

**Deck:** Part 2 · **Indicator:** 1 · **Time:** 2 min
**start/** = `/stages/stage-6-block-0/` · **end/** = `/stages/stage-6-block-1/` byte for byte.
Line 1 of each file (the slide comment) is not typed live.

## Open when the slide appears
Working copy of `start/`; `style.css` open; three browser tabs.

## Typed live — style.css, in order
1. Above the existing `h1` rule, type the block header:
   `/* ===== 1. A first rule: element selectors (§2) ===== */`
   (`end/` also has a two-line file comment at the top; paste it or skip it — it changes nothing on screen.)
2. Under the header, the body rule, one declaration per line:
   ```
   body {
     font-family: "Helvetica Neue", Arial, sans-serif;
     color: #1C2B2B;
     background-color: #FCFDFC;
   }
   ```
3. Below the `h1` rule: `h2 {` / `color: #064E4F;` / `}`. Ctrl+S; refresh all three tabs.

## Room sees
Sans-serif text, a near-black body colour, dark teal headings — on all three pages.

## What to say
- `body` is an element selector too, and everything inside it inherits the font and
  colour. That is the "cascade", mentioned but not developed.
- The font-family value is a list; Part 3 says why. Do not explain the hex values yet.

## Fault to expect
Missing semicolon after `color: #1C2B2B` — the next declaration silently dies and the
background stays white. (`/demos/` has the pair.)
