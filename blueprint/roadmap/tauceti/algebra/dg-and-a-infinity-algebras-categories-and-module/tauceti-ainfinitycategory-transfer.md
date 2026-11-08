---
declaration: def
origin: cited
lean: TauCeti.AInfinityCategory.transfer
statement: formalized
---

# TauCeti.AInfinityCategory.transfer

The **transferred `A∞` category**: the `A∞` structure transferred from the total algebra of
morphisms of `𝒞` along a special contraction onto the total module of morphisms of `D` which is
compatible with the hom modules along a bijection of objects `e : D ≃ C`.  Its differential is the
differential `d_D` of the retract (`homInclusion_homDifferential_transfer`), its composition is
`g ∘ f = p m₂(i g, i f)` (`homInclusion_comp_transfer`), and its higher operations are those of the
transferred `A∞` algebra.

```lean
TauCeti.AInfinityCategory.transfer.{u₁, u₂, v₁, v₂, w} {R : Type w} [CommRing R] {C : Type u₁}
  {D : Type u₂} [TauCeti.GradedLinearQuiver R C] [TauCeti.GradedLinearQuiver R D]
  (𝒞 : TauCeti.AInfinityCategory R C) (e : D ≃ C)
  {dD : Module.End R (TauCeti.GradedLinearQuiver.TotalHom R D)}
  (c : TauCeti.LinearSpecialContraction 𝒞.differential dD)
  (hh : TauCeti.LinearMap.IsHomogeneous c.homotopy (𝒞.grading.piece ℤ) (𝒞.grading.piece ℤ) (-1))
  (hincl :
    TauCeti.LinearMap.IsHomogeneous c.incl ((TauCeti.GradedLinearQuiver.totalGrading R D).piece ℤ)
      (𝒞.grading.piece ℤ) 0)
  (hproj :
    TauCeti.LinearMap.IsHomogeneous c.proj (𝒞.grading.piece ℤ)
      ((TauCeti.GradedLinearQuiver.totalGrading R D).piece ℤ) 0)
  (hc : TauCeti.LinearSpecialContraction.IsHomCompatible e c) : TauCeti.AInfinityCategory R D
```

## Depends on

- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Proof depends on

- [The suspended Stasheff identity free of the structural coefficient holds exactly when the unsuspended one does](../homology/the-suspended-stasheff-identity-free-of-the-stru.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityCategory.transfer`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Transfer/Basic.html#TauCeti.AInfinityCategory.transfer).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityCategory.transfer`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Transfer/Basic.html#TauCeti.AInfinityCategory.transfer)
- [Source of `TauCeti.AInfinityCategory.transfer` in TauCeti/CategoryTheory/AInfinity/Transfer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/AInfinity/Transfer/Basic.lean#L334)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
