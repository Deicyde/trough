---
declaration: section
origin: cited
lean: DerivedCategory.Plus.depth, Stacks.LocalCohomology.exists_annihilator_localCohomology_iff_depth_add_dim, Stacks.LocalCohomology.annihilatorDepthCriterionPlus
statement: formalized
proof: formalized
---

# 51.13 Annihilators of local cohomology, II

Section 51.13 of the Stacks Project, [Tag 0EHX](https://stacks.math.columbia.edu/tag/0EHX). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EHY, a definition

[Tag 0EHY](https://stacks.math.columbia.edu/tag/0EHY) in the Stacks Project.

**`DerivedCategory.Plus.depth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/AnnihilatorsLocalCohomology/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/AnnihilatorsLocalCohomology/Basic.lean#L49).

> The `I`-depth of a bounded-below derived object: the first degree of nonzero local
> cohomology, or infinity if local cohomology vanishes throughout.

```lean
noncomputable abbrev depth (A : Type u) [CommRing A]
    (I : Ideal A) (K : DerivedCategory.Plus (ModuleCat.{max u v} A)) : WithTop ℤ
```

## Tag 0EHZ, a proposition

[Tag 0EHZ](https://stacks.math.columbia.edu/tag/0EHZ) in the Stacks Project.

**`Stacks.LocalCohomology.exists_annihilator_localCohomology_iff_depth_add_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/DepthDimensionCriterion.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/DepthDimensionCriterion.lean#L657).

> Uniform annihilation of low local cohomology is equivalent to the
> depth–dimension inequality along all relevant chains of primes.

```lean
public theorem exists_annihilator_localCohomology_iff_depth_add_dim
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (omega : DerivedCategory (ModuleCat.{u} A))
    (_homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (T T' : Set (PrimeSpectrum A)) (_hTT' : T ⊆ T')
    (_hT : StableUnderSpecialization T)
    (_hT' : StableUnderSpecialization T')
    (s : ℤ) (K : DerivedCategory.Plus (ModuleCat.{u} A))
    (_hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{u} A) i).obj K)) :
    (∃ J : Ideal A, PrimeSpectrum.zeroLocus (J : Set A) ⊆ T' ∧
      ∀ i : ℤ, i ≤ s → J ≤ Module.annihilator A
        (localCohomologyWithSupportInPlus
          A T K i)) ↔
    (∀ p q : PrimeSpectrum A, p ∉ T' → q ∈ T → (hpq : p.asIdeal ≤ q.asIdeal) →
      letI : (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)).IsPrime :=
        Ideal.isPrime_map_quotientMk_of_isPrime hpq
      ((DerivedCategory.Plus.depth (Localization.AtPrime p.asIdeal)
          (maximalIdeal (Localization.AtPrime p.asIdeal))
          (localizedComplex p K) : EInt) +
        krullDimToEInt
          (ringKrullDim (Localization.AtPrime
            (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)))) > (s : EInt)))
```

**`Stacks.LocalCohomology.annihilatorDepthCriterionPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/DepthDimensionCriterion.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/DepthDimensionCriterion.lean#L688). The attribute's comment: “the criterion, in predicate form”.

> **Stacks 0EHZ.** The annihilator criterion for a bounded-below complex with finite
> cohomology over a Noetherian ring admitting a dualizing complex, in the predicate form in
> which this library states it.

```lean
public theorem annihilatorDepthCriterionPlus (A : Type u) [CommRing A] [IsNoetherianRing A] :
    AnnihilatorDepthCriterionPlus.{u, u, u} A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.13, Tag 0EHX](https://stacks.math.columbia.edu/tag/0EHX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
