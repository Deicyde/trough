---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: Metric.IsCover
---

# $\varepsilon$-cover

A set $C \subseteq E$ is an $\varepsilon$-cover of a set $A \subseteq E$ if for every $x \in A$, there exists $y \in C$ such that $d_E(x, y) \le \varepsilon$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Metric.IsCover`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Metric.IsCover).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 26](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L26)
