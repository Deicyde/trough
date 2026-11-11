---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedTensor_and_isIso_baseChange, AlgebraicGeometry.Space.exists_finiteProjective_model_derivedSections, AlgebraicGeometry.Space.isPseudoCoherent_derivedModulePushforward_derivedTensor_and_isIso_baseChange, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_and_isIso_baseChange_of_isFlat, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_single_and_isIso_baseChange, AlgebraicGeometry.Space.isPseudoCoherent_derivedModulePushforward_and_isIso_baseChange, AlgebraicGeometry.Space.isIso_homEquiv_single_limitComparison_baseRingTensorModule_of_isProper, Stacks.Cohomology.SiteModules.isIso_homEquiv_baseRingTensorLimitComparison_iff
statement: formalized
proof: formalized
---

# 75.25 Cohomology and base change, VI

Section 75.25 of the Stacks Project, [Tag 0A1N](https://stacks.math.columbia.edu/tag/0A1N). 8 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A1P, a lemma

[Tag 0A1P](https://stacks.math.columbia.edu/tag/0A1P) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedTensor_and_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeIso.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeIso.lean#L268).

> **Stacks 0A1P.** For `f : X ⟶ Y` of finite presentation, a perfect `E` and a bounded complex
> `𝒢^•` of `𝒪_X`-modules of finite presentation, flat over `Y`, with support proper over `Y`,
> `Rf_*(E ⊗^L 𝒢^•)` is perfect, and its formation commutes with arbitrary base change: for every
> cartesian square, `Lg^*Rf_*(E ⊗^L 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L (g')^*𝒢^•)` is an isomorphism.

```lean
theorem isPerfect_derivedModulePushforward_derivedTensor_and_isIso_baseChange
    (f : X ⟶ Y) (hf : IsFinitePresentation B S hS f.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hGb : {i : ℤ | ¬ IsZero (G.X i)}.Finite) (hGfp : ∀ n, (G.X n).IsFinitePresentation)
    (hGflat : ∀ n, IsFlatOver B S hS X.2 f.hom (G.X n))
    (hGsupp : ∀ n, HasProperSupport B S hS X.2 Y.2 f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf.1)
      ((SheafOfModules.toSheaf _).obj (G.X n))) :
    RingedSite.IsPerfect (smallEtaleRingedSite B S hS Y.1 Y.2)
        ((derivedModulePushforward B S hS f).obj
          (((smallEtaleDerivedTensor B S hS X).obj E).obj (DerivedCategory.Q.obj G))) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedBaseChangeComp B S hS f g f' g' sq.w
          (((smallEtaleDerivedTensor B S hS X).obj E).obj (DerivedCategory.Q.obj G))
          (((smallEtaleDerivedTensor B S hS X').obj
            ((smallEtaleDerivedModulePullback B S hS g').obj E)).obj
            (DerivedCategory.Q.obj (((modulePullback B S hS g').mapHomologicalComplex
              (ComplexShape.up ℤ)).obj G)))
          ((smallEtaleDerivedPullbackTensorIso g').hom.app (E, DerivedCategory.Q.obj G) ≫
            ((smallEtaleDerivedTensor B S hS X').obj
              ((smallEtaleDerivedModulePullback B S hS g').obj E)).map
              (smallEtaleDerivedModulePullbackQComparison g' G)))
```

## Tag 0A1Q, a remark

[Tag 0A1Q](https://stacks.math.columbia.edu/tag/0A1Q) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteProjective_model_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeIso.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeIso.lean#L315).

> **Stacks 0A1Q.** Let `U` have affine underlying scheme `Spec R`, `f : X ⟶ U` of finite
> presentation and `𝒢` an `𝒪_X`-module of finite presentation, flat over `U`, with support proper
> over `U`. There is a bounded complex `M^•` of finite projective `R`-modules (so that
> `M^• ⊗ᴸ_R R' = M^• ⊗_R R'`) and isomorphisms `RΓ(X_{R'}, 𝒢_{R'}) ≅ M^• ⊗ᴸ_R R'`, functorial in the
> `R`-algebra `R' = Γ(U', 𝒪)`: compatible with the pullback maps and the composition law of
> derived extensions of scalars.

```lean
theorem exists_finiteProjective_model_derivedSections
    {U : BigFppfOver B S hS} [IsAffine ((BigFppfOver.toScheme B S hS).obj U)]
    {X : AlgebraicSpaces B S hS} (f : X ⟶ ⟨yoneda.obj U, isAlgebraicSpace_yoneda B S hS U⟩)
    (hf : IsFinitePresentation B S hS f.hom)
    (G : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
    (hGfp : G.IsFinitePresentation) (hGflat : IsFlatOver B S hS X.2 f.hom G)
    (hGsupp : HasProperSupport B S hS X.2 (isAlgebraicSpace_yoneda B S hS U) f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf.1)
      ((SheafOfModules.toSheaf _).obj G)) :
    ∃ (M : CochainComplex (ModuleCat.{u} Γ((BigFppfOver.toScheme B S hS).obj U, ⊤)) ℤ) (a b : ℤ),
      M.IsStrictlyGE a ∧ M.IsStrictlyLE b ∧
      (∀ i, Module.Finite Γ((BigFppfOver.toScheme B S hS).obj U, ⊤) (M.X i)) ∧
      (∀ i, Module.Projective Γ((BigFppfOver.toScheme B S hS).obj U, ⊤) (M.X i)) ∧
      (∀ {U' : BigFppfOver B S hS} [IsAffine ((BigFppfOver.toScheme B S hS).obj U')]
        (g : U' ⟶ U), IsIso ((representedAffineDerivedExtension B S hS g).comparison.app M)) ∧
      ∃ φ : ∀ {U' : BigFppfOver B S hS} [IsAffine ((BigFppfOver.toScheme B S hS).obj U')]
          (g : U' ⟶ U) {X' : AlgebraicSpaces B S hS}
          (f' : X' ⟶ ⟨yoneda.obj U', isAlgebraicSpace_yoneda B S hS U'⟩) (g' : X' ⟶ X),
          IsPullback g' f' f (representedSpaceMap B S hS g) →
          ((representedAffineDerivedSections B S hS U').obj
            ((derivedModulePushforward B S hS f').obj (DerivedCategory.Q.obj
              (((Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
                (X := smallEtaleRingedTopos B S hS _) (Y := smallEtaleRingedTopos B S hS X)
                (smallEtaleRingedToposHom B S hS g').toModulesHom).mapHomologicalComplex
                  (ComplexShape.up ℤ)).obj
                ((HomologicalComplex.single
                  (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
                  (ComplexShape.up ℤ) 0).obj G)))) ≅
            (representedAffineDerivedExtension B S hS g).functor.obj (DerivedCategory.Q.obj M)),
        ∀ {U' U'' : BigFppfOver B S hS} [IsAffine ((BigFppfOver.toScheme B S hS).obj U')]
          [IsAffine ((BigFppfOver.toScheme B S hS).obj U'')] (g : U' ⟶ U) (g₂ : U'' ⟶ U')
          {X' X'' : AlgebraicSpaces B S hS}
          (f' : X' ⟶ ⟨yoneda.obj U', isAlgebraicSpace_yoneda B S hS U'⟩)
          (f'' : X'' ⟶ ⟨yoneda.obj U'', isAlgebraicSpace_yoneda B S hS U''⟩) (g' : X' ⟶ X)
          (g₂' : X'' ⟶ X') (sq : IsPullback g' f' f (representedSpaceMap B S hS g))
          (sq₂ : IsPullback g₂' f'' f' (representedSpaceMap B S hS g₂))
          (sq₃ : IsPullback (g₂' ≫ g') f'' f (representedSpaceMap B S hS (g₂ ≫ g))),
          affineBaseDerivedSectionsPullbackMap B S hS g₂ f' f'' g₂' sq₂.w
              (((Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
                (X := smallEtaleRingedTopos B S hS _) (Y := smallEtaleRingedTopos B S hS X)
                (smallEtaleRingedToposHom B S hS g').toModulesHom).mapHomologicalComplex
                  (ComplexShape.up ℤ)).obj
                ((HomologicalComplex.single
                  (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
                  (ComplexShape.up ℤ) 0).obj G)) ≫
            (representedAffineDerivedSections B S hS U'').map
              ((derivedModulePushforward B S hS f'').map (DerivedCategory.Q.map
                ((NatIso.mapHomologicalComplex (smallEtaleModulePullbackCompIso B S hS g₂' g')
                  (ComplexShape.up ℤ)).hom.app
                  ((HomologicalComplex.single
                    (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X))
                    (ComplexShape.up ℤ) 0).obj G)))) ≫
            (φ (g₂ ≫ g) f'' (g₂' ≫ g') sq₃).hom =
          (representedAffineDerivedExtension B S hS g₂).functor.map (φ g f' g' sq).hom ≫
            (RingTheory.TorIndependence.totalDerivedExtensionScalarsCompOfEq
              (representedAffineCommRingCatHom B S hS g).hom
              (representedAffineCommRingCatHom B S hS g₂).hom
              (representedAffineCommRingCatHom B S hS (g₂ ≫ g)).hom
              (representedAffineRingHom_comp B S hS g₂ g).symm).hom.app
                (DerivedCategory.Q.obj M)
```

## Tag 0CTL, a lemma

[Tag 0CTL](https://stacks.math.columbia.edu/tag/0CTL) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_derivedModulePushforward_derivedTensor_and_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangePseudoCoherentIso.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangePseudoCoherentIso.lean#L43).

> **Stacks 0CTL.** For `f : X ⟶ Y` of finite presentation, a pseudo-coherent `E` and a bounded
> above complex `𝒢^•` of `𝒪_X`-modules of finite presentation, flat over `Y`, with support proper
> over `Y`, `Rf_*(E ⊗^L 𝒢^•)` is pseudo-coherent, and its formation commutes with arbitrary base
> change: for every cartesian square,
> `Lg^*Rf_*(E ⊗^L 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L (g')^*𝒢^•)` is an isomorphism.

```lean
theorem isPseudoCoherent_derivedModulePushforward_derivedTensor_and_isIso_baseChange
    (f : X ⟶ Y) (hf : IsFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hGb : ∃ b : ℤ, ∀ i, b < i → IsZero (G.X i)) (hGfp : ∀ n, (G.X n).IsFinitePresentation)
    (hGflat : ∀ n, IsFlatOver B S hS X.2 f.hom (G.X n))
    (hGsupp : ∀ n, HasProperSupport B S hS X.2 Y.2 f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf.1)
      ((SheafOfModules.toSheaf _).obj (G.X n))) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPseudoCoherent
        ((derivedModulePushforward B S hS f).obj
          (((smallEtaleDerivedTensor B S hS X).obj E).obj (DerivedCategory.Q.obj G))) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedBaseChangeComp B S hS f g f' g' sq.w
          (((smallEtaleDerivedTensor B S hS X).obj E).obj (DerivedCategory.Q.obj G))
          (((smallEtaleDerivedTensor B S hS X').obj
            ((smallEtaleDerivedModulePullback B S hS g').obj E)).obj
            (DerivedCategory.Q.obj (((modulePullback B S hS g').mapHomologicalComplex
              (ComplexShape.up ℤ)).obj G)))
          ((smallEtaleDerivedPullbackTensorIso g').hom.app (E, DerivedCategory.Q.obj G) ≫
            ((smallEtaleDerivedTensor B S hS X').obj
              ((smallEtaleDerivedModulePullback B S hS g').obj E)).map
              (smallEtaleDerivedModulePullbackQComparison g' G)))
```

## Tag 0CTM, a lemma

[Tag 0CTM](https://stacks.math.columbia.edu/tag/0CTM) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_and_isIso_baseChange_of_isFlat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProper.lean#L61), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProperTags.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProperTags.lean#L28) (StacksFrontier): “(1)”.
- [`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_single_and_isIso_baseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProper.lean#L90), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProperTags.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProperTags.lean#L31) (StacksFrontier): “(2), with 𝒢 flat over Y (the source's 'flat over S' is false)”.

## Tag 0CTN, a lemma

[Tag 0CTN](https://stacks.math.columbia.edu/tag/0CTN) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_derivedModulePushforward_and_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangePseudoCoherentIso.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangePseudoCoherentIso.lean#L82).

> **Stacks 0CTN.** For a flat and proper morphism `f : X ⟶ Y` of finite presentation and a
> pseudo-coherent `E`, `Rf_*E` is pseudo-coherent, and its formation commutes with arbitrary base
> change: for every cartesian square, the base change map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` of
> Stacks 07A7 is an isomorphism.

```lean
theorem isPseudoCoherent_derivedModulePushforward_and_isIso_baseChange
    (f : X ⟶ Y) (hfl : IsFlat B S hS f.hom) (hpr : IsProper B S hS f.hom)
    (hf : IsFinitePresentation B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPseudoCoherent
        ((derivedModulePushforward B S hS f).obj E) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (g' : X' ⟶ X) (f' : X' ⟶ Y')
        (sq : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedModuleBaseChangeMap B S hS f g f' g' sq.w E)
```

## Tag 0D3F, a lemma

[Tag 0D3F](https://stacks.math.columbia.edu/tag/0D3F) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_homEquiv_single_limitComparison_baseRingTensorModule_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperFlatLimitComparisonOverIntegers.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperFlatLimitComparisonOverIntegers.lean#L125). The attribute's comment: “`Spec(R)` is an affine object `T` of the site, with `R = Γ(T, 𝒪_T)`.”.

> Let `f : X ⟶ T` be proper, flat and of finite presentation, with `T` affine and
> `R = Γ(T, 𝒪_T)`, and let `(M_n)` be an inverse system of `R`-modules with surjective transition
> maps. Then the canonical map `𝒪_X ⊗_R lim M_n ⟶ lim 𝒪_X ⊗_R M_n` induces an isomorphism from
> the source, an object of `D_QCoh(𝒪_X)`, to `DQ_X` applied to the target: the morphism
> `𝒪_X ⊗_R lim M_n ⟶ DQ_X(lim 𝒪_X ⊗_R M_n)` corresponding to it under the adjunction
> `D_QCoh(𝒪_X) ⇄ D(𝒪_X)` of Stacks 0CR4 (both modules placed in degree zero) is an isomorphism.
>
> The source's `Spec(R)` is the affine object `T` of the site with `R = Γ(T, 𝒪_T)`.

```lean
theorem isIso_homEquiv_single_limitComparison_baseRingTensorModule_of_isProper
    (f : X ⟶ schemeSpace T) (hf : IsProper B S hS f.hom) (hflat : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom)
    (hT : IsAffine ((BigFppfOver.toScheme B S hS).obj T))
    (Msys : ℕᵒᵖ ⥤ ModuleCat.{u} (baseRing B S hS T))
    (hsurj : ∀ n : ℕ, Function.Surjective (Msys.map (homOfLE (Nat.le_succ n)).op)) :
    letI : ∀ (C : Type (u + 1)) [Category.{u + 1} C] [Abelian C], HasDerivedCategory.{u + 1} C :=
      fun C _ _ => HasDerivedCategory.standard C
    letI := quasicoherentDerivedInclusion_isLeftAdjoint_of_qcqs B S hS B.contains_terminal X.1 X.2
      (qcqs_of_isFinitePresentation_schemeSpace B.contains_terminal f hT hfp).1
      (qcqs_of_isFinitePresentation_schemeSpace B.contains_terminal f hT hfp).2
    IsIso ((Adjunction.ofIsLeftAdjoint (qcohDerivedProp B S hS X).ι).homEquiv
      ⟨(DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).obj
          ((baseRingTensorModule B S hS X (baseRingHomOfMap f)).obj (limit Msys)),
        qcohDerivedProp_singleFunctor_obj B S hS _
          (isQuasicoherentOnSite_baseRingTensorModule B S hS X _ _)⟩
      ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).obj
        (limit (Msys ⋙ baseRingTensorModule B S hS X (baseRingHomOfMap f))))
      ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).map
        (limit.post Msys (baseRingTensorModule B S hS X (baseRingHomOfMap f)))))
```

**`Stacks.Cohomology.SiteModules.isIso_homEquiv_baseRingTensorLimitComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/BaseRingTensorInverseLimitCoherator.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/BaseRingTensorInverseLimitCoherator.lean#L201). The attribute's comment: “the source's rereading of the headline, proved as an equivalence: the canonical map induces an isomorphism from its source onto DQ\_X of its target iff composition with it is bijective on morphisms out of every object of D\_QCoh(𝒪\_X). Neither side is proved; the bijectivity asserted by the headline under properness, flatness and finite presentation is NOT proved here, and is not assumed. The existence of DQ\_X is a named hypothesis, which is Stacks 0CR4 on the small étale site of a quasi-compact quasi-separated algebraic space”.

> **The two readings of the headline of Stacks 0D3F agree.**  Let `DQ_X` be a right adjoint of
> the inclusion `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` — on the small étale site of a quasi-compact
> quasi-separated algebraic space one exists by Stacks 0CR4,
> `AlgebraicGeometry.Space.quasicoherentDerivedInclusion_isLeftAdjoint`, and on a general site it
> is the hypothesis `adj` — and suppose the source `𝒪_X ⊗_R (lim M_n)` of the canonical map of
> Stacks 0D3F lies in `D_QCoh(𝒪_X)`.  Then:
>
> the canonical map `𝒪_X ⊗_R (lim M_n) ⟶ lim (𝒪_X ⊗_R M_n)` induces an isomorphism from its source
> onto `DQ_X` applied to its target **if and only if** composition with it is bijective on
> morphisms out of every object of `D_QCoh(𝒪_X)`.
>
> This is the source's own rereading of its headline.  **Neither side is proved**: the statement is
> an equivalence of the two framings, and its proof is
> `CategoryTheory.Adjunction.bijective_comp_map_iff_isIso_homEquiv`, that is the adjunction alone.
> No properness, flatness or finite-presentation hypothesis appears, and the transition maps of
> `(M_n)` are not assumed surjective, because the equivalence needs none of them.

```lean
theorem isIso_homEquiv_baseRingTensorLimitComparison_iff
    {DQ : DerivedCategory (SheafOfModules.{max u r w} (ringSheafOfSite O)) ⥤
      (quasicoherentDerivedOnSite.{u, v, r, w} O).FullSubcategory}
    (adj : (quasicoherentDerivedOnSite.{u, v, r, w} O).ι ⊣ DQ)
    (hsrc : quasicoherentDerivedOnSite.{u, v, r, w} O
      ((DerivedCategory.singleFunctor _ 0).obj ((baseRingTensorFunctor φ).obj c.pt))) :
    IsIso (adj.homEquiv ⟨_, hsrc⟩ ((DerivedCategory.singleFunctor _ 0).obj d.pt)
        ((DerivedCategory.singleFunctor _ 0).map
          (baseRingTensorLimitComparison φ Msys c d hd))) ↔
      ∀ E : (quasicoherentDerivedOnSite.{u, v, r, w} O).FullSubcategory,
        Function.Bijective
          (fun a : E.obj ⟶
              (DerivedCategory.singleFunctor _ 0).obj ((baseRingTensorFunctor φ).obj c.pt) =>
            a ≫ (DerivedCategory.singleFunctor _ 0).map
              (baseRingTensorLimitComparison φ Msys c d hd))
```

## Tag 0CWH, a lemma

[Tag 0CWH](https://stacks.math.columbia.edu/tag/0CWH) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isPseudoCoherent_representedAffineDerivedSections_tensor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PseudoCoherentSectionsTensor.lean#L97), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountablePseudoCoherentDualityTags.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountablePseudoCoherentDualityTags.lean#L36) (StacksFrontier).

## Tag 0A1R, a lemma

[Tag 0A1R](https://stacks.math.columbia.edu/tag/0A1R) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedSheafHom_and_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeSheafHomIso.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeSheafHomIso.lean#L88).

> For `f : X ⟶ Y` of finite presentation, a perfect `E` and a bounded complex `𝒢^•` of
> `𝒪_X`-modules of finite presentation, flat over `Y`, with support proper over `Y`,
> `Rf_*R𝓗om(E, 𝒢^•)` is perfect, and its formation commutes with arbitrary base change: for every
> cartesian square, `Lg^*Rf_*R𝓗om(E, 𝒢^•) ⟶ Rf'_*R𝓗om(L(g')^*E, (g')^*𝒢^•)` is an isomorphism.

```lean
theorem isPerfect_derivedModulePushforward_derivedSheafHom_and_isIso_baseChange
    (f : X ⟶ Y) (hf : IsFinitePresentation B S hS f.hom)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hGb : {i : ℤ | ¬ IsZero (G.X i)}.Finite) (hGfp : ∀ n, (G.X n).IsFinitePresentation)
    (hGflat : ∀ n, IsFlatOver B S hS X.2 f.hom (G.X n))
    (hGsupp : ∀ n, HasProperSupport B S hS X.2 Y.2 f.hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hf.1)
      ((SheafOfModules.toSheaf _).obj (G.X n))) :
    RingedSite.IsPerfect (smallEtaleRingedSite B S hS Y.1 Y.2)
        ((derivedModulePushforward B S hS f).obj
          (((smallEtaleDerivedSheafHom B S hS X).obj (op E)).obj (DerivedCategory.Q.obj G))) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (smallEtaleDerivedSheafHomBaseChangeMap f g f' g' sq.w E G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.25, Tag 0A1N](https://stacks.math.columbia.edu/tag/0A1N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
