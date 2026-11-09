---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app
statement: formalized
proof: formalized
---

# Symmetric powers commute with pullback of quasicoherent sheaves

for every morphism of
schemes `f : X ⟶ Y` and every quasicoherent `𝒪_Y`-module `M`, the canonical comparison
`f^* (Symⁿ M) ⟶ Symⁿ (f^* M)` is an isomorphism.

```lean
TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app.{u}
  {X Y : AlgebraicGeometry.Scheme} (f : X ⟶ Y) (n : ℕ) (M : Y.Modules)
  [SheafOfModules.IsQuasicoherent M] :
  CategoryTheory.IsIso
    ((AlgebraicGeometry.Scheme.Modules.pullbackSymmetricPowerComparison f n).app M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/SymmetricPower/Pullback/Quasicoherent.html#TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Modules/SymmetricPower/Pullback/Quasicoherent.html#TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app)
- [Source of `TauCeti.AlgebraicGeometry.isIso_pullbackSymmetricPowerComparison_app` in TauCeti/AlgebraicGeometry/Modules/SymmetricPower/Pullback/Quasicoherent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Modules/SymmetricPower/Pullback/Quasicoherent.lean#L49)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
