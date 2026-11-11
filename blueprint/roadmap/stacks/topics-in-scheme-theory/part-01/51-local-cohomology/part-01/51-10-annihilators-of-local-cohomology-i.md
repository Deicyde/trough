---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.exists_ideal_le_annihilator_localCohomology_iff, Stacks.LocalCohomology.exists_notMem_mem_annihilator_localCohomologyWithSupportIn_of_dualizing, Stacks.LocalCohomology.exists_notMem_and_mem_annihilator_localCohomologyWithSupportIn
statement: formalized
proof: formalized
---

# 51.10 Annihilators of local cohomology, I

Section 51.10 of the Stacks Project, [Tag 0EFB](https://stacks.math.columbia.edu/tag/0EFB). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EFC, a proposition

[Tag 0EFC](https://stacks.math.columbia.edu/tag/0EFC) in the Stacks Project.

**`Stacks.LocalCohomology.exists_ideal_le_annihilator_localCohomology_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/DepthDimensionCriterion.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsAnnihilator/DepthDimensionCriterion.lean#L698).

> **Stacks 0EFC, Faltings' annihilator theorem.** For a finite module `M` over a Noetherian
> ring with a dualizing complex and nested specialization-closed subsets `T ⊆ T'`, an ideal
> supported in `T'` annihilates `H^i_T(M)` for every `i ≤ s` exactly when
> `depth_{A_p}(M_p) + dim((A/p)_q) > s` for every `p ∉ T'` and `q ∈ T` with `p ⊆ q`.

```lean
public theorem exists_ideal_le_annihilator_localCohomology_iff
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (T T' : Set (PrimeSpectrum A)) (hTT' : T ⊆ T')
    (hT : StableUnderSpecialization T) (hT' : StableUnderSpecialization T')
    (s : ℤ) (hs : 0 ≤ s)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega)) :
    (∃ J : Ideal A, PrimeSpectrum.zeroLocus (J : Set A) ⊆ T' ∧
        ∀ i : ℤ, i ≤ s → J ≤ Module.annihilator A
          (localCohomologyWithSupportIn.{u, u} A T
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A M)) i)) ↔
      (∀ p q : PrimeSpectrum A, p ∉ T' → q ∈ T → p.asIdeal ≤ q.asIdeal →
        Stacks.Algebraization.enatToEInt
            (Module.depth (Localization.AtPrime p.asIdeal)
              (maximalIdeal (Localization.AtPrime p.asIdeal))
              (LocalizedModule p.asIdeal.primeCompl M)) +
          krullDimToEInt
            (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
              p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) > (s : EInt))
```

## Tag 0EFE, a lemma

[Tag 0EFE](https://stacks.math.columbia.edu/tag/0EFE) in the Stacks Project.

**`Stacks.LocalCohomology.exists_notMem_mem_annihilator_localCohomologyWithSupportIn_of_dualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LocalCohomologyAnnihilatorInputs.lean#L171). The attribute's comment: “the lemma unconditionally, the hypothesis `hFaltings` of `Stacks.LocalCohomology.exists_notMem_and_mem_annihilator_localCohomologyWithSupportIn` being discharged by Tag 0EFC”.

> **Stacks 0EFE, unconditionally.** For `M` finite over a Noetherian ring `A` with a dualizing
> complex and `p` a prime outside `V(I)`, if `depth_{A_{p'}}(M_{p'}) + dim((A/p')_q) > s` for all
> primes `p' ⊆ p` and all `q ∈ V(I)` with `p' ⊆ q`, then some `f ∈ A` outside `p` annihilates
> `H^i_{V(I)}(M)` for every `i ≤ s`.

```lean
theorem exists_notMem_mem_annihilator_localCohomologyWithSupportIn_of_dualizing
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I : Ideal A) (p : PrimeSpectrum A) (s : ℤ) (hs : 0 ≤ s)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hp : p ∉ PrimeSpectrum.zeroLocus (I : Set A))
    (hdepth : ∀ x y : PrimeSpectrum A, x.asIdeal ≤ p.asIdeal →
      y ∈ PrimeSpectrum.zeroLocus (I : Set A) → x.asIdeal ≤ y.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime x.asIdeal)
            (maximalIdeal (Localization.AtPrime x.asIdeal))
            (LocalizedModule x.asIdeal.primeCompl M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime y.asIdeal) ⧸
            x.asIdeal.map (algebraMap A (Localization.AtPrime y.asIdeal)))) > (s : EInt)) :
    ∃ f : A, f ∉ p.asIdeal ∧ ∀ i : ℤ, i ≤ s →
      f ∈ Module.annihilator A
        (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)
```

**`Stacks.LocalCohomology.exists_notMem_and_mem_annihilator_localCohomologyWithSupportIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AnnihilatorLocalCohomologyI.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AnnihilatorLocalCohomologyI.lean#L57). The attribute's comment: “the lemma, on the hypothesis hFaltings carrying Tag 0EFC”.

> **Stacks 0EFE.** For `M` finite over a Noetherian ring `A` with a dualizing complex and `p`
> a prime outside `V(I)`, if `depth_{A_{p'}}(M_{p'}) + dim((A/p')_q) > s` for all primes `p' ⊆ p`
> and all `q ∈ V(I)` with `p' ⊆ q`, then some `f ∈ A` outside `p` annihilates `H^i_{V(I)}(M)`
> for every `i ≤ s`.

```lean
public theorem exists_notMem_and_mem_annihilator_localCohomologyWithSupportIn
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I : Ideal A) (p : PrimeSpectrum A) (s : ℤ) (hs : 0 ≤ s)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hFaltings : ∀ (T T' : Set (PrimeSpectrum A)), T ⊆ T' →
      StableUnderSpecialization T → StableUnderSpecialization T' →
      ∀ (s₀ : ℤ), 0 ≤ s₀ →
      ∀ (ω : DerivedCategory (ModuleCat.{u} A)),
        Dualizing.IsDualizingComplex (A := A) (K := ω) →
        ((∃ J : Ideal A, PrimeSpectrum.zeroLocus (J : Set A) ⊆ T' ∧
            ∀ i : ℤ, i ≤ s₀ → J ≤ Module.annihilator A
              (localCohomologyWithSupportIn.{u, u} A T
                ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                  (ModuleCat.of A M)) i)) ↔
          (∀ x y : PrimeSpectrum A, x ∉ T' → y ∈ T → x.asIdeal ≤ y.asIdeal →
            Stacks.Algebraization.enatToEInt
                (Module.depth (Localization.AtPrime x.asIdeal)
                  (maximalIdeal (Localization.AtPrime x.asIdeal))
                  (LocalizedModule x.asIdeal.primeCompl M)) +
              krullDimToEInt
                (ringKrullDim ((Localization.AtPrime y.asIdeal) ⧸
                  x.asIdeal.map (algebraMap A (Localization.AtPrime y.asIdeal)))) > (s₀ : EInt))))
    (hp : p ∉ PrimeSpectrum.zeroLocus (I : Set A))
    (hdepth : ∀ x y : PrimeSpectrum A, x.asIdeal ≤ p.asIdeal →
      y ∈ PrimeSpectrum.zeroLocus (I : Set A) → x.asIdeal ≤ y.asIdeal →
      Stacks.Algebraization.enatToEInt
          (Module.depth (Localization.AtPrime x.asIdeal)
            (maximalIdeal (Localization.AtPrime x.asIdeal))
            (LocalizedModule x.asIdeal.primeCompl M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime y.asIdeal) ⧸
            x.asIdeal.map (algebraMap A (Localization.AtPrime y.asIdeal)))) > (s : EInt)) :
    ∃ f : A, f ∉ p.asIdeal ∧ ∀ i : ℤ, i ≤ s →
      f ∈ Module.annihilator A
        (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.10, Tag 0EFB](https://stacks.math.columbia.edu/tag/0EFB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
