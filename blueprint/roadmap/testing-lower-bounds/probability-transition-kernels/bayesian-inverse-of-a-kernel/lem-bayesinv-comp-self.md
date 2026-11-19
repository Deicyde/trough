---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior_comp_self
---

# bayesInv_comp_self

For $\mu \in \mathcal M(\mathcal X)$ s-finite, $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ a Markov kernel and $\kappa_\mu^\dagger$ the Bayesian inverse of $\kappa$ with respect to $\mu$, these objects satisfy the equality $\kappa_\mu^\dagger \circ \kappa \circ \mu = \mu$.

## Depends on

- [bayesInv](def-bayesinv.md)

## Proof

The measure $\kappa_\mu^\dagger \circ (\kappa \circ \mu)$ is the projection on $\mathcal X$ of $(\kappa \circ \mu) \otimes \kappa_\mu^\dagger$. But $(\kappa \circ \mu) \otimes \kappa_\mu^\dagger = (\mu \otimes \kappa)_\leftrightarrow$ by definition of the Bayesian inverse. Since $\kappa$ is a Markov kernel, the projection on $\mathcal X$ of that measure is simply $\mu$.

## Lean

Formalized as [`ProbabilityTheory.posterior_comp_self`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior_comp_self).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 342](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L342)
