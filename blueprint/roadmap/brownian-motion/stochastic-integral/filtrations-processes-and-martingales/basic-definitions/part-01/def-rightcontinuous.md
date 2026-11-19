---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: IsRightContinuous
---

# Right continuous function

Let $T$ be equipped with a partial order and $f : T \to E$ be a function. Then $f$ is right continuous if for all $t \in T$, $\lim_{s \downarrow t} f(s) = f(t)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`IsRightContinuous`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsRightContinuous).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 31](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L31)
