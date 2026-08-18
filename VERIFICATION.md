# Verification and reproducibility — R010

## Proof architecture

R010 proves the exact rational lower bound

$$
c=\frac{3827090879}{10000000000}=0.3827090879
$$

in the sense stated in `CLAIM.md`. The proof is hybrid:

1. an analytic entropy/protocol reduction;
2. an analytic kernel inequality with one exact rational polynomial-positivity check;
3. analytic boundary estimates for the main two-variable inequality;
4. a rigorous interval certificate on the remaining compact rectangle.

## One-command clean-checkout replay

On Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install -y g++ python3 libboost-all-dev libmpfr-dev libgmp-dev
./verify_release.sh
```

A successful replay ends with markers including:

```text
ALL EXACT AUXILIARY CHECKS PASSED
ALL CHECKS PASSED
MPFR ALL CHECKS PASSED
STATIC MPFR CERTIFICATE PASSED
R010 PUBLIC RELEASE INTEGRITY PASSED
R010 RELEASE VERIFICATION PASSED
```

## Payload integrity

`materialize_release.py` concatenates `payload/part-01.b64` through `part-06.b64`, decodes the archive, and verifies the frozen archive SHA-256

```text
3bb6d879f7bf55083678c3a0cdce0e33bc980f32bde1bb76e300f89bca2fc098
```

before extraction. It rejects missing/unexpected payload segments, invalid base64, hash mismatch, path traversal, absolute paths, symlinks, and hard links.

## Numerical verification paths

### Directed-rounding Boost.Interval

Materialized source: `union_closed_sharp_verifier.cpp`.

```bash
g++ -std=c++20 -O2 -frounding-math -fno-fast-math -ffp-contract=off \
  union_closed_sharp_verifier.cpp -o sharp
./sharp
```

Reference core result:

```text
core: boxes=3273, splits=3272, max_depth=39
ALL CHECKS PASSED
```

This path uses directed binary64 rounding and an internally bounded logarithm series.

### Independent MPFR-256

Materialized source: `mpfr_independent_verifier.cpp`.

```bash
g++ -std=c++20 -O2 mpfr_independent_verifier.cpp -lmpfr -lgmp -o mpfr
./mpfr
```

Reference core result:

```text
MPFR core: boxes=3210, splits=3209, max_depth=39
MPFR ALL CHECKS PASSED
```

This checker is separately written, uses MPFR transcendental functions and outward rounding, and generates its own adaptive subdivision.

### Static MPFR partition replay

Materialized source: `mpfr_static_replay.cpp`.

```bash
python3 materialize_static_certificate.py
g++ -std=c++20 -O2 mpfr_static_replay.cpp -lmpfr -lgmp -o static-replay
./static-replay r_leaf_paths.txt core_leaf_paths.txt
```

Reference result:

```text
static R: leaves=39, max_depth=14
static core: leaves=3210, max_depth=39
STATIC MPFR CERTIFICATE PASSED
```

Before evaluating inequalities, the checker verifies that the prefix-coded leaves form a complete partition and rejects duplicates, prefix collisions, missing siblings, mixed-axis branches, and incomplete trees.

### Exact rational auxiliary check

`verify_auxiliary_inequality.py` recomputes with exact `fractions.Fraction` arithmetic the polynomial identity used in the kernel proof, the comparison `j(84/125)-1/2>0`, and all sixteen positive Bernstein coefficients.

## Trust boundary

Included in the final correctness oracle are the public analytic proof, the exact rational auxiliary computation, the documented directed-rounding semantics, GMP/MPFR outward rounding, the frozen certificate and coverage checks, and the SHA-256 integrity of the verifier payload.

Explicitly outside the final correctness oracle are the frontier-AI generation process, private conversations/prompts, heuristic search or optimization used during discovery, sampled floating-point experiments not replayed rigorously, and unpublished external review.

## Proof-assistant status

No Lean theorem is currently part of the R010 proof object. The highest-value future formalization targets are the protocol-to-entropy deduction, the implication from the two pointwise inequalities to the exact union-closed bound, the analytic kernel argument, and the elementary boundary reductions. The large interval partition is already represented more directly as a frozen certificate checked by independent rigorous programs.

## Manuscript build and rendered artifact

Canonical paper source:

```text
manuscript/r010_union_closed_bound.tex
```

Committed rendered paper:

```text
manuscript/r010_union_closed_bound.pdf
```

Build it with:

```bash
make -C manuscript
```

The expected PDF SHA-256 is:

```text
2731b1b278c4edb8f8f72e229e96a14cb9f2753f0c6d842a3dd27c75601fe546
```

CI checks the committed digest, rebuilds the manuscript with the pinned `SOURCE_DATE_EPOCH`, requires the rebuild to be byte-identical to the committed PDF, extracts its text, and verifies the exact theorem constant and pending-review disclosure. The LaTeX source remains the canonical typeset statement source; the PDF is its reproducible rendered artifact.

## Repository-level integrity

```bash
python3 scripts/check_release_integrity.py
```

This verifies exact-constant consistency, pending review status, required public artifacts, the committed manuscript PDF digest, the historical proof/payload reconstruction hashes, GitHub-safe math delimiters in primary Markdown, and absence of common local/private filesystem paths.
