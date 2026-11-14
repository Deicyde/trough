---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsGaussian.ext, ProbabilityTheory.IsGaussian.ext_iff
---

# IsGaussian.ext_iff

Two Gaussian measures $\mu$ and $\nu$ on a separable Hilbert space are equal if and only if they have same mean and same covariance.

## Depends on

- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [Covariance in a Hilbert space](../../../characteristic-function-and-covariance/covariance/def-covinnerbilin.md)

## Proof depends on

- [ext_of_charFun](../../../characteristic-function-and-covariance/characteristic-functions/thm-ext-of-charfun.md)
- [IsGaussian.charFun_eq](lem-isgaussian-charfun-eq.md)

## Proof

The forward direction is immediate.

For the converse direction, it is enough to show that $\mu$ and $\nu$ have the same characteristic function by Theorem [ext_of_charFun](../../../characteristic-function-and-covariance/characteristic-functions/thm-ext-of-charfun.md). As they are both Gaussian, their characteristic functions only depend on their mean and covariance by Lemma [IsGaussian.charFun_eq](lem-isgaussian-charfun-eq.md). Thus they are equal.

## Lean

Formalized as [`ProbabilityTheory.IsGaussian.ext`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsGaussian.ext), [`ProbabilityTheory.IsGaussian.ext_iff`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsGaussian.ext_iff).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 289](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L289)
