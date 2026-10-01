# Week 4 teaching note — slide by slide

DG234507 · Week 4 · CSS, Structure and Publishing · 150 minutes

Keep this open next to the deck. It follows the deck from slide 1 to slide 51 and tells you,
for every slide, whether you switch to VS Code, what to open, and what the room should see.
The exact keystrokes for each live edit are in that walkthrough's `README.md`.

**Deck:** [DG234507 W4 – CSS, Structure and Publishing](https://claude.ai/artifact/WvqCGEGNZcGXteDYDyqhE5)

---

## How to read the tables

| Tag | Meaning |
|---|---|
| **LIVE** | Switch to VS Code and type. Copy the walkthrough's `start/` into a scratch folder first. |
| **SHOW** | Open a file and point at it. Nothing is typed. |
| **TALK** | Slides only. VS Code stays closed. |
| **ACTIVITY** | Students work on their own laptops. Circulate. |

- **Min** comes from the deck's speaker notes. The clock windows in each heading come from the
  agenda slide, and they win when the two disagree.
- **WT 08** means walkthrough 08: [walkthrough/08-s2-specificity/](walkthrough/08-s2-specificity/).
- **Fell behind?** Copy that walkthrough's `end/` into your scratch folder and carry on.
- **Reset?** Copy `start/` in again.
- **Variants** (`try-*.css`): copy over `style.css` in your scratch folder, then refresh.

---

## The session at a glance

| Clock | Block | Slides | Live edits | Students |
|---|---|---|---|---|
| 0:00 – 0:25 | Opening + Part 1 · From elements to a site | 1–12 | WT 02, 03 | watch |
| 0:25 – 0:50 | Part 2 · Rules and selectors | 13–21 | WT 05, 06, 07, 08 | watch |
| 0:50 – 1:05 | **Activity 1** · Link a stylesheet, write five rules | 22 | — | individual |
| 1:05 – 1:15 | Break | 23 | — | — |
| 1:15 – 1:45 | Part 3 · Colour and text + Part 4 · Box model | 24–33 | WT 10, 11, 13 | watch |
| 1:45 – 2:00 | Part 5 · Document flow and alignment | 34–39 | WT 14, 15, 16, 17 | watch |
| 2:00 – 2:10 | **Activity 2** · Box it, centre it, make the menu a bar | 40 | — | pairs |
| 2:10 – 2:30 | Part 6 · GitHub Pages + **Activity 3** · Deploy | 41–47 | WT 18 (browser) | everyone |
| 2:30 | Close | 48–51 | — | — |

**Tight spot:** Part 6 and Activity 3 add up to 26 minutes of speaker-note time, but the window
is 20. The agenda's notes name two places to save time earlier: slide 18
(s2-descendant-child, leave the table up and move on) and slide 37 (s5-align, which Activity 2
repeats). Never cut Activity 1 or Activity 3.

---

## Before class

- [ ] Copy `/walkthrough/` somewhere you can type freely. Live edits happen in copies, never in the repo.
- [ ] VS Code open with Live Preview; one browser with three empty tabs; DevTools works (F12).
- [ ] Signed in to GitHub on the projector laptop. Know which account you will demo with.
- [ ] Capture the three GitHub screens for slide 43 into [walkthrough/18-s6-process/screens/](walkthrough/18-s6-process/) and update the deck.
- [ ] Test the campus network for uploads. If it blocks them, students tether to a phone.
- [ ] Note the error page GitHub shows when "Book a table" is submitted, so you can say it exactly on slide 46.
- [ ] Confirm you may publish the two dish photos (the falafel photo is from The Mediterranean Dish).

---

## Opening + Part 1 · From elements to a site · 0:00 – 0:25

| # · Slide | Min | Mode | What you do → what the room sees | Repo |
|---|---|---|---|---|
| 1 · `cover` | — | TALK | Collect the Week 3 homework at the door. One sentence: today we organise, style and publish. | — |
| 2 · `objectives` | — | TALK | Read the outcomes. Say plainly that flexbox and media queries are not today. | — |
| 3 · `agenda` | — | TALK | Post the run sheet so students pace themselves. | — |
| 4 · `hook` | 2 | SHOW | The Week 3 page beside a real restaurant site. Sort answers into two board columns, unlabelled. → Organisation vs appearance. | [WT 00](walkthrough/00-hook/) `start/` |
| 5 · `d1` | — | TALK | Divider. Structure before style. | — |
| 6 · `s1-before` | 3 | SHOW | Ask what a customer looks for first; point out what is missing. Point at the `<style>` block too. → No name, buried link, form under the menu. | [WT 01](walkthrough/01-s1-before/) `start/` |
| 7 · `s1-regions` | 4 | TALK | Draw the four bands on the board: identity, navigation, content, boilerplate. | — |
| 8 · `s1-div-code` | 4 | **LIVE** | Delete `<style>`, wrap in four `div id=` regions, add the nav `ul`, split into three pages. → The nav list appears; the table loses its borders. Say both. | [WT 02](walkthrough/02-s1-div-code/) `start/ → end/` |
| 9 · `s1-div-result` | 2 | TALK | Structure alone answered three of the customer's four questions. | ([WT 02](walkthrough/02-s1-div-code/) `end/` if asked) |
| 10 · `s1-shift` | 5 | **LIVE** | Four find-and-replace (Ctrl+Shift+H), then the closing tags by hand. → Pixel-identical; open 5a and 5b side by side. | [WT 03](walkthrough/03-s1-shift/) `start/ → end/` |
| 11 · `s1-both-valid` | 3 | TALK | Ask a student to read the screen-reader row aloud. | — |
| 12 · `s1-site-map` | 3 | SHOW | Three tabs, click through the nav. "The header is copied three times; the style will not be." | [WT 04](walkthrough/04-s1-site-map/) `start/` |

**If it goes wrong:** a missing `</div>` still looks right on screen, so keep the indentation
tidy and diff against `end/`. In WT 03, rename only the closers at four spaces; the dish-card
`</div>`s at six spaces stay divs.

---

## Part 2 · Rules and selectors · 0:25 – 0:50

| # · Slide | Min | Mode | What you do → what the room sees | Repo |
|---|---|---|---|---|
| 13 · `d2` | — | TALK | Divider. Indicators 1–3. | — |
| 14 · `s2-anatomy` | 3 | TALK | Selector, property, value — the room says them back. Warn about the semicolon. | — |
| 15 · `s2-link` | 3 | **LIVE** | Create `style.css` with the h1 rule, then add the `link` to three heads. → Three headings turn teal on one save. | [WT 05](walkthrough/05-s2-link/) `start/ → end/` |
| 16 · `s2-first-rules` | 2 | **LIVE** | Type `body`, then `h2`, around the existing `h1`. → New font and colours on every page. | [WT 06](walkthrough/06-s2-first-rules/) `start/ → end/` |
| 17 · `s2-selectors` | 4 | TALK | Walk the rows; stress the space versus the `>`. | — |
| 18 · `s2-descendant-child` | 3 | TALK | Read the three rows aloud. **Can be cut** if behind — leave the table up. | — |
| 19 · `s2-our-selectors` | 3 | **LIVE** | Add the ids and classes to the HTML first, then the seven rules. → Big site name, amber prices, bold current link, underline on hover. | [WT 07](walkthrough/07-s2-our-selectors/) `start/ → end/` |
| 20 · `s2-specificity` | 4 | **LIVE** | Append `a { color: red; }` — the room predicts, then sees it lose. Change it to `a.current` — it wins. Delete it. | [WT 08](walkthrough/08-s2-specificity/) `start/ → end/` · `variants/try-red-*.css` |
| 21 · `s2-result` | 2 | TALK | Rapid-fire quiz. If "Menu is bold because it's first" comes up, move `class="current"` and refresh. | ([WT 08](walkthrough/08-s2-specificity/) `end/`) |

**If it goes wrong:**
- **Link in `body`, or `styles.css`:** no error and no style. Pair: [link-in-body](demos/link-in-body-broken.html), [href](demos/href-broken.html).
- **Missing semicolon:** the next declaration dies silently. Pair: [semicolon](demos/semicolon-broken.html).
- **Red wins on `location.html`:** that in-text link has no competing rule, so red is right there. Order only decides ties.

---

## Activity 1 · 0:50 – 1:05 · then Break · 1:05 – 1:15

| # · Slide | Min | Mode | What happens | Repo |
|---|---|---|---|---|
| 22 · `act1` | 15 | ACTIVITY | Individual. Own Week 3 site: regions, nav, `style.css`, five rules of five different kinds. Check question 4 is the assessable bit — hear the sentence. | Starter [activity-1-starter/](activities/activity-1-starter/) · Answers [activity-1-solution/check-answers.md](activities/activity-1-solution/check-answers.md) |
| 23 · `break` | 10 | — | Students save `style.css` and check all pages still open. Restart strictly at 1:15. | — |

**Faults you will see, in this order:** missing semicolon → `link` in body or wrong file name →
an id used twice ([reused-id](demos/reused-id-broken.html) — it "works", which is why it is wrong).

---

## Part 3 · Colour and text · Part 4 · The box model · 1:15 – 1:45

| # · Slide | Min | Mode | What you do → what the room sees | Repo |
|---|---|---|---|---|
| 24 · `d3` | — | TALK | Divider. Indicator 4. | — |
| 25 · `s3-colour` | 4 | SHOW | One red, five ways (the RGBA line is lighter — that is alpha). Read `#064E4F` as three pairs; F is 15, FF is 255. | [WT 09](walkthrough/09-s3-colour/) `variants/colours.html` |
| 26 · `s3-text` | 3 | **LIVE** | h1 size and uppercase; the footer band. Save `color` alone first — the text vanishes. → OUR MENU; teal footer. Ctrl+U: the HTML still says "Our Menu". | [WT 10](walkthrough/10-s3-text/) `start/ → end/` |
| 27 · `s3-debt` | 4 | **LIVE** | Type the table border rule → borders return **doubled**; add `border-collapse` → **single**. Then `required`, `min`, `max` in `book.html`; submit it empty → the browser refuses. Say "Week 8". | [WT 11](walkthrough/11-s3-debt/) `start/ → end/` |
| 28 · `s3-result` | 1 | TALK | Colour and text are decoration; from here CSS is layout. | — |
| 29 · `d4` | — | TALK | Divider. Indicator 5. The pivot of the session. | — |
| 30 · `s4-diagram` | 4 | TALK | Restaurant analogy; draw four nested rectangles and label them from the inside out. | — |
| 31 · `s4-sizes` | 3 | SHOW | Do 720 + 24 + 24 + 1 + 1 aloud, then DevTools on `main`. → **770**, not 720. Open this folder, not your working copy. | [WT 12](walkthrough/12-s4-sizes/) `start/` |
| 32 · `s4-code` | 3 | **LIVE** | `main`, `.dish`, `footer` padding at the bottom. → Content boxed, mist cards. Try it: padding 0, then margin-bottom 0. | [WT 13](walkthrough/13-s4-code/) `start/ → end/` · `variants/try-*-0.css` |
| 33 · `s4-result` | 1 | TALK | "Why is `main` on the left?" — "Because nothing said otherwise." That is document flow. | — |

**If it goes wrong:**
- **`dish {` without the dot:** matches nothing, no error.
- **Zoomed browser:** reset zoom with Ctrl+0 before reading DevTools numbers.
- **`min-height` does nothing yet:** it matters once the image floats in Part 5 ([float-spill](demos/float-spill-broken.html) shows why; the spill is small, so point with F12).

---

## Part 5 · Document flow and alignment · 1:45 – 2:00

| # · Slide | Min | Mode | What you do → what the room sees | Repo |
|---|---|---|---|---|
| 34 · `d5` | — | TALK | Divider. Indicator 6. The pre-flexbox way. | — |
| 35 · `s5-block-inline` | 4 | **LIVE** | Change the middle `span` to a `div` — both tags. Zoom in. → Sentence two drops, **and sentence three moves too**. | [WT 14](walkthrough/14-s5-block-inline/) `variants/flow.html` |
| 36 · `s5-display` | 3 | **LIVE** | `nav ul`, `nav li`, `nav` — type `display: inline` **last**. → The stack becomes a row on one save. | [WT 15](walkthrough/15-s5-display/) `start/ → end/` |
| 37 · `s5-align` | 4 | **LIVE** | `main` auto margins → jumps to centre; `header, footer`; float the images; `.dish h2`. Try it: delete the width → back to full width. **Can be shortened** — Activity 2 repeats it. | [WT 16](walkthrough/16-s5-align/) `start/ → end/` · `variants/try-no-width.css` |
| 38 · `s5-result` | 1 | SHOW | Click through the three finished pages live. One file, three pages, the HTML barely changed. | [WT 16](walkthrough/16-s5-align/) `end/` |
| 39 · `s5-old-way` | 2 | **LIVE** | In `float-header.css`: site name left, tagline right. → Header height **0**. Do not fix it — flexbox, supplementary session. | [WT 17](walkthrough/17-s5-old-way/) `variants/` · [collapsed-header](demos/collapsed-header-broken.html) |

**If it goes wrong:**
- **Only the opening tag changed** (WT 14): sentence three stays on sentence two's line. Fix the closing tag.
- **`display: inline` on `nav ul`:** nothing happens; it belongs on `nav li`.
- **Only one float typed** (WT 17): the header doesn't collapse. It takes both.

---

## Activity 2 · 2:00 – 2:10

| # · Slide | Min | Mode | What happens | Repo |
|---|---|---|---|---|
| 40 · `act2` | 10 | ACTIVITY | Pairs, on their Activity 1 site: box and centre `main`, nav bar, footer band, one float. Swap and check. Fast finisher: site name left, tagline right. End with every folder complete. | Answers [activity-2-solution/check-answers.md](activities/activity-2-solution/check-answers.md) |

**Check 3 (shrink the window):** nothing here fixes it — that is indicator 8, deferred. Students
say "media query"; you do not fix it.

---

## Part 6 · Publishing + Activity 3 · 2:10 – 2:30

| # · Slide | Min | Mode | What you do → what the room sees | Repo |
|---|---|---|---|---|
| 41 · `d6` | — | TALK | Divider. Say it is not examinable in Week 10. | — |
| 42 · `s6-hosting` | 3 | TALK | The four Week 2 hosting rows, then the fifth: static, free. | — |
| 43 · `s6-process` | 4 | **LIVE** (browser) | New repo `username.github.io` → upload the *files* → Settings → Pages → Actions tick → open the URL. Name each step. | [WT 18](walkthrough/18-s6-process/) `start/` (= [deploy/](deploy/)) |
| 44 · `s6-url` | 3 | TALK | Read the new address as Week 2 taught: protocol, username, GitHub's domain, path. Warn about case. | — |
| 45 · `s6-pitfalls` | 2 | SHOW | The case link, the `file:///` href, the folder with no top-level index. **Keep this slide up during Activity 3.** | [WT 19](walkthrough/19-s6-pitfalls/) `variants/` |
| 46 · `s6-limits` | 2 | TALK | What "deployment" means on a quote. Book a table fails: static hosting runs no code. | — |
| 47 · `act3` | 12 | ACTIVITY | Everyone deploys their own folder; checks on a phone over mobile data; posts the URL in the class channel. Point at the pitfall card — do not fix sites yourself. | Runbook [activities/activity-3/README.md](activities/activity-3/README.md) |

**If it goes wrong:** wait the full ten minutes and check the Actions tab before anyone
re-uploads. Wrong repository name, `index.html` inside a folder, or a capitalised file name
cause almost every blank site.

---

## Close · 2:30

| # · Slide | Min | Mode | What you do | Repo |
|---|---|---|---|---|
| 48 · `summary` | 1.5 | TALK | Tick the takeaways against slide 2. Say when indicators 7–8 will be taught. If Part 6 was cut, open Week 5 with it. | — |
| 49 · `next-week` | 1 | TALK | Homework is still a placeholder — set it once you know how many sites are live. | — |
| 50 · `references` | — | TALK | Leave up while students pack. | — |
| 51 · `closing` | — | TALK | Stay for questions; most are about a site that won't load. | — |

---

## Never upload

Students upload only their own folder; you demo with [deploy/](deploy/). Nothing in
[demos/](demos/), any `variants/` folder or [activities/](activities/) answer keys belongs on a public site.
