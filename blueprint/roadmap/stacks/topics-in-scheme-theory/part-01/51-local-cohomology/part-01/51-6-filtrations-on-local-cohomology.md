---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.nonempty_exactSequenceData, Stacks.LocalCohomology.range_changeOfSupport_eq_localizationKernel, Stacks.LocalCohomology.kernel_changeOfSupport_eq_closedSupportImages, PrimeSpectrum.stableUnderSpecialization_nonminimalPrimes, Stacks.LocalCohomology.localCohomologyWithSupportIn_map_eq_zero_of_local, Stacks.LocalCohomology.eventually_injective_image_localCohomologyWithSupportIn
statement: formalized
proof: formalized
---

# 51.6 Filtrations on local cohomology

Section 51.6 of the Stacks Project, [Tag 0EHV](https://stacks.math.columbia.edu/tag/0EHV). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EF8, a lemma

[Tag 0EF8](https://stacks.math.columbia.edu/tag/0EF8) in the Stacks Project.

**`Stacks.LocalCohomology.nonempty_exactSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/ExactSequence.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/ExactSequence.lean#L369). The attribute's comment: “the exact sequence”.

> **Stacks 0EF8, the exact sequence.** Let `A` be a Noetherian ring, let `T ⊆ Spec(A)` be
> stable under specialization and let `T' ⊆ T` be the set of primes of `T` that are not minimal in
> `T`. For every `A`-module `M` and every `i` there is an exact sequence
> `0 ⟶ colim_{Z,f} H¹_f(Hⁱ⁻¹_Z(M)) ⟶ Hⁱ_{T'}(M) ⟶ Hⁱ_T(M) ⟶ ⨁_{𝔭 ∈ T ∖ T'} Hⁱ_{𝔭A_𝔭}(M_𝔭)`
> where the colimit is over the closed subsets `Z ⊆ T` and the `f ∈ A` with `V(f) ∩ Z ⊆ T'`.

```lean
theorem nonempty_exactSequenceData (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (M : ModuleCat.{max u v} A) (i : ℤ) :
    Nonempty (ExactSequenceData.{u, v} A T M i)
```

**`Stacks.LocalCohomology.range_changeOfSupport_eq_localizationKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/LocalizationKernel.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/LocalizationKernel.lean#L91). The attribute's comment: “exactness at local cohomology with support in T”.

> **Exactness at local cohomology with support in `T`.** Over a Noetherian ring, a class in
> `Hⁱ_T(K)` is the image of a class supported in the nonminimal primes of `T` if and only if it
> localizes to zero at every prime that is minimal in `T`.

```lean
theorem range_changeOfSupport_eq_localizationKernel
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (K : DerivedCategory (ModuleCat.{max u v} A)) (i : ℤ)
    (x : localCohomologyWithSupportIn.{u, v} A T K i) :
    (∃ y : localCohomologyWithSupportIn.{u, v} A (PrimeSpectrum.nonminimalPrimes T) K i,
      (changeOfSupport A (PrimeSpectrum.nonminimalPrimes_subset T) K i).hom y = x) ↔
      ∀ p : PrimeSpectrum A, p ∈ T \ PrimeSpectrum.nonminimalPrimes T →
        (ModuleCat.localizedModuleMkLinearMap
          (localCohomologyWithSupportIn.{u, v} A T K i) p.asIdeal.primeCompl) x = 0
```

**`Stacks.LocalCohomology.kernel_changeOfSupport_eq_closedSupportImages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/LocalizationKernel.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/LocalizationKernel.lean#L127). The attribute's comment: “exactness at local cohomology with support in the nonminimal primes T'”.

> **Exactness at local cohomology with support in the nonminimal primes.** Over a Noetherian
> ring, a class in `Hⁱ_{T'}(K)` dies in `Hⁱ_T(K)` if and only if it is the image of a class with
> closed support `V(I) ∩ V(f) ⊆ T'`, where `V(I) ⊆ T`, which already vanishes in
> `Hⁱ_{V(I)}(K)`.

```lean
theorem kernel_changeOfSupport_eq_closedSupportImages
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (K : DerivedCategory (ModuleCat.{max u v} A)) (i : ℤ)
    (x : localCohomologyWithSupportIn.{u, v} A (PrimeSpectrum.nonminimalPrimes T) K i) :
    (changeOfSupport A (PrimeSpectrum.nonminimalPrimes_subset T) K i).hom x = 0 ↔
      ∃ (I : Ideal A) (f : A) (_hI : PrimeSpectrum.zeroLocus (I : Set A) ⊆ T)
        (hadm : PrimeSpectrum.zeroLocus (I : Set A) ∩ PrimeSpectrum.zeroLocus ({f} : Set A) ⊆
          PrimeSpectrum.nonminimalPrimes T)
        (y : localCohomologyWithSupportIn.{u, v} A (PrimeSpectrum.zeroLocus (I : Set A) ∩
          PrimeSpectrum.zeroLocus ({f} : Set A)) K i),
        (changeOfSupport A hadm K i).hom y = x ∧
          (changeOfSupport A Set.inter_subset_left K i).hom y = 0
```

**`PrimeSpectrum.stableUnderSpecialization_nonminimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/NonminimalPrimes.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/NonminimalPrimes.lean#L75). The attribute's comment: “T' is stable under specialization”.

> The nonminimal primes of a subset of the prime spectrum stable under specialization are
> again stable under specialization.

```lean
theorem stableUnderSpecialization_nonminimalPrimes (hT : StableUnderSpecialization T) :
    StableUnderSpecialization (nonminimalPrimes T)
```

## Tag 0EF9, a lemma

[Tag 0EF9](https://stacks.math.columbia.edu/tag/0EF9) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyWithSupportIn_map_eq_zero_of_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/ProZero.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/ProZero.lean#L452).

> Let `A` be a Noetherian ring of finite Krull dimension, let `T ⊆ Spec(A)` be stable under
> specialization and let `{M_n}` be an inverse system of `A`-modules. If for every `m` the
> transition maps `Hⁱ_{pA_p}(M_{k,p}) → Hⁱ_{pA_p}(M_{m,p})` vanish for all `p ∈ T` and all
> `k ≥ m'(m)`, then `Hⁱ_T(M_k) → Hⁱ_T(M_m)` vanishes for all `k` beyond the `2 ^ dim T`-fold
> iterate of `m'` at `m`.

```lean
theorem localCohomologyWithSupportIn_map_eq_zero_of_local
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (hdim : ringKrullDim A < ⊤)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (F : ℕᵒᵖ ⥤ ModuleCat.{max u v} A) (i : ℕ)
    (m' : ℕ → ℕ) (hm' : ∀ m, m ≤ m' m)
    (hlocal : ∀ (m k : ℕ) (hbound : m' m ≤ k),
      ∀ (p : PrimeSpectrum A), p ∈ T →
      ((ModuleCat.localizedModuleFunctor.{max u v} p.asIdeal.primeCompl ⋙
        localCohomologyModuleFunctor (Localization p.asIdeal.primeCompl) (i : ℤ)).map
        (F.map (homOfLE ((hm' m).trans hbound)).op) = 0))
    (m k : ℕ)
    (hk : m'^[2 ^ ((topologicalKrullDim (↥T)).unbotD 0).toNat] m ≤ k) :
    (localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
      (F.map (homOfLE
        ((Function.id_le_iterate_of_id_le (fun m => hm' m) _ m).trans hk)).op) = 0
```

## Tag 0EFA, a lemma

[Tag 0EFA](https://stacks.math.columbia.edu/tag/0EFA) in the Stacks Project.

**`Stacks.LocalCohomology.eventually_injective_image_localCohomologyWithSupportIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/StableImage.lean, line 593](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/MinimalPrimeFiltration/StableImage.lean#L593).

> **Stacks 0EFA.** Let `A` be a Noetherian ring of finite dimension, let `T ⊆ Spec(A)` be
> stable under specialization and let `{M_n}` be an inverse system of `A`-modules. If for every `m`
> there is `c ≥ m` such that at every prime `𝔭 ∈ T` and for every `k ≥ c` the transition map
> vanishes on `Hⁱ⁻¹_{𝔭A_𝔭}`, its image on `Hⁱ_{𝔭A_𝔭}` is independent of `k` and that image injects
> into `Hⁱ_{𝔭A_𝔭}(M_{0,𝔭})`, then there is `m₀` such that for every `m ≥ m₀` the image of
> `Hⁱ_T(M_k) → Hⁱ_T(M_m)` injects into `Hⁱ_T(M_{m₀})` for all large `k`.
>
> The independence of the image from `k` is not needed for the conclusion; see
> `eventually_injective_image_localCohomologyWithSupportIn_of_image_injective`.

```lean
theorem eventually_injective_image_localCohomologyWithSupportIn
    (A : Type u) [CommRing A] [IsNoetherianRing A] (hdim : ringKrullDim A < ⊤)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (M : ℕᵒᵖ ⥤ ModuleCat.{max u v} A) (i : ℕ)
    (hloc : ∀ m : ℕ, ∃ c : ℕ, ∃ hmc : m ≤ c, ∀ p ∈ T, ∀ (k : ℕ) (hck : c ≤ k),
      ((M ⋙ ModuleCat.localizedModuleFunctor.{max u v} p.asIdeal.primeCompl ⋙
        localCohomologyModuleFunctor (Localization p.asIdeal.primeCompl)
          ((i : ℤ) - 1)).map (homOfLE (hmc.trans hck)).op = 0) ∧
      (LinearMap.range ((M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).map (homOfLE (hmc.trans hck)).op).hom =
        LinearMap.range ((M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).map (homOfLE hmc).op).hom) ∧
      (∀ x : (M ⋙ ModuleCat.localizedModuleFunctor.{max u v} p.asIdeal.primeCompl ⋙
          localCohomologyModuleFunctor (Localization p.asIdeal.primeCompl) (i : ℤ)).obj (op k),
        ((M ⋙ ModuleCat.localizedModuleFunctor.{max u v} p.asIdeal.primeCompl ⋙
          localCohomologyModuleFunctor (Localization p.asIdeal.primeCompl) (i : ℤ)).map
            (homOfLE (hmc.trans hck)).op).hom x ∈
          LinearMap.ker ((M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
            p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
              (Localization p.asIdeal.primeCompl) (i : ℤ)).map
                (homOfLE (Nat.zero_le m)).op).hom →
        ((M ⋙ ModuleCat.localizedModuleFunctor.{max u v} p.asIdeal.primeCompl ⋙
          localCohomologyModuleFunctor (Localization p.asIdeal.primeCompl) (i : ℤ)).map
            (homOfLE (hmc.trans hck)).op).hom x = 0)) :
    ∃ m₀ : ℕ, ∀ (m : ℕ) (hm₀m : m₀ ≤ m), ∃ c : ℕ, ∃ hmc : m ≤ c, ∀ (k : ℕ) (hck : c ≤ k),
      ∀ x : (M ⋙ localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).obj (op k),
        ((M ⋙ localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
          (homOfLE (hmc.trans hck)).op).hom x ∈
          LinearMap.ker ((M ⋙ localCohomologyWithSupportInModuleFunctor.{u, v} A T
            (i : ℤ)).map (homOfLE hm₀m).op).hom →
        ((M ⋙ localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
          (homOfLE (hmc.trans hck)).op).hom x = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.6, Tag 0EHV](https://stacks.math.columbia.edu/tag/0EHV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
