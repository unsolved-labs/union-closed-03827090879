# Statement audit — R010

This document maps every load-bearing public claim to the human proof and to the machine-checked obligation that supports it.

## Canonical theorem identity

Public theorem:

$$
\forall\ \text{finite union-closed }\mathcal F\neq\{\varnothing\},\quad
\exists x:\
|\{A\in\mathcal F:x\in A\}|
\ge
\frac{3827090879}{10000000000}\,|\mathcal F|.
$$

Canonical human statement: Theorem 1 in `manuscript/r010_union_closed_bound.tex`.

Canonical machine-readable constant: `verification-report.json`:

- numerator: `3827090879`
- denominator: `10000000000`
- decimal string: `0.3827090879`

## Claim-to-proof-to-checker map

| Public claim | Human proof location | Machine/certificate obligation | Status |
|---|---|---|---|
| Exact theorem constant is `3827090879/10000000000` | Manuscript Theorem 1; `CLAIM.md` | root/frozen verification metadata plus release-integrity CI | checked |
| Protocol weights are exact and sum to 1 | Manuscript §2 | frozen verification report and exact `Fraction(...)` CI check | checked |
| Liu's conditionally-i.i.d. protocol with `f(r)=r(1-r)` yields the kernel `J(x,y)` used here | Manuscript §4; frozen proof §3 | analytic proof obligation; source pinned in `SOURCE_AUDIT.md` | human mathematical dependency |
| The two pointwise inequalities imply the union-closed theorem | Manuscript §4 | analytic proof obligation | human mathematical dependency |
| Kernel inequality `h(J(x,y)) ≥ sqrt(h(j(x))h(j(y)))` | Manuscript §5 | exact rational checker verifies polynomial identity, endpoint comparison, and 16 Bernstein coefficients | mixed analytic + exact check |
| Main entropy inequality holds on the small-variable strip | Manuscript §6.1 | analytic estimates + rigorous `verify_R()` interval calculation | checked as documented |
| Main entropy inequality holds on the near-one strip | Manuscript §6.2 | analytic estimates + directed-rounding reference bound | checked as documented |
| Main entropy inequality holds on `[0.01,0.999999]^2` | Manuscript §6.3 | Boost.Interval adaptive directed-rounding checker | checked |
| Compact-core result is independently reproduced | Manuscript §7 | separately written MPFR-256 checker with independent subdivision/backend | checked |
| Frozen MPFR leaves cover the entire certified domain | Manuscript §7 | prefix-tree completeness validation before numerical replay | checked |
| Public proof segments reconstruct the proof frozen in the payload | `PROOF.md`, `proof/README.md` | verify raw segment hash, insert the documented one-byte Part 1→Part 2 newline, extract payload `PROOF.md`, require identical SHA-256 `27bccc…` and byte-for-byte equality | checked by release-integrity CI |
| Search/heuristic optimization is outside the final correctness oracle | Manuscript §§7–8; `VERIFICATION.md` | final checkers accept frozen artifacts directly | checked structurally |
| Independent specialist review has occurred | — | `verification-report.json` says `pending` | **not claimed** |
| Full proof-assistant formalization has occurred | — | no Lean theorem is in the release trust boundary | **not claimed** |

## Public wording rules

Evidence-supported descriptions include:

- “computer-assisted proof”
- “reproducible exact/directed-rounding certificate”
- “independent MPFR verification path”
- “unconditional exact rational constant `0.3827090879`”
- “independent specialist review pending”

Unsupported descriptions include:

- “Frankl's conjecture is solved”
- “best possible constant”
- “formally verified in Lean”
- “peer reviewed” or “independently reviewed” while review status is pending
- any wording that presents Liu's approximately `0.38271` numerical evaluation as unconditional
- any wording that attributes invention of the conditionally-i.i.d. protocol to R010
