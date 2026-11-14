---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.ae_eq_posterior_of_compProd_eq
---

# a.e.-uniqueness of the Bayesian inverse

Let $\mu \in \mathcal M(\mathcal X)$ be a finite measure and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a finite kernel. If $\eta : \mathcal Y \rightsquigarrow \mathcal X$ is such that $\mu \otimes \kappa = ((\kappa \circ \mu) \otimes \eta)_\leftrightarrow$, then $\eta(y) = \kappa_\mu^\dagger(y)$ for $(\kappa \circ \mu)$-almost all $y$.

## Depends on

- [bayesInv](def-bayesinv.md)

## Proof

TODO: uniqueness of the conditional kernel.

## Lean

Formalized as [`ProbabilityTheory.ae_eq_posterior_of_compProd_eq`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.ae_eq_posterior_of_compProd_eq).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 327](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L327)
