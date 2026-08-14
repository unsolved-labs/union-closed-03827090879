# External review checklist

This checklist separates the proof into independently auditable claims. A reviewer need not trust numerical optimization or heuristic search.

## A. Entropy/protocol deduction

1. Verify the sequential protocol construction and that each marginal has the uniform law on the family.
2. Under the independent protocol, check that the conditional probability of OR-bit zero is `xy` after the substitution `x=1-s`, `y=1-t`.
3. Under Liu's Example 5 with `f(r)=r(1-r)`, check that the corresponding probability is `J(x,y)=xy(1+(1-x)(1-y))` and that the history-derived variables are conditionally i.i.d.
4. Check the two integrations, conditional Jensen step, chain-rule inequality, and strict endpoint argument when all frequencies are below `c`.

## B. Analytic kernel inequality

1. Check the comparisons `J(x,y)<=j(y)` and `2J_y(x,y)<=j'(y)` for `x<=y`.
2. Check both sign cases when `j(y)>=1/2`.
3. In the region `j(y)<1/2`, verify the formula for `G_xy` and the two scalar comparisons in equation (5) of the manuscript.
4. In the entropy comparison, keep the cases `0<a<=1` and `a>=1` separate; this is needed for the inequality direction after multiplying by `1-a`.
5. Re-run `verify_auxiliary_inequality.py` to check the polynomial identity and all sixteen positive Bernstein coefficients exactly.

## C. Boundary estimates for the main inequality

1. Verify `u'(t)=log(1-t)/t^2<0` and `u(xy)>=u(x)-log y`.
2. Check the small-variable estimates and the three intervals used to prove positivity of `R(y)`.
3. Verify concavity of `g(t)=u(exp(-t))` and the near-one reduction to one variable.
4. Check every displayed rational/logarithmic comparison in Section 6.

## D. Compact interval certificate

1. Confirm the formulas for `u'`, `u''`, `v'`, `v''`, and the gradient/Hessian of `Delta`.
2. Rebuild and run the Boost.Interval checker with the documented strict floating-point flags.
3. Rebuild and run the independent MPFR-256 checker.
4. Replay `r_leaf_paths.txt` and `core_leaf_paths.txt` with `mpfr_static_replay.cpp`; then delete one leaf and confirm that coverage validation fails.
5. Compare the least lower endpoints and leaf counts with the reference output.

## E. Acceptance standard

The result should be regarded as externally reproduced only after at least one reviewer completes A-C line by line and at least one independent machine runs both D.2 and D.3/D.4. Proof-assistant formalization would provide an additional, stronger trust boundary but is not logically required for an ordinary computer-assisted proof.
