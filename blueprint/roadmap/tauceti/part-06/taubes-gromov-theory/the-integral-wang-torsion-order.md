---
declaration: theorem
origin: cited
lean: TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det
statement: formalized
proof: formalized
---

# The integral Wang torsion order

If `H₁(F; ℤ)` is free of finite rank and
`det (1 - φ_*) ≠ 0` on it, the torsion subgroup of `H₁(T_φ; ℤ)` has order `|det (1 - φ_*)|`.

```lean
TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det {F : Type} [TopologicalSpace F]
  (φ : F ≃ₜ F)
  [Module.Free ℤ
      ↑(HomologicalComplex.homology
          (((AlgebraicTopology.singularChainComplexFunctor (ModuleCat ℤ)).obj ↧ℤ).obj ↧F) 1)]
  [Module.Finite ℤ
      ↑(HomologicalComplex.homology
          (((AlgebraicTopology.singularChainComplexFunctor (ModuleCat ℤ)).obj ↧ℤ).obj ↧F) 1)]
  (hdet :
    LinearMap.det
        (LinearMap.id -
          ModuleCat.Hom.hom
            (HomologicalComplex.homologyMap (TauCeti.MappingTorus.monodromyChainMap φ ↧ℤ) 1)) ≠
      0) :
  Nat.card
      ↥(Submodule.torsion ℤ
          ↑(HomologicalComplex.homology
              (((AlgebraicTopology.singularChainComplexFunctor (ModuleCat ℤ)).obj ↧ℤ).obj
                ↧(TauCeti.MappingTorus φ))
              1)) =
    (LinearMap.det
        (LinearMap.id -
          ModuleCat.Hom.hom
            (HomologicalComplex.homologyMap (TauCeti.MappingTorus.monodromyChainMap φ ↧ℤ)
              1))).natAbs
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/MappingTorus/Torsion.html#TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det).

## Sources

- [Tau Ceti documentation: `TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/MappingTorus/Torsion.html#TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det)
- [Source of `TauCeti.MappingTorus.card_torsion_homology_one_eq_natAbs_det` in TauCeti/AlgebraicTopology/Singular/MappingTorus/Torsion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/MappingTorus/Torsion.lean#L149)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
