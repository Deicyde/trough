---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.isGaussian_iff_charFun_eq
---

# isGaussian_iff_charFun_eq

A finite measure $\mu$ on a Hilbert space $E$ is Gaussian if and only if for every $t \in E$, the characteristic function of $\mu$ at $t$ is

$$
\begin{aligned}
\hat{\mu}(t) =  \exp\left(i \mu[\langle t, \cdot \rangle] - \mathbb{V}_\mu[\langle t, \cdot \rangle] / 2\right) \: .
\end{aligned}
$$

## Depends on

- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [Characteristic function](../../../characteristic-function-and-covariance/characteristic-functions/def-charfundual.md)
- [Characteristic function](../../../../../mathlib/overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)

## Proof depends on

- [isGaussian_iff_charFunDual_eq](thm-isgaussian-iff-charfundual-eq.md)

## Proof

By Theorem [isGaussian_iff_charFunDual_eq](thm-isgaussian-iff-charfundual-eq.md), $\mu$ is Gaussian iff for every continuous linear form $L \in E^*$, the characteristic function of $\mu$ at $L$ is

$$
\begin{aligned}
\hat{\mu}(L) = \exp\left(i \mu[L] - \mathbb{V}_\mu[L] / 2\right) \: .
\end{aligned}
$$

Every continuous linear form $L \in E^*$ can be written as $L(x) = \langle t, x \rangle$ for some $t \in E$, hence we have that $\mu$ is Gaussian iff for every $t \in E$,

$$
\begin{aligned}
\hat{\mu}(t) = \exp\left(i \mu[\langle t, \cdot \rangle] - \mathbb{V}_\mu[\langle t, \cdot \rangle] / 2\right) \: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.isGaussian_iff_charFun_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.isGaussian_iff_charFun_eq).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 202](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L202)
