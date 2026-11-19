---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.upperCrossingTime
---

# Upper crossing time

Let $X : T \to \Omega \to \mathbb{R}$ be a stochastic process, $t \in T$, and $a, b \in \mathbb{R}$. The $n$-th upper crossing time $\tau^n_{a, b, t}$ of the interval $[a, b]$ by $X$ before time $t$ is the hitting time of the set $[b, \infty)$ by $X$ after hitting the set $(-\infty, a]$ for the $n-1$-th time.

That is, $\tau^0_{a, b, t} = 0$, and for all $n$, $\tau^{n+1}_{a, b, t}$ is the hitting time of $[b, \infty)$ by $X$ between $\sigma'_{a, \tau^{n}_{a, b, t}, t}$ and $t$.

## Depends on

- [lowerCrossingTimeAux](def-lowercrossingtimeaux.md)

## Lean

Formalized as [`MeasureTheory.upperCrossingTime`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.upperCrossingTime).

## Sources

- [Brownian motion blueprint: chapters/cadlag.tex, line 77](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L77)
