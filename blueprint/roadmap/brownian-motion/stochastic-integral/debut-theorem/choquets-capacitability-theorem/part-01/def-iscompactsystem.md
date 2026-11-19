---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: IsCompactSystem
---

# IsCompactSystem

A set of sets $K$ is a compact system if for every countable family $(C_n)_{n \in \mathbb{N}}$ of sets in $K$ such that $\bigcap_{n \in\mathbb{N}} C_n = \emptyset$, there exists a finite subset $S$ of $\mathbb{N}$ such that $\bigcap_{n \in S} C_n = \emptyset$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`IsCompactSystem`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsCompactSystem).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 74](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L74)
