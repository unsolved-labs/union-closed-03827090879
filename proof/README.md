# Frozen proof transcript

`part-01.md`, `part-02.md`, and `part-03.md` are the original public transport segments for the R010 proof and remain unchanged.

An integrity audit found that raw concatenation of these historical files omits one newline at the Part 1 → Part 2 boundary. To reproduce the `PROOF.md` actually frozen in the verifier payload, use exactly:

```text
part-01.md + "\n" + part-02.md + part-03.md
```

`scripts/check_release_integrity.py` verifies both the raw-segment hash and byte-for-byte equality of this reconstructed transcript with the payload proof.

These archival files still contain legacy `\(...\)` / `\[...\]` TeX delimiters. For the canonical typeset public proof, use:

- [`../manuscript/r010_union_closed_bound.tex`](../manuscript/r010_union_closed_bound.tex)
- [`../manuscript/README.md`](../manuscript/README.md) for the one-command PDF build

Do not rewrite the historical segments solely for Markdown rendering; the explicit reconstruction rule preserves and audits their relationship to the frozen payload.
