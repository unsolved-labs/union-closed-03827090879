\rho(t)=\frac{q'(t)}{2q(t)}-\frac1t.
\]

Then

\[
v'(t)=v(t)\rho(t),
\]

\[
v''(t)=v(t)\left(
\rho(t)^2+
\frac12\left[\frac{q''(t)}{q(t)}-\frac{q'(t)^2}{q(t)^2}\right]
+\frac1{t^2}
\right).
\]

For each rectangle \(B\), centered at \(c\), the program combines natural interval evaluation with the second-order enclosure

\[
\Delta(c+d)
\in
\Delta(c)+\nabla\Delta(c)\cdot d
+\frac12 d^T H(B)d.
\tag{7.2}
\]

If either enclosure has a nonnegative lower endpoint, the box is accepted; otherwise it is bisected along its longest side.

A GCC run produced

```text
core: boxes=3273, splits=3272, max_depth=39,
      least_box_lower=4.1293562138181227e-12
ALL CHECKS PASSED
```

The GCC and Clang outputs were byte-for-byte identical. An address/undefined-behavior-sanitized build also passed.

## 8. Independent high-precision audit

The supplementary file `mpfr_independent_verifier.cpp` is a second interval
implementation written independently of the Boost checker.  It uses MPFR at
256-bit precision with explicit directed rounding, MPFR's own logarithm and
square-root functions, exact rational domain endpoints rounded outward, and an
independently generated adaptive subdivision.  It does not replay the original
leaf boxes.

Its sharp run reports

```text
MPFR R: boxes=39, splits=38, max_depth=14,
        least_box_lower_down=0.0033854057974144654
MPFR core: boxes=3210, splits=3209, max_depth=39,
           least_box_lower_down=4.1428237777820989e-12
MPFR ALL CHECKS PASSED
```

The different subdivision and transcendental backend materially reduce the
risk of a shared implementation error.

## 9. Static partition certificate

The MPFR run also exports its accepted leaves as two fixed prefix-coded files. In the public release these are stored losslessly in `static_certificate.json` and materialized by `materialize_static_certificate.py` as `r_leaf_paths.txt` for the one-dimensional boundary calculation and `core_leaf_paths.txt` for the compact square. In the core certificate, each
internal node has either the two children `X0`, `X1` or the two children `Y0`,
`Y1`, according to the bisected coordinate.

The separate program `mpfr_static_replay.cpp` builds a trie from these paths
and rejects duplicate leaves, leaf-prefix collisions, missing siblings,
mixed-axis branches, and incomplete trees. Thus it verifies that the leaves
form a complete partition before evaluating any inequalities. It then
reconstructs every box with MPFR-256 directed rounding and checks the fixed
leaf enclosures, without performing adaptive accept-or-split decisions. Its
reference output is

```text
static R: leaves=39, max_depth=14,
          least_box_lower_down=0.0033854057974144654
static core: leaves=3210, max_depth=39,
             least_box_lower_down=4.1428237777820989e-12
STATIC MPFR CERTIFICATE PASSED
```

A corruption test obtained by deleting one leaf is rejected with `paths do not
form a complete partition`.

## 10. Reproduction

From this directory, run

```bash
g++ -std=c++20 -O2 -frounding-math -fno-fast-math -ffp-contract=off \
    union_closed_sharp_verifier.cpp -o union_closed_sharp_verifier
./union_closed_sharp_verifier
python3 verify_auxiliary_inequality.py
```

The interval verifier assumes:

* IEEE-754 binary64 arithmetic;
* a compiler that honors changes to the floating-point rounding mode;
* no fast-math reassociation or floating-point contraction;
* Boost.Interval's `rounded_arith_std<double>` policy.

To replay the frozen static MPFR certificate:

```bash
python3 materialize_static_certificate.py
g++ -std=c++20 -O2 mpfr_static_replay.cpp -lmpfr -lgmp \
    -o mpfr_static_replay
./mpfr_static_replay r_leaf_paths.txt core_leaf_paths.txt
```

To regenerate the frozen subdivision independently, run `mpfr_independent_verifier --emit-static .` and compare the resulting files against the SHA-256 digests in `static_certificate.json`. `verification-report.json` records the reference margins and leaf counts.

## 11. What this does and does not establish

The package proves the exact rational constant

\[
0.3827090879.
\]

It does **not** yet prove Liu's full numerically suggested value

\[
0.382709087918741\ldots.
\]

The rational slack of roughly \(1.9\times10^{-11}\) is important. The rational protocol weight
\[
\beta=\frac{1250657}{12500000}=0.10005256
\]
is within about \(1.4\times10^{-10}\) of Liu's numerically optimized weight. No claim about the optimizer's structure is used. The remaining slack means that the main two-variable inequality has a strict positive margin near the conjectured tangency point, which permits a modest interval certificate. At the full optimized constant the inequality is tangent to zero, so a proof would require a local analytic factorization or substantially more delicate interval treatment.

For a wider numerical safety margin, `union_closed_conservative_verifier.cpp` independently certifies the exact constant \(0.382709\); its least core-box lower bound is approximately \(2.97\times10^{-8}\), compared with approximately \(4.13\times10^{-12}\) for the sharp checker.

## Reference

Jingbo Liu, *Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling*, arXiv:2306.08824, 2023.
