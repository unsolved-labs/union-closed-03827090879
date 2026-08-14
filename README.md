# R010 — Union-closed sets: unconditional 0.3827090879 bound

**Unsolved Labs Research Release R010**

A computer-assisted proof that every finite union-closed family other than `{∅}` contains an element appearing in at least

```text
3827090879 / 10000000000 = 0.3827090879
```

of the member sets.

## Result

For every finite union-closed family `F != {∅}`, there exists an element `x` such that

```text
|{A in F : x in A}| >= (3827090879 / 10000000000) |F|.
```

The exact protocol weights are

```text
alpha = 11249343 / 12500000
beta  =  1250657 / 12500000
```

## Previous frontier

The established dependent-coupling line gives an unconditional bound around `0.3823455`. Jingbo Liu's conditionally-i.i.d. protocol identifies a stronger value around `0.38271`, but the published statement explicitly depends on numerically verified hypotheses, including a nine-dimensional optimization.

This release proves the exact rational constant `0.3827090879` without those hypotheses.

Primary references:

- Stijn Cambie, *Better bounds for the union-closed sets conjecture using the entropy approach*, arXiv:2212.12500.
- Jingbo Liu, *Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling*, arXiv:2306.08824.

## Trust boundary

The proof has an analytic component and a rigorous computer-assisted component. The numerical part is checked three ways:

1. a directed-rounding binary64 `Boost.Interval` verifier;
2. an independently written 256-bit MPFR verifier using a different transcendental backend and independently generated subdivision;
3. a non-adaptive MPFR replay of a frozen prefix-coded leaf certificate with explicit coverage validation.

The auxiliary polynomial/Bernstein inequality is checked using exact rational arithmetic. The complete executable package is stored as a deterministic compressed payload whose SHA-256 is checked before extraction; the mathematical proof itself is directly readable under `proof/`.

Independent specialist review is **pending**.

## Reproduce

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
R010 RELEASE VERIFICATION PASSED
```

`materialize_release.py` first concatenates `payload/part-01.b64` through `part-06.b64`, verifies the exact archive SHA-256 `3bb6d879f7bf55083678c3a0cdce0e33bc980f32bde1bb76e300f89bca2fc098`, and safely extracts the verifier sources and certificate into a temporary directory. No generated prose is consulted by the checkers.

## Files

- `CLAIM.md` — frozen theorem, baseline, assumptions, limitations, and trust boundary.
- `PROOF.md` and `proof/part-*.md` — complete human-readable proof.
- `verification-report.json` — machine-readable frozen claim and reference margins.
- `EXTERNAL_REVIEW_CHECKLIST.md` — modular checklist for outside review.
- `payload/part-*.b64` — deterministic verifier/certificate package.
- `materialize_release.py` — checksum-verifying safe materializer.
- `verify_release.sh` — one-command clean-checkout replay entry point.
- `.github/workflows/verify.yml` — independent CI jobs for the exact/Boost, MPFR, and static-certificate trust boundaries.

The materialized payload contains the complete verifier sources (`union_closed_sharp_verifier.cpp`, `union_closed_conservative_verifier.cpp`, `mpfr_independent_verifier.cpp`, `mpfr_static_replay.cpp`), the exact auxiliary checker, the frozen static certificate, a machine-readable report, integrity hashes, and the inner reproduction script.

## Scope

This release improves the proved constant in the union-closed sets conjecture. It does **not** prove the full `1/2` conjecture and does not claim that `0.3827090879` is the optimal constant achievable by entropy methods.

## Public release page

https://unsolved-labs.github.io/results/r010-union-closed-03827090879/
