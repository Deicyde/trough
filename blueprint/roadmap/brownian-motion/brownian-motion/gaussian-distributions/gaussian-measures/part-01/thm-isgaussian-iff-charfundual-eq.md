---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.isGaussian_iff_charFunDual_eq
---

# isGaussian_iff_charFunDual_eq

A finite measure $\mu$ on $F$ is Gaussian if and only if for every continuous linear form $L \in F^*$, the characteristic function of $\mu$ at $L$ is

$$
\begin{aligned}
\hat{\mu}(L) = \exp\left(i \mu[L] - \mathbb{V}_\mu[L] / 2\right) \: ,
\end{aligned}
$$

in which $\mathbb{V}_\mu[L]$ is the variance of $L$ with respect to $\mu$.

## Depends on

- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [Characteristic function](../../../characteristic-function-and-covariance/characteristic-functions/def-charfundual.md)

## Proof depends on

- [ext_of_charFunDual](../../../characteristic-function-and-covariance/characteristic-functions/thm-ext-of-charfundual.md)
- [charFun_gaussianReal](lem-charfun-gaussianreal.md)

## Lean

Formalized as [`ProbabilityTheory.isGaussian_iff_charFunDual_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussian_iff_charFunDual_eq).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 83](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L83)
