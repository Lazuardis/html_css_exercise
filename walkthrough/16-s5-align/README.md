# 16 · s5-align — "Centre with margin: auto; push aside with float"

**Deck:** Part 5 · **Indicator:** 6 · **Time:** 4 min
**start/** = walkthrough 15's `end/` · **end/** = `/stages/stage-6-block-5/` byte for byte
(= `/stages/stage-6-styled/`, final). Line 1 of each file is not typed live.

## Typed live — style.css, block 5
Between the `nav li` rule and the `nav` rule:
1. `main {` / `margin-left: auto;` / `margin-right: auto;` / `margin-bottom: 24px;` / `}` — Ctrl+S.
   **main jumps to the centre.**
2. `header {` / `text-align: center;` / `}` — Ctrl+S.

After the `nav` rule, at the bottom:
3. `.dish img {` / `float: right;` / `margin-left: 16px;` / `margin-bottom: 8px;` / `}` — Ctrl+S.
   The images park on the right; heading and text wrap round them.
4. `.dish h2 {` / `margin-top: 0px;` / `}` — Ctrl+S. The dish name lifts to the top of the card.
5. `footer {` / `text-align: center;` / `}` — Ctrl+S.

## Try it — the critical constraint
6. In block 4's `main` rule, delete `width: 720px;` — Ctrl+S. main fills the width again:
   no leftover space to split. Ctrl+Z, Ctrl+S to restore.
   Fallback: copy `variants/try-no-width.css` over `style.css`.

## Note
The slide groups `header, footer { text-align: center; }`. The file keeps them as two rules
(header here, footer last) — same result; `end/` is the canonical form.

## Fault to expect
"Why is the image above the h2 in the HTML?" A float starts on the line where it appears,
so it must come first — one of float's awkwardnesses, and walkthrough 17 is about that.
