#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PROOF_SHA256 = "27bccc453fd94d50cdb25e788fe23df8f1472d6e8a368b91f33cf0a0e4d8277c"
EXPECTED_C = (3827090879, 10_000_000_000)


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


report_path = ROOT / "verification-report.json"
report = json.loads(report_path.read_text(encoding="utf-8"))
claim = report["claim"]
if (claim["constant_numerator"], claim["constant_denominator"]) != EXPECTED_C:
    fail("verification-report claim constant drift")
if claim["constant_decimal"] != "0.3827090879":
    fail("verification-report decimal drift")
if report.get("external_specialist_review") != "pending":
    fail("external review status changed without an explicit audited update")

required = [
    "README.md",
    "CLAIM.md",
    "PROOF.md",
    "STATEMENT_AUDIT.md",
    "VERIFICATION.md",
    "SOURCE_AUDIT.md",
    "manuscript/r010_union_closed_bound.tex",
    "manuscript/r010_union_closed_bound.pdf",
    "manuscript/README.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        fail(f"missing public release artifact: {rel}")

# Keep the original proof transcript byte-identical to the artifact frozen in the
# verifier bundle. Public rendered mathematics lives in manuscript/.
proof = b"".join((ROOT / "proof" / f"part-{i:02d}.md").read_bytes() for i in range(1, 4))
got = hashlib.sha256(proof).hexdigest()
if got != EXPECTED_PROOF_SHA256:
    fail(f"frozen proof transcript hash mismatch: {got}")

# GitHub-facing primary docs should use GitHub-supported $ / $$ math instead of
# legacy \( \) / \[ \] delimiters. The byte-frozen proof transcript is excluded
# deliberately and documented in proof/README.md.
primary_markdown = [
    "README.md",
    "CLAIM.md",
    "PROOF.md",
    "STATEMENT_AUDIT.md",
    "VERIFICATION.md",
    "SOURCE_AUDIT.md",
    "EXTERNAL_REVIEW_CHECKLIST.md",
    "manuscript/README.md",
]
legacy = re.compile(r"\\\(|\\\)|\\\[|\\\]")
for rel in primary_markdown:
    text = (ROOT / rel).read_text(encoding="utf-8")
    if legacy.search(text):
        fail(f"legacy TeX delimiter in public Markdown: {rel}")

# Guard against accidental publication of common local/private path forms.
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

print("R010 PUBLIC RELEASE INTEGRITY PASSED")
print(f"proof_sha256={got}")
