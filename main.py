#!/usr/bin/env python3
"""news-image-20261120: deliver the bundled front page as entry.png.

The picture is the entry, so this program does one small job: copy the
PNG stored next to it into the directory the grader provides. It runs
with no network and no third-party packages. Copying the same stored
bytes on every run keeps the output deterministic, so the grader's two
runs agree.
"""

import os
import shutil
from pathlib import Path

ENTRY_NAME = "entry.png"


def output_dir() -> Path:
    """Where the grader wants the image (or /output by default)."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def deliver() -> Path:
    """Copy the bundled front page to the output directory."""
    here = Path(__file__).resolve().parent
    source = here / ENTRY_NAME
    if not source.is_file():
        raise SystemExit(f"bundled image not found: {source}")
    target = output_dir() / ENTRY_NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit(f"copy incomplete: {target}")
    return target


if __name__ == "__main__":
    deliver()
