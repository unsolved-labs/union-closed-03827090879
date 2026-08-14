# Frozen claim — R010

## Exact theorem

Let `F != {∅}` be a finite union-closed family. Then some element belongs to at least

```text
3827090879 / 10000000000
```

of the members of `F`.

Equivalently, there exists `x` such that

```text
|{A in F : x in A}| >= (3827090879 / 10000000000) |F|.
```

The decimal value is exactly `0.3827090879`.

## Exact constants used by the proof

```text
alpha = 11249343 / 12500000
beta  =  1250657 / 12500000
c     = 3827090879 / 10000000000
m     = 6172909121 / 10000000000
kappa = 5000000000 / 6172909121
```

with `alpha + beta = 1` and `m = 1-c`.

## Baseline / novelty boundary

Cambie's dependent-coupling analysis gives the established improvement around `0.3823455333667` over the independent-coupling constant. Liu subsequently introduced a conditionally-i.i.d. protocol and reported a value around `0.38271`, but explicitly states that the latter conclusion holds under numerically verified hypotheses tied to a finite-dimensional optimization.

R010 establishes the exact rational constant `0.3827090879` without assuming Liu's positive-semidefiniteness/global-optimization hypotheses. The new proof instead uses two pointwise entropy inequalities, one analytic and one rigorously interval-certified.

Primary sources:

- https://arxiv.org/abs/2212.12500
- https://arxiv.org/abs/2306.08824
- 2026 context survey: https://arxiv.org/abs/2607.24414

## Assumptions

Only the ordinary definitions of finite union-closed families and Shannon/binary entropy, plus Liu's published conditionally-i.i.d. sampling protocol, are used. The result has no unproved numerical optimization hypothesis.

## Computer-assisted trust boundary

The compact two-variable inequality is certified by:

- `union_closed_sharp_verifier.cpp`: Boost.Interval with directed floating-point rounding;
- `mpfr_independent_verifier.cpp`: independent 256-bit MPFR implementation;
- `mpfr_static_replay.cpp`: non-adaptive replay of the frozen complete subdivision encoded by `r_leaf_paths.txt` and `core_leaf_paths.txt`;
- `verify_auxiliary_inequality.py`: exact rational algebra/Bernstein coefficient check.

The MPFR static replay rejects incomplete, duplicate, prefix-colliding, or axis-inconsistent leaf sets before checking any numerical leaf inequality.

## Limitations

- The full Frankl union-closed sets conjecture at constant `1/2` remains open.
- No optimality claim is made for `0.3827090879` or for the proof architecture.
- Independent specialist review is pending.
- The trusted software/hardware base includes a conforming C++ compiler, Boost.Interval for one checker, and GMP/MPFR for the independent and static checkers. The analytic proof itself is not yet formalized in a proof assistant.
