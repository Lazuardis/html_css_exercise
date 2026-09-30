# Activity 2 — check answers (lecturer and TAs)

This folder is the Little Lemon solution: `/stages/stage-6-block-5/` (final), identical apart
from line 1 of each file. Pairs work on their own sites from Activity 1; check the ideas.

## The build, and where it is in the solution
- `main`: width, padding, border (block 4); `margin-left: auto; margin-right: auto` (block 5).
- Nav bar: `nav ul` (no bullets, no indent), `nav li { display: inline; }`, `nav { text-align: center; }`.
- Footer band: `color` + `background-color` (block 3), `padding` (block 4).
- One floated image with a margin: `.dish img { float: right; margin-left: 16px; … }`.

## Check 1 — delete the width on main. Does it still centre?
No. main fills the whole width again. `auto` margins share out the *leftover* space, and
without a width there is none left over. Centring = set a width, let the margins absorb the rest.

## Check 2 — measure main in the developer tools
**770px**, not the 720 typed: 720 content + 24 + 24 padding + 1 + 1 border. An element's
size is its border box. (Indicator 5 again.)

## Check 3 — shrink the window to half. What breaks first?
main keeps its fixed 770px. Below about 786px wide it stops centring and hugs the left; below
about 778px it runs off the right edge, a horizontal scrollbar appears, and the footer band
(which has no width) keeps shrinking while main sticks out past it. The nav bar still fits.

**Nothing here fixes it; that is indicator 8, deferred.** Students say the words
"media query" — the supplementary session, date announced in Week 5. Do not fix it.

## Check 4 — is the nav still an unordered list in the HTML?
It must be: `nav > ul > li > a`. CSS changed how it looks, not what it is. A nav rewritten as
three links in a `p` fails this check even if it looks the same.

## Fast finishers
- Site name left, tagline right: the header collapses to height 0, because floats take no
  height and nothing else is left in it. Walkthrough 17 and `/demos/collapsed-header-broken.*`
  show it. That problem is why flexbox exists. Leave it unfixed.
- Current link with a bottom border instead of bold, for example
  `a.current { border-bottom: 2px solid #0067AC; }` — still visible without hovering.

## Before they leave the activity
Every student confirms one folder holds three pages, `style.css` and the images, all
lowercase. That folder is what they deploy in Activity 3.
