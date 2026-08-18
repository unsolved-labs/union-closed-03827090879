# Proof artifacts

The canonical public typeset proof is the manuscript source:

- [LaTeX source](manuscript/r010_union_closed_bound.tex)
- [Build instructions](manuscript/README.md)

Run `make -C manuscript` to generate the PDF locally. CI rebuilds the same source.

## Frozen transcript

The original release proof is retained as three consecutive byte-frozen Markdown segments:

1. [Part 1](proof/part-01.md)
2. [Part 2](proof/part-02.md)
3. [Part 3](proof/part-03.md)

Concatenating those three files byte-for-byte reproduces the proof text frozen inside the original verifier payload. Its SHA-256 remains:

```text
27bccc453fd94d50cdb25e788fe23df8f1472d6e8a368b91f33cf0a0e4d8277c
```

Those archival files intentionally retain their original bytes, including legacy TeX delimiters, because changing them alone would break the recorded proof/payload identity. For canonical typesetting, use the manuscript source above.

`scripts/check_release_integrity.py` verifies this frozen transcript hash directly from the public repository files.
