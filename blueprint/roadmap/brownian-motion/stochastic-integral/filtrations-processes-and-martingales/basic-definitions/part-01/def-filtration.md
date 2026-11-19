---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Filtration
---

# Filtration

A filtration on a measurable space $(\Omega, \mathcal{A})$ with measure $P$ indexed by a preordered set $T$ is a family of sigma-algebras $\mathcal{F} = (\mathcal{F}_t)_{t \in T}$ such that for all $i \le j$, $\mathcal{F}_i \subseteq \mathcal{F}_j$ and for all $t \in T$, $\mathcal{F}_t \subseteq \mathcal{A}$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.Filtration`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.Filtration).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 9](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L9)
