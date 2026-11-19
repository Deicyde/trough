---
declaration: definition
origin: cited
lean: ProbabilityTheory.covMatrix, ProbabilityTheory.posSemidef_covMatrix
statement: formalized
---

# Covariance matrix

The covariance matrix of a finite measure $\mu$ with finite second moment on a finite dimensional inner product space $E$ is the positive semidefinite matrix $\Sigma_\mu$ such that for $u, v \in E$,

$$
\begin{aligned}
\langle u, \Sigma_\mu v\rangle = \mu[\langle u, x - m_\mu \rangle \langle x - m_\mu, v \rangle] \: .
\end{aligned}
$$

This is the covariance bilinear form $C'_\mu(u, v)$, as a matrix.

## Depends on

- [Gaussian measures](../../../../mathlib/overview/probability-theory/random-variables-and-their-laws/gaussian-measures.md)
- [covarianceBilin_same_eq_variance](lem-covariancebilin-same-eq-variance.md)

## Lean

Formalized as [`ProbabilityTheory.covMatrix`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.covMatrix), [`ProbabilityTheory.posSemidef_covMatrix`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.posSemidef_covMatrix).

## Sources

- [Brownian motion blueprint: chapters/characteristic_function.tex, line 154](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/characteristic_function.tex#L154)
