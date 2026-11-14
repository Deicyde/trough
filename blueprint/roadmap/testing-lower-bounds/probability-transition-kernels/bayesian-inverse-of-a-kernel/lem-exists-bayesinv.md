---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.posterior, ProbabilityTheory.compProd_posterior_eq_map_swap
---

# Existence of the Bayesian inverse

For $\mathcal X$ standard Borel, $\mu$ and $\kappa$ s-finite, the Bayesian inverse of $\kappa$ with respect to $\mu$ exists and is obtained by disintegration of the measure $\mu \otimes \kappa$ on $\mathcal X \times \mathcal Y$ into a measure $\kappa \circ \mu \in \mathcal M(\mathcal Y)$ and a Markov kernel $\kappa_\mu^\dagger : \mathcal Y \rightsquigarrow \mathcal X$.

## Depends on

- [bayesInv](def-bayesinv.md)

## Proof depends on

- [Disintegration in standard Borel spaces](../disintegration/thm-disintegration.md)

## Lean

Formalized as [`ProbabilityTheory.posterior`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.posterior), [`ProbabilityTheory.compProd_posterior_eq_map_swap`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.compProd_posterior_eq_map_swap).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 311](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L311)
