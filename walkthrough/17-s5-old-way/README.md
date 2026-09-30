# 17 · s5-old-way — "This is the layout method of 2010; it is taught for what comes next"

**Deck:** Part 5 · **Indicator:** 6 (motivation for deferred indicator 7) · **Time:** 2 min
**Folder:** README + `start/` + `variants/`. The live edit happens in `variants/`, so the
canonical `style.css` is never touched. `start/` = `/stages/stage-6-block-5/`.
Also the Activity 2 fast finisher.

## Open when the slide appears
`variants/float-header.html` in the browser (a copy of the finished index page that links
`float-header.css`, a copy of block 5), and `variants/float-header.css` in VS Code.

## Typed live — at the bottom of float-header.css
```
#site-name {
  float: left;
}

#tagline {
  float: right;
}
```
Ctrl+S, refresh.

## Room sees
The site name jumps left, the tagline right, and the nav bar rides up between them.
F12 → click `<header>`: its height is **0**. Floats take no height, so a header holding
only floats collapses.

## Not fixed — on purpose
No clearfix, no overflow trick. The fix is flexbox: supplementary CSS session, indicator 7,
date announced in Week 5. Say the week, not "later". Reset: re-copy `float-header.css`.

## Note
Same exercise as the Activity 2 fast finisher: site name left, tagline right — the only two
things in the header, so floating both leaves it holding nothing.

## Fault to expect
Only one float typed: the header keeps the tagline's height (18px). It takes both.
