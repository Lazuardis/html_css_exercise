# demos — broken/correct pairs (CLAUDE.md §8)

Every `*-broken.*` file is **broken on purpose** and says so on line 1. None of this folder
goes into `/deploy/`. All pages are copies of the final `index.html`; they share the images
and `style.css` here. Open any page by double-click.

| Pair | Slide | The fault | What you see |
|---|---|---|---|
| `semicolon-broken` / `-correct` (.html + .css) | act1 notes | `color: #064E4F` with no `;` before `text-transform:` | "Our Menu" stays mixed case; the heading is still teal (block 1 sets it) — the next declaration died silently |
| `href-broken` / `-correct` | act1 notes | `href="styles.css"`; the file is `style.css` | No style at all, and no error anywhere |
| `link-in-body-broken` / `-correct` | s2-link notes | the `link` element right after `<body>` | Looks identical — it works in most browsers, and is still wrong |
| `reused-id-broken` (.html + .css) / `reused-id-correct` | act1 check 3 | `id="price"` on both prices, styled by `#price` | Looks identical — it "works", which is why it is wrong. An id is unique per page |
| `float-spill-broken` (.html + .css) / `float-spill-correct` | s4-code L7 | `.dish` without `min-height` | The floated image hangs below the card's bottom border — see the note below |
| `collapsed-header-broken` (.html + .css) / `collapsed-header-correct` | s5-old-way, act2 fast finisher | two floats in `header`, nothing else | F12 on `<header>`: height 0. Not fixed — flexbox, supplementary session |

Three more §8 faults live inside walkthroughs, where they are demonstrated:
red that loses → `walkthrough/08-s2-specificity/variants/`;
case and absolute path → `walkthrough/19-s6-pitfalls/variants/`.

## Note on the float spill
With the canonical dish text the overhang is small: 2px at 1100px wide in Chromium, where
the card's text is nearly as tall as the 135px image. Show it with F12 (hover the `img`
and the `.dish`) rather than expecting the room to see it. On a student's own site with
one-line descriptions it is obvious.
