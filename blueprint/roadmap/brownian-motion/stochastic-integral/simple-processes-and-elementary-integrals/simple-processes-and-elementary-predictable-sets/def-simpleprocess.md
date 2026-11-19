---
declaration: definition
origin: cited
lean: ProbabilityTheory.SimpleProcess
statement: formalized
---

# Simple process

Let $(s_k < t_k)_{k \in \{1, ..., n\}}$ be points in a linear order $T$ with a bottom element 0. Let $(\eta_k)_{0 \le k \le n}$ be bounded random variables with values in a normed real vector space $E$ such that $\eta_0$ is $\mathcal{F}_0$-measurable and $\eta_k$ is $\mathcal{F}_{s_k}$-measurable for $k \ge 1$ . Then the simple process for that sequence is the process $V : T \to \Omega \to E$ defined by

$$
\begin{aligned}
V_t = \eta_0 \mathbb{1}_{\{0\}}(t) + \sum_{k=1}^{n} \eta_k \mathbb{1}_{(s_k, t_k]}(t)
\: .
\end{aligned}
$$

Let $\mathcal{E}_{T, E}$ be the set of simple processes indexed by $T$ with value in $E$.

## Depends on

- [Filtration](../../filtrations-processes-and-martingales/basic-definitions/part-01/def-filtration.md)

## Lean

Formalized as [`ProbabilityTheory.SimpleProcess`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.SimpleProcess).

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 247](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L247)
