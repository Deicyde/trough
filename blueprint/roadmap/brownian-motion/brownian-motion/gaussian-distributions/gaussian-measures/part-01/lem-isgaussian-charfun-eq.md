---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsGaussian.charFun_eq
---

# IsGaussian.charFun_eq

The characteristic function of a Gaussian measure $\mu$ on $E$ is given by

$$
\begin{aligned}
\hat{\mu}(t) = \exp\left(i \langle t, m_\mu \rangle - \frac{1}{2} C'_\mu(t, t)\right) \: .
\end{aligned}
$$

## Depends on

- [Gaussian measures](../../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [Characteristic function](../../../../../mathlib/overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)
- [Covariance in a Hilbert space](../../../characteristic-function-and-covariance/covariance/def-covinnerbilin.md)

## Proof depends on

- [isGaussian_iff_charFun_eq](lem-isgaussian-iff-charfun-eq.md)
- [IsGaussian.memLp_id](lem-isgaussian-memlp-id.md)
- [covarianceBilin_same_eq_variance](../../../characteristic-function-and-covariance/covariance/lem-covariancebilin-same-eq-variance.md)

## Proof

By Lemma [isGaussian_iff_charFun_eq](lem-isgaussian-iff-charfun-eq.md), for every $t \in E$,

$$
\begin{aligned}
\hat{\mu}(t) = \exp\left(i \mu[\langle t, \cdot \rangle] - \mathbb{V}_\mu[\langle t, \cdot \rangle] / 2\right) \: .
\end{aligned}
$$

By Lemma [IsGaussian.memLp_id](lem-isgaussian-memlp-id.md), $\mu$ has finite first moment and $\mu[\langle t, \cdot \rangle] = \langle t, m_\mu \rangle$. By the same lemma, $\mu$ has finite second moment and for any $t$ we have $\mathbb{V}_\mu[\langle t, \cdot\rangle] = C'_\mu(t, t)$.

## Lean

Formalized as [`ProbabilityTheory.IsGaussian.charFun_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsGaussian.charFun_eq).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 226](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L226)
