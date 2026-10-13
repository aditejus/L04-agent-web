"""Only if Google's built-in page reader stops working on the free tier (it is a Preview feature).

A page reader of our own, with Python's standard library only. It is cruder than the built-in one:
it strips the page down to plain text and keeps the first 3,000 characters.

Test it alone, free, with no request to the model:   python read_page_fallback.py
To use it in agent.py, follow "If the built-in reader stops working" in README.md.
"""
import gzip
import html
import re
import urllib.request


def read_page(address):
    request = urllib.request.Request(address, headers={"User-Agent": "first-agent-tutorial/1.0"})
    raw = urllib.request.urlopen(request, timeout=30).read()
    if raw[:2] == b"\x1f\x8b":                     # some sites send the page compressed
        raw = gzip.decompress(raw)
    text = raw.decode("utf-8", "replace")
    text = re.sub(r"(?is)<(script|style|nav|header|footer).*?</\1>", " ", text)   # drop code and menus
    text = re.sub(r"<[^>]+>", " ", text)                                          # drop the tags
    return re.sub(r"\s+", " ", html.unescape(text)).strip()[:3000]


if __name__ == "__main__":
    print(read_page("https://www.python.org/downloads/")[:400])
