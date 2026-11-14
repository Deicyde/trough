---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.HasIndepIncrements
---

# HasIndepIncrements

We say that a stochastic process $X : T \to \Omega \to E$ has independent increments if for all $t_1, \ldots, t_n \in T$ with $t_1 \le t_2 \le \cdots \le t_n$, the random variables $X_{t_2} - X_{t_1}, X_{t_3} - X_{t_2}, \ldots, X_{t_n} - X_{t_{n-1}}$ are independent.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.HasIndepIncrements`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.HasIndepIncrements).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 155](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L155)
