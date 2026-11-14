---
declaration: definition
origin: cited
lean: MeasureTheory.Capacity
statement: formalized
---

# Capacity

Let $F$ be a set of sets of a type $\mathcal{X}$. An $F$-capacity is a function $I$ from the sets of $\mathcal{X}$ to $\mathbb{R}_{+,\infty}$ such that

1. $I$ is monotone for set inclusion: for $s \subseteq t$, $I(s) \le I(t)$,
2. if $(s_n)_{n\in\mathbb{N}}$ is an increasing sequence of sets of $\mathcal{X}$, then $I(s_n)$ tends to $I(\bigcup_{n\in\mathbb{N}} s_n)$ at infinity,
3. if $(s_n)_{n\in\mathbb{N}}$ is a decreasing sequence of sets in $F$, then $I(s_n)$ tends to $I(\bigcap_{n\in\mathbb{N}} s_n)$ at infinity.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.Capacity`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Capacity).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 482](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L482)
