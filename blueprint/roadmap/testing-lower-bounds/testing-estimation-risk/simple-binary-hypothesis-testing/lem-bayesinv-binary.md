---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior_boolKernel_apply_true, ProbabilityTheory.posterior_boolKernel_apply_false
---

# bayesInv_binary

The Bayesian inverse of a kernel $P : \{0,1\} \rightsquigarrow \mathcal X$ with respect to a prior $\xi \in \mathcal M(\{0,1\})$ is $P_\xi^\dagger(x) = \left(\xi_0\frac{d P(0)}{d(P \circ \xi)}(x), \xi_1\frac{d P(1)}{d(P \circ \xi)}(x)\right)$ (almost surely w.r.t. $P \circ \xi = \xi_0 P(0) + \xi_1 P(1)$).

## Depends on

- [bayesInv](../../probability-transition-kernels/bayesian-inverse-of-a-kernel/def-bayesinv.md)

## Lean

Formalized as [`ProbabilityTheory.posterior_boolKernel_apply_true`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior_boolKernel_apply_true), [`ProbabilityTheory.posterior_boolKernel_apply_false`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior_boolKernel_apply_false).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/risk.tex, line 532](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/risk.tex#L532)
