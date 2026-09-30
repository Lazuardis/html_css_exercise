# 08 · s2-specificity — "Why is the nav link blue when "a" says teal?"

**Deck:** Part 2 · **Indicator:** 3 · **Time:** 4 min
**start/** = `/stages/stage-6-block-2/` · **end/** = `/stages/stage-6-block-2/` byte for byte
(the demonstration rule is deleted at the end).

## Open when the slide appears
Working copy of `start/`; `style.css` scrolled to the bottom; `index.html` in the browser.

## Typed live, in order
1. At the very bottom of `style.css`: `a {` Enter `color: red;` Enter `}`. Ctrl+S, refresh.
2. Ask the room to predict first, then look.
3. Change `a {` to `a.current {`. Ctrl+S, refresh.
4. Delete the rule. Ctrl+S — back to block 2.

## Room sees
- Step 1: the nav links stay blue and the header link stays teal, even though red came
  last. `nav > ul > li > a` (four elements) and `header a` (two) beat `a` (one).
- Step 3: the current nav link turns red — a class beats any chain of elements.
- Bonus, if asked: on `location.html` the "book a table online" link *does* turn red at step
  1. Nothing else targets it, so there is no competition. Order only decides ties.

## variants/
Drop-in copies of `style.css` if typing fails — copy over the working `style.css`, refresh:
- `try-red-element.css` — step 1 (broken on purpose: the red loses).
- `try-red-class.css` — step 3 (the class wins).
Reset: copy `start/style.css` back.

## Fault to expect
"The last rule always wins." It does only when the selectors are equally specific.
Keep the weights table informal; the ordering is examined, the point-counting is not.
