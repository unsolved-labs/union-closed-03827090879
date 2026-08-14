# Complete proof

The complete proof of R010 is stored as three consecutive Markdown segments for repository transport and reviewability. Read them in order:

1. [Part 1](proof/part-01.md)
2. [Part 2](proof/part-02.md)
3. [Part 3](proof/part-03.md)

Concatenating the three segments byte-for-byte reproduces the proof file frozen inside the verifier bundle. Its SHA-256 is:

```text
27bccc453fd94d50cdb25e788fe23df8f1472d6e8a368b91f33cf0a0e4d8277c
```

The executable verification package is independently integrity-checked by `materialize_release.py` before every CI replay.
