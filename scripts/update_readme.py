#!/usr/bin/env python3
"""Update the README with the current timestamp."""

from __future__ import annotations

import datetime as _dt
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

START_MARKER = "<!--START_SECTION:last_updated-->"
END_MARKER = "<!--END_SECTION:last_updated-->"


def main() -> None:
    content = README.read_text(encoding="utf-8")
    pattern = re.compile(rf"{START_MARKER}.*?{END_MARKER}", re.DOTALL)
    timestamp = _dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    replacement = f"{START_MARKER}\n上次更新时间：{timestamp}\n{END_MARKER}"
    new_content = pattern.sub(replacement, content)
    README.write_text(new_content, encoding="utf-8")


if __name__ == "__main__":
    main()
