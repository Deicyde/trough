---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior
---

# bayesInv

For $\mu \in \mathcal M(\mathcal X)$ and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$, a Bayesian inverse of $\kappa$ is a Markov kernel $\kappa_\mu^\dagger : \mathcal Y \rightsquigarrow \mathcal X$ such that $\mu \otimes \kappa = ((\kappa \circ \mu) \otimes \kappa_\mu^\dagger)_\leftrightarrow$ in which $(\cdot)_\leftrightarrow$ denotes swapping the two coordinates. If such an inverse exists it is unique up to a $(\kappa \circ \mu)$-null set, and we talk about *the* Bayesian inverse of $\kappa$ with respect to $\mu$.

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ProbabilityTheory.posterior`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 296](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L296)
