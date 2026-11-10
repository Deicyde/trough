---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ModuleMapFlatTargetSituation, AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.exists_closedSubscheme_isZeroAt_of_isZeroAt_of_quasiCompact, AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.exists_closedSubscheme_isZeroAt_locallyOfFinitePresentation_of_isZeroAt_of_quasiCompact, Module.exists_ideal_rTensor_eq_zero_iff_map_eq_bot, AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.fibreMapEqZero_of_mem_closure, AlgebraicGeometry.Space.ModuleMapSituation.isClosedSubspace_zeroSubfunctor_of_isPureRelative, AlgebraicGeometry.Space.ModuleMapSituation.isFinitePresentation_zeroSubfunctor_ι_of_isPureRelative, AlgebraicGeometry.Space.ModuleMapSituation.zeroLocusRepresentation_of_hasProperSupport
statement: formalized
proof: formalized
---

# 77.8 Making a map zero

Section 77.8 of the Stacks Project, [Tag 0CW9](https://stacks.math.columbia.edu/tag/0CW9). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CWA, a situation

[Tag 0CWA](https://stacks.math.columbia.edu/tag/0CWA) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapFlatTargetSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapFlatTargetSituation.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapFlatTargetSituation.lean#L68).

> **Stacks 0CWA.** The standing data of Stacks 0CWA: an affine base `S = Spec R`, an
> algebraic space `X` over `S`, and a map `u : F ⟶ G` of quasi-coherent `𝒪_X`-modules whose
> target is flat over `S`.

```lean
structure ModuleMapFlatTargetSituation [IsAffine S]
```

## Tag 083K, a lemma

[Tag 083K](https://stacks.math.columbia.edu/tag/083K) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.exists_closedSubscheme_isZeroAt_of_isZeroAt_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartMapQuasiCompactTest.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartMapQuasiCompactTest.lean#L273). The attribute's comment: “main clause”.

> **The main clause of Stacks 083K.**
>
> In Situation 0CWA — `S = \Spec(R)` affine, `X` an algebraic space over `S`, `u : ℱ ⟶ 𝒢` a map
> of quasi-coherent `𝒪_X`-modules with `𝒢` flat over `S` — let `T ⟶ S` be a quasi-compact
> morphism of schemes such that the base change `u_T` is zero.  Then there is a closed subscheme
> `Z ⊆ S` such that (a) `T ⟶ S` factors through `Z` and (b) the base change `u_Z` is zero.
>
> The subscheme is `Z = \Spec(\Gamma(S, ⊤)/I)` for `I = \ker(\Gamma(S, ⊤) ⟶ \Gamma(T, ⊤))`, the
> smallest closed subscheme of `S` through which `T ⟶ S` factors; the factorisation is therefore
> `AlgebraicGeometry.Space.exists_hom_specQuotientOver` at an equality of ideals.  That `I` kills
> the image of `u` over every affine chart is
> `val_app_mem_ker_smul_top_of_isZeroAt_of_quasiCompact`,
> and
> `AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.isZeroAt_specQuotient_of_forall_mem_smul_top`
> turns that into `u_Z = 0`.

```lean
theorem exists_closedSubscheme_isZeroAt_of_isZeroAt_of_quasiCompact (T : BigFppfOver B S hS)
    (hqc : QuasiCompact (B.inclusion.map T.hom))
    (hzero : (D.toModuleMapSituation B S hS).IsZeroAt (modulePullbackSystem B S hS)
      (D.baseTest B S hS T)) :
    ∃ Z : BigFppfOver B S hS,
      _root_.AlgebraicGeometry.IsClosedImmersion (B.inclusion.map Z.hom) ∧ Nonempty (T ⟶ Z) ∧
        (D.toModuleMapSituation B S hS).IsZeroAt (modulePullbackSystem B S hS)
          (D.baseTest B S hS Z)
```

**`AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.exists_closedSubscheme_isZeroAt_locallyOfFinitePresentation_of_isZeroAt_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartMapQuasiCompactTest.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartMapQuasiCompactTest.lean#L349). The attribute's comment: “finite presentation clause”.

> **The finite-presentation clause of Stacks 083K, in the shape the source states it.**
>
> In Situation 0CWA, assume in addition that `ℱ` is a finite type `𝒪_X`-module whose scheme
> theoretic support is quasi-compact, and let `T ⟶ S` be a quasi-compact morphism of schemes such
> that the base change `u_T` is zero.  Then there is a closed subscheme `Z ⊆ S`, locally of finite
> presentation over `S` — and affine, hence quasi-compact and quasi-separated, so of finite
> presentation — through which `T ⟶ S` factors and at which `u_Z = 0`.
>
> This is
> `exists_fg_ideal_isZeroAt_specQuotient_of_quasiCompact`
> with `Z = \Spec(\Gamma(S, ⊤)/J)`, whose closed immersion into `S` is
> `AlgebraicGeometry.Space.isClosedImmersion_specQuotientToBase`.

```lean
theorem exists_closedSubscheme_isZeroAt_locallyOfFinitePresentation_of_isZeroAt_of_quasiCompact
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hcpt : CompactSpace (points B S hS (schemeTheoreticSupport B S hS D.X D.F).toFunctor))
    (T : BigFppfOver B S hS) (hqc : QuasiCompact (B.inclusion.map T.hom))
    (hzero : (D.toModuleMapSituation B S hS).IsZeroAt (modulePullbackSystem B S hS)
      (D.baseTest B S hS T)) :
    ∃ Z : BigFppfOver B S hS,
      _root_.AlgebraicGeometry.IsClosedImmersion (B.inclusion.map Z.hom) ∧
        LocallyOfFinitePresentation (B.inclusion.map Z.hom) ∧ Nonempty (T ⟶ Z) ∧
        (D.toModuleMapSituation B S hS).IsZeroAt (modulePullbackSystem B S hS)
          (D.baseTest B S hS Z)
```

## Tag 083L, a lemma

[Tag 083L](https://stacks.math.columbia.edu/tag/083L) in the Stacks Project.

**`Module.exists_ideal_rTensor_eq_zero_iff_map_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/VanishingAfterBaseChange.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/VanishingAfterBaseChange.lean#L48).

> **Stacks Project, Tag 083L.** If the target of a linear map is projective, the base
> changes on which the map vanishes are cut out by an ideal of the base ring.

```lean
theorem exists_ideal_rTensor_eq_zero_iff_map_eq_bot
    {A : Type u} [CommRing A]
    {M : Type v} [AddCommGroup M] [Module A M]
    {N : Type w} [AddCommGroup N] [Module A N]
    (f : M →ₗ[A] N) (hN : Module.Projective A N) :
    ∃ I : Ideal A, ∀ (B : Type x) [CommRing B] (φ : A →+* B),
      letI := φ.toAlgebra
      f.rTensor B = 0 ↔ Ideal.map φ I = ⊥
```

## Tag 0CWB, a lemma

[Tag 0CWB](https://stacks.math.columbia.edu/tag/0CWB) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapFlatTargetSituation.fibreMapEqZero_of_mem_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapVanishingAlongClosureProjective.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapVanishingAlongClosureProjective.lean#L231).

> In Situation 0CWA, let `T` be a subset of the base and let `s` be a point of the closure of
> `T`.  If `X` is locally of finite presentation over the base, `𝒢` is of finite presentation, and
> `u_t = 0` for every `t ∈ T`, then `u_s = 0`.
>
> The geometric reduction is
> `ModuleMapFlatTargetSituation.fibreMapEqZero_of_mem_closure_of_forall_point`, which asks for one
> affine étale chart per point of `|X|` at which the ideal condition passes from `T` to `s`.  The
> chart is produced by Stacks 0CVY,
> `AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_of_isFlatOverAt`,
> whose three hypotheses are discharged from the two finite-presentation hypotheses and the
> flatness carried by Situation 0CWA; the ideal condition at the chart it returns is
> `ModuleMapFlatTargetSituation.forall_mem_basePointIdeal_smul_top_of_projective_pullback`.
> See the implementation notes of this file.

```lean
theorem fibreMapEqZero_of_mem_closure
    (hfp : IsLocallyOfFinitePresentation B S hS (D.structureMorphism B S hS).hom)
    (hGfp : SheafOfModules.IsFinitePresentationOnSite D.G)
    (T : Set S) (s : S) (hs : s ∈ closure T)
    (hT : ∀ t ∈ T, D.FibreMapEqZero B S hS t) :
    D.FibreMapEqZero B S hS s
```

## Tag 0CWC, a lemma

[Tag 0CWC](https://stacks.math.columbia.edu/tag/0CWC) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isClosedSubspace_zeroSubfunctor_of_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroLocusClosedUnconditional.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZeroLocusClosedUnconditional.lean#L72). The attribute's comment: “closed immersion: the vanishing locus is a closed subspace of the base, at the source's hypotheses alone”.

> **Stacks 0CWC, the closed-immersion clause.**  In Situation 083F, assume (1) `f` is of finite
> presentation and (2) `𝒢` is of finite presentation, flat over the base and pure relative to it.
> Then the vanishing locus of `u` is a closed subspace of the base.
>
> The hypotheses are the source's, and only those: purity relative to the base is stated on the
> situation of Stacks 0CV6 whose finite-type and decency conditions are *derived* from (1) and
> (2) by `fpTargetPrePureSituation`, as the source does implicitly.

```lean
theorem isClosedSubspace_zeroSubfunctor_of_isPureRelative (D : ModuleMapSituation.{u, u} B S hS)
    (hf : IsFinitePresentation B S hS D.f.hom)
    (hGfp : SheafOfModules.IsFinitePresentationOnSite D.G)
    (hGflat : _root_.AlgebraicGeometry.Space.IsFlatOver B S hS D.X.2 D.f.hom D.G)
    (hpure : ∀ y : points B S hS D.Y.1, IsPureRelative (D.fpTargetPrePureSituation hf hGfp y)) :
    IsClosedSubspace B S hS D.zeroSubfunctor
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isFinitePresentation_zeroSubfunctor_ι_of_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroLocusClosedUnconditional.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZeroLocusClosedUnconditional.lean#L88). The attribute's comment: “finite presentation: the vanishing locus is of finite presentation over the base when the source module is of finite type, at the source's hypotheses alone”.

> **Stacks 0CWC, the finite-presentation clause.**  Under the hypotheses of
> `isClosedSubspace_zeroSubfunctor_of_isPureRelative`, if moreover `ℱ` is of finite type, the
> vanishing locus of `u` is of finite presentation over the base.

```lean
theorem isFinitePresentation_zeroSubfunctor_ι_of_isPureRelative
    (D : ModuleMapSituation.{u, u} B S hS)
    (hf : IsFinitePresentation B S hS D.f.hom)
    (hGfp : SheafOfModules.IsFinitePresentationOnSite D.G)
    (hGflat : _root_.AlgebraicGeometry.Space.IsFlatOver B S hS D.X.2 D.f.hom D.G)
    (hpure : ∀ y : points B S hS D.Y.1, IsPureRelative (D.fpTargetPrePureSituation hf hGfp y))
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F) :
    IsFinitePresentation B S hS D.zeroSubfunctor.ι
```

## Tag 083M, a lemma

[Tag 083M](https://stacks.math.columbia.edu/tag/083M) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.zeroLocusRepresentation_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroLocusClosedProperSupportUnconditional.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZeroLocusClosedProperSupportUnconditional.lean#L369). The attribute's comment: “every case: f locally of finite presentation (which includes the case of the first paragraph of the proof, f of finite presentation), G of finite presentation and flat over B, the support of G proper over B; F_zero is represented by a closed subspace of B, of finite presentation over B when F is of finite type -- at the source's hypotheses alone”.

> **Stacks 083M.**  In Situation 083F, assume that
> 1. `f` is locally of finite presentation,
> 2. `𝒢` is an `𝒪_X`-module of finite presentation flat over `B`,
> 3. the support of `𝒢` is proper over `B`.
>
> Then the functor `F_zero` is an algebraic space and `F_zero ⟶ B` is a closed immersion; if `ℱ`
> is of finite type, then `F_zero ⟶ B` is of finite presentation.
>
> The conclusion `AlgebraicGeometry.Space.ModuleMapSituation.ZeroLocusRepresentation` is the
> existence of a subfunctor `Z` of `B` which is a closed subspace (an algebraic space whose
> inclusion is a closed immersion), whose inclusion is of finite presentation when `ℱ` is of finite
> type, and which represents `F_zero`.  The hypotheses are exactly the source's.
>
> The proof is the source's: pass to the closed subspace cut out by the zeroth Fitting ideal of
> `𝒢` (`AlgebraicGeometry.Space.ModuleMapSituation.nonempty_fittingReduction`) and apply Stacks
> 0CWC there, whose dévissage is `AlgebraicGeometry.Space.ModuleMapSituation.devissageInput`.  The
> case of the first paragraph of the proof, `f` of finite presentation, is the special case of a
> morphism of finite presentation, which is in particular locally of finite presentation.

```lean
theorem zeroLocusRepresentation_of_hasProperSupport (D : ModuleMapSituation.{u, u} B S hS)
    (hf : IsLocallyOfFinitePresentation B S hS D.f.hom)
    (hGfp : SheafOfModules.IsFinitePresentationOnSite D.G)
    (hGflat : IsFlatOver B S hS D.X.property D.f.hom D.G)
    (hproper : HasProperSupport B S hS D.X.property D.Y.property D.f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf)
      ((SheafOfModules.toSheaf _).obj D.G)) :
    D.ZeroLocusRepresentation
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.8, Tag 0CW9](https://stacks.math.columbia.edu/tag/0CW9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
