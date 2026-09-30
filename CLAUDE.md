# DG234507 — Week 4 Teaching Materials

Working repo for **Week 4: CSS, Structure and Publishing**. Everything here supports one
150-minute lecture session and the walkthroughs the lecturer performs in VS Code while the deck is
on the projector. Read this whole file before creating or editing anything.

The deliverables are **example files a lecturer demonstrates and students copy**. They are not
production web pages. A file that is technically better but uses something not yet taught is a
worse file for this repo. Week 3's CLAUDE.md governed a folder of plain `.html`; this one adds a
stylesheet, a three-page site, and a deployment target — and the same discipline.

**Order of authority.** The deck is the top reference, then this file. Within the deck, the
screenshots and code panels outrank the speaker notes: a note that contradicts what the slide
shows is corrected, not followed. Where this file and the deck disagree, flag it and change this file.

---

## 1. Course facts

| | |
|---|---|
| Course | DG234507 Pemrograman Web dan Mobile · 3 SKS · Curriculum 2023 |
| Programme | Bisnis Digital (Digital Business), Dept. of Business Management |
| Faculty | Design, Creative and Digital Business, ITS |
| Coordinator | Lazuardi Al-Muzaki · zaki@its.ac.id |
| This week | Week 4, Block 2 "Building Web Pages" · 150 minutes · break at 1:05 |
| Cohort | Digital Business students, **not** Informatics. They wrote their first HTML last week. |
| Companion deck | Claude Slides artifact **"DG234507 W4 – CSS, Structure and Publishing"**, 51 slides, built on MB-Deck-Template-1. Slide ids are used throughout this file (§7). |
| Seed files | `/stages/` was seeded from the `little-lemon-week4.zip` built alongside the deck. Every screenshot in the deck is a render of those exact files. **Do not regenerate or "tidy" them.** |
| Session plan | Not yet written. When it exists it lives at `claude/week-04-…-session-plan.md` in the Claude project. |

**Course texts.** `[CH]` Connolly & Hoar (2022), *Fundamentals of Web Development*, 3rd ed.,
Pearson — ch. 4 (CSS 1: selectors and basic styling) and ch. 7 (CSS 2: layout) this week.
`[LT]` Laudon & Traver (2023), *E-commerce 2023–2024*, 18th Global Edition — ch. 3 for the
hosting comparison revisited in Part 6. `[OUT]` the course reference document *CSS: Selection,
Styling and Layout — an academic outline of Lessons 1–6*, the primary source for Parts 2–5.
Cite `[CH]` chapters as **3rd edition**.

**Why a business cohort types CSS.** They will approve redesign quotations, read a vendor's
"we set the brand colour in one place" and know whether to believe it, and say "deployment"
knowing what it costs. Keep that framing in any student-facing prose. Never imply they are
training to be developers.

**Session shape.** Six parts: (1) from elements to a site, (2) rules and selectors, (3) colour
and text, (4) the box model, (5) document flow and alignment, (6) GitHub Pages. Three activities.
Part 1 and Part 6 are additions beyond the RPS; Parts 2–5 are the RPS.

---

## 2. The indicators — the spine

RPS Week 4 lists eight. **Six are taught this session; two are deferred.** Every file traces to
at least one indicator, or to one of the two non-RPS parts, and says which in its header comment.

| # | Indicator | Source | Status |
|---|---|---|---|
| 1 | Write a CSS rule and attach an external stylesheet to a document | CH 4 | Taught — Part 2 |
| 2 | Select elements by type, class, id, descendant and child | CH 4 | Taught — Part 2 |
| 3 | Resolve conflicting rules using specificity | CH 4 | Taught — Part 2 |
| 4 | Set colour and typography using colour models and font stacks | CH 4 | Taught — Part 3 |
| 5 | Explain the box model and size an element with it | CH 4 | Taught — Part 4 |
| 6 | Explain document flow, block vs inline, and align elements | CH 7 | Taught — Part 5 |
| 7 | Build a page layout using flexbox | CH 7 | **Deferred** — supplementary session, date TBA |
| 8 | Adapt a layout to small screens using media queries | CH 7 | **Deferred** — same session |
| — | Structure a page into site regions (header, nav, main, footer) | CH 3; WHATWG | Part 1, not RPS, examinable as HTML |
| — | Publish a static site to GitHub Pages; state what static hosting cannot do | GitHub Docs; LT 3 | Part 6, **not examinable** |

Files serving indicators 7–8 are **not to be built** until the supplementary session is scheduled
(§13, backlog item 12). If a file needs flexbox to work, it is the wrong file for this repo.

---

## 3. HARD RULE — the taught vocabulary

**Use only what Weeks 3 and 4 have taught.** Everything in Week 3's Allowed list remains allowed.
Week 4 adds the following and nothing else.

### HTML added in Week 4

```
Regions      <header>  <nav>  <main>  <footer>        — the four site regions, one each per page
Grouping     <div>  <span>                            — generic; div for the dish cards, span only in
                                                        the document-flow demo (§7, 14-s5-block-inline)
Attributes   class="..."   id="..."                   — id unique per page; class shared
Head         <link rel="stylesheet" href="style.css">  — now real, one per page, in head
Validation   required   min="..."  max="..."           — on the three book.html inputs only
```

`<section>`, `<article>`, `<aside>`, `<figure>` remain out. If a region needs a name and the four
above do not fit, it is a `div` with an id.

### CSS allowed — the whole list

```
Selectors    element   #id   .class   element.class   A B (descendant)   A > B (child)
             A, B (grouping)   :hover
Colour       color  background-color        values: named, #hex, rgb(), rgba(), hsl()
Text         font-family (always a fallback list)  font-size (px)  font-weight  font-style
             text-transform  text-decoration  text-align
Box          width  min-height  padding  padding-*  margin  margin-*  border  border-*
             border-collapse   (shorthand forms as on slide s4-sizes)
Flow         display: block | inline        list-style: none        float: left | right
Units        px, %, auto — nothing else
```

### Banned — do not use, do not "improve" a file by adding

| Thing | Taught in | If you feel the pull |
|---|---|---|
| `display: flex`, `grid`, `gap`, `justify-content`, `align-items` | Supplementary session (ind. 7) | Use `display: inline` on `li`, `margin: auto`, `float`. The strain is the point. |
| `@media`, `max-width` breakpoints, viewport meta | Supplementary session (ind. 8); Week 13 | Let the page break at phone width. Activity 2 check 3 asks students to notice. |
| `position`, `z-index`, `transform`, transitions, animations | Deferred by [OUT] itself | — |
| `rem`, `em`, `vw`, `calc()`, CSS variables | not in this course | px and % only |
| `box-sizing`, `:root`, `*` selector, `!important`, pseudo-elements | not taught | `!important` in particular undoes the specificity lesson. Never. |
| Frameworks (Bootstrap, Tailwind), preprocessors, resets | not in this course | — |
| Inline `style="…"` attributes and `<style>` blocks | superseded this week | The Week 3 `<style>` trick is deleted at stage 5a and repaid in style.css on slide s3-debt. Never reintroduce. |
| JavaScript, `<script>`, event attributes | **Week 5** | Not even to demonstrate `:hover`'s JS equivalent. |
| Server code, form handling, what happens after submit | **Week 8** | Say "Week 8" and stop. |
| Custom domains, DNS, CNAME files, GitHub Actions workflows, git CLI | **Week 12** | Browser upload only. No terminal. |

**Escape hatch.** If a requested file cannot be built inside this vocabulary, stop and say so.
The answer is almost always "that is flexbox, and it waits for the supplementary session".

---

## 4. The Little Lemon canon

One restaurant site, extended from Week 3. **Every file uses these exact strings.** Students
compare their screen against the projector; a changed string reads as an error in their own work.
Week 3's canon (restaurant name, address, dishes, prices, image names, alts, `/book` + `post`,
author meta, description meta) is unchanged. Week 4 adds:

```
Tagline        Middle Eastern food in the Main District        (no full stop — the meta keeps its stop)
Hours          Open daily, 11:00–22:00                          (en dash)
Phone          (021) 555 0123
Footer line 2  Open daily, 11:00–22:00 · (021) 555 0123         (middle dot, spaces either side)
Nav labels     Menu → index.html   Location → location.html   Book a Table → book.html
Site-name link <p id="site-name"><a href="index.html">Little Lemon</a></p>
Tagline        <p id="tagline">…</p>
Page titles    index.html "Little Lemon" · location.html "Our Location" · book.html "Book a Table"
h1s            Our Menu · Our Location · Book a Table
Dish cards     <div class="dish">  img first, then h2, then p, then <p class="price">
Price list     h2 "Price list" precedes the table on index.html
Current page   class="current" on the nav <a> for the page you are on — a different link per page
Validation     name: required · email: required · party: min="1" max="12" required
Stylesheet     style.css, same folder as the pages, linked from every head
Demo-only ids  named · rgb · rgba · hex · hsl · teal — walkthrough 09's colours.html only, never on a site page
```

### The palette — the only colours in style.css

```
#FCFDFC  body background          #1C2B2B  body text
#064E4F  h1, h2, header link, footer background
#5F7171  tagline, table borders   #B9CECE  main and card borders
#E8EFEF  card background, th background
#0067AC  nav links                #B86B00  prices
"Helvetica Neue", Arial, sans-serif   — the one font stack
```

These are the MB ITS deck tokens, so the site and the slides agree. Do not introduce a colour
outside this list. On slide s3-colour the worked hex is `#064E4F`; a demo that reads a hex code
uses that one.

### The stages

Each stage is a saved state the lecturer opens. **Stages 4–6 are seeded and canonical**; the
block sub-stages of stage 6 are cumulative snapshots of one `style.css`.

| Stage | Deck slide(s) | Folder | State |
|---|---|---|---|
| 4 | s1-before | `/stages/stage-4/` | Week 3's endpoint: one flat `index.html` with the Activity 2 form appended and the `<style>` border trick |
| 5a | s1-div-code, s1-div-result | `/stages/stage-5a-div/` | Three pages; regions as `<div id="header|nav|main|footer">`; identical nav list; no CSS — the Week 3 `<style>` is deleted here, so the table loses its borders until 6·4 |
| 5b | s1-shift, s1-both-valid, s1-site-map | `/stages/stage-5b-semantic/` | Same, regions as `header nav main footer`; pixel-identical to 5a |
| 6·0 | s2-link | `/stages/stage-6-block-0/` | 5b + `style.css` containing **only** `h1 { color: #064E4F; }` + link in three heads |
| 6·1 | s2-first-rules | `/stages/stage-6-block-1/` | + body font/colour/background, h1, h2 (element selectors) |
| 6·2 | s2-our-selectors, s2-result | `/stages/stage-6-block-2/` | + ids, classes, descendant, child, :hover, a.current; HTML gains ids and classes |
| 6·3 | s3-text, s3-result | `/stages/stage-6-block-3/` | + h1 size and transform, footer colours, font-size |
| 6·4 | s3-debt, s4-code, s4-result | `/stages/stage-6-block-4/` | + table rules (the Week 3 `<style>` debt from 5a, repaid in style.css), main box, .dish cards, padding; book.html gains validation attributes |
| 6·5 | s5-display, s5-align, s5-result | `/stages/stage-6-block-5/` = `/stages/stage-6-styled/` | + nav bar, margin: auto, text-align, float, h2 margin fix. **Final.** |

`style.css` in the final stage is written in five commented blocks, in this order, and each block
sub-stage is the file truncated after that block. When you generate a block sub-stage, truncate;
never rewrite. `gen_site.py` in `/tools/` regenerates 5a/5b/6 from one source; it is a
convenience for the lecturer, not a build step, and the committed HTML is the source of truth.

Images: `falafel.jpeg` and `salad.jpeg` are 240×135 placeholder JPEGs. Keep them; the float demo
needs real dimensions.

---

## 5. House style

### HTML
All Week 3 rules hold (two-space indent, one element per line, lowercase, double quotes, `img`
attribute order `src width height alt`, `input` order `type id name value` then validation
attributes last, label before input, blank line between blocks). Additions:

- Region order in `body` is always `header`, `nav`, `main`, `footer`. Nothing outside them.
- `header`, `nav` and `footer` are **byte-identical across the three pages** except for which
  nav link carries `class="current"`. Diff them before claiming a stage is done.
- The `head` is identical across pages except `<title>`.
- Inside a dish card: `img`, `h2`, `p`, `p.price` — in that order. The image comes first
  because `float` starts on the line where the element appears; slide s5-align's notes say so.
- `class` and `id` values: lowercase, hyphenated, and only the ones in §4. No new ones without
  updating §4.

### CSS
- One rule per selector per block. A selector may reappear in a later block (e.g. `h1`, `footer`,
  `main`) — that is deliberate: it shows that later declarations add to earlier ones.
- One declaration per line, two-space indent, a space after the colon, semicolon on every line
  including the last. The slide code panels compress rules to one line to fit; **files never do**.
- Property order within a rule: as the deck's code panel shows it — the deck is the reference,
  because students type from it. Where no panel shows the rule: colour/text first, then box
  (width, padding, margin, border), then flow (display, float, text-align).
- Comments: `/* ===== N. Title (§part) ===== */` as block headers, nothing else. No commented-out
  rules left behind.
- No blank rules, no rules that match nothing (except in a broken demo, §8).
- Colours as `#RRGGBB` uppercase in `style.css`. `rgb()`, `rgba()`, `hsl()` and names appear
  only in the colour demo (§7, 09-s3-colour).

### Files
- UTF-8, LF, final newline, no BOM. Lowercase file names, always — the deployment target is
  case-sensitive and the deck makes a point of it.
- Files open by double-click from the file system. **No server, no build step, no package
  manager, no linter.** A `.html` + `.css` + `.jpeg` folder must be droppable onto GitHub Pages
  as-is (§10).

### Accessibility rules that still hold
Week 3's seven rules apply to every file. Week 4 adds:

8. The nav is a `ul` of `li` of `a`, styled into a bar with CSS. Never three links in a `p`.
9. `text-transform` changes display only; the HTML keeps the real capitalisation.
10. Every colour pair used for text has visible contrast (the palette in §4 was chosen for that;
    do not pair `#5F7171` on `#064E4F`).
11. `:hover` is never the only way a state is shown — `a.current` is bold *and* a nav link.

---

## 6. Repo conventions

```
/stages/            the nine Little Lemon states from §4, one folder each — seeded, canonical
/walkthrough/       one folder per demonstrated slide (§7): README + start/ + end/ (+ variants/)
/demos/             broken/correct pairs (§8) not tied to one walkthrough
/activities/        starter + solution + check answer key for Activities 1, 2, 3
/deploy/            the folder a student uploads in Activity 3: stage 6 final, verified per §10
/handouts/          printable one-pagers: pre-class GitHub check, CSS cheat sheet, pitfalls card
/tools/             gen_site.py, screenshot script — lecturer conveniences, never required
README.md           folder map for a teaching assistant
```

- Student-facing files keep the canonical names (`index.html`, `location.html`, `book.html`,
  `style.css`) so they match the projector.
- A solution file is `*-solution.*` and never sits inside a starter folder.
- Every `.html` and `.css` file opens with a comment naming the **deck slide id**, the indicator
  (or "Part 1 / Part 6, not RPS"), and its role (`start`, `end`, `final`, `variant`, `broken`, `correct`).
  In CSS: `/* slide: s2-link · indicator 1 · end state */`.

---

## 7. The walkthrough map — deck slide ↔ VS Code

This is the section this repo exists for. The lecturer presents from the deck and switches to
VS Code with Live Preview open. Each walkthrough folder is the thing on the screen at that slide.

**Folder contract.** `/walkthrough/NN-<slide-id>/` contains:

- `README.md` — slide id and title, deck part, indicator, *what is open when the slide appears*,
  *what is typed live* (exact keystrokes, in order), *what the room should see change*, the fault
  to expect, and time in minutes. Under 40 lines.
- `start/` — the folder state before the live edit. The lecturer copies this to reset.
- `end/` — the state after. Must equal the corresponding `/stages/` folder byte for byte where
  one exists; say which.
- `variants/` — optional: a deliberately altered copy for a "Try it" or a fault (named
  `try-<what>.css`, `fault-<what>.html`), each with a one-line comment at the top.

`start/` and `end/` are **copies**, not symlinks, so a folder can be zipped and handed to a
student. Stage folders in `/stages/` are the authority; a walkthrough `end/` that drifts from its
stage is a bug.

| NN | Slide id | Part · ind. | start → end | Typed live | Room sees |
|---|---|---|---|---|---|
| 00 | hook | Open | stage-4 (no edit) | — | stage-4 index.html next to a real restaurant site in another tab |
| 01 | s1-before | 1 | stage-4 (no edit) | — | The flat page; lecturer points at what is missing (name, nav, address) |
| 02 | s1-div-code | 1 | stage-4 → stage-5a | Delete the Week 3 `<style>` block; wrap body in four `div id=` regions; add the nav `ul`; split into three files | Nothing visibly changes except the nav list appearing and the table borders vanishing — say so, and say the border comes back in Part 3 |
| 03 | s1-shift | 1 | stage-5a → stage-5b | Four find-and-replace: `<div id="header">`→`<header>` etc. and closers | Pixel-identical; open 5a and 5b side by side |
| 04 | s1-site-map | 1 | stage-5b (no edit) | — | Three tabs, click through the nav |
| 05 | s2-link | 2 · 1 | stage-5b → stage-6-block-0 | Create `style.css` with the h1 rule; add the `link` to three heads | Three headings turn teal on one save |
| 06 | s2-first-rules | 2 · 1 | block-0 → block-1 | body, h1, h2 rules | Font and colours change on all pages |
| 07 | s2-our-selectors | 2 · 2 | block-1 → block-2 | Add ids/classes to HTML first, then the six rules | Site name large, prices amber, current bold, hover underline |
| 08 | s2-specificity | 2 · 3 | block-2 + `variants/` | Append `a { color: red; }` at the bottom; refresh; change to `a.current { color: red; }` | Red does *not* win the first time; wins the second. Variants: `try-red-element.css`, `try-red-class.css` |
| 09 | s3-colour | 3 · 4 | `variants/colours.html` | — | One page with five `p`s: one red written five ways as on the slide (named, rgb, rgba at 0.8, hex, hsl), plus the `#064E4F` breakdown |
| 10 | s3-text | 3 · 4 | block-2 → block-3 | h1 size/transform, footer, font-size | OUR MENU uppercase; teal footer band |
| 11 | s3-debt | 3 · 4 | block-3 → block-4 (table + book.html part) | Type the table border rule (the Week 3 rule, deleted at 5a) into style.css, save; then add `border-collapse`; add `required`/`min`/`max` | Borders return doubled, then become single; empty submit refused with the browser's own message |
| 12 | s4-sizes | 4 · 5 | block-4 (no edit) | — | DevTools box diagram on `main` showing 770 not 720. Deck order puts it before s4-code, so it opens the prebuilt block-4 |
| 13 | s4-code | 4 · 5 | 11 end → block-4 (box part) + `variants/` | main box, .dish cards, padding | Content boxed; cards mist. Variants: `try-padding-0.css`, `try-margin-0.css` — which gap disappears |
| 14 | s5-block-inline | 5 · 6 | `variants/flow.html` | Change the middle `span` to a `div` | Sentence three moves too. [OUT] Lesson 5's demo in the slide's words: "Sentence one.", "Sentence two.", "Sentence three." in spans inside a div |
| 15 | s5-display | 5 · 6 | block-4 → block-5 (nav part) | `nav ul`, `nav li`, `nav` rules — `display: inline` typed last | Stack becomes a row on one save |
| 16 | s5-align | 5 · 6 | block-5 (nav) → block-5 final + `variants/` | main margins auto, text-align, float, h2 margin | main jumps to centre. Variant `try-no-width.css`: delete width → back to the left |
| 17 | s5-old-way | 5 | `variants/float-header.html` + `.css` | Float site name left, tagline right — the two things the header holds | Header collapses to zero height — the motivation for flexbox. Not fixed. |
| 18 | s6-process | 6 | `/deploy/` (no edit) | Browser only: new repo → upload → Settings → Pages | The live URL. Screenshots captured the morning of class into `README.md` |
| 19 | s6-pitfalls | 6 | `variants/` | — | `fault-Location.html` (capitalised) with a lowercase link to it; `fault-href-absolute.html` with a `file:///` href; `fault-index-in-folder/` |

Walkthroughs 00, 01, 04, 12 and 18 have no live edit; their folder is a README plus `start/`
only. Build the numbered folders **in order**; each `start/` is the previous `end/` — except 12,
which opens the prebuilt block-4, and 18–19, which open `/deploy/`. Numbering follows deck order.

---

## 8. Deliberately broken files

Faults that must be shown wrong-then-right. Named `*-broken.*` and `*-correct.*` (or
`fault-*` inside a walkthrough `variants/`), with a top comment saying it is broken on purpose.

| Demo | Slide | The fault, exactly |
|---|---|---|
| Missing semicolon | act1 notes | `color: #064E4F` with no `;` before `text-transform:` — the second declaration silently dies |
| Wrong href | act1 notes | `href="styles.css"` for a file named `style.css` — no error, no style |
| Link in body | s2-link notes | The `link` element placed after `<body>` — works in most browsers, is still wrong |
| Reused id | act1 check 3 | `id="price"` on both price paragraphs — "works", which is why it is wrong |
| Red that loses | s2-specificity | `a { color: red; }` appended last — element loses to child chain and to class |
| Float spill | s4-code L7 | `.dish` without `min-height` — image spills out of the card's border |
| Collapsed header | s5-old-way, act2 fast finisher | Two floats in `header`, nothing else — header height 0 |
| Case | s6-pitfalls | `Location.html` on disk, `location.html` in the link — opens locally, 404 deployed |
| Absolute path | s6-pitfalls | `href="file:///C:/Users/…/style.css"` — works on one laptop only |

Never leave a broken file unlabelled, and never put one inside `/deploy/`.

---

## 9. The three activities

### Activity 1 — Link a stylesheet, write five rules (15 min, slide act1)
Individual. On the student's *own* Week 3 homework site: wrap regions, add the nav list, create
and link `style.css`, write **one of each**: element, id, class used twice, descendant *or* child,
`a:hover`. Check: change propagates to all pages · semicolons · id unique / class repeated · write
two conflicting rules and say in one sentence which wins and why.

Starter: `/activities/activity-1-starter/` is a **stage-5b copy of Little Lemon with no
style.css** and a README saying "or use your own site". Solution: block-2 plus a
`check-answers.md` with the one-sentence specificity answer.

Faults to expect, in order: missing semicolon; wrong filename or link in body; reused id.

### Activity 2 — Box it, centre it, make the menu a bar (10 min, slide act2)
Pairs. Width + padding + border on main, centred with auto margins · nav into a bar · footer
band · one floated image with margin. Swap and check: delete the width — does it still centre ·
DevTools width of main · shrink the window — what breaks first (say "media query", do not fix) ·
is the nav still a `ul`.

Solution: block-5 final. `check-answers.md` must say for check 3: *nothing here fixes it; that is
indicator 8, deferred.* Fast finisher: site name left, tagline right — the collapsed-header float (walkthrough 17).

### Activity 3 — Deploy (12 min, slide act3)
Everyone. Five steps from slide s6-process on the student's own folder. Check: all pages reachable
· press Book a table and explain the result (static hosting) · post the URL in the class channel
with which pitfall they hit · open a classmate's link.

`/activities/activity-3/` holds only a `README.md` runbook (the five steps, the four pitfalls, the
"wait the full ten minutes" rule) — there is no solution file for a deployment. The register is
the list of URLs in the class channel.

### Homework
**Not yet set.** Slide next-week carries a bracketed placeholder. When set, it will be assessed
at the student's published URL. Do not write a homework exemplar or rubric until the brief exists.

---

## 10. Deployment constraints — `/deploy/` must stay droppable

`/deploy/` is stage 6 final, and every file in it must satisfy, at all times:

1. `index.html` at the top level of the folder, lowercase, ending `.html`.
2. All file names lowercase; all `href` and `src` values match the file name exactly.
3. Relative paths only, same folder, no leading `/`, no `file://`, no `..`.
4. No build step, no `package.json`, no `_config.yml`, no `.nojekyll` needed. Plain files.
5. The booking form's `action="/book"` stays as taught. Submitting it fails on GitHub Pages (an error page — confirm the exact status code on the day),
   and slide s6-limits says why. Do not change it to make deployment "work".
6. Nothing in `/deploy/` that should not be on a billboard: no notes, no answer keys, no
   broken variants.

The repository name in every handout is `username.github.io`, lowercase, public. The published
address is `https://username.github.io`. Publishing takes one to ten minutes; the runbook says
to check the Actions tab, not to re-upload.

---

## 11. Deferrals — say the week number

- Flexbox, grid, `position`, vertical centring → **supplementary CSS session, date announced
  Week 5** (indicator 7)
- Media queries, phone layouts → **same session** (indicator 8); Week 13 builds on it
- JavaScript, making `:hover` do something → **Week 5**
- Components, one header in one file → **Week 7**; a CMS doing it for you → **Week 9**
- The server receiving the form, real validation → **Week 8**
- What a repository is, beyond "a folder that remembers its history" → **Week 6** (slide s6-process)
- Custom domains, pointing a bought name at the Pages site, git and the CLI → **Week 12**
- ARIA → out of scope this semester. The semantic four are landmarks; that is the accessible win.

---

## 12. Verify before claiming done

1. Open every page by double-click from the file system. It must render, with style and images.
2. Read `style.css` against §3 — every property and selector is in the Allowed list; nothing
   from the Banned table.
3. Diff `header`, `nav`, `footer` across the three pages: identical except `class="current"`.
4. Check every canonical string against §4 character for character, including the en dash in
   the hours and the middle dot in the footer.
5. For a block sub-stage: confirm it is the final `style.css` truncated after that block's
   comment header, not rewritten.
6. For a walkthrough: `end/` equals its named stage folder (`diff -r`); `start/` equals the
   previous walkthrough's `end/`.
7. For `/deploy/`: run the six checks in §10, then `find . -name '*[A-Z]*'` returns nothing.
8. For a broken file: the top comment says it is broken and names the slide.

`/tools/screenshot.py` (Playwright, Chromium, 1100px wide) renders a folder's `index.html` to
PNG for comparison against the deck's checkpoint slides. Optional; never a dependency of any
student-facing file.

---

## 13. Backlog — work top-down

1. `/stages/stage-6-block-0…5/` — truncate the seeded final `style.css` into the five
   cumulative snapshots plus block-0 (h1 rule only). Verify per §12 item 5.
2. `/walkthrough/00…19/` per §7, in order, each with README, start, end.
3. `/demos/` — the nine broken/correct pairs from §8 not already inside a walkthrough.
4. `/activities/activity-1-starter/` + `-solution/` + `check-answers.md`.
5. `/activities/activity-2-solution/` + `check-answers.md` (with the "deferred, indicator 8" line).
6. `/activities/activity-3/README.md` — the runbook.
7. `/deploy/` — stage 6 final, verified per §10.
8. `/handouts/pre-class-github.md` — one page, issued before class: sign in and confirm your
   username; what a repository is in one paragraph; have your site folder ready with lowercase
   names; which browser; what to do if you have no account. Printable.
9. `/handouts/css-cheat-sheet.md` — one page: rule anatomy, the seven selectors, the palette,
   the box model diagram, the five allowed flow properties, the four pitfalls.
10. `/handouts/pitfalls-card.md` — slide s6-pitfalls as a quarter-page card.
11. `README.md` for a teaching assistant: the folder map and the slide↔walkthrough table.
12. **Placeholder only, do not build:** `/supplementary/` for flexbox and media queries. Create
    the folder with a README saying it waits for the supplementary session's outline and deck.
13. Screenshots for slide s6-process (three GitHub screens) — captured on the day, saved to
    `/walkthrough/18-s6-process/screens/`, and the deck updated by the lecturer.

Do not build past item 13 without asking. Do not add a build step, a package manager, a linter,
a framework or a git workflow to this repo — it is a folder of `.html`, `.css` and `.jpeg` files
a lecturer opens by double-clicking and a student uploads through a browser, and it must stay
that way.
