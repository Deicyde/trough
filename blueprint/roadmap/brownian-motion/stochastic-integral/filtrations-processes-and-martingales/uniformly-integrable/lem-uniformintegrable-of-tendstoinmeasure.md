---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.UniformIntegrable.uniformIntegrable_of_tendstoInMeasure
---

# uniformIntegrable_of_tendstoInMeasure

Let $(X_t)_{t \in T}$ be a family of $p$-uniformly integrable stochastic processes. Then the family of limits in probability of sequences of $X$ is $p$-uniformly integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

A subfamily of a $p$-uniformly integrable family is $p$-uniformly integrable. As convergence in probability implies the existence of a subsequence that converges almost everywhere, the family of limits in probability is a subfamily of the family of limits in almost everywhere convergence, which is $p$-uniformly integrable by Lemma [uniformIntegrable_of_tendsto_ae](lem-uniformintegrable-of-tendsto-ae.md).

## Lean

Formalized as [`MeasureTheory.UniformIntegrable.uniformIntegrable_of_tendstoInMeasure`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.UniformIntegrable.uniformIntegrable_of_tendstoInMeasure).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 900](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L900)
