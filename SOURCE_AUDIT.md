# Source and novelty audit — R010

This file pins the public literature boundary used by R010. It is not a claim of priority beyond what these sources establish.

## Primary sources

### Gilmer — first constant entropy bound

Justin Gilmer, *A constant lower bound for the union-closed sets conjecture*.

- arXiv: `2211.09055`
- Public source: https://arxiv.org/abs/2211.09055
- Role in R010: historical origin of the constant entropy method.

### Sawin — improved coupling idea

Will Sawin, *An improved lower bound for the union-closed set conjecture*.

- arXiv: `2211.11504`
- Public source: https://arxiv.org/abs/2211.11504
- Role in R010: dependent-coupling improvement beyond the independent-coupling constant.

### Yu — computable dimension-free optimization framework

Lei Yu, *Dimension-Free Bounds for the Union-Closed Sets Conjecture*.

- arXiv: `2212.00658`
- Public source: https://arxiv.org/abs/2212.00658
- Role in R010: numerical/computable dependent-coupling frontier around `0.38234`.

### Cambie — sharpened dependent-coupling frontier

Stijn Cambie, *Better bounds for the union-closed sets conjecture using the entropy approach*.

- arXiv: `2212.12500v2`
- Revision date: 16 February 2025
- Public source: https://arxiv.org/abs/2212.12500v2
- Role in R010: public dependent-coupling frontier. The paper gives the sharpness value approximately `0.382345533366703` for the specified Sawin-style approach and describes computer verification in its proof.

### Liu — conditionally-i.i.d. protocol used by R010

Jingbo Liu, *Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling*.

- arXiv: `2306.08824v1`
- Submission date: 15 June 2023
- Public source: https://arxiv.org/abs/2306.08824v1
- Role in R010: introduces the conditionally-i.i.d. coupling framework and the Example 5 protocol used by the proof.

Liu's public abstract distinguishes two levels of result:

1. an **analytic strict improvement** beyond the previous approximately `0.3823455` frontier;
2. an **approximately `0.38271`** evaluation obtained under numerically verified hypotheses from a finite-dimensional optimization.

That distinction is essential to the R010 novelty claim.

## R010 novelty boundary

R010 claims:

- the exact rational constant `3827090879/10000000000`;
- an unconditional proof using Liu's published conditionally-i.i.d. protocol;
- removal, for this exact rational constant, of the numerical structural/global-optimization hypotheses associated with Liu's approximately `0.38271` evaluation;
- a reproducible hybrid analytic/interval proof with independent numerical verification paths.

R010 does **not** claim:

- invention of the conditionally-i.i.d. protocol;
- invention of the numerical approximately `0.38271` target;
- proof of the full `1/2` Frankl conjecture;
- optimality of the R010 constant or entropy method;
- peer-reviewed or independently specialist-reviewed status while the release metadata says `pending`.

## Citation hygiene rule

README and manuscript language should use the version-pinned primary links above for technical claims. Secondary surveys may be useful for context but must not be the sole support for the main novelty boundary.
