# 19 · s6-pitfalls — "Four faults cause almost every blank site"

**Deck:** Part 6 · **Indicator:** Part 6, not RPS, not examinable · **Time:** 2 min
**Folder:** README + `start/` + `variants/` — no file edit. `start/` = `/deploy/`.
Everything in `variants/` except the support copies is **broken on purpose**. Never upload it
to your `username.github.io` repository.

## variants/
| File | Card on the slide | Locally | Deployed |
|---|---|---|---|
| `fault-Location.html` + `fault-case-link.html` | 4 — case | Click Location: it opens (Windows ignores case) | 404 — the link says `fault-location.html` |
| `fault-href-absolute.html` | 4 — path on your laptop | No style here: `file:///C:/Users/student/…` does not exist on this machine | No style anywhere |
| `fault-index-in-folder/` | 3 — 404 on the front page | Opens fine from inside `little-lemon/` | Upload it as-is: no top-level `index.html`, 404 |

`style.css`, `falafel.jpeg`, `salad.jpeg` are support copies so the fault pages render.

## Open when the slide appears
Keep the slide up through Activity 3. Open `variants/fault-case-link.html` and click
Location; open `variants/fault-href-absolute.html` and point at the missing style.

## Optional, before class
To show the 404s live, upload `variants/` to a scratch repository (not `username.github.io`)
and turn Pages on. It publishes as a project site at `https://username.github.io/<repo>/`.

## Typed live
Nothing.

## What to say
Cards 1 and 2 (not up yet; wrong repository name) have no file — they are in the
repository, not the folder. The professional habit: F12 → Console and Network; a 404 names
the missing file. That is Week 6, used early.

## Fault to expect
A phone photo named `Falafel.JPEG`: the capitals do not match the `src`. Lowercase everything.
