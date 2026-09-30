# Activity 1 — Link a stylesheet to your site and write five rules

15 minutes · on your own · slide act1

**Use your own Week 3 homework site if you have it.** This folder is a spare: Little Lemon
with its regions and nav already in place (stage 5b) and **no style.css yet**. Open
`index.html` by double-clicking it.

## Build — 10 minutes
1. Wrap each page's body in `header`, `nav`, `main`, `footer`. Put the same nav list on
   every page. *(Already done in this spare.)*
2. Create `style.css` beside the pages — same folder, lowercase name.
3. Link it from the `head` of every page: `<link rel="stylesheet" href="style.css">`
4. Write five rules, one of each kind:
   - an element selector (for example `h1`)
   - an id (add `id="…"` to one element, select it with `#…`)
   - a class used on at least two elements (add `class="…"`, select it with `.…`)
   - a descendant (`header a`) or child (`nav > ul`) selector
   - `a:hover`
5. Refresh every page. Each rule must visibly change something.

## Check — 3 minutes
1. Change one value in `style.css` and save once. Does it change on **all** your pages?
2. Does every declaration end in a semicolon — the last one too?
3. Is each id used once per page, and your class used more than once?
4. Write two rules that conflict on one element. Which wins — and can you say why in one sentence?

## Fast finishers
- Mark the current page's nav link with a class and style it — a different link on each page.
- Write a rule whose selector matches nothing. What happens?
