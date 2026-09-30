"""Generates the Little Lemon stage 5a / 5b / 6 sites from one source of truth.
Canonical strings follow the Week 3 CLAUDE.md canon; new strings are listed in NEW_CANON."""
import os

NEW_CANON = {
    "tagline": "Middle Eastern food in the Main District",
    "hours": "Open daily, 11:00–22:00",
    "phone": "(021) 555 0123",
    "book_title": "Book a Table",
    "menu_title": "Our Menu",
    "loc_title": "Our Location",
}

def head(title, styled):
    link = '\n    <link rel="stylesheet" href="style.css">' if styled else ""
    return f"""  <head>
    <title>{title}</title>
    <meta name="description" content="Middle Eastern food in the Main District.">
    <meta name="author" content="Lazuardi Al-Muzaki">{link}
  </head>"""

def region(sem, name, inner, extra_attr=""):
    """sem=True -> <header>, False -> <div id="header">"""
    if sem:
        return f'    <{name}{extra_attr}>\n{inner}\n    </{name}>'
    return f'    <div id="{name}"{extra_attr}>\n{inner}\n    </div>'

def header_nav(sem, styled, current):
    site = f"""      <p><a href="index.html">Little Lemon</a></p>
      <p>{NEW_CANON['tagline']}</p>"""
    if styled:
        site = f"""      <p id="site-name"><a href="index.html">Little Lemon</a></p>
      <p id="tagline">{NEW_CANON['tagline']}</p>"""
    hdr = region(sem, "header", site)
    links = [("index.html", "Menu"), ("location.html", "Location"), ("book.html", "Book a Table")]
    lis = []
    for href, text in links:
        cur = ' class="current"' if styled and href == current else ""
        lis.append(f'        <li><a href="{href}"{cur}>{text}</a></li>')
    nav_inner = "      <ul>\n" + "\n".join(lis) + "\n      </ul>"
    nav = region(sem, "nav", nav_inner)
    return hdr + "\n\n" + nav

def footer(sem):
    inner = f"""      <p>123 Rome Road, Main District, Capital City</p>
      <p>{NEW_CANON['hours']} · {NEW_CANON['phone']}</p>"""
    return region(sem, "footer", inner)

def main_index(sem, styled):
    pc = ' class="price"' if styled else ""
    dish = ' class="dish"' if styled else ""
    inner = f"""      <h1>{NEW_CANON['menu_title']}</h1>

      <div{dish}>
        <img src="falafel.jpeg" width="240" height="135" alt="A falafel">
        <h2>Falafel</h2>
        <p>Chickpea, herbs, and spices</p>
        <p{pc}>$10</p>
      </div>

      <div{dish}>
        <img src="salad.jpeg" width="240" height="135" alt="A pasta salad">
        <h2>Pasta Salad</h2>
        <p>Lettuce, vegetables, and mozzarella</p>
        <p{pc}>$12</p>
      </div>

      <h2>Price list</h2>
      <table>
        <tr>
          <th>Dish</th>
          <th>Price</th>
        </tr>
        <tr>
          <td>Falafel</td>
          <td>$10</td>
        </tr>
        <tr>
          <td>Pasta Salad</td>
          <td>$12</td>
        </tr>
      </table>"""
    return region(sem, "main", inner)

def main_location(sem, styled):
    inner = f"""      <h1>{NEW_CANON['loc_title']}</h1>
      <p>123 Rome Road, Main District, Capital City</p>
      <p>{NEW_CANON['hours']}</p>
      <p>Call us on {NEW_CANON['phone']} or <a href="book.html">book a table online</a>.</p>"""
    return region(sem, "main", inner)

def main_book(sem, styled):
    req = " required" if styled else ""
    minmax = ' min="1" max="12"' if styled else ""
    inner = f"""      <h1>{NEW_CANON['book_title']}</h1>
      <form action="/book" method="post">
        <label for="name">Name</label>
        <input type="text" id="name" name="name"{req}>
        <br>
        <label for="email">Email</label>
        <input type="email" id="email" name="email"{req}>
        <br>
        <label for="party">Party size</label>
        <input type="number" id="party" name="party"{minmax}{req}>
        <br>
        <input type="radio" id="indoor" name="seating" value="indoor">
        <label for="indoor">Indoor</label>
        <input type="radio" id="outdoor" name="seating" value="outdoor">
        <label for="outdoor">Outdoor</label>
        <br>
        <label for="requests">Special requests</label>
        <textarea id="requests" name="requests" rows="3"></textarea>
        <br>
        <input type="submit" value="Book a table">
      </form>"""
    return region(sem, "main", inner)

def page(title, current, main_fn, sem, styled):
    return f"""<!DOCTYPE html>
<html>
{head(title, styled)}
  <body>
{header_nav(sem, styled, current)}

{main_fn(sem, styled)}

{footer(sem)}
  </body>
</html>
"""

SITES = {
    "stage-5a-div": (False, False),
    "stage-5b-semantic": (True, False),
    "stage-6-styled": (True, True),
}
for folder, (sem, styled) in SITES.items():
    os.makedirs(f"little-lemon/{folder}", exist_ok=True)
    for fn, title, main_fn in [("index.html", "Little Lemon", main_index),
                               ("location.html", "Our Location", main_location),
                               ("book.html", "Book a Table", main_book)]:
        with open(f"little-lemon/{folder}/{fn}", "w", encoding="utf-8") as f:
            f.write(page(title, fn, main_fn, sem, styled))
print("generated")
