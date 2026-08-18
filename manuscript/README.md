# R010 manuscript

Public paper artifacts:

- [`r010_union_closed_bound.pdf`](r010_union_closed_bound.pdf) — committed rendered paper.
- [`r010_union_closed_bound.tex`](r010_union_closed_bound.tex) — canonical typeset source.

Build from a clean checkout with:

```bash
make -C manuscript
```

The build is deterministic under the pinned `SOURCE_DATE_EPOCH` in the Makefile. CI requires the fresh build to be byte-identical to the committed PDF and to have SHA-256

```text
2731b1b278c4edb8f8f72e229e96a14cb9f2753f0c6d842a3dd27c75601fe546
```

CI also extracts the rendered text and checks the exact release constant and the pending independent-review disclosure.

The files under `../proof/part-*.md` are retained as the historical public proof transport segments. Their original split omitted one newline at the Part 1 → Part 2 boundary; `../scripts/check_release_integrity.py` applies the documented separator rule and requires the reconstructed transcript to be byte-identical to the proof frozen in the verifier payload.

The research statement and verification boundary must stay synchronized with `../CLAIM.md`, `../STATEMENT_AUDIT.md`, `../VERIFICATION.md`, and `../verification-report.json`.
