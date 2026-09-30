# 13 · s4-code — "Boxing the content and the dish cards"

**Deck:** Part 4 · **Indicator:** 5 · **Time:** 3 min
**start/** = walkthrough 11's `end/` (12 has no end/) · **end/** = `/stages/stage-6-block-4/`
byte for byte. Line 1 of each file (the slide comment) is not typed live.

## Typed live — style.css, inside block 4
Between the `/* ===== 4. Box model (§4) ===== */` header and `table, th, td`:
1. ```
   main {
     width: 720px;
     padding: 24px;
     border: 1px solid #B9CECE;
   }
   ```
   Ctrl+S — the content is boxed and stops running to the window edge.
2. ```
   .dish {
     min-height: 135px;
     padding: 16px;
     margin-bottom: 24px;
     border: 1px solid #B9CECE;
     background-color: #E8EFEF;
   }
   ```
   Ctrl+S — two mist cards. `min-height` changes nothing yet; it is needed when the image
   floats in Part 5.
3. After the `th` rule: `footer {` / `padding: 16px 24px;` / `}`. Ctrl+S.

## Try it (the slide's box)
- `.dish` padding → `0px`, save: the text touches the card's edge. Restore.
- `.dish` margin-bottom → `0px`, save: the two cards touch. Restore.
Have a student call out which gap disappeared each time.
Fallback: copy `variants/try-padding-0.css` or `try-margin-0.css` over `style.css`.

## Fault to expect
`dish {` without the dot: matches no element, no error, nothing happens.
