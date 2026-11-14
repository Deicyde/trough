---
declaration: theorem
origin: cited
lean: ProbabilityTheory.maximal_ineq
statement: formalized
---

# Doob Inequality

Let $X: \mathbb{R}_+ \to \Omega \to \mathbb{R}$ be a right-continuous non-negative sub-martingale. For every $T \in \mathbb{R}_+$ and $\lambda>0$ we have

$$
\begin{aligned}
P\left( \sup_{t\in[0,T]}X_t \geq \lambda \right)
\leq \frac{\mathbb{E}[X_T \mathbb{I}_{\sup_{i \le T}X_i \ge \lambda}]}{\lambda}
\leq \frac{\mathbb{E}[X_T]}{\lambda}
\: .
\end{aligned}
$$

## Depends on

- [Submartingale](../basic-definitions/part-01/def-submartingale.md)
- [Right continuous function](../basic-definitions/part-01/def-rightcontinuous.md)

## Proof depends on

- [Doob's maximal Inequality for countable](lem-doob-countable.md)

## Proof

Since $X$ is right-continuous and $[0,T]$ is a compact interval, we have that

$$
\begin{aligned}
\sup_{t\in[0,T]}X_t = \sup_{t\in[0,T] \cap \mathbb{Q}}X_t
\: .
\end{aligned}
$$

Then apply Lemma [Doob's maximal Inequality for countable](lem-doob-countable.md) with $I = [0,T] \cap \mathbb{Q}$ and $M = T$.

## Lean

Stated as [`ProbabilityTheory.maximal_ineq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.maximal_ineq); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1366](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1366)
