# 02 · s1-div-code — "A div is a box with no meaning; the id gives it one"

**Deck:** Part 1 · **Indicator:** Part 1, not RPS · **Time:** 4 min (deck)
**start/** = `/stages/stage-4/` · **end/** = `/stages/stage-5a-div/` byte for byte.
Line 1 of each file (the slide comment) is not typed live.

## Open when the slide appears
Copy `start/` to a working folder; open it in VS Code with `index.html` in Live Preview.

## Typed live — index.html, in order
1. In `head`, delete the three `<style>` lines (Ctrl+Shift+K ×3). Say: "the Week 3 trick goes; the border comes back properly in Part 3."
2. Under `<body>`: `<div id="header">`, `<p><a href="index.html">Little Lemon</a></p>`, `<p>Middle Eastern food in the Main District</p>`, `</div>`.
3. Then `<div id="nav">`, `<ul>`, three lines `<li><a href="index.html">Menu</a></li>` / `location.html` Location / `book.html` Book a Table, `</ul>`, `</div>`.
4. Above `<h1>Our Menu</h1>`: `<div id="main">`.
5. Each dish: wrap in `<div>`…`</div>`; move the `img` line to the top (Alt+↑ ×2); under the description add `<p>$10</p>` (Falafel) or `<p>$12</p>` (Pasta Salad).
6. Above `<table>`: `<h2>Price list</h2>`. After `</table>`: `</div>`.
7. Delete `<p><a href="location.html">Our Location</a></p>`.
8. Select `<h2>Book a table</h2>` through `</form>`; Ctrl+X (it goes to book.html).
9. Last in body: `<div id="footer">`, `<p>123 Rome Road, Main District, Capital City</p>`, `<p>Open daily, 11:00–22:00 · (021) 555 0123</p>`, `</div>`. Paste the en dash and middle dot from this README.
10. Indent each region's contents one level (select, Tab). Ctrl+S.

## Then split into three files
11. Explorer: copy `index.html`, paste, rename `location.html`. Title `Our Location`. Replace the inside of `<div id="main">` with `<h1>Our Location</h1>`, `<p>123 Rome Road, Main District, Capital City</p>`, `<p>Open daily, 11:00–22:00</p>`, `<p>Call us on (021) 555 0123 or <a href="book.html">book a table online</a>.</p>`.
12. Copy again, rename `book.html`. Title `Book a Table`. Inside main: `<h1>Book a Table</h1>`, then Ctrl+V the form; delete the pasted `<h2>Book a table</h2>`; indent the form one level.

If you are short of time, do steps 1–4 live, then copy `end/` in: "the rest is the same move, repeated."

## Room sees
Nothing changes visibly except the nav list appearing — and the table losing its borders.
Say both out loud: a div is invisible, an id is a name and not a style, and the border
returns in Part 3.

## Fault to expect
A `</div>` left off: the page still looks right. That is why the indentation matters.
