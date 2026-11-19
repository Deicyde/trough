---
declaration: definition
origin: cited
lean: MeasureTheory.IsCapacitable
statement: formalized
---

# IsCapacitable

Let $F$ be a set of sets of $\mathcal{X}$ and let $I$ be an $F$-capacity. A set $s$ of $\mathcal{X}$ is said to be $I$-capacitable if for all $a < I(s)$, there exists a set $t \in F_\delta$ such that $t \subseteq s$ and $a \le I(t)$.

## Depends on

- [Capacity](def-capacity.md)

## Lean

Formalized as [`MeasureTheory.IsCapacitable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsCapacitable).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 524](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L524)
