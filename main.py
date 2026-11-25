#!/usr/bin/env python3
"""One Line, One Laugh (u-coral-404-one-line-one-laugh-22f2c9f3).

Writes a single original funny line of at most 200 characters to
/output/entry.txt. Stdlib only; no network, no secrets, no input files.
"""

import os

LINE = "My password manager forgot my password. Now we stare at each other like strangers at a reunion."

MAX_CHARS = 200


def verify(path: str) -> dict:
    """Gate check: UTF-8, 1-200 characters, not only whitespace, and
    byte-identical to the chosen line. Returns a report dict."""
    raw = open(path, "rb").read()
    text = raw.decode("utf-8")
    return {
        "path": path,
        "chars": len(text),
        "bytes": len(raw),
        "non_whitespace": bool(text.strip()),
        "within_gate": 1 <= len(text) <= MAX_CHARS,
        "byte_identical": raw == LINE.encode("utf-8"),
    }


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    report = verify(path)
    print(f"chars={report['chars']} bytes={report['bytes']} "
          f"non_whitespace={report['non_whitespace']} "
          f"within_gate={report['within_gate']} "
          f"byte_identical={report['byte_identical']}")
    assert report["within_gate"], "gate failed: length outside 1-200"
    assert report["non_whitespace"], "gate failed: only whitespace"
    assert report["byte_identical"], "read-back differs from chosen line"
    print("OK: entry.txt passes the gate and matches the chosen line.")


if __name__ == "__main__":
    main()
