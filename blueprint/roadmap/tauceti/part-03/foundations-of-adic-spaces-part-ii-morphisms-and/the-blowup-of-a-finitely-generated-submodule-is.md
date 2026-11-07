---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec
statement: formalized
proof: formalized
---

# The blowup of a finitely generated submodule is proper

If `F` is finite, the structure
morphism `Proj R(J) ⟶ Spec C` is proper.

```lean
TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec.{u} (C : Type u) {B : Type u} [CommRing C]
  [CommRing B] [Algebra C B] {F : Set B} (hF : F.Finite) :
  AlgebraicGeometry.IsProper (TauCeti.AlgebraicGeometry.submoduleBlowup.toSpec C F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Blowup/Submodule/Basic.html#TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Blowup/Submodule/Basic.html#TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec)
- [Source of `TauCeti.AlgebraicGeometry.submoduleBlowup.isProper_toSpec` in TauCeti/AlgebraicGeometry/Blowup/Submodule/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Blowup/Submodule/Basic.lean#L158)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
