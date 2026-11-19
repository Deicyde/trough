---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.map_eq_of_forall_ae_eq
---

# map_eq_of_modification

Let $X, Y : T \to \Omega \to E$ be two stochastic processes that are modifications of each other. Then for all $t_1, \ldots, t_n \in T$, the random vector $(X_{t_1}, \ldots, X_{t_n})$ has the same distribution as the random vector $(Y_{t_1}, \ldots, Y_{t_n})$. That is, $X$ and $Y$ have same finite-dimensional distributions.

## Depends on

Its statement uses no other node that has an article here.

## Proof

By the modification property, almost surely $X_{t_i} = Y_{t_i}$ for all $i \in [n]$. Thus the function $\omega \mapsto (X_{t_1}(\omega), \ldots, X_{t_n}(\omega))$ is equal to $\omega \mapsto (Y_{t_1}(\omega), \ldots, Y_{t_n}(\omega))$ almost surely, hence the maps of $\mathbb{P}$ by these two functions are equal.

## Lean

Formalized as [`ProbabilityTheory.map_eq_of_forall_ae_eq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.map_eq_of_forall_ae_eq).

## Sources

- [Brownian motion blueprint: chapters/process.tex, line 46](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/process.tex#L46)
