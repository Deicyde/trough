---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Submartingale
---

# Submartingale

Let $\mathcal{F}$ be a filtration on a measurable space $\Omega$ with measure $P$ indexed by $T$. A family of functions $M : T \to \Omega \to E$ is a submartingale with respect to a filtration $\mathcal{F}$ if $M$ is adapted with respect to $\mathcal{F}$ and for all $i \le j$, $P[M_j \mid \mathcal{F}_i] \ge M_i$ almost surely.

## Depends on

- [adapted](def-adapted.md)

## Lean

Formalized as [`MeasureTheory.Submartingale`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Submartingale).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 78](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L78)
