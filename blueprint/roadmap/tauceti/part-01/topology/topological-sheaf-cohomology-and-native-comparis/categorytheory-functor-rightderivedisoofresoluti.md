---
declaration: def
origin: cited
lean: CategoryTheory.Functor.rightDerivedIsoOfResolution
statement: formalized
---

# CategoryTheory.Functor.rightDerivedIsoOfResolution

A functorial resolution by objects of a class adapted to `F` computes `RⁿF`, naturally in
its argument. The components are the comparisons through arbitrary injective resolutions given
by `rightDerivedObjIsoOfResolution_hom_comp_homologyMap`.

```lean
CategoryTheory.Functor.rightDerivedIsoOfResolution.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.Abelian C] {D : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} D] [CategoryTheory.Abelian D]
  [CategoryTheory.EnoughInjectives C] (F : CategoryTheory.Functor C D) [F.Additive]
  (P : CategoryTheory.ObjectProperty C) [P.IsClosedUnderIsomorphisms]
  (hinj : ∀ (Y : C), CategoryTheory.Injective Y → P Y)
  (hP : ∀ (S : CategoryTheory.ShortComplex C), S.ShortExact → P S.X₁ → P S.X₂ → P S.X₃)
  (hF :
    ∀ (S : CategoryTheory.ShortComplex C), S.ShortExact → P S.X₁ → P S.X₂ → (S.map F).ShortExact)
  (K : CategoryTheory.Functor C (CochainComplex C ℕ)) (ι : CochainComplex.single₀ C ⟶ K)
  [∀ (X : C), QuasiIso (ι.app X)] (hK : ∀ (X : C) (n : ℕ), P ((K.obj X).X n)) (n : ℕ) :
  F.rightDerived n ≅
    K.comp
      ((F.mapHomologicalComplex (ComplexShape.up ℕ)).comp
        (HomologicalComplex.homologyFunctor D (ComplexShape.up ℕ) n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.rightDerivedIsoOfResolution`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Abelian/AcyclicResolution.html#CategoryTheory.Functor.rightDerivedIsoOfResolution).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.rightDerivedIsoOfResolution`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Abelian/AcyclicResolution.html#CategoryTheory.Functor.rightDerivedIsoOfResolution)
- [Source of `CategoryTheory.Functor.rightDerivedIsoOfResolution` in TauCeti/CategoryTheory/Abelian/AcyclicResolution.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Abelian/AcyclicResolution.lean#L360)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
