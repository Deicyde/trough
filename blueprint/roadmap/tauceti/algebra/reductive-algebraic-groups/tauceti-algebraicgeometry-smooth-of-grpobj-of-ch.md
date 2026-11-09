---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero
statement: formalized
proof: formalized
---

# TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero

An affine group scheme of finite type over a field of characteristic zero is smooth.

```lean
TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero.{u} {k : Type u} [Field k] [CharZero k]
  (G : CategoryTheory.Over (AlgebraicGeometry.Spec ↧k)) [CategoryTheory.GrpObj G]
  [AlgebraicGeometry.IsAffine G.left] [AlgebraicGeometry.LocallyOfFiniteType G.hom] :
  AlgebraicGeometry.Smooth G.hom
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartier's theorem](../algebraic-group/cartiers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Group/Cartier.html#TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Group/Cartier.html#TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero)
- [Source of `TauCeti.AlgebraicGeometry.smooth_of_grpObj_of_charZero` in TauCeti/AlgebraicGeometry/Group/Cartier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Group/Cartier.lean#L31)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
