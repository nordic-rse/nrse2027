#!/usr/bin/env python3
"""Install the scaffold's pinned Zola binary into this website directory."""

import hashlib
import io
import platform
import tarfile
import urllib.request
from pathlib import Path

VERSION = "0.21.0"
SHA256 = "a070b4d6e85dad9c8b821bcd985dd2f07e807f699c881971a73d986fb92f5f7d"


def main():
    if platform.system() != "Linux" or platform.machine() not in ("x86_64", "amd64"):
        raise SystemExit(
            "This helper supports Linux x86_64. Install Zola 0.21.0 from "
            "https://www.getzola.org/documentation/getting-started/installation/ "
            "and run zola serve --port 8877 from the website directory."
        )
    url = (
        f"https://github.com/getzola/zola/releases/download/v{VERSION}/"
        f"zola-v{VERSION}-x86_64-unknown-linux-gnu.tar.gz"
    )
    request = urllib.request.Request(url, headers={"User-Agent": "NRSE2027-local-preview"})
    with urllib.request.urlopen(request, timeout=60) as response:
        archive_bytes = response.read()
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:gz") as archive:
        member = next(
            item for item in archive.getmembers()
            if item.isfile() and Path(item.name).name == "zola"
        )
        with archive.extractfile(member) as source:
            binary = source.read()
    if hashlib.sha256(binary).hexdigest() != SHA256:
        raise SystemExit("The Zola binary does not match the upstream workflow checksum.")
    target = Path(__file__).resolve().parents[1] / ".tools" / "zola"
    target.parent.mkdir(exist_ok=True)
    temporary = target.with_suffix(".download")
    temporary.write_bytes(binary)
    temporary.chmod(0o755)
    temporary.replace(target)
    print(f"Installed Zola {VERSION} at {target}")


if __name__ == "__main__":
    main()
