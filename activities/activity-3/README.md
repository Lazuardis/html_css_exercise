# Activity 3 — Put your site on the internet before you leave the room

12 minutes · everyone · slide act3 · Part 6, not examinable
There is no solution file for a deployment. The register is the list of addresses posted
in the class channel.

## Before you start
- Your site folder from Activity 2: `index.html`, the other pages, `style.css`, the images.
- **Lowercase every file name.** Check the images from your phone — `Falafel.JPEG` is the classic.
- Signed in to github.com. Know your username exactly as GitHub shows it.

## Do — 8 minutes: the five steps (slide s6-process)
1. **Sign in** to github.com with your own account.
2. **New repository.** Name it `username.github.io` — lowercase, your username, nothing else.
   Public. Create repository.
3. **Upload the folder.** Add file → Upload files. Drag in the *files* — `index.html`, the other
   pages, `style.css`, the images — not the folder that holds them. Commit changes.
4. **Check Pages.** Settings → Pages. Source: Deploy from a branch · `main` · `/ (root)`.
   Save if it is not already set. Copy the address it shows.
5. **Wait, then visit.** Open `https://username.github.io` — on your phone, on mobile data,
   not the campus wifi.

## The rule: wait the full ten minutes
Publishing takes one to ten minutes after each upload. Watch the **Actions** tab for the
green tick, then refresh. **Do not re-upload** — that restarts the clock.

## Check — 4 minutes
1. Are all pages reachable from the nav, with style and images on each?
2. Press **Book a table.** What happens, and why? (An error page from GitHub: Pages is static
   hosting — it serves files and runs no code, so nothing can receive the form. The server is Week 8.)
3. Post your address in the class channel. One line: the URL, then which of the four
   pitfalls you hit, or "none".
4. Open a classmate's link. Does it load faster or slower than yours? Guess why.

## Stuck? The four pitfalls (slide s6-pitfalls)
| Symptom | Likely cause |
|---|---|
| Nothing at the address yet | **Not up yet.** Wait the ten minutes; look for the green tick on Actions. |
| Nothing ever appears | **Wrong repository name.** It must be exactly `username.github.io`, lowercase, public. |
| 404 on the front page | **No `index.html` at the top level.** Uploaded inside a folder, or `Index.html`, or `index.html.txt`. |
| Page loads, no style or images | `style.css` or an image missing, a **case** mismatch with the link, or an href that is a **path on your laptop** (`file:///C:/…`). Relative paths only, same folder, lowercase. |

Still blank: pair up with someone who is live and compare repositories, file by file.
Before asking for help: F12 → Console and Network. A 404 names the missing file.

## If the campus network blocks the upload
Tether to a phone. (Test the network the morning of class.)
