---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: IsOrderedModule
---

# Ordered Module

Let $\alpha, \beta$ be preorders with $0$ elements and such that there is a scalar multiplication $(\_ \cdot \_) : \alpha \times \beta \to \beta$. Then $\beta$ is said to be an *ordered $\alpha$-module* (or *ordered module* if $\alpha$ is clear from the context) if the following hold:

- $\forall a \in \alpha, \forall b_1, b_2 \in \beta, 0 \le a \implies b_1 \le b_2 \implies a \cdot b_1 \le a \cdot b_2$;
- $\forall a_1, a_2 \in \alpha, \forall b \in \beta, 0 \le b \implies a_1 \le a_2 \implies a_1 \cdot b \le a_2 \cdot b$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`IsOrderedModule`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsOrderedModule).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 930](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L930)
