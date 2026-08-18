# Frozen claim — R010

## Exact theorem

Let $\mathcal F\neq\{\varnothing\}$ be a finite union-closed family. Then some element belongs to at least

$$
c=\frac{3827090879}{10000000000}=0.3827090879
$$

of the members of $\mathcal F$.

Equivalently, there exists $x$ such that

$$
\bigl|\{A\in\mathcal F:x\in A\}\bigr|\ge c|\mathcal F|.
$$

## Exact constants used by the proof

$$
\alpha=\frac{11249343}{12500000},
\qquad
\beta=\frac{1250657}{12500000},
\qquad
c=\frac{3827090879}{10000000000},
$$

$$
m=1-c=\frac{6172909121}{10000000000},
\qquad
\kappa=\frac1{2m}=\frac{5000000000}{6172909121},
$$

with $\alpha+\beta=1$.

## Baseline / novelty boundary

The public source boundary is pinned in [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md).

In brief:

- Gilmer initiated the constant entropy method.
- Sawin, Yu, and Cambie developed the dependent-coupling frontier; Liu's paper summarizes the resulting unconditional value as approximately $0.3823455$.
- Liu introduced the conditionally-i.i.d. protocol used by R010 and proved an analytic strict improvement.
- Liu's numerical section suggested a value approximately $0.38271$ under numerically verified hypotheses associated with a finite-dimensional optimization.

R010 establishes the exact rational constant $0.3827090879$ without assuming those numerical structural/global-optimization hypotheses. The proof instead uses two pointwise entropy inequalities, one analytic and one rigorously interval-certified.

R010 does **not** claim invention of Liu's protocol or of the numerically suggested target value.

## Computer-assisted trust boundary

The compact two-variable inequality is certified by three public numerical paths in the frozen payload:

- `union_closed_sharp_verifier.cpp`: Boost.Interval with directed binary64 rounding;
- `mpfr_independent_verifier.cpp`: separately written 256-bit MPFR interval implementation;
- `mpfr_static_replay.cpp`: non-adaptive replay of the frozen complete prefix-coded subdivision.

The analytic kernel proof has one algebraic positivity sub-obligation checked independently by `verify_auxiliary_inequality.py` using exact rational arithmetic.

The release materializer verifies the frozen payload SHA-256 before extraction, and the static replay rejects incomplete, duplicate, prefix-colliding, or axis-inconsistent leaf sets before checking numerical inequalities.

## Formalization status

No proof-assistant formalization is currently part of the R010 correctness claim.

A future formalization would be most valuable for the protocol-to-entropy reduction, the analytic kernel inequality, and the theorem that the two pointwise inequalities imply the stated union-closed bound. The large interval partition is already represented as a deterministic certificate with independent exact/outward-rounded replay and need not be treated as a search procedure in the final trust boundary.

## Limitations

- The full Frankl union-closed sets conjecture at constant $1/2$ remains open.
- No optimality claim is made for $0.3827090879$ or for this proof architecture.
- Independent specialist review remains pending.
- The trusted software/hardware base includes conforming C++ implementations, the stated floating-point semantics, Boost.Interval for one path, and GMP/MPFR for the independent/static paths.
