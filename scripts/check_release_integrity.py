#!/usr/bin/env python3
from __future__ import annotations

import base64
import difflib
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PAYLOAD_SHA256 = "3bb6d879f7bf55083678c3a0cdce0e33bc980f32bde1bb76e300f89bca2fc098"
EXPECTED_C = (3827090879, 10_000_000_000)


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


report = json.loads((ROOT / "verification-report.json").read_text(encoding="utf-8"))
claim = report["claim"]
if (claim["constant_numerator"], claim["constant_denominator"]) != EXPECTED_C:
    fail("verification-report claim constant drift")
if claim["constant_decimal"] != "0.3827090879":
    fail("verification-report decimal drift")
if report.get("external_specialist_review") != "pending":
    fail("external review status changed without an explicit audited update")

required = [
    "README.md", "CLAIM.md", "PROOF.md", "STATEMENT_AUDIT.md",
    "VERIFICATION.md", "SOURCE_AUDIT.md",
    "manuscript/r010_union_closed_bound.tex", "manuscript/Makefile",
    "manuscript/README.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        fail(f"missing public release artifact: {rel}")

# Reconstruct the frozen release archive and inspect the proof actually shipped
# inside it. This turns an old prose assertion about proof identity into an
# executable audit.
parts = sorted((ROOT / "payload").glob("part-*.b64"))
if [p.name for p in parts] != [f"part-{i:02d}.b64" for i in range(1, 7)]:
    fail("unexpected payload segment set")
encoded = "".join(p.read_text(encoding="utf-8").strip() for p in parts)
try:
    archive_bytes = base64.b64decode(encoded, validate=True)
except Exception as exc:
    fail(f"invalid base64 payload: {exc}")
payload_sha = hashlib.sha256(archive_bytes).hexdigest()
if payload_sha != EXPECTED_PAYLOAD_SHA256:
    fail(f"payload SHA-256 mismatch: {payload_sha}")

with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:gz") as tf:
    proof_members = [m for m in tf.getmembers() if m.isfile() and Path(m.name).name == "PROOF.md"]
    if len(proof_members) != 1:
        fail(f"expected exactly one payload PROOF.md, found {len(proof_members)}")
    fh = tf.extractfile(proof_members[0])
    if fh is None:
        fail("could not read payload PROOF.md")
    payload_proof = fh.read()

public_proof = b"".join((ROOT / "proof" / f"part-{i:02d}.md").read_bytes() for i in range(1, 4))
public_sha = hashlib.sha256(public_proof).hexdigest()
payload_proof_sha = hashlib.sha256(payload_proof).hexdigest()

if public_proof != payload_proof:
    public_text = public_proof.decode("utf-8", errors="replace").splitlines()
    payload_text = payload_proof.decode("utf-8", errors="replace").splitlines()
    diff = list(difflib.unified_diff(public_text, payload_text, fromfile="public-proof-segments", tofile="payload-PROOF.md", n=2))
    print(f"PUBLIC_PROOF_SHA256={public_sha}")
    print(f"PAYLOAD_PROOF_SHA256={payload_proof_sha}")
    print(f"PUBLIC_PROOF_BYTES={len(public_proof)}")
    print(f"PAYLOAD_PROOF_BYTES={len(payload_proof)}")
    print("FIRST_PROOF_DIFF_LINES:")
    for line in diff[:80]:
        print(line)
    fail("public proof segments are not byte-identical to payload PROOF.md; reconcile or document deliberately")

primary_markdown = [
    "README.md", "CLAIM.md", "PROOF.md", "STATEMENT_AUDIT.md",
    "VERIFICATION.md", "SOURCE_AUDIT.md", "EXTERNAL_REVIEW_CHECKLIST.md",
    "manuscript/README.md",
]
legacy = re.compile(r"\\\(|\\\)|\\\[|\\\]")
for rel in primary_markdown:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if legacy.search(text):
        fail(f"legacy TeX delimiter in primary public Markdown: {rel}")

private_path_patterns = [
    re.compile(r"/home/[A-Za-z0-9_.-]+/"),
    re.compile(r"/Users/[A-Za-z0-9_.-]+/"),
    re.compile(r"[A-Za-z]:\\\\Users\\\\"),
]
for rel in primary_markdown + ["manuscript/r010_union_closed_bound.tex"]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    for pat in private_path_patterns:
        if pat.search(text):
            fail(f"local/private filesystem path found in {rel}")

for rel in ["README.md", "CLAIM.md", "STATEMENT_AUDIT.md", "manuscript/r010_union_closed_bound.tex"]:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if "3827090879" not in text or "10000000000" not in text:
        fail(f"exact theorem constant missing from {rel}")

print("R010 PUBLIC RELEASE INTEGRITY PASSED")
print(f"public_proof_sha256={public_sha}")
print(f"payload_proof_sha256={payload_proof_sha}")
print(f"payload_sha256={payload_sha}")
