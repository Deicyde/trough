---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.lowerCrossingTime
---

# Lower crossing time

Let $X : T \to \Omega \to \mathbb{R}$ be a stochastic process, $t \in T$, and $a, b \in \mathbb{R}$. The $n$-th lower crossing time $\sigma^n_{a, b, t}$ of the interval $[a, b]$ by $X$ before time $t$ is the hitting time of the set $(-\infty, a]$ by $X$ after hitting the set $[b, \infty)$ for the $n$-th time.

That is, it is the hitting time of $(-\infty, a]$ by $X$ between $\tau^n_{a, b, t}$ and $t$.

## Depends on

- [Upper crossing time](def-uppercrossingtime.md)

## Lean

Formalized as [`MeasureTheory.lowerCrossingTime`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.lowerCrossingTime).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 88](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L88)
