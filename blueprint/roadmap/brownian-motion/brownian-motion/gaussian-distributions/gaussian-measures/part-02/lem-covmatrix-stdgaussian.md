---
declaration: lemma
origin: cited
lean: ProbabilityTheory.covMatrix_stdGaussian
statement: formalized
proof: formalized
---

# covMatrix_stdGaussian

The covariance matrix of the standard Gaussian measure is the identity matrix.

## Depends on

- [Standard Gaussian measure](../part-01/def-stdgaussian.md)
- [Covariance matrix](../../../characteristic-function-and-covariance/covariance/def-covmatrix.md)

## Proof depends on

- [isGaussian_iff_gaussian_charFun](../part-01/lem-isgaussian-iff-gaussian-charfun.md)
- [charFun_stdGaussian](../part-01/lem-charfun-stdgaussian.md)

## Proof

From Lemma [charFun_stdGaussian](../part-01/lem-charfun-stdgaussian.md), we know that for all $t \in \mathbb{R}$,

$$
\hat{\mu}(t) = \exp\left(-\frac{\|t\|^2}{2}\right) = \exp\left(-\frac{\langle t, \mathrm{I}t\rangle}{2}\right).
$$

As the identity is positive semidefinite, we deduce from Lemma [isGaussian_iff_gaussian_charFun](../part-01/lem-isgaussian-iff-gaussian-charfun.md) that $\Sigma_\mu$ is the identity matrix.

## Lean

Formalized as [`ProbabilityTheory.covMatrix_stdGaussian`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covMatrix_stdGaussian).

## Sources

- [Brownian motion blueprint: chapters/gaussian.tex, line 408](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/gaussian.tex#L408)
