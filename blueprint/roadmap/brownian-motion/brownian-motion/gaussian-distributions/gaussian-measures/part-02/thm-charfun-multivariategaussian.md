---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.charFun_multivariateGaussian
---

# charFun_multivariateGaussian

The characteristic function of a multivariate Gaussian measure $\mathcal{N}(m, \Sigma)$ is given by

$$
\begin{aligned}
\hat{\mu}(t) = \exp\left(i \langle m, t \rangle - \frac{1}{2} \langle t, \Sigma t \rangle\right)
\: .
\end{aligned}
$$

## Depends on

- [Multivariate Gaussian](def-multivariategaussian.md)
- [Characteristic function](../../../../../mathlib/overview/probability-theory/definitions-in-probability-theory/characteristic-function.md)

## Proof depends on

- [isGaussian_multivariateGaussian](lem-isgaussian-multivariategaussian.md)
- [IsGaussian.charFun_eq](../part-01/lem-isgaussian-charfun-eq.md)
- [integral_id_multivariateGaussian](lem-integral-id-multivariategaussian.md)
- [covMatrix_multivariateGaussian](lem-covmatrix-multivariategaussian.md)

## Proof

Since the multivariate Gaussian measure is a Gaussian measure, we can apply Lemma [IsGaussian.charFun_eq](../part-01/lem-isgaussian-charfun-eq.md) to it. It suffices then to show that the mean and the covariance matrix of the multivariate Gaussian measure are equal to $m$ and $\Sigma$, respectively. This is given by Lemma [integral_id_multivariateGaussian](lem-integral-id-multivariategaussian.md) and Lemma [covMatrix_multivariateGaussian](lem-covmatrix-multivariategaussian.md).

## Lean

Formalized as [`ProbabilityTheory.charFun_multivariateGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.charFun_multivariateGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 471](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L471)
