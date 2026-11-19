---
declaration: corollary
origin: cited
lean: ProbabilityTheory.maximal_ineq_norm
statement: formalized
---

# Doob Inequality for normed spaces

Let $X:\mathbb{R}_+ \to \Omega \to E$ be a right-continuous martingale with values in a normed space $E$. For every $T$ and $\lambda>0$ we have

$$
P\left( \sup_{t\in[0,T]} \lVert X_t \rVert \geq \lambda \right)
\leq \frac{\mathbb{E}[\lVert X_T \rVert]}{\lambda}.
$$

## Depends on

- [Martingale](../../../../mathlib/overview/probability-theory/stochastic-processes/martingale.md)
- [Right continuous function](../basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [Martingale.submartingale_norm](../basic-definitions/part-01/cor-martingale-submartingale-norm.md)
- [Doob Inequality](thm-doob-ineq.md)

## Proof

By Corollary [Martingale.submartingale_norm](../basic-definitions/part-01/cor-martingale-submartingale-norm.md), $\lVert X \rVert$ is a sub-martingale. Then apply Theorem [Doob Inequality](thm-doob-ineq.md).

## Lean

Stated as [`ProbabilityTheory.maximal_ineq_norm`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.maximal_ineq_norm); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1391](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1391)
