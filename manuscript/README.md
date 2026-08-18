# R010 manuscript

The public paper source is [`r010_union_closed_bound.tex`](r010_union_closed_bound.tex).

Build it from a clean checkout with:

```bash
make -C manuscript
```

CI rebuilds the PDF and checks that the rendered text contains the exact release constant and the correct pending-review status. The generated PDF is a build product; the LaTeX source is the canonical typeset source in version control.

The files under `../proof/part-*.md` are retained as the original byte-frozen proof transcript because their concatenation is integrity-linked to the verifier payload. They intentionally are not rewritten solely for Markdown rendering.

The research statement and verification boundary must stay synchronized with `../CLAIM.md`, `../STATEMENT_AUDIT.md`, `../VERIFICATION.md`, and `../verification-report.json`.
