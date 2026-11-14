---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.isGaussian_multivariateGaussian
---

# isGaussian_multivariateGaussian

A multivariate Gaussian measure is a Gaussian measure.

## Depends on

- [Multivariate Gaussian](def-multivariategaussian.md)
- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)

## Proof depends on

- [isGaussian_stdGaussian](lem-isgaussian-stdgaussian.md)
- [isGaussian_map](../part-01/lem-isgaussian-map.md)

## Proof

The multivariate Gaussian measure is the pushforward of the standard Gaussian measure by an affine map, and is thus Gaussian by Lemma [isGaussian_add_const](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L115) and Lemma [isGaussian_map](../part-01/lem-isgaussian-map.md).

## Lean

Formalized as [`ProbabilityTheory.isGaussian_multivariateGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussian_multivariateGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 458](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L458)
