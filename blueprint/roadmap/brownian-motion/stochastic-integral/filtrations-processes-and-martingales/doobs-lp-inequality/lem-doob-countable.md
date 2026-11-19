---
declaration: lemma
origin: cited
lean: MeasureTheory.Submartingale.ae_bddAbove_Iic, ProbabilityTheory.maximal_ineq_countable
statement: formalized
proof: formalized
---

# Doob's maximal Inequality for countable

Let $X : I \rightarrow \Omega \rightarrow \mathbb{R}$ be a non-negative sub-martingale with $I$ countable. Then for every $M \in I,\lambda > 0$ and $p>1$ we have

$$
\begin{aligned}
P\left( \sup_{i\in I, i\leq M}X_i\geq\lambda \right)
\le \frac{\mathbb{E}\left[X_M \mathbb{I}_{\sup_{i \le M}X_i \ge \lambda}\right]}{\lambda}
\le \frac{\mathbb{E}[X_M]}{\lambda}
\: .
\end{aligned}
$$

## Depends on

- [Submartingale](../basic-definitions/part-01/def-submartingale.md)

## Proof depends on

- [Doob's maximal inequality for $\mathbb{N}$](lem-maximal-ineq.md)

## Proof

For any finite subset $J \subset I$ with $M \in J$, we have by Lemma [Doob's maximal inequality for $\mathbb{N}$](lem-maximal-ineq.md)

$$
\begin{aligned}
P\left( \sup_{i\in J, i \le M}X_i\geq\lambda \right)
\le \frac{\mathbb{E}\left[X_{M} \mathbb{I}_{\sup_{i \in J, i \le M}X_i \ge \lambda}\right]}{\lambda}
\: .
\end{aligned}
$$

Then we build a countable increasing sequence of finite sets $J_n$ with $\bigcup_nJ_n=I$. Note for any $\lambda' < \lambda$,

$$
\begin{aligned}
\lambda' P\left( \sup_{i\in I, i\leq M}X_i>\lambda' \right)
&= \lambda' P\left( \bigcup_{i\in I, i\leq M}\{X_i>\lambda'\} \right) \\
&= \lambda' \lim_{n\to\infty} P\left( \bigcup_{i\in J_n, i\leq M}\{X_i>\lambda'\} \right) \\
&\le \lim_{n\to\infty} \mathbb{E}\left[X_{M} \mathbb{I}_{\sup_{i \in J_n, i \le M}X_i \ge \lambda'}\right] \\
&\le \mathbb{E}\left[X_{M} \mathbb{I}_{\sup_{i \in I, i \le M}X_i \ge \lambda'}\right]
\end{aligned}
$$

Now take $\lambda'\uparrow\lambda$ and use monotone or dominated convergence to derive the desired inequality.

In the above, we first interpret $\sup_{i\in I, i\leq M}X_i$ in extended reals for well-definedness, then observe by the (now proved) maximal inequality that $\sup_{i\in I, i\leq M}X_i < \infty$ a.s. by taking $\lambda\to\infty$, so the supremum is well-defined in $\mathbb{R}$.

## Lean

Formalized as [`MeasureTheory.Submartingale.ae_bddAbove_Iic`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale.ae_bddAbove_Iic), [`ProbabilityTheory.maximal_ineq_countable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.maximal_ineq_countable).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 1284](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L1284)
