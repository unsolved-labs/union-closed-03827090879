# Proof artifacts

The canonical public typeset proof is the manuscript source:

- [LaTeX source](manuscript/r010_union_closed_bound.tex)
- [Build instructions](manuscript/README.md)

Run `make -C manuscript` to generate the PDF locally. CI rebuilds the same source.

## Frozen transcript and payload identity

The original public proof transcript is stored in three transport segments:

1. [Part 1](proof/part-01.md)
2. [Part 2](proof/part-02.md)
3. [Part 3](proof/part-03.md)

An integrity audit found a one-byte transport-boundary discrepancy in the original repository: raw concatenation of the three unchanged segment files omits one newline between Part 1 and Part 2.

The raw segment concatenation has SHA-256:

```text
e01a06007344591ddaee74854e19581ad3ca3e53a483d054bff1cf896be5871e
```

The proof actually frozen inside the verifier payload is reconstructed exactly as:

```text
part-01.md + "\n" + part-02.md + part-03.md
```

and has SHA-256:

```text
27bccc453fd94d50cdb25e788fe23df8f1472d6e8a368b91f33cf0a0e4d8277c
```

`scripts/check_release_integrity.py` reconstructs the payload archive, extracts its `PROOF.md`, applies this explicit one-byte separator rule to the public segments, and requires byte-for-byte equality. Thus the transport discrepancy is documented and mechanically checked rather than hidden by rewriting the historical segment files.

The archival segments intentionally retain their original bytes and legacy TeX delimiters. For canonical typesetting, use the manuscript source above.
