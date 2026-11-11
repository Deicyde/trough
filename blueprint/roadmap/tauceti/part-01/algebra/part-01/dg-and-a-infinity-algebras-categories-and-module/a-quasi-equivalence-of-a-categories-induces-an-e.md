---
declaration: theorem
origin: cited
lean: TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory
statement: formalized
proof: formalized
---

# A quasi-equivalence of `A∞` categories induces an equivalence of homotopy categories

```lean
TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory.{u₁, u₂, v₁, v₂, w}
  {R : Type w} [CommRing R] {C : Type u₁} {D : Type u₂} [TauCeti.GradedLinearQuiver R C]
  [TauCeti.GradedLinearQuiver R D] {ℬ : TauCeti.AInfinityCategory R C}
  {𝒞 : TauCeti.AInfinityCategory R D} {ℱ : TauCeti.AInfinityFunctor ℬ 𝒞}
  {h𝒞 : 𝒞.CohomologicallyUnital} (hℱ : ℱ.IsQuasiEquivalence h𝒞) (hℬ : ℬ.CohomologicallyUnital) :
  (TauCeti.AInfinityFunctor.mapHomotopyCategory hℬ h𝒞 ⋯).IsEquivalence
```

## Depends on

- [TauCeti.AInfinityFunctor](tauceti-ainfinityfunctor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Functor/QuasiEquivalence.html#TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Functor/QuasiEquivalence.html#TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory)
- [Source of `TauCeti.AInfinityFunctor.IsQuasiEquivalence.isEquivalence_mapHomotopyCategory` in TauCeti/CategoryTheory/AInfinity/Functor/QuasiEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/AInfinity/Functor/QuasiEquivalence.lean#L460)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
