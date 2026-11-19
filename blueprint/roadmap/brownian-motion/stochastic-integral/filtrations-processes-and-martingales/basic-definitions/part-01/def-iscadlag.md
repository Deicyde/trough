---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: IsCadlag
---

# Cadlag function

A function $f : T \to E$ is cadlag if it is right continuous and the limit $\lim_{s \uparrow t} f(s)$ exists for all $t \in T$.

## Depends on

- [Right continuous function](def-rightcontinuous.md)

## Lean

Formalized as [`IsCadlag`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsCadlag).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 38](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L38)
