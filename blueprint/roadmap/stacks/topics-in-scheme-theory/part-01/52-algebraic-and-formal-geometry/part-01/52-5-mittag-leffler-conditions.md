---
declaration: section
origin: cited
lean: Stacks.Algebraization.isArtinian_homology_puncturedSpectrumDerivedSections, Stacks.LocalCohomology.isArtinian_localCohomology_maximalIdeal, Stacks.Algebraization.isMittagLefflerCategorical_puncturedSpectrumCohomologySystem, Stacks.LocalCohomology.isMittagLeffler_localCohomology, Stacks.LocalCohomology.isEssentiallyConstantInverseSystem_localCohomology, Stacks.LocalCohomology.isIso_completedLocalCohomologyToLimit, Stacks.LocalCohomology.isIso_completedLocalCohomologyToLimit_derivedCompletion, Stacks.LocalCohomology.completedLocalCohomologyDerivedCompletionIsoLimit
statement: formalized
proof: formalized
---

# 52.5 Mittag-Leffler conditions

Section 52.5 of the Stacks Project, [Tag 0EFN](https://stacks.math.columbia.edu/tag/0EFN). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DX0, a lemma

[Tag 0DX0](https://stacks.math.columbia.edu/tag/0DX0) in the Stacks Project.

**`Stacks.Algebraization.isArtinian_homology_puncturedSpectrumDerivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCohomologyMittagLeffler.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCohomologyMittagLeffler.lean#L332). The attribute's comment: “part (2), for the derived sections of the punctured spectrum read as a ringed space”.

> **Stacks Project, Tag 0DX0, part (2).** Let `(A, 𝔪)` be a Noetherian local ring, let
> `U = Spec A ∖ {𝔪}` be its punctured spectrum and let `ℱ` be a coherent `𝒪_U`-module. Then the
> `A`-module `Hⁱ(U, ℱ)` satisfies the descending chain condition for every `i > 0`.
>
> As in the source this comes from part (1) through Local Cohomology, Lemma [Stacks, Tag 0BK0]: the
> coherent module `ℱ` is `M̃|_U` for a finite `A`-module `M`, the cohomology of `M̃` on the open
> `Spec A ∖ V(𝔪)` of the ambient affine scheme computes `Hⁱ(U, ℱ)` by [Stacks, Tag 01E1] (2), and
> in positive degrees that module is the local cohomology `H^{i+1}_𝔪(M)`, which is Artinian by part
> (1). See the module documentation for the chain of identifications.

```lean
theorem isArtinian_homology_puncturedSpectrumDerivedSections [IsNoetherianRing A]
    (F : SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A)))
    [hFc : SheafOfModules.IsCoherent F] (p : ℕ) (hp : 1 ≤ p) :
    IsArtinian A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (p : ℤ)).obj
      ((puncturedSpectrumDerivedSections A).obj
        ((DerivedCategory.singleFunctor (SheafOfModules.{u}
          (structureSheafRing (puncturedSpectrumRingedSpace A))) 0).obj F)))
```

**`Stacks.LocalCohomology.isArtinian_localCohomology_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ArtinianOverLocalRing.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ArtinianOverLocalRing.lean#L520). The attribute's comment: “part (1)”.

> Local cohomology of a finite module over a Noetherian local ring has the
> descending chain condition in every degree.

```lean
public theorem isArtinian_localCohomology_maximalIdeal
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (M : ModuleCat.{w} A) [Module.Finite A M] (i : ℤ) :
    IsArtinian A
      ((DerivedCategory.homologyFunctor (ModuleCat.{w} A) i).obj
        ((Dualizing.derivedPowerTorsionProperty A (IsLocalRing.maximalIdeal A)
          (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing).ι.obj
          ((Dualizing.localCohomologyFunctor A (IsLocalRing.maximalIdeal A)
            (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing).obj
            ((DerivedCategory.singleFunctor (ModuleCat.{w} A) 0).obj M))))
```

## Tag 0DX1, a lemma

[Tag 0DX1](https://stacks.math.columbia.edu/tag/0DX1) in the Stacks Project.

**`Stacks.Algebraization.isMittagLefflerCategorical_puncturedSpectrumCohomologySystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCohomologyMittagLeffler.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCohomologyMittagLeffler.lean#L397). The attribute's comment: “part (2), for the derived sections of the punctured spectrum read as a ringed space”.

> **Stacks Project, Tag 0DX1, part (2).** Let `(A, 𝔪)` be a Noetherian local ring and let
> `U = Spec A ∖ {𝔪}` be its punctured spectrum. Let `(ℱₙ)` be an inverse system of coherent
> `𝒪_U`-modules. Then for every `i > 0` the inverse system of `A`-modules `n ↦ Hⁱ(U, ℱₙ)` satisfies
> the Mittag-Leffler condition.
>
> As in the source this follows immediately from part (2) of [Stacks, Tag 0DX0]: each term of the
> system has the descending chain condition, so the images of the transition maps into a fixed term
> are eventually constant. No compatibility between the modules realizing the `ℱₙ` is needed,
> because the Mittag-Leffler condition is a statement about one term at a time.

```lean
theorem isMittagLefflerCategorical_puncturedSpectrumCohomologySystem [IsNoetherianRing A]
    (S : ℕᵒᵖ ⥤ SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A)))
    (hScoherent : ∀ n : ℕᵒᵖ, SheafOfModules.IsCoherent (S.obj n))
    (p : ℕ) (hp : 1 ≤ p) :
    IsMittagLefflerCategorical (puncturedSpectrumCohomologySystem A S (p : ℤ))
```

**`Stacks.LocalCohomology.isMittagLeffler_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/MittagLefflerSystems.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/MittagLefflerSystems.lean#L76). The attribute's comment: “local_cohomology_system”.

> **Stacks Project, Tag 0DX1.** Over a Noetherian local ring, the local cohomology modules of
> an inverse system of finite modules satisfy the Mittag-Leffler condition in every degree.

```lean
public theorem isMittagLeffler_localCohomology
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (M : ℕᵒᵖ ⥤ ModuleCat.{v} A) (hM : ∀ n, Module.Finite A (M.obj n)) (i : ℤ) :
    IsMittagLefflerCategorical
      (M ⋙ DerivedCategory.singleFunctor (ModuleCat.{v} A) 0 ⋙
        Dualizing.localCohomologyFunctor A (IsLocalRing.maximalIdeal A)
          (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing ⋙
        (Dualizing.derivedPowerTorsionProperty A (IsLocalRing.maximalIdeal A)
          (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing).ι ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{v} A) i)
```

## Tag 0EHB, a lemma

[Tag 0EHB](https://stacks.math.columbia.edu/tag/0EHB) in the Stacks Project.

**`Stacks.LocalCohomology.isEssentiallyConstantInverseSystem_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantSystem.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantSystem.lean#L519).

> **Stacks 0EHB.** If the canonical map from the local cohomology of a finite
> module to the inverse limit of the local cohomology of a countable inverse
> system of finite modules is an isomorphism, that local cohomology system is
> essentially constant.

```lean
public theorem isEssentiallyConstantInverseSystem_localCohomology
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (F : CategoryTheory.Functor ℕᵒᵖ (ModuleCat.{v} A))
    (hF : ∀ n, Module.Finite A (F.obj n))
    (M : ModuleCat.{v} A) [Module.Finite A M] (i : ℤ)
    [HasLimit F] [HasLimit (F ⋙ localCohomologyModuleFunctor A i)]
    (f : M ⟶ limit F)
    (_ : IsIso ((localCohomologyModuleFunctor A i).map f ≫
      limit.post F (localCohomologyModuleFunctor A i))) :
    CategoryTheory.IsEssentiallyConstantInverseSystem
      (F ⋙ localCohomologyModuleFunctor A i)
```

## Tag 0DXJ, a lemma

[Tag 0DXJ](https://stacks.math.columbia.edu/tag/0DXJ) in the Stacks Project.

**`Stacks.LocalCohomology.isIso_completedLocalCohomologyToLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean#L178). The attribute's comment: “for a derived limit of the tower of local cohomologies of the adic quotients”.

> **Stacks Project, Tag 0DXJ.** Let `(A, 𝔪)` be a Noetherian local ring, let `I ⊆ A` be an
> ideal and let `M` be a finite `A`-module. For every `i`, the comparison map from the degree-`i`
> cohomology of a derived limit of the tower `n ↦ RΓ_𝔪(M/IⁿM)` to the inverse limit of the local
> cohomology modules `Hⁱ_𝔪(M/IⁿM)` is an isomorphism: the `R¹lim` term of the Milnor short exact
> sequence vanishes because the system `n ↦ H^{i-1}_𝔪(M/IⁿM)` is Mittag-Leffler.

```lean
theorem isIso_completedLocalCohomologyToLimit
    [IsLocalRing A] [IsNoetherianRing A] (I : Ideal A) (M : ModuleCat.{u} A)
    [Module.Finite A M] (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsDerivedLimit (Dualizing.adicQuotientLocalCohomologySystem A I
      (IsLocalRing.maximalIdeal A) (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M) K)
    (i : ℤ) :
    IsIso (Dualizing.completedLocalCohomologyToLimit A I (IsLocalRing.maximalIdeal A)
      (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M K hK i)
```

**`Stacks.LocalCohomology.isIso_completedLocalCohomologyToLimit_derivedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean#L214).

> **Stacks Project, Tag 0DXJ, for the derived `I`-adic completion.** Let `(A, 𝔪)` be a
> Noetherian local ring, let `I ⊆ A` be an ideal and let `M` be a finite `A`-module. For every
> `i` the comparison map `Hⁱ(RΓ_𝔪(M)^∧) ⟶ lim Hⁱ_𝔪(M/IⁿM)` is an isomorphism.
>
> Tag 0EEW part (1), `Dualizing.isDerivedLimit_completedLocalCohomology`, identifies the derived
> `I`-adic completion of `RΓ_𝔪(M)` with a derived limit of the tower `n ↦ RΓ_𝔪(M/IⁿM)`; feeding
> that identification into `isIso_completedLocalCohomologyToLimit` transports the conclusion from
> an abstract derived limit to the completion itself.

```lean
theorem isIso_completedLocalCohomologyToLimit_derivedCompletion
    [IsLocalRing A] [IsNoetherianRing A] (I : Ideal A) (M : ModuleCat.{u} A)
    [Module.Finite A M] (i : ℤ) :
    IsIso (Dualizing.completedLocalCohomologyToLimit A I (IsLocalRing.maximalIdeal A)
      (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M
      (Dualizing.completedLocalCohomology A I (IsLocalRing.maximalIdeal A)
        I.fg_of_isNoetherianRing (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M)
      (Dualizing.isDerivedLimit_completedLocalCohomology A I (IsLocalRing.maximalIdeal A)
        I.fg_of_isNoetherianRing (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M) i)
```

**`Stacks.LocalCohomology.completedLocalCohomologyDerivedCompletionIsoLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean#L232).

> **Stacks Project, Tag 0DXJ.** For a finite module `M` over a Noetherian local ring
> `(A, 𝔪)` and an ideal `I ⊆ A`, the degree-`i` cohomology of the derived `I`-adic completion
> `RΓ_𝔪(M)^∧` is isomorphic to the inverse limit of the local cohomology modules
> `Hⁱ_𝔪(M/IⁿM)`, for every `i`. This is the equality `Hⁱ(RΓ_𝔪(M)^∧) = lim Hⁱ_𝔪(M/IⁿM)` of the
> tag, realized by the comparison map
> `Dualizing.completedLocalCohomologyToLimit`.

```lean
def completedLocalCohomologyDerivedCompletionIsoLimit [IsLocalRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : ModuleCat.{u} A) [Module.Finite A M] (i : ℤ) :
    (DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
        (Dualizing.completedLocalCohomology A I (IsLocalRing.maximalIdeal A)
          I.fg_of_isNoetherianRing (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M) ≅
      limit (Dualizing.adicQuotientLocalCohomologySystem A I (IsLocalRing.maximalIdeal A)
          (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} A) i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.5, Tag 0EFN](https://stacks.math.columbia.edu/tag/0EFN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
