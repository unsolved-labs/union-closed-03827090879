#!/usr/bin/env python3
import base64
import hashlib
import sys
import tarfile
from pathlib import Path

EXPECTED = "3bb6d879f7bf55083678c3a0cdce0e33bc980f32bde1bb76e300f89bca2fc098"
root = Path(__file__).resolve().parent
parts = sorted((root / "payload").glob("part-*.b64"))
if [p.name for p in parts] != [f"part-{i:02d}.b64" for i in range(1, 7)]:
    raise SystemExit("FAIL: expected payload/part-01.b64 through part-06.b64")
encoded = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
try:
    data = base64.b64decode(encoded, validate=True)
except Exception as exc:
    raise SystemExit(f"FAIL: invalid base64 payload: {exc}")
got = hashlib.sha256(data).hexdigest()
if got != EXPECTED:
    raise SystemExit(f"FAIL: payload SHA-256 mismatch: {got} != {EXPECTED}")
out = Path(sys.argv[1] if len(sys.argv) > 1 else ".release-work").resolve()
out.mkdir(parents=True, exist_ok=True)
archive = out / "release_bundle.tgz"
archive.write_bytes(data)
with tarfile.open(archive, "r:gz") as tf:
    for member in tf.getmembers():
        p = Path(member.name)
        if p.is_absolute() or ".." in p.parts:
            raise SystemExit(f"FAIL: unsafe archive path: {member.name}")
        if member.issym() or member.islnk():
            raise SystemExit(f"FAIL: archive links are not permitted: {member.name}")
    try:
        tf.extractall(out, filter="data")
    except TypeError:
        tf.extractall(out)
print("R010 PAYLOAD MATERIALIZED")
print(got)
