---
declaration: definition
origin: cited
lean: Finset.nearestPt
statement: formalized
---

# nearestPt

Let $S$ be a finite set of $E$ and $x \in E$. We denote by $\pi(x, S)$ the point in $S$ which is closest to $x$, i.e. a point such that $d_E(x, S) = \min_{y \in S} d_E(x, y)$ (chosen arbitrarily among the minima if there are several).

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Finset.nearestPt`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Finset.nearestPt).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 349](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L349)
