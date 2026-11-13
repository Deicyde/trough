---
declaration: section
origin: cited
lean: Dualizing.depth_eq_least_nonzero_homology, Dualizing.isCohenMacaulay_tfae_dualizingComplex, Dualizing.dualizingModule_isMaximalCohenMacaulay, Dualizing.isCohenMacaulayRing_of_dualizingModule, Dualizing.cohenMacaulayLocus_subset_support, Dualizing.isOpen_cohenMacaulayLocus, Dualizing.dense_cohenMacaulayLocus, Dualizing.isOpen_and_dense_setOf_isMaximalCohenMacaulay_of_isDualizingComplex
statement: formalized
proof: formalized
---

# 47.20 Cohen-Macaulay rings

Section 47.20 of the Stacks Project, [Tag 0DW4](https://stacks.math.columbia.edu/tag/0DW4). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AWR, a lemma

[Tag 0AWR](https://stacks.math.columbia.edu/tag/0AWR) in the Stacks Project.

**`Dualizing.depth_eq_least_nonzero_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean#L303).

> **Stacks Project, Tag 0AWR.** The depth of a Noetherian local ring `A` with normalized
> dualizing complex `ω_A` is the least `δ ≥ 0` with `H^{-δ}(ω_A) ≠ 0`.

```lean
public theorem depth_eq_least_nonzero_homology {A : Type u} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsNormalizedDualizingComplex.{u, 0} K) :
    ∃ δ : ℕ,
      IsLeast
          {i : ℕ |
            ¬ IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(i : ℤ))).obj K)}
          δ ∧
        Module.depth A (IsLocalRing.maximalIdeal A) A = (δ : ℕ∞)
```

## Tag 0AWS, a lemma

[Tag 0AWS](https://stacks.math.columbia.edu/tag/0AWS) in the Stacks Project.

**`Dualizing.isCohenMacaulay_tfae_dualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean#L484). The attribute's comment: “equivalent conditions (1)--(3)”.

> **Stacks Project, Tag 0AWS, equivalent conditions (1)--(3).** A Noetherian local ring is
> Cohen--Macaulay exactly when its normalized dualizing complex is concentrated in one degree,
> and exactly when it is its dualizing module placed in degree minus the dimension.

```lean
public theorem isCohenMacaulay_tfae_dualizingComplex {A : Type u} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsNormalizedDualizingComplex.{u, 0} K) :
    List.TFAE
      [ IsCohenMacaulayLocalRing A,
        IsCohomologicallyConcentratedInOneDegree K,
        Nonempty
          (K ≅
            (DerivedCategory.singleFunctor (ModuleCat.{u} A)
              (-(localRingDimension A : ℤ))).obj (dualizingModule K)) ]
```

**`Dualizing.dualizingModule_isMaximalCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean#L551). The attribute's comment: “the dualizing module is maximal Cohen--Macaulay”.

> **Stacks Project, Tag 0AWS, final assertion.** Over a Cohen--Macaulay local ring, the
> dualizing module of a normalized dualizing complex is maximal Cohen--Macaulay.

```lean
public theorem dualizingModule_isMaximalCohenMacaulay {A : Type u} [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsNormalizedDualizingComplex.{u, 0} K)
    (hA : IsCohenMacaulayLocalRing A) :
    Module.IsMaximalCohenMacaulay A (dualizingModule K)
```

## Tag 0DW5, a lemma

[Tag 0DW5](https://stacks.math.columbia.edu/tag/0DW5) in the Stacks Project.

**`Dualizing.isCohenMacaulayRing_of_dualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayFromModule.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayFromModule.lean#L180).

> **Stacks Project, Tag 0DW5.** A Noetherian ring admitting a finite module whose degree-zero
> complex is a dualizing complex is Cohen--Macaulay.

```lean
theorem isCohenMacaulayRing_of_dualizingModule {A : Type u} [CommRing A] [IsNoetherianRing A]
    (omega : ModuleCat.{max u v} A) [Module.Finite A omega]
    (homega : IsDualizingComplex
      ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj omega)) :
    IsCohenMacaulayRing A
```

## Tag 0EHS, a lemma

[Tag 0EHS](https://stacks.math.columbia.edu/tag/0EHS) in the Stacks Project.

**`Dualizing.cohenMacaulayLocus_subset_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean, line 929](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean#L929). The attribute's comment: “the locus is contained in the support”.

> A Cohen--Macaulay localization of a module is nonzero, so its prime lies in the support.

```lean
public theorem cohenMacaulayLocus_subset_support
    {A : Type u} [CommRing A]
    {M : Type v} [AddCommGroup M] [Module A M] :
    {p : PrimeSpectrum A |
      Module.IsCohenMacaulayAtMaximalIdeal (Localization.AtPrime p.asIdeal)
        (LocalizedModule.AtPrime p.asIdeal M)} ⊆ Module.support A M
```

**`Dualizing.isOpen_cohenMacaulayLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean, line 955](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean#L955). The attribute's comment: “relative openness”.

> **Stacks Project, Tag 0EHS, openness.** The Cohen--Macaulay locus of a finite module over a
> Noetherian ring with a dualizing complex is open in the support of the module.

```lean
public theorem isOpen_cohenMacaulayLocus
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (ω : DerivedCategory (ModuleCat.{w} A)) (hω : Dualizing.IsDualizingComplex ω) :
    IsOpen {p : ↥(Module.support A M) |
      Module.IsCohenMacaulayAtMaximalIdeal (Localization.AtPrime p.1.asIdeal)
        (LocalizedModule.AtPrime p.1.asIdeal M)}
```

**`Dualizing.dense_cohenMacaulayLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayRings.lean#L1010). The attribute's comment: “density”.

> **Stacks Project, Tag 0EHS, density.** The Cohen--Macaulay locus of a finite module over a
> Noetherian ring is dense in the support of the module.

```lean
public theorem dense_cohenMacaulayLocus
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M] :
    Dense {p : ↥(Module.support A M) |
      Module.IsCohenMacaulayAtMaximalIdeal (Localization.AtPrime p.1.asIdeal)
        (LocalizedModule.AtPrime p.1.asIdeal M)}
```

## Tag 0EHT, a lemma

[Tag 0EHT](https://stacks.math.columbia.edu/tag/0EHT) in the Stacks Project.

**`Dualizing.isOpen_and_dense_setOf_isMaximalCohenMacaulay_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/CohenMacaulayLocus.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/CohenMacaulayLocus.lean#L320).

> **Stacks Project, Tag 0EHT.** For a Noetherian ring with a dualizing complex, the set of
> primes at which the local ring is Cohen--Macaulay is a dense open subset of the spectrum.

```lean
theorem isOpen_and_dense_setOf_isMaximalCohenMacaulay_of_isDualizingComplex
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (omega : DerivedCategory (ModuleCat.{max u v} A)) (homega : IsDualizingComplex omega) :
    IsOpen {q : PrimeSpectrum A | Module.IsMaximalCohenMacaulay
        (Localization.AtPrime q.asIdeal) (Localization.AtPrime q.asIdeal)} ∧
      Dense {q : PrimeSpectrum A | Module.IsMaximalCohenMacaulay
        (Localization.AtPrime q.asIdeal) (Localization.AtPrime q.asIdeal)}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.20, Tag 0DW4](https://stacks.math.columbia.edu/tag/0DW4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
