#!/usr/bin/env python3
from __future__ import annotations

import base64
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PAYLOAD_SHA256 = "3bb6d879f7bf55083678c3a0cdce0e33bc980f32bde1bb76e300f89bca2fc098"
EXPECTED_RAW_SEGMENTS_SHA256 = "e01a06007344591ddaee74854e19581ad3ca3e53a483d054bff1cf896be5871e"
EXPECTED_PAYLOAD_PROOF_SHA256 = "27bccc453fd94d50cdb25e788fe23df8f1472d6e8a368b91f33cf0a0e4d8277c"
EXPECTED_MANUSCRIPT_PDF_SHA256 = "2731b1b278c4edb8f8f72e229e96a14cb9f2753f0c6d842a3dd27c75601fe546"
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
    "manuscript/r010_union_closed_bound.tex",
    "manuscript/r010_union_closed_bound.pdf",
    "manuscript/Makefile", "manuscript/README.md", "proof/README.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        fail(f"missing public release artifact: {rel}")

pdf_sha = hashlib.sha256((ROOT / "manuscript/r010_union_closed_bound.pdf").read_bytes()).hexdigest()
if pdf_sha != EXPECTED_MANUSCRIPT_PDF_SHA256:
    fail(f"committed manuscript PDF SHA-256 mismatch: {pdf_sha}")

# Reconstruct the frozen archive and inspect the proof actually shipped inside.
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

# Historical transport split: raw file concatenation is missing one newline at
# the part-01 -> part-02 boundary. Preserve the original public segment bytes,
# but encode the separator explicitly when reconstructing the payload proof.
p1 = (ROOT / "proof/part-01.md").read_bytes()
p2 = (ROOT / "proof/part-02.md").read_bytes()
p3 = (ROOT / "proof/part-03.md").read_bytes()
raw_segments = p1 + p2 + p3
raw_sha = hashlib.sha256(raw_segments).hexdigest()
if raw_sha != EXPECTED_RAW_SEGMENTS_SHA256:
    fail(f"raw public proof-segment hash drift: {raw_sha}")
reconstructed_proof = p1 + b"\n" + p2 + p3
reconstructed_sha = hashlib.sha256(reconstructed_proof).hexdigest()
payload_proof_sha = hashlib.sha256(payload_proof).hexdigest()
if reconstructed_sha != EXPECTED_PAYLOAD_PROOF_SHA256:
    fail(f"reconstructed proof SHA-256 mismatch: {reconstructed_sha}")
if payload_proof_sha != EXPECTED_PAYLOAD_PROOF_SHA256:
    fail(f"payload proof SHA-256 mismatch: {payload_proof_sha}")
if reconstructed_proof != payload_proof:
    fail("reconstructed public transcript is not byte-identical to payload PROOF.md")

primary_markdown = [
    "README.md", "CLAIM.md", "PROOF.md", "STATEMENT_AUDIT.md",
    "VERIFICATION.md", "SOURCE_AUDIT.md", "EXTERNAL_REVIEW_CHECKLIST.md",
    "manuscript/README.md", "proof/README.md",
]
legacy = re.compile(r"\\\(|\\\)|\\\[|\\\]")
for rel in primary_markdown:
    text = (ROOT / rel).read_text(encoding="utf-8")
    # proof/README.md necessarily documents the literal legacy delimiters.
    if rel != "proof/README.md" and legacy.search(text):
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
print(f"manuscript_pdf_sha256={pdf_sha}")
print(f"raw_segment_sha256={raw_sha}")
print(f"reconstructed_payload_proof_sha256={reconstructed_sha}")
print(f"payload_sha256={payload_sha}")
