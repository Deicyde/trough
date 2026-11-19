---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.upcrossingsBefore
---

# Upcrossings before time $t$

Let $X : T \to \Omega \to \mathbb{R}$ be a stochastic process, $t \in T$, and $a, b \in \mathbb{R}$. The number of upcrossings $U_t[a, b]$ of the interval $[a, b]$ by $X$ before time $t$ is the largest $n$ such that $\tau^n_{a, b, t} < t$, or $\infty$ if there is no such largest $n$.

## Depends on

- [Upper crossing time](def-uppercrossingtime.md)

## Lean

Formalized as [`MeasureTheory.upcrossingsBefore`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.upcrossingsBefore).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 99](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L99)
