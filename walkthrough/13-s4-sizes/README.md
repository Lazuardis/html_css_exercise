# 13 · s4-sizes — "Each box is the one inside it plus its own two sides"

**Deck:** Part 4 · **Indicator:** 5 · **Time:** 3 min
**Folder:** README + `start/` only — no live edit. `start/` = `/stages/stage-6-block-4/`.

## Deck order — read this first
In the deck this slide comes **before** s4-code (walkthrough 12). When it appears, your
working copy does not yet have the `main` rule. Open this folder's `start/`, not the
working copy.

## Open when the slide appears
`start/index.html` in the browser. F12 → Elements → click `<main>` → the box diagram
(Computed tab in Chrome and Edge; Layout in Firefox).

## Typed live
Nothing. Do the arithmetic aloud first, then show the diagram.

## Room sees
The diagram, with the numbers filled in: content 720, padding 24 on each side, border 1 on
each side. Hover `main` on the page: the tooltip says **770**, not 720.
720 + 24 + 24 = 768 → + 1 + 1 = 770. An element's size is its border box.

## What to say
The Elements panel is a Week 6 skill; the box diagram needs no explanation.
The shorthand table is reading knowledge: `padding: 8px 16px` and `margin: 0px auto` are in
every stylesheet students will open, including ours.

## Fault to expect
Someone measures with the page zoomed. Reset zoom (Ctrl+0) before reading numbers.
