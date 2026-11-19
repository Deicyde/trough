---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.maximal_ineq
---

# Doob's maximal inequality for $\mathbb{N}$

Let $X : \mathbb{N} \rightarrow \Omega \rightarrow \mathbb{R}$ be a non-negative sub-martingale. Then for every $n \in \mathbb{N}$ and $\lambda > 0$,

$$
\begin{aligned}
\mathbb{P}\left(\sup_{i \le n}X_i\geq\lambda \right)
\le \frac{\mathbb{E}\left[X_n \mathbb{I}_{\sup_{i \le n}X_i \ge \lambda}\right]}{\lambda}
\le \frac{\mathbb{E}[X_n]}{\lambda}
\: .
\end{aligned}
$$

## Depends on

- [Submartingale](../basic-definitions/part-01/def-submartingale.md)

## Lean

Formalized as [`MeasureTheory.maximal_ineq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.maximal_ineq).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1265](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1265)
