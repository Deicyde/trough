---
declaration: def
origin: cited
lean: MonoidHom.restrictScalarsMonoidalLeftAction
statement: formalized
---

# MonoidHom.restrictScalarsMonoidalLeftAction

The left action of a monoid `H` on `ModuleCat A` by twisting along a homomorphism
`a : H →* RingAut A`: an element `h` acts by restricting scalars along `(a h)⁻¹`. The associator
`(g * h) ⊙ₗ M ≅ g ⊙ₗ h ⊙ₗ M` and the unitor `1 ⊙ₗ M ≅ M` are the comparison isomorphisms
of restriction of scalars, with identity underlying linear maps.

```lean
MonoidHom.restrictScalarsMonoidalLeftAction.{v, u, u_1} {H : Type u_1} [Monoid H] {A : Type u}
  [Ring A] (a : H →* RingAut A) :
  CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete H) (ModuleCat A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonoidHom.restrictScalarsMonoidalLeftAction`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Twist.html#MonoidHom.restrictScalarsMonoidalLeftAction).

## Sources

- [Tau Ceti documentation: `MonoidHom.restrictScalarsMonoidalLeftAction`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Twist.html#MonoidHom.restrictScalarsMonoidalLeftAction)
- [Source of `MonoidHom.restrictScalarsMonoidalLeftAction` in TauCeti/Algebra/Category/ModuleCat/Twist.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Twist.lean#L81)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
