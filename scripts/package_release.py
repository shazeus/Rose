#!/usr/bin/env python3
"""Create Rose-style Windows release assets for Aurelia."""

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _zip_directory(source: Path, target: Path, root_name: str) -> None:
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_dir():
                continue
            relative = path.relative_to(source)
            archive.write(path, Path(root_name) / relative)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/package_release.py <version>")
        return 2

    version = sys.argv[1].strip().lstrip("v")
    if not version:
        print("Version is required")
        return 2

    dist_dir = ROOT / "dist" / "Aurelia"
    installer_dir = ROOT / "installer"
    release_dir = ROOT / "release"

    if not dist_dir.exists():
        print(f"Missing build output: {dist_dir}")
        return 1

    installers = sorted(installer_dir.glob("Aurelia_Setup*.exe"))
    if not installers:
        print(f"Missing installer output in {installer_dir}")
        return 1

    release_dir.mkdir(exist_ok=True)
    for old in release_dir.iterdir():
        if old.is_file():
            old.unlink()

    setup_target = release_dir / f"Aurelia_Setup_{version}.exe"
    update_target = release_dir / f"update_package_{version}.zip"

    shutil.copy2(installers[-1], setup_target)
    _zip_directory(dist_dir, update_target, "Aurelia")

    print(f"Created {setup_target}")
    print(f"Created {update_target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
