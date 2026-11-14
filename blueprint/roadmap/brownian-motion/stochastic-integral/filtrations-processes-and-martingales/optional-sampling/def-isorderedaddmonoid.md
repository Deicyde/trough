---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: IsOrderedAddMonoid
---

# Ordered Monoid

Let $(M, +)$ be a commutative monoid that is also a partial order. It is said to be an *ordered monoid* if for all $a, b, c \in M$, we have the following implication:

$$
a \le b \implies a + c \le b + c.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`IsOrderedAddMonoid`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsOrderedAddMonoid).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 923](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L923)
