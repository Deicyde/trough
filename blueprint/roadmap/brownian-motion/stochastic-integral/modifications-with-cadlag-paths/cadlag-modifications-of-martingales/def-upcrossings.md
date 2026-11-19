---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.upcrossings
---

# Upcrossings

Let $X : T \to \Omega \to \mathbb{R}$ be a stochastic process and $a, b \in \mathbb{R}$. The number of upcrossings $U[a, b]$ of the interval $[a, b]$ by $X$ is the supremum over $t \in T$ of the number of upcrossings $U_t[a, b]$ of $[a, b]$ by $X$ before time $t$.

## Depends on

- [Upcrossings before time $t$](def-upcrossingsbefore.md)

## Lean

Formalized as [`MeasureTheory.upcrossings`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.upcrossings).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 108](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L108)
