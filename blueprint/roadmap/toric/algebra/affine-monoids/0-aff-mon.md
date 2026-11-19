---
declaration: definition
origin: cited
lean: AddCancelCommMonoid, AddMonoid.FG, IsAddTorsionFree
statement: formalized
---

# Affine monoid

An *affine monoid* is a finitely generated commutative monoid which is:

- cancellative: if $a + c = b + c$ then $a = b$, and
- torsion-free: if $n a = n b$ then $a = b$ (for $n \geq 1$).

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`AddCancelCommMonoid`](https://yaeldillies.github.io/toric/docs/find/#doc/AddCancelCommMonoid), [`AddMonoid.FG`](https://yaeldillies.github.io/toric/docs/find/#doc/AddMonoid.FG), [`IsAddTorsionFree`](https://yaeldillies.github.io/toric/docs/find/#doc/IsAddTorsionFree).

## Sources

- [Toric varieties blueprint: chapters/2-2-affine-monoids.tex, line 20](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/2-2-affine-monoids.tex#L20)
