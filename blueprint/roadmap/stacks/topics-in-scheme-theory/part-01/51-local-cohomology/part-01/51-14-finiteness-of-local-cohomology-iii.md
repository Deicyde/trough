---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.exists_annihilator_localCohomologyWithSupportInPlus_of_finite, Stacks.LocalCohomology.exists_pow_annihilator_localCohomologyWithSupportInPlus_of_finite, Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_tfae, Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_tfae_zeroLocus, Stacks.LocalCohomology.depth_add_dim_gt_of_finite_localCohomologyWithSupportInPlus, Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_iff_depth_add_dim, Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_iff_depth_add_dim_sameUniverse
statement: formalized
proof: formalized
---

# 51.14 Finiteness of local cohomology, III

Section 51.14 of the Stacks Project, [Tag 0EI0](https://stacks.math.columbia.edu/tag/0EI0). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EI1, a lemma

[Tag 0EI1](https://stacks.math.columbia.edu/tag/0EI1) in the Stacks Project.

**`Stacks.LocalCohomology.exists_annihilator_localCohomologyWithSupportInPlus_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlus.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlus.lean#L182). The attribute's comment: “the implication (1) ⟹ (2); the converse (2) ⟹ (1) is not proved”.

> **Stacks 0EI1, the implication (1) ⟹ (2).** Let `A` be a Noetherian ring, let
> `T ⊆ Spec(A)` be any subset, let `K` be an object of the bounded-below derived category of
> `A`-modules and let `n ∈ ℤ`. If `H^i_T(K)` is finite for every `i ≤ n`, then there is an ideal
> `J ⊆ A` with `V(J) ⊆ T` annihilating `H^i_T(K)` for every `i ≤ n`.
>
> Below a degree `a` bounding `K` below the modules vanish, so their annihilator is the unit
> ideal; on `[a, n]` each is annihilated by its own annihilator, whose zero locus is its support
> and hence contained in `T`; the product of those finitely many ideals is the required `J`.

```lean
theorem exists_annihilator_localCohomologyWithSupportInPlus_of_finite (A : Type u) [CommRing A]
    [IsNoetherianRing A] (T : Set (PrimeSpectrum A))
    (K : DerivedCategory.Plus (ModuleCat.{max u v} A)) (n : ℤ)
    (hfin : ∀ i : ℤ, i ≤ n →
      Module.Finite A (localCohomologyWithSupportInPlus.{u, v} A T K i)) :
    ∃ J : Ideal A, PrimeSpectrum.zeroLocus (J : Set A) ⊆ T ∧
      ∀ i : ℤ, i ≤ n → J ≤ Module.annihilator A
        (localCohomologyWithSupportInPlus.{u, v} A T K i)
```

**`Stacks.LocalCohomology.exists_pow_annihilator_localCohomologyWithSupportInPlus_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlus.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlus.lean#L217). The attribute's comment: “the implication (1) ⟹ (3) for closed support T = V(I); (3) ⟹ (1) is not proved”.

> **Stacks 0EI1, the implication (1) ⟹ (3) for closed support.** Let `A` be a Noetherian ring,
> let `I ⊆ A` be an ideal and write `Z = V(I)`, let `K` be an object of the bounded-below derived
> category of `A`-modules and let `n ∈ ℤ`. If `H^i_Z(K)` is finite for every `i ≤ n`, then there is
> an `e ≥ 0` such that `I ^ e` annihilates `H^i_Z(K)` for every `i ≤ n`.
>
> The ideal produced by the implication `(1) ⟹ (2)` has zero locus inside `V(I)`, so `I` lies in
> its radical and a power of `I` lies inside it.

```lean
theorem exists_pow_annihilator_localCohomologyWithSupportInPlus_of_finite (A : Type u)
    [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (K : DerivedCategory.Plus (ModuleCat.{max u v} A)) (n : ℤ)
    (hfin : ∀ i : ℤ, i ≤ n → Module.Finite A (localCohomologyWithSupportInPlus.{u, v} A
      (PrimeSpectrum.zeroLocus (I : Set A)) K i)) :
    ∃ e : ℕ, ∀ i : ℤ, i ≤ n → I ^ e ≤ Module.annihilator A
      (localCohomologyWithSupportInPlus.{u, v} A
        (PrimeSpectrum.zeroLocus (I : Set A)) K i)
```

**`Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlusEquivalence.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlusEquivalence.lean#L70). The attribute's comment: “the equivalence of (1) and (2), for T stable under specialization and K bounded below with finite cohomology modules”.

> **Stacks 0EI1, the equivalence of (1) and (2).** Let `A` be a Noetherian ring, let
> `T ⊆ Spec(A)` be stable under specialization, let `K` be an object of `D⁺_{Coh}(A)` and let
> `n ∈ ℤ`. Then `H^i_T(K)` is finite for every `i ≤ n` exactly when one ideal `J ⊆ A` with
> `V(J) ⊆ T` annihilates `H^i_T(K)` for every `i ≤ n`.

```lean
theorem localCohomologyWithSupportInPlus_finite_tfae (A : Type u) [CommRing A]
    [IsNoetherianRing A] (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (K : DerivedCategory.Plus (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{max u v} A) i).obj K))
    (n : ℤ) :
    List.TFAE
      [∀ i : ℤ, i ≤ n → Module.Finite A (localCohomologyWithSupportInPlus.{u, v} A T K i),
        ∃ J : Ideal A, PrimeSpectrum.zeroLocus (J : Set A) ⊆ T ∧
          ∀ i : ℤ, i ≤ n → J ≤ Module.annihilator A
            (localCohomologyWithSupportInPlus.{u, v} A T K i)]
```

**`Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_tfae_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlusEquivalence.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterionPlusEquivalence.lean#L96). The attribute's comment: “the equivalence of (1), (2) and (3) for closed support T = V(I), for K bounded below with finite cohomology modules”.

> **Stacks 0EI1, the equivalence of (1), (2) and (3) for closed support.** Let `A` be a
> Noetherian ring, let `I ⊆ A` be an ideal and write `Z = V(I)`, let `K` be an object of
> `D⁺_{Coh}(A)` and let `n ∈ ℤ`. Then the following are equivalent: `H^i_Z(K)` is finite for every
> `i ≤ n`; one ideal `J ⊆ A` with `V(J) ⊆ Z` annihilates `H^i_Z(K)` for every `i ≤ n`; some power
> `I ^ e` annihilates `H^i_Z(K)` for every `i ≤ n`.
>
> A zero locus is closed, so the first equivalence is the one above, and the second is the
> ideal-theoretic statement that an ideal has zero locus inside `V(I)` exactly when it contains a
> power of `I`.

```lean
theorem localCohomologyWithSupportInPlus_finite_tfae_zeroLocus (A : Type u) [CommRing A]
    [IsNoetherianRing A] (I : Ideal A) (K : DerivedCategory.Plus (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{max u v} A) i).obj K))
    (n : ℤ) :
    List.TFAE
      [∀ i : ℤ, i ≤ n → Module.Finite A (localCohomologyWithSupportInPlus.{u, v} A
          (PrimeSpectrum.zeroLocus (I : Set A)) K i),
        ∃ J : Ideal A,
          PrimeSpectrum.zeroLocus (J : Set A) ⊆ PrimeSpectrum.zeroLocus (I : Set A) ∧
          ∀ i : ℤ, i ≤ n → J ≤ Module.annihilator A (localCohomologyWithSupportInPlus.{u, v} A
            (PrimeSpectrum.zeroLocus (I : Set A)) K i),
        ∃ e : ℕ, ∀ i : ℤ, i ≤ n → I ^ e ≤ Module.annihilator A
          (localCohomologyWithSupportInPlus.{u, v} A
            (PrimeSpectrum.zeroLocus (I : Set A)) K i)]
```

## Tag 0EI2, a proposition

[Tag 0EI2](https://stacks.math.columbia.edu/tag/0EI2) in the Stacks Project.

**`Stacks.LocalCohomology.depth_add_dim_gt_of_finite_localCohomologyWithSupportInPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessCriterionPlus.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessCriterionPlus.lean#L107). The attribute's comment: “the implication (1) ⟹ (2), assuming only Tag 0EHZ's annihilator criterion (`AnnihilatorDepthCriterionPlus`), which is proved in `FaltingsAnnihilator.lean`; the step from finiteness to a uniform annihilator is proved”.

> **Stacks 0EI2, the implication (1) ⟹ (2).** Let `A` be a Noetherian ring with a dualizing
> complex, let `T ⊆ Spec(A)` be stable under specialization, let `s ∈ ℤ` and let `K` be a
> bounded-below complex with finite cohomology modules. If `H^i_T(K)` is finite for every `i ≤ s`,
> then `depth_{A_p}(K_p) + dim((A/p)_q) > s` for every `p ∉ T` and `q ∈ T` with `p ⊆ q`.
>
> Finiteness gives one ideal supported in `T` annihilating all of `H^i_T(K)` for `i ≤ s`, by
> `exists_annihilator_localCohomologyWithSupportInPlus_of_finite`; the annihilator criterion of
> Tag 0EHZ at `T' = T` turns that ideal into the depth-dimension inequality.

```lean
theorem depth_add_dim_gt_of_finite_localCohomologyWithSupportInPlus
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (hEHZ : AnnihilatorDepthCriterionPlus.{u, v, w} A)
    (omega : DerivedCategory (ModuleCat.{w} A))
    (homega : Dualizing.IsDualizingComplex omega)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (s : ℤ) (K : DerivedCategory.Plus (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{max u v} A) i).obj K))
    (hfin : ∀ i : ℤ, i ≤ s →
      Module.Finite A (localCohomologyWithSupportInPlus.{u, v} A T K i)) :
    ∀ p q : PrimeSpectrum A, p ∉ T → q ∈ T → (hpq : p.asIdeal ≤ q.asIdeal) →
      letI : (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)).IsPrime :=
        Ideal.isPrime_map_quotientMk_of_isPrime hpq
      (DerivedCategory.Plus.depth.{u, v} (Localization.AtPrime p.asIdeal)
          (maximalIdeal (Localization.AtPrime p.asIdeal))
          (localizedComplex.{u, v} p K) : EInt) +
        Stacks.Algebraization.krullDimToEInt
          (ringKrullDim (Localization.AtPrime
            (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)))) > (s : EInt)
```

**`Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_iff_depth_add_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessCriterionPlus.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessCriterionPlus.lean#L144). The attribute's comment: “the full equivalence (1) ⟺ (2), assuming Tag 0EI1's finiteness criterion (`FinitenessAnnihilatorCriterionPlus`), whose direction from an annihilator to finiteness is not proved in this library, and Tag 0EHZ's annihilator criterion (`AnnihilatorDepthCriterionPlus`), which is proved in `FaltingsAnnihilator.lean`”.

> **Stacks 0EI2, Proposition 51.14.2: finiteness of local cohomology, III.** Let `A` be a
> Noetherian ring with a dualizing complex, let `T ⊆ Spec(A)` be stable under specialization, let
> `s ∈ ℤ` and let `K` be a bounded-below complex with finite cohomology modules. Then `H^i_T(K)` is
> finite for every `i ≤ s` if and only if `depth_{A_p}(K_p) + dim((A/p)_q) > s` for every `p ∉ T`
> and `q ∈ T` with `p ⊆ q`.
>
> This is the composition the source performs: the finiteness criterion of Tag 0EI1 replaces
> finiteness through degree `s` by uniform annihilation by one ideal supported in `T`, and the
> annihilator criterion of Tag 0EHZ at `T' = T` replaces that uniform annihilation by the
> depth-dimension inequality.

```lean
theorem localCohomologyWithSupportInPlus_finite_iff_depth_add_dim
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (hEI1 : FinitenessAnnihilatorCriterionPlus.{u, v} A)
    (hEHZ : AnnihilatorDepthCriterionPlus.{u, v, w} A)
    (omega : DerivedCategory (ModuleCat.{w} A))
    (homega : Dualizing.IsDualizingComplex omega)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (s : ℤ) (K : DerivedCategory.Plus (ModuleCat.{max u v} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{max u v} A) i).obj K)) :
    (∀ i : ℤ, i ≤ s →
      Module.Finite A (localCohomologyWithSupportInPlus.{u, v} A T K i)) ↔
      (∀ p q : PrimeSpectrum A, p ∉ T → q ∈ T → (hpq : p.asIdeal ≤ q.asIdeal) →
        letI : (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)).IsPrime :=
          Ideal.isPrime_map_quotientMk_of_isPrime hpq
        (DerivedCategory.Plus.depth.{u, v} (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (localizedComplex.{u, v} p K) : EInt) +
          Stacks.Algebraization.krullDimToEInt
            (ringKrullDim (Localization.AtPrime
              (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)))) > (s : EInt))
```

**`Stacks.LocalCohomology.localCohomologyWithSupportInPlus_finite_iff_depth_add_dim_sameUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessCriterionPlusUnconditional.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessCriterionPlusUnconditional.lean#L121).

> **Stacks 0EI2, Proposition 51.14.2: finiteness of local cohomology, III.** Let `A` be a
> Noetherian ring admitting a dualizing complex, let `T ⊆ Spec(A)` be stable under specialization,
> let `s ∈ ℤ` and let `K` be an object of the bounded-below derived category of `A`-modules whose
> cohomology modules are all finite. Then `H^i_T(K)` is finite for every `i ≤ s` if and only if
> `depth_{A_p}(K_p) + dim((A/p)_q) > s` for every pair of primes `p ∉ T`, `q ∈ T` with `p ⊆ q`.
>
> This is the composition the source performs: the finiteness criterion of Tag 0EI1 replaces
> finiteness through degree `s` by uniform annihilation by one ideal supported in `T`, and the
> annihilator criterion of Tag 0EHZ at `T' = T` replaces that uniform annihilation by the
> depth-dimension inequality. Both criteria are proved in this library, so nothing is assumed here
> beyond the hypotheses of the source.

```lean
theorem localCohomologyWithSupportInPlus_finite_iff_depth_add_dim_sameUniverse
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex omega)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (s : ℤ) (K : DerivedCategory.Plus (ModuleCat.{u} A))
    (hK : ∀ i : ℤ, Module.Finite A
      ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{u} A) i).obj K)) :
    (∀ i : ℤ, i ≤ s →
      Module.Finite A (localCohomologyWithSupportInPlus.{u, u} A T K i)) ↔
      (∀ p q : PrimeSpectrum A, p ∉ T → q ∈ T → (hpq : p.asIdeal ≤ q.asIdeal) →
        letI : (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)).IsPrime :=
          Ideal.isPrime_map_quotientMk_of_isPrime hpq
        (DerivedCategory.Plus.depth.{u, u} (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (localizedComplex.{u, u} p K) : EInt) +
          Stacks.Algebraization.krullDimToEInt
            (ringKrullDim (Localization.AtPrime
              (q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)))) > (s : EInt))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.14, Tag 0EI0](https://stacks.math.columbia.edu/tag/0EI0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
