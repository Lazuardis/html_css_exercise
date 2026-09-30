# 03 · s1-shift — "A div that says what it is"

**Deck:** Part 1 · **Indicator:** Part 1, not RPS · **Time:** 5 min
**start/** = `/stages/stage-5a-div/` · **end/** = `/stages/stage-5b-semantic/` byte for byte.
Line 1 of each file (the slide comment) is not typed live.

## Open when the slide appears
Working copy of `start/` in VS Code, `index.html` in Live Preview.

## Typed live — four find-and-replace, all three files at once
Ctrl+Shift+H (Replace in Files), scoped to the working folder. Replace All each time:
1. `<div id="header">` → `<header>`
2. `<div id="nav">` → `<nav>`
3. `<div id="main">` → `<main>`
4. `<div id="footer">` → `<footer>`

## Then the closers, by hand, in each file
The four region closers are the `</div>` lines at **four spaces** of indent. Top to bottom:
`</header>`, `</nav>`, `</main>`, `</footer>`. Do not touch the dish-card `</div>` lines at
six spaces — the dish cards stay divs. Ctrl+K S (save all).

## Room sees
Nothing changes. Open `start/index.html` and `end/index.html` side by side: pixel for pixel
identical (checked in Chromium). Then say the three cards on the slide — the middle one
("one new idea, not four new tags") for the weaker students, the right one ("div stays in
the toolbox") for the stronger ones.

## Fault to expect
A dish-card `</div>` renamed to `</main>`: the browser quietly repairs it and the page
still looks right. Diff against `end/` if anything seems off.
