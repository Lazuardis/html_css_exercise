# 14 · s5-block-inline — "Block elements stack; inline elements form a row"

**Deck:** Part 5 · **Indicator:** 6 · **Time:** 4 min
**Folder:** README + `start/` + `variants/`. The live edit happens in `variants/flow.html`;
the site is not touched. `start/` = `/stages/stage-6-block-4/`.

## Open when the slide appears
`variants/flow.html` in VS Code and in Live Preview. Zoom the preview (Ctrl+=) so the
room can read it — the page has no stylesheet on purpose.

## Typed live
1. The middle line: `<span>Sentence two.</span>` → `<div>Sentence two.</div>`.
   Change **both** tags. Ctrl+S.

## Room sees
Before: `Sentence one. Sentence two. Sentence three.` on one line.
After: three lines. Sentence two moved because a div is block-level — and **sentence three
moved too, though nothing was done to it**. Flow is relational: change one element's
category and its neighbours move. That is why layout bugs appear far from the line you edited.

## Reset
Change it back, or re-copy `flow.html` from the repo.

## Fault to expect
Only the opening tag changed (`<div>Sentence two.</span>`): the browser drops the stray
`</span>`, keeps the div open, and sentence three ends up inside it, on sentence two's line —
it looks as if sentence three did *not* move. Fix the closing tag and save.

## Note
The sentences are the slide's own words ("Sentence one." …), so the screen matches the projector.
