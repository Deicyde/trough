---
declaration: section
origin: cited
lean: Stacks.UniversalInjectivity.finite_maximalSpectrum_localization_nonZeroSMulDivisors, Stacks.UniversalInjectivity.range_under_localization_nonZeroSMulDivisors, Stacks.UniversalInjectivity.exists_assStacks_closedFibre_of_isMaximal_localization, Stacks.UniversalInjectivity.universallyInjectivePoly_lsmul_of_nonZeroSMulDivisors, Stacks.UniversalInjectivity.universallyInjectivePoly_mkLinearMap_nonZeroSMulDivisors, Stacks.UniversalInjectivity.universallyInjectivePoly_tensorUnit_of_flat, Stacks.UniversalInjectivity.universallyInjective_baseChange_of_flat, Module.Flat.rTensor_injective_of_projective_of_mem_maximalIdeal_smul_top
statement: formalized
proof: formalized
---

# 38.7 Localization and universally injective maps

Section 38.7 of the Stacks Project, [Tag 05DD](https://stacks.math.columbia.edu/tag/05DD). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05DE, a lemma

[Tag 05DE](https://stacks.math.columbia.edu/tag/05DE) in the Stacks Project.

**`Stacks.UniversalInjectivity.finite_maximalSpectrum_localization_nonZeroSMulDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean#L267). The attribute's comment: “semilocality; the multiplicative subset is `nonZeroSMulDivisors`”.

> Localizing at the elements regular on a finite module over the Noetherian closed fibre of a
> local base produces a semilocal ring.

```lean
theorem finite_maximalSpectrum_localization_nonZeroSMulDivisors : Finite (MaximalSpectrum T)
```

**`Stacks.UniversalInjectivity.range_under_localization_nonZeroSMulDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean#L285). The attribute's comment: “the prime spectrum”.

> The contractions of the primes of the localization are exactly the primes of `S` contained
> in an associated prime of the closed-fibre module.

```lean
theorem range_under_localization_nonZeroSMulDivisors :
    Set.range (fun q : PrimeSpectrum T ↦ q.asIdeal.under S) =
      {q : Ideal S | q.IsPrime ∧
        ∃ p ∈ assStacks S
          (N ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S N))), q ≤ p}
```

**`Stacks.UniversalInjectivity.exists_assStacks_closedFibre_of_isMaximal_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean#L302). The attribute's comment: “the maximal ideals”.

> Every maximal ideal of the localization corresponds to an associated prime of the
> closed-fibre module over the closed-fibre ring, whose contraction to `S` is the maximal ideal's.

```lean
theorem exists_assStacks_closedFibre_of_isMaximal_localization (q : MaximalSpectrum T) :
    ∃ p ∈ assStacks (S ⧸ Ideal.map (algebraMap R S) (maximalIdeal R))
      (N ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S N))),
      p.comap (Ideal.Quotient.mk (Ideal.map (algebraMap R S) (maximalIdeal R))) =
        q.asIdeal.under S
```

## Tag 05DF, a lemma

[Tag 05DF](https://stacks.math.columbia.edu/tag/05DF) in the Stacks Project.

**`Stacks.UniversalInjectivity.universallyInjectivePoly_lsmul_of_nonZeroSMulDivisors`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean#L363). The attribute's comment: “the homotheties”.

> Every element acting injectively on the closed fibre defines a universally injective
> `R`-linear homothety of `N`.

```lean
lemma universallyInjectivePoly_lsmul_of_nonZeroSMulDivisors
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation)
    (s : nonZeroSMulDivisors S
      (N ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S N)))) :
    UniversallyInjectivePoly (((LinearMap.lsmul S N) s.1).restrictScalars R)
```

**`Stacks.UniversalInjectivity.universallyInjectivePoly_mkLinearMap_nonZeroSMulDivisors`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean#L376). The attribute's comment: “the localization map”.

> The canonical map from `N` to its localization at the elements acting injectively on the
> closed fibre is universally injective over `R`.

```lean
lemma universallyInjectivePoly_mkLinearMap_nonZeroSMulDivisors
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation) :
    UniversallyInjectivePoly
      ((LocalizedModule.mkLinearMap
        (nonZeroSMulDivisors S
          (N ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) •
            (⊤ : Submodule S N)))) N).restrictScalars R)
```

## Tag 05DG, a lemma

[Tag 05DG](https://stacks.math.columbia.edu/tag/05DG) in the Stacks Project.

**`Stacks.UniversalInjectivity.universallyInjectivePoly_tensorUnit_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChange.lean#L494).

> Let `R → S` be a local homomorphism of local rings, essentially of finite presentation, let
> `N` be a finitely presented `S`-module which is flat over `R`, and let `S → S'` be flat. If the
> image of `Spec(S') → Spec(S)` contains every prime of `S` lying over the maximal ideal of `R`
> which is an associated prime of the closed fibre `N / 𝔪_R N`, then the canonical map
> `N → N ⊗[S] S'` is universally injective over `R`.

```lean
theorem universallyInjectivePoly_tensorUnit_of_flat {R : Type u} {S : Type v} {S' : Type w}
    {N : Type x} [CommRing R] [CommRing S] [CommRing S'] [IsLocalRing R] [IsLocalRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)] [Algebra S S']
    [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.FinitePresentation S N] [Module.Flat R N] [Module.Flat S S']
    (hS : (algebraMap R S).EssentiallyOfFinitePresentation)
    (hspec : ∀ q : Ideal S, Ideal.comap (algebraMap R S) q = maximalIdeal R →
      IsAssociatedPrimeStacks S
        (N ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S N))) q →
      ∃ q' : Ideal S', q'.IsPrime ∧ Ideal.comap (algebraMap S S') q' = q) :
    UniversallyInjectivePoly (((TensorProduct.mk S N S').flip 1).restrictScalars R)
```

## Tag 05DH, a lemma

[Tag 05DH](https://stacks.math.columbia.edu/tag/05DH) in the Stacks Project.

**`Stacks.UniversalInjectivity.universallyInjective_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChangeFlat.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/UniversallyInjectiveBaseChangeFlat.lean#L589).

> **Stacks 05DH.** Under the stated finite-presentation and flatness hypotheses, if every
> associated prime of each fibre of `N` lifts to `S'`, then the canonical base-change map
> `N → N ⊗[S] S'` is universally injective over `R`.

```lean
theorem universallyInjective_baseChange_of_flat
    {R : Type u} {S : Type v} {S' N : Type w}
    [CommRing R] [CommRing S] [CommRing S']
    [AddCommGroup N] [Module S N] [Algebra R S] [Algebra S S']
    [Module R N] [IsScalarTower R S N] [Algebra R S'] [IsScalarTower R S S']
    [Algebra.FinitePresentation R S] [Module.FinitePresentation S N]
    [Module.Flat R N] [Module.Flat S S']
    (himage : ∀ (q : Ideal S) [q.IsPrime],
      IsAssociatedPrimeStacks S (N ⊗[R] (q.under R).ResidueField) q →
        ∃ q' : Ideal S', q'.IsPrime ∧ q'.under S = q) :
    UniversallyInjective
      (((TensorProduct.mk S N S').flip 1).restrictScalars R)
```

## Tag 05FQ, a lemma

[Tag 05FQ](https://stacks.math.columbia.edu/tag/05FQ) in the Stacks Project.

**`Module.Flat.rTensor_injective_of_projective_of_mem_maximalIdeal_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/MittagLeffler.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/MittagLeffler.lean#L291). The attribute's comment: “the hypothesis spells out injectivity of `M/𝔪M → N/𝔪N` as `u x ∈ 𝔪 • ⊤ → x ∈ 𝔪 • ⊤`, the form `Submodule.injective_mapQ_smul_top_iff` shows it to be equivalent to; the conclusion spells out universal injectivity, which `Mathlib` has no name for, as in Stacks 0AS5, 05CJ and 05CM.”.

> **Stacks 05FQ.** Let `(R, 𝔪)` be a local ring and let `u : M →ₗ[R] N` be a map of `R`-modules
> with `M` projective and `N` flat. If the reduction `M/𝔪M → N/𝔪N` is injective -- that is, if
> `u x ∈ 𝔪 • ⊤` forces `x ∈ 𝔪 • ⊤` -- then `u` is universally injective, i.e. `u ⊗ id_Q` is
> injective for every `R`-module `Q`.

```lean
public theorem Module.Flat.rTensor_injective_of_projective_of_mem_maximalIdeal_smul_top
    {R : Type u} [CommRing R] [IsLocalRing R] [Small.{v} R] {M N : Type v} [AddCommGroup M]
    [Module R M] [Module.Projective R M] [AddCommGroup N] [Module R N] [Module.Flat R N]
    (u : M →ₗ[R] N)
    (hu : ∀ x : M, u x ∈ maximalIdeal R • (⊤ : Submodule R N) →
      x ∈ maximalIdeal R • (⊤ : Submodule R M)) :
    ∀ (Q : Type v) [AddCommGroup Q] [Module R Q], Function.Injective (u.rTensor Q)
```

**`Module.Flat.rTensor_injective_of_projective_of_injective_mapQ_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/MittagLeffler.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/MittagLeffler.lean#L347). The attribute's comment: “`M/𝔪M` is `M ⧸ 𝔪 • ⊤` and the reduction of `u` is `Submodule.mapQ` along `u`, as in Stacks 0AS5 and 046Y; the conclusion spells out universal injectivity, which `Mathlib` has no name for.”.

> **Stacks 05FQ.** Let `(R, 𝔪)` be a local ring and let `u : M →ₗ[R] N` be a map of `R`-modules
> with `M` projective and `N` flat. If the induced map `M/𝔪M → N/𝔪N` is injective, then `u` is
> universally injective, i.e. `u ⊗ id_Q` is injective for every `R`-module `Q`.

```lean
public theorem Module.Flat.rTensor_injective_of_projective_of_injective_mapQ_maximalIdeal
    {R : Type u} [CommRing R] [IsLocalRing R] [Small.{v} R] {M N : Type v} [AddCommGroup M]
    [Module R M] [Module.Projective R M] [AddCommGroup N] [Module R N] [Module.Flat R N]
    (u : M →ₗ[R] N)
    (hu : Function.Injective ((maximalIdeal R • (⊤ : Submodule R M)).mapQ
      (maximalIdeal R • (⊤ : Submodule R N)) u
      (Submodule.smul_top_le_comap_smul_top (maximalIdeal R) u))) :
    ∀ (Q : Type v) [AddCommGroup Q] [Module R Q], Function.Injective (u.rTensor Q)
```

## Tag 05FR, a lemma

[Tag 05FR](https://stacks.math.columbia.edu/tag/05FR) in the Stacks Project.

**`Stacks.UniversalInjectivity.universallyInjective_lsmul_of_mem_nonZeroSMulDivisors_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/UniversalInjectivity.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/UniversalInjectivity.lean#L54). The attribute's comment: “elementwise_universal_injectivity”.

> **Stacks Project, Tag 05FR.** An element which acts injectively on the closed fibre of a
> projective module acts universally injectively on the module over the local base ring.

```lean
theorem universallyInjective_lsmul_of_mem_nonZeroSMulDivisors_quotient
    {R : Type u} {S : Type v} {N : Type w}
    [CommRing R] [CommRing S] [IsLocalRing R] [Algebra R S]
    [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [IsNoetherianRing
      (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))]
    [Module.Finite
      (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))
      (N ⧸ (Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R) •
        (⊤ : Submodule S N)))]
    [Module.Projective R N]
    {s : S}
    (hs : s ∈ nonZeroSMulDivisors S
      (N ⧸ (Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R) •
        (⊤ : Submodule S N)))) :
    UniversallyInjective ((LinearMap.lsmul S N s).restrictScalars R)
```

**`Stacks.UniversalInjectivity.universallyInjective_localizedModule_mkLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/UniversalInjectivity.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/UniversalInjectivity.lean#L103). The attribute's comment: “localization_universal_injectivity”.

> **Stacks Project, Tag 05FR.** If a module is projective over a local base ring, its
> canonical map to the localization at the elements acting injectively on its closed fibre is
> universally injective over the base.

```lean
theorem universallyInjective_localizedModule_mkLinearMap
    {R : Type u} {S : Type v} {N : Type (max v w)} [CommRing R] [CommRing S] [IsLocalRing R]
    [Algebra R S] [AddCommGroup N] [Module S N] [Module R N] [IsScalarTower R S N]
    [Module.Projective R N]
    [IsNoetherianRing
      (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))]
    [Module.Finite
      (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))
      (N ⧸ (Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R) •
        (⊤ : Submodule S N)))] :
    UniversallyInjective
      ((LocalizedModule.mkLinearMap
        (nonZeroSMulDivisors S
          (N ⧸ (Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R) •
            (⊤ : Submodule S N)))) N).restrictScalars R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.7, Tag 05DD](https://stacks.math.columbia.edu/tag/05DD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
