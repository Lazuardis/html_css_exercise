"""Render a folder's pages to PNG at 1100px wide, for comparison with the deck checkpoints.
Usage: python3 tools/screenshot.py stages/stage-6-styled out/   (needs playwright + chromium)"""
import sys, os
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1100, "height": 800})
    for fn in sorted(f for f in os.listdir(src) if f.endswith(".html")):
        pg.goto("file://" + os.path.abspath(os.path.join(src, fn))); pg.wait_for_timeout(200)
        pg.screenshot(path=os.path.join(out, fn[:-5] + ".png"), full_page=True)
    b.close()
