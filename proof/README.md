# Frozen proof transcript

`part-01.md`, `part-02.md`, and `part-03.md` are the original byte-frozen proof transcript for R010.

Their concatenation is SHA-256 linked to the verifier payload and is therefore retained byte-for-byte. In particular, these archival files still contain legacy `\(...\)` / `\[...\]` TeX delimiters.

For the canonical typeset public proof, use:

- [`../manuscript/r010_union_closed_bound.tex`](../manuscript/r010_union_closed_bound.tex)
- [`../manuscript/README.md`](../manuscript/README.md) for the one-command PDF build

Do not edit the frozen parts without deliberately regenerating the payload, proof hash, and every integrity record that depends on them.
