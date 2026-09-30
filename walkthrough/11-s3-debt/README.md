# 11 · s3-debt — "Table borders done properly; the form that can say no"

**Deck:** Part 3 · **Indicator:** 4 (form half: Week 3 promise, Week 8 caveat) · **Time:** 4 min
**start/** = `/stages/stage-6-block-3/` · **end/** = no stage of its own: the HTML equals
`/stages/stage-6-block-4/` (line 1 aside); `style.css` is block 3 plus the block-4 header and
the three table rules. Walkthrough 12 completes block 4.

## Before you start — the seed differs from the deck notes
The notes say "paste the Week 3 style-tag rule into style.css, delete the style tag from
index.html". In the seed the `<style>` was already deleted at stage 5a (walkthrough 02), and
the table has had no borders since. So the rule is *typed back*, not moved.

## Typed live — style.css, after block 3
1. Block header: `/* ===== 4. Box model (§4) ===== */`
2. `table, th, td {` / `border: 1px solid #5F7171;` / `}` — Ctrl+S. The borders return, **doubled**:
   the table and every cell draw their own line.
3. Inside that rule, add `border-collapse: collapse;` — Ctrl+S. **Single** lines.
4. `th, td {` / `padding: 8px 16px;` / `}` then `th {` / `background-color: #E8EFEF;` / `}`. Ctrl+S.

## Typed live — book.html
5. Name input: add ` required` before `>`. Email input: the same.
6. Party input: add ` min="1" max="12" required` before `>`. Ctrl+S.
7. Press **Book a table** with everything empty: the browser refuses and writes its own message.
   Then type 0 in Party size: refused again.

## Room sees
Double lines becoming single on one save; then an empty submit refused, with no code of ours.

## The caveat (say it)
This runs in the customer's browser and can be switched off. The server checks again in
Week 8 — the Week 1 layer argument.

## Fault to expect
A complete, valid submit goes to `/book` and gets an error page — there is no server.
Say "Week 8" and stop.
