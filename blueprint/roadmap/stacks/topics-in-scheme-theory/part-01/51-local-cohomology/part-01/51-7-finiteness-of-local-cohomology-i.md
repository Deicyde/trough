---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.exists_annihilator_iff_exists_power_annihilator, Stacks.LocalCohomology.finite_localCohomologyWithSupportIn_iff_exists_annihilator, Stacks.LocalCohomology.localCohomology_finite_iff_localizations_finite, Stacks.LocalCohomology.exists_pow_smul_localCohomology_eq_bot, Stacks.LocalCohomology.localCohomologyWithSupportIn_finite_of_finiteLocallyFree_away
statement: formalized
proof: formalized
---

# 51.7 Finiteness of local cohomology, I

Section 51.7 of the Stacks Project, [Tag 0AW7](https://stacks.math.columbia.edu/tag/0AW7). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AW8, a lemma

[Tag 0AW8](https://stacks.math.columbia.edu/tag/0AW8) in the Stacks Project.

**`Stacks.LocalCohomology.exists_annihilator_iff_exists_power_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/AnnihilatorPower.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/AnnihilatorPower.lean#L68). The attribute's comment: “equivalence of (2) and (3) for closed support”.

> **Stacks 0AW8, equivalence of (2) and (3) for closed support.** For support `V(I)` in a
> Noetherian ring, an ideal supported in `V(I)` annihilates local cohomology through degree `n`
> exactly when a single power of `I` does so.

```lean
theorem exists_annihilator_iff_exists_power_annihilator
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : ModuleCat.{max u v} A) (n : ℕ) :
    (∃ J : Ideal A,
      PrimeSpectrum.zeroLocus (J : Set A) ⊆ PrimeSpectrum.zeroLocus (I : Set A) ∧
      ∀ i : ℤ, i ≤ (n : ℤ) → J ≤ Module.annihilator A
        (localCohomologyWithSupportIn.{u, v} A (PrimeSpectrum.zeroLocus (I : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj M) i)) ↔
      (∃ e : ℕ, ∀ i : ℤ, i ≤ (n : ℤ) → I ^ e ≤ Module.annihilator A
        (localCohomologyWithSupportIn.{u, v} A (PrimeSpectrum.zeroLocus (I : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj M) i))
```

**`Stacks.LocalCohomology.finite_localCohomologyWithSupportIn_iff_exists_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterion.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessAnnihilatorCriterion.lean#L479). The attribute's comment: “equivalence of (1) and (2)”.

> **Stacks 0AW8, equivalence of (1) and (2).** Let `A` be a Noetherian ring, `T ⊆ Spec(A)` a
> subset stable under specialization, `M` a finite `A`-module and `n ≥ 0`. The local cohomology
> modules `H^i_T(M)` are finite for every `i ≤ n` if and only if there is an ideal `J` with
> `V(J) ⊆ T` annihilating `H^i_T(M)` for every `i ≤ n`.
>
> Forward: a finite module is annihilated by its own annihilator, whose zero locus is its support,
> and `H^i_T(M)` is supported in `T`. Backward: Faltings' induction on `n`, replacing `M` by
> `M/Γ_T(M)` and using a nonzerodivisor in `J` to relate degree `i + 1` for `M` to degree `i` for
> `M/fM`.

```lean
theorem finite_localCohomologyWithSupportIn_iff_exists_annihilator (A : Type u) [CommRing A]
    [IsNoetherianRing A] (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (M : ModuleCat.{max u v} A) [Module.Finite A (M : Type (max u v))] (n : ℕ) :
    (∀ i : ℤ, i ≤ (n : ℤ) → Module.Finite A (localCohomologyWithSupportIn A T
        ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj M) i)) ↔
      ∃ J : Ideal A, PrimeSpectrum.zeroLocus (J : Set A) ⊆ T ∧
        ∀ i : ℤ, i ≤ (n : ℤ) → J ≤ Module.annihilator A (localCohomologyWithSupportIn A T
          ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj M) i)
```

## Tag 0AW9, a lemma

[Tag 0AW9](https://stacks.math.columbia.edu/tag/0AW9) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomology_finite_iff_localizations_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessIsLocal.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessIsLocal.lean#L724).

> **Stacks 0AW9.** For a finite module over a Noetherian ring, finiteness of
> local cohomology through degree `n` can be checked after localization at every
> prime ideal.

```lean
public theorem localCohomology_finite_iff_localizations_finite
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : Type v) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (n : ℕ) :
    let hI : I.FG := Ideal.fg_of_isNoetherianRing I
    let RΓ := Dualizing.localCohomologyFunctor A I hI ⋙
      (Dualizing.derivedPowerTorsionProperty A I hI).ι
    let H := fun i : ℕ ↦
      (DerivedCategory.homologyFunctor (ModuleCat.{v} A) (i : ℤ)).obj
        (RΓ.obj ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
          (ModuleCat.of A M)))
    (∀ i : ℕ, i ≤ n → Module.Finite A (H i)) ↔
      ∀ p : PrimeSpectrum A, ∀ i : ℕ, i ≤ n →
        Module.Finite (Localization.AtPrime p.asIdeal)
          (LocalizedModule p.asIdeal.primeCompl (H i))
```

## Tag 0BPX, a lemma

[Tag 0BPX](https://stacks.math.columbia.edu/tag/0BPX) in the Stacks Project.

**`Stacks.LocalCohomology.exists_pow_smul_localCohomology_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/F6Rank301/AnnihilatingLocalCohomology.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/F6Rank301/AnnihilatingLocalCohomology.lean#L264).

> **Stacks 0BPX.** If a power of `J` annihilates the `i`-th local cohomology of `A` supported
> on `V(I)`, then a power of `J` annihilates the corresponding local cohomology of every finitely
> presented `A`-module which is finite locally free after localization at every element of `I`.

```lean
theorem exists_pow_smul_localCohomology_eq_bot (J I : Ideal A) (hJI : J ≤ I) (hI : I.FG) (i : ℕ)
    (hA : ∃ n : ℕ,
      J ^ n • (⊤ : Submodule A
        (localCohomologyWithSupportIn.{u, 0} A (PrimeSpectrum.zeroLocus (I : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A A)) (i : ℤ))) = ⊥) :
    ∀ (M : ModuleCat.{u} A), Module.FinitePresentation A M →
      (∀ f ∈ I, Module.IsFiniteLocallyFree (Localization.Away f) (LocalizedModule.Away f M)) →
      ∃ m : ℕ,
        J ^ m • (⊤ : Submodule A
          (localCohomologyWithSupportIn.{u, 0} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M) (i : ℤ))) = ⊥
```

## Tag 0BPY, a lemma

[Tag 0BPY](https://stacks.math.columbia.edu/tag/0BPY) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyWithSupportIn_finite_of_finiteLocallyFree_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FiniteLocallyFreeFiniteness.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FiniteLocallyFreeFiniteness.lean#L83).

> **Stacks 0BPY.** Let `A` be a Noetherian ring, `I ⊆ A` an ideal, `Z = V(I)` and `n ≥ 0`. If
> the local cohomology `H^i_Z(A)` of the ring is finite for `0 ≤ i ≤ n`, then `H^i_Z(M)` is finite
> for `0 ≤ i ≤ n`, for every finite `A`-module `M` such that `M_f` is a finite locally free
> `A_f`-module for every `f ∈ I`.
>
> Finiteness for `A` through degree `n` produces a power `I ^ e` annihilating `H^i_Z(A)` for
> `i ≤ n`; that power-torsion property transfers to `M`, degree by degree, and the exponents are
> collected into a single one; the annihilator criterion then returns finiteness for `M`.

```lean
theorem localCohomologyWithSupportIn_finite_of_finiteLocallyFree_away
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) (n : ℕ)
    (hA : ∀ i : ℕ, i ≤ n → Module.Finite A
      (localCohomologyWithSupportIn.{u, 0} A
        (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A A)) (i : ℤ)))
    (M : ModuleCat.{u} A) [Module.Finite A (M : Type u)]
    (hM : ∀ f ∈ I, Module.IsFiniteLocallyFree (Localization.Away f)
      (LocalizedModule.Away f (M : Type u))) :
    ∀ i : ℕ, i ≤ n → Module.Finite A
      (localCohomologyWithSupportIn.{u, 0} A
        (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M) (i : ℤ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.7, Tag 0AW7](https://stacks.math.columbia.edu/tag/0AW7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
