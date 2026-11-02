---
declaration: definition
origin: cited
lean: LiftingMagmaFamily
statement: formalized
---

# Lifting Magma Family

A *lifting magma family* is a family of magmas $\{G_\alpha\}$, one for each type $\alpha$, satisfying the following properties:

- For each type $\alpha$, there is a function $\iota_\alpha : \alpha \to G_\alpha$.
- Given a function $f : \alpha \to G_\alpha$, there is a magma homomorphism $\operatorname{lift}{f} : G_\alpha \to G_\alpha$ such that $\operatorname{lift}{f}(\iota_\alpha(x)) = f(x)$ for all $x$ in $\alpha$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`LiftingMagmaFamily`](https://teorth.github.io/equational_theories/docs/find/#doc/LiftingMagmaFamily).

## Sources

- [Equational Theories blueprint: chapter/metatheorems_from_invariants.tex, line 114](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/metatheorems_from_invariants.tex#L114)
