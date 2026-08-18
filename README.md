# R010 — Union-closed sets: unconditional 0.3827090879 bound

**Unsolved Labs Research Release R010**

This repository contains a computer-assisted proof that every finite union-closed family other than $\{\varnothing\}$ has an element appearing in at least

$$
\frac{3827090879}{10000000000}=0.3827090879
$$

of its member sets.

## Result

For every finite union-closed family $\mathcal F\neq\{\varnothing\}$, there exists an element $x$ such that

$$
\bigl|\{A\in\mathcal F:x\in A\}\bigr|
\ge
\frac{3827090879}{10000000000}\,|\mathcal F|.
$$

The exact protocol weights are

$$
\alpha=\frac{11249343}{12500000},
\qquad
\beta=\frac{1250657}{12500000},
\qquad
\alpha+\beta=1.
$$

## Why this matters

The entropy method initiated by Gilmer produced the first constant lower bound for the union-closed sets conjecture. Subsequent dependent-coupling work of Sawin, Yu, and Cambie reached an unconditional frontier near $0.3823455$. Liu then introduced a conditionally-i.i.d. protocol and proved an analytic strict improvement; a nine-dimensional numerical optimization in that work suggested a value near $0.38271$ under explicitly numerically verified structural hypotheses.

R010 proves the exact rational constant $0.3827090879$ **without assuming those optimization/positive-semidefiniteness hypotheses**. The release replaces them with two pointwise entropy inequalities: one analytic (with an exact rational Bernstein check) and one rigorously certified by interval arithmetic.

See [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) for the pinned literature boundary.

## Manuscript

- [Typeset manuscript PDF](manuscript/r010_union_closed_bound.pdf)
- [LaTeX source](manuscript/r010_union_closed_bound.tex)
- [Manuscript build instructions](manuscript/README.md)

The files under `proof/part-*.md` are retained as the **byte-frozen proof transcript** linked to the original verifier payload. They intentionally preserve their original bytes; use the manuscript above for the canonical rendered proof.

## Verification

The mathematical reduction and the numerical certificate have separate trust boundaries.

The compact numerical inequality is checked three ways:

1. **Boost.Interval / binary64** — directed rounding, strict floating-point compiler flags, an internally bounded logarithm series, and adaptive subdivision.
2. **Independent MPFR-256** — a separately written implementation using MPFR transcendental functions, exact rational domain endpoints, and an independently generated subdivision.
3. **Static MPFR replay** — a non-adaptive checker that first validates that the frozen prefix-coded leaves form a complete partition, then checks every leaf with outward-rounded MPFR arithmetic.

The auxiliary polynomial/Bernstein inequality is independently reproduced using exact rational arithmetic.

Read [`VERIFICATION.md`](VERIFICATION.md) for the complete trust boundary and [`STATEMENT_AUDIT.md`](STATEMENT_AUDIT.md) for claim-to-proof-to-checker correspondence.

### Clean-checkout replay

Ubuntu/Debian prerequisites:

```bash
sudo apt-get update
sudo apt-get install -y g++ python3 libboost-all-dev libmpfr-dev libgmp-dev
```

Then run:

```bash
./verify_release.sh
```

A successful replay ends with:

```text
ALL EXACT AUXILIARY CHECKS PASSED
ALL CHECKS PASSED
MPFR ALL CHECKS PASSED
STATIC MPFR CERTIFICATE PASSED
R010 PUBLIC RELEASE INTEGRITY PASSED
R010 RELEASE VERIFICATION PASSED
```

The payload materializer checks the exact archive SHA-256 before extraction and rejects unsafe paths and archive links.

## Verification status

- Exact rational auxiliary certificate: **verified by CI**
- Directed-rounding Boost interval certificate: **verified by CI**
- Independent MPFR-256 certificate: **verified by CI**
- Frozen static MPFR partition replay: **verified by CI**
- Analytic proof in a proof assistant: **not currently part of the trust boundary**
- Independent specialist review: **pending**

The result should therefore be described as a **reproducible computer-assisted proof with multiple independent numerical verification paths**, not as a fully proof-assistant-formalized theorem.

## Repository map

- `CLAIM.md` — frozen theorem, exact constants, non-claims, and trust boundary.
- `manuscript/` — public paper source, PDF, and build instructions.
- `STATEMENT_AUDIT.md` — public claim → manuscript → certificate/checker mapping.
- `VERIFICATION.md` — exact reproduction commands and trust assumptions.
- `SOURCE_AUDIT.md` — pinned prior-work and novelty boundary.
- `PROOF.md` / `proof/part-*.md` — original byte-frozen proof transcript.
- `verification-report.json` — machine-readable frozen claim and reference margins.
- `EXTERNAL_REVIEW_CHECKLIST.md` — modular public checklist for independent review.
- `payload/part-*.b64` — deterministic verifier/certificate package.
- `materialize_release.py` — checksum-verifying safe materializer.
- `verify_release.sh` — one-command verifier entry point.
- `scripts/check_release_integrity.py` — public metadata/manuscript/proof-integrity checks.
- `.github/workflows/verify.yml` — CI for all verification paths and manuscript/release integrity.

## Scope

This release improves the proved constant in the union-closed sets conjecture. It does **not** prove the full $1/2$ conjecture and does not claim that $0.3827090879$ is optimal for entropy methods or globally optimal.

## Attribution

This research release was generated with frontier AI and published by Unsolved Labs. The repository separates that generation process from the final public proof and deterministic verification artifacts; no private conversation or hidden reasoning is part of the proof object.

## Public release page

https://unsolved-labs.github.io/results/r010-union-closed-03827090879/
