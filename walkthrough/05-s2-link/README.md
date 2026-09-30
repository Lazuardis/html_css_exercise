# 05 · s2-link — "One link in each head; one file styles the whole site"

**Deck:** Part 2 · **Indicator:** 1 · **Time:** 3 min
**start/** = `/stages/stage-5b-semantic/` · **end/** = `/stages/stage-6-block-0/` byte for byte.
Line 1 of each file (the slide comment) is not typed live.

## Open when the slide appears
Working copy of `start/` in VS Code. Three browser tabs: index, location, book.

## Typed live, in order
1. Explorer → New File → `style.css` (lowercase, same folder as the pages).
2. Type the h1 rule from the previous slide, one declaration per line:
   `h1 {` Enter `color: #064E4F;` Enter `}` — VS Code closes the brace for you. Ctrl+S.
   Nothing changes yet: no page knows the file exists.
3. `index.html`: after the `<meta name="author" …>` line, type
   `<link rel="stylesheet" href="style.css">`
4. The same line, in the same place, in `location.html` and `book.html`. Ctrl+K S.
5. Refresh all three tabs.

## Room sees
Three headings turn teal at once, from one rule in one file. Say the business sentence:
change the brand colour once, and every page changes.

## Fault to expect
- The `link` typed after `<body>` instead of in `head`. It works in most browsers; say
  it belongs in `head` anyway. (`/demos/` has the broken/correct pair.)
- `href="styles.css"` for a file named `style.css`: no error, no style.
