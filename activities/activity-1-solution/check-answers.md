# Activity 1 — check answers (lecturer and TAs)

This folder is the Little Lemon solution: `/stages/stage-6-block-2/`, identical apart from
line 1 of each file. Students' own sites will differ; check the *kinds*, not the values.

## The build rules to enforce
- The stylesheet is **external** and linked from **every** page's head.
- Five rules, **one of each kind**. Five element selectors is not indicator 2.
  In the solution: `h1` (element) · `#site-name` (id) · `.price` (class, used twice on
  index.html) · `nav > ul > li > a` (child) and `header a` (descendant) · `nav a:hover`.

## Check 1 — does one save change every page?
Yes, if every head has the link. A page that does not change has no `link`, or its `href`
differs from the file name (`styles.css` vs `style.css`, or a capital letter).

## Check 2 — semicolons
Every declaration ends in `;`, the last one included. A missing semicolon kills the *next*
declaration silently: no error, it just does not apply. See `/demos/semicolon-broken.*`.

## Check 3 — ids once, classes many
In the solution, `site-name` and `tagline` appear once per page; `price` is on both price
paragraphs; `current` is on one nav link per page — a different one on each page.
An id used twice still renders (`/demos/reused-id-broken.*`). That is why it is wrong: the
browser does not tell you. An id names one element.

## Check 4 — the conflict, in one sentence (the assessable bit)
Hear the sentence. A model answer on Little Lemon:

> `a { color: red; }` loses to `nav > ul > li > a { color: #0067AC; }` because the more
> specific selector wins, and four elements are more specific than one — the order in the
> file only decides a tie.

Accept any correct sentence that names **specificity** (or "more precise selector") and
says which rule wins. "The last one wins" is wrong unless the two selectors are equally
specific — then it is right, and the student should say so.

## Fast finishers
- Current page: `class="current"` on a different nav link on each page, styled by `a.current`.
  Menu marked current on all three pages is the usual slip.
- A selector that matches nothing: nothing happens, and there is no error. That silence
  is the hard part of CSS.

## Faults you will see, in this order
1. A missing semicolon killing the next declaration.
2. The `link` inside `body`, or the wrong file name — the browser says nothing.
   (`/demos/link-in-body-broken.html`, `/demos/href-broken.html`)
3. An id reused on two elements — it "works", which is why it is wrong.
