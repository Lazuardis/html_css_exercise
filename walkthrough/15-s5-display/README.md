# 15 · s5-display — "A vertical list becomes a menu bar in two rules"

**Deck:** Part 5 · **Indicator:** 6 · **Time:** 3 min
**start/** = `/stages/stage-6-block-4/` · **end/** = no stage of its own: block 4 plus the
block-5 header and the three nav rules. Walkthrough 16 completes block 5.
Line 1 of each file (the slide comment) is not typed live.

## Typed live — style.css, after block 4
1. Block header: `/* ===== 5. Document flow and alignment (§5) ===== */`
2. ```
   nav ul {
     list-style: none;
     padding: 0px;
   }
   ```
   Ctrl+S — the bullets and the indent go. Still a list to a screen reader.
3. `nav li {` / `margin-right: 24px;` / `}` — Ctrl+S. Nothing visible yet.
4. `nav {` / `text-align: center;` / `}` — Ctrl+S. Each item centred, still stacked.
5. **Last:** click to the start of the `nav li` body, above `margin-right`, and type
   `display: inline;` — Ctrl+S.

## Room sees
At step 5, on one save, the stack becomes a row: centred, spaced, on every page.

## What to say
li is block-level, so the items stacked. `display: inline` makes them behave like words,
and `text-align` on the parent centres them because inline things align like text. The HTML
stays a `ul` — Week 3's honest HTML, Week 4's look.

## Fault to expect
`display: inline` put on `nav ul` instead of `nav li`: nothing changes — the list items
inside are still block-level.
