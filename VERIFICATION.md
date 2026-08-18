# Verification and reproducibility — R010

## What the release proves

The release proves the exact rational lower bound

$$
c=\frac{3827090879}{10000000000}=0.3827090879
$$

for the union-closed sets conjecture in the sense stated in `CLAIM.md`.

The proof is hybrid:

1. an analytic entropy/protocol reduction;
2. an analytic kernel inequality with one exact rational polynomial-positivity check;
3. analytic boundary estimates for the main two-variable inequality;
4. a rigorous interval certificate on the remaining compact rectangle.

## One-command clean-checkout replay

Ubuntu/Debian prerequisites:

```bash
sudo apt-get update
sudo apt-get install -y g++ python3 libboost-all-dev libmpfr-dev libgmp-dev
```

Run:

```bash
./verify_release.sh
```

Expected terminal markers include:

```text
ALL EXACT AUXILIARY CHECKS PASSED
ALL CHECKS PASSED
MPFR ALL CHECKS PASSED
STATIC MPFR CERTIFICATE PASSED
R010 PUBLIC RELEASE INTEGRITY PASSED
R010 RELEASE VERIFICATION PASSED
```

## Payload integrity

`materialize_release.py` concatenates `payload/part-01.b64` through `part-06.b64`, base64-decodes the archive, and verifies the frozen archive SHA-256

```text
3bb6d879f7bf55083678c3a0cdce0e33bc980f32bde1bb76e300f89bca2fc098
```

before extraction.

The materializer rejects:

- unexpected or missing payload segments;
- invalid base64;
- archive hash mismatch;
- absolute or parent-traversing archive paths;
- symlinks and hard links.

## Numerical trust paths

### A. Directed-rounding Boost.Interval

Materialized source: `union_closed_sharp_verifier.cpp`

```bash
g++ -std=c++20 -O2 \
  -frounding-math -fno-fast-math -ffp-contract=off \
  union_closed_sharp_verifier.cpp -o sharp
./sharp
```

Reference core result:

```text
core: boxes=3273, splits=3272, max_depth=39
ALL CHECKS PASSED
```

This path uses binary64 directed rounding and an internally bounded logarithm series rather than relying on the system logarithm.

### B. Independent MPFR-256

Materialized source: `mpfr_independent_verifier.cpp`

```bash
g++ -std=c++20 -O2 mpfr_independent_verifier.cpp -lmpfr -lgmp -o mpfr
./mpfr
```

Reference core result:

```text
MPFR core: boxes=3210, splits=3209, max_depth=39
MPFR ALL CHECKS PASSED
```

This implementation is intentionally separate from the Boost path and uses MPFR transcendental functions plus an independently generated adaptive subdivision.

### C. Static MPFR partition replay

Materialized source: `mpfr_static_replay.cpp`

The frozen adaptive partition is first materialized from `static_certificate.json`; the static checker then validates partition completeness before evaluating leaf inequalities.

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

The checker rejects incomplete, duplicate, prefix-colliding, or mixed-axis partitions.

### D. Exact rational auxiliary checker

Materialized source: `verify_auxiliary_inequality.py`

```bash
python3 verify_auxiliary_inequality.py
```

It recomputes using exact `fractions.Fraction` arithmetic:

- the polynomial identity used in the kernel proof;
- the exact comparison `j(84/125) - 1/2 > 0`;
- all sixteen positive tensor-product Bernstein coefficients.

## Trust boundary

### Included in the final correctness oracle

- the public analytic proof/manuscript;
- exact rational arithmetic in the auxiliary checker;
- directed-rounding semantics and strict compiler flags for the Boost path;
- GMP/MPFR outward rounding for the independent/static paths;
- the frozen certificate data and its partition-completeness checks;
- the SHA-256 integrity of the verifier payload.

### Explicitly outside the final correctness oracle

- the frontier-AI generation process;
- private conversations or prompts;
- heuristic search or numerical optimization used during discovery;
- any sampled floating-point experiment not replayed by the rigorous checkers;
- unpublished external review.

## Proof-assistant status

No Lean theorem is currently part of the R010 proof object.

A proof-assistant upgrade would most profitably target:

1. the protocol-to-entropy deduction;
2. the theorem that the two pointwise inequalities imply the exact union-closed constant;
3. the analytic kernel inequality up to an imported exact Bernstein certificate;
4. the elementary boundary-strip reductions.

Formalizing the entire adaptive interval search is not necessary for a strong trust boundary if the final frozen partition is independently replayed by small rigorous checkers.

## Manuscript build

```bash
make -C manuscript
```

The committed PDF is generated from `manuscript/r010_union_closed_bound.tex`.

## Repository-level integrity checks

```bash
python3 scripts/check_release_integrity.py
```

This verifies:

- exact public constant consistency;
- review status remains `pending`;
- manuscript source/PDF presence;
- proof transcript SHA-256;
- absence of accidental legacy TeX delimiters in the primary public Markdown files, excluding the explicitly byte-frozen proof transcript;
- absence of obvious local absolute paths in public text.
