---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.isGaussian_stdGaussian
---

# isGaussian_stdGaussian

The standard Gaussian measure on $E$ is a Gaussian measure.

## Depends on

- [Standard Gaussian measure](../part-01/def-stdgaussian.md)
- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)

## Proof depends on

- [isGaussian_iff_gaussian_charFun](../part-01/lem-isgaussian-iff-gaussian-charfun.md)
- [charFun_stdGaussian](../part-01/lem-charfun-stdgaussian.md)
- [isProbabilityMeasure_stdGaussian](../part-01/lem-isprobabilitymeasure-stdgaussian.md)

## Proof

Since the standard Gaussian is a probability measure (hence finite), we can apply Lemma [isGaussian_iff_gaussian_charFun](../part-01/lem-isgaussian-iff-gaussian-charfun.md) that states that it suffices to show that the characteristic function has a particular form. That form is given by Lemma [charFun_stdGaussian](../part-01/lem-charfun-stdgaussian.md), taking $m=0$ and $C = \langle\cdot, \cdot\rangle$.

## Lean

Formalized as [`ProbabilityTheory.isGaussian_stdGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussian_stdGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 381](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L381)
