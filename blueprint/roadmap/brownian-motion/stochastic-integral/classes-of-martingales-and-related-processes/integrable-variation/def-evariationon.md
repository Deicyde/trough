---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: eVariationOn
---

# Extended variation

The (extended-real-valued) variation of a function $f : T \to E$ on a set $s$ inside a linear order is the supremum of $\sum_i \mathrm{edist}(f(u_{i+1}, f(u_i)))$ over all finite increasing sequences $u : N \to T$ in $s$. We denote it by $V_f(s)$ .

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`eVariationOn`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/eVariationOn).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 48](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L48)
