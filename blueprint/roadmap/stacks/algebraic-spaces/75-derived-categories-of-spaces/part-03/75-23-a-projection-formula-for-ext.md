---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_cohomologyTensorDirectImage_iso, AlgebraicGeometry.Space.exists_extPerfectCohomologyIso, AlgebraicGeometry.Space.exists_isPseudoCoherent_extAddEquiv_tensorPullbackComplex, AlgebraicGeometry.Space.exists_isPerfect_tensorPullbackExtGroup_smallEtaleTensorCohomology, AlgebraicGeometry.Space.exists_isPseudoCoherent_extAddEquiv_baseChange
statement: formalized
proof: formalized
---

# 75.23 A projection formula for Ext

Section 75.23 of the Stacks Project, [Tag 08JM](https://stacks.math.columbia.edu/tag/08JM). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A1M, a lemma

[Tag 0A1M](https://stacks.math.columbia.edu/tag/0A1M) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_cohomologyTensorDirectImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyTensorPullbackComplex.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyTensorPullbackComplex.lean#L721).

> **Stacks 0A1M.** Let `Y` be a Noetherian algebraic space and `f : X ⟶ Y` a morphism locally of
> finite type and quasi-separated. Let `E` be a perfect object of `D(𝒪_X)` and `𝒢^•` a bounded
> complex of coherent `𝒪_X`-modules, flat over `Y`, with support proper over `Y`, and
> `K = Rf_*(E ⊗^L 𝒢^•)` (Stacks 0DKJ). Then there are maps
> `H^i(Y, K ⊗^L ℱ) ⟶ H^i(X, E ⊗^L (𝒢^• ⊗ f^*ℱ))`, natural in the `𝒪_Y`-module `ℱ`, which are
> isomorphisms for `ℱ` quasi-coherent, and which are compatible with the boundary maps: for a short
> exact sequence `0 → ℱ₁ → ℱ₂ → ℱ₃ → 0` the boundary maps of the triangle
> `K ⊗^L ℱ₁ → K ⊗^L ℱ₂ → K ⊗^L ℱ₃ → K ⊗^L ℱ₁[1]` correspond to those of the triangle of the short
> exact sequence of complexes `0 → 𝒢^• ⊗ f^*ℱ₁ → 𝒢^• ⊗ f^*ℱ₂ → 𝒢^• ⊗ f^*ℱ₃ → 0` tensored with `E`.
> Here `⊗^L` is the canonical derived tensor product on the small étale site.

```lean
theorem exists_cohomologyTensorDirectImage_iso :
    ∃ η : ∀ i : ℤ, cohomologyTensorDirectImage B S hS f E G i ⟶
        cohomologyTensorPullbackComplex B S hS f E G i,
      (∀ (i : ℤ) (F : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)),
        F.IsQuasicoherentOnSite → IsIso ((η i).app F)) ∧
      ∀ {T : ShortComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))}
        (hT : T.ShortExact) (i j : ℤ) (h : i + 1 = j),
        (forget₂ (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS Y.1 Y.2))
              AddCommGrpCat.{u + 1}).map
            ((DerivedCategory.homologyFunctor
              (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS Y.1 Y.2)) 0).homologySequenceδ
              ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS Y.1 Y.2).mapTriangle.obj
                (((smallEtaleDerivedTensor B S hS Y).obj
                  (tensorDirectImageObj B S hS f E G)).mapTriangle.obj
                  (DerivedCategory.triangleOfSES
                    (hT.map_of_exact (HomologicalComplex.single (SheafOfModules.{u}
                      (ringedToposStructureRingSheaf B S hS Y)) (ComplexShape.up ℤ) 0)))))
              i j h) ≫ (η j).app T.X₁ =
          (η i).app T.X₃ ≫
            (forget₂ (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS X.1 X.2))
              AddCommGrpCat.{u + 1}).map
            ((DerivedCategory.homologyFunctor
              (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS X.1 X.2)) 0).homologySequenceδ
              ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS X.1 X.2).mapTriangle.obj
                (((smallEtaleDerivedTensor B S hS X).obj E).mapTriangle.obj
                  (DerivedCategory.triangleOfSES (shortExact_tensorPullbackComplex_map_single
                    ((FlatProperSupportComplex.isFlatOverAtGeometricPoint B S hS hG))
                      hT))))
              i j h)
```

## Tag 08JN, a lemma

[Tag 08JN](https://stacks.math.columbia.edu/tag/08JN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_extPerfectCohomologyIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtPerfectDirectImageCoefficient.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtPerfectDirectImageCoefficient.lean#L91).

> **Stacks 08JN.**  Let `Y` be a Noetherian algebraic space and `f : X ⟶ Y` a morphism locally
> of finite type and quasi-separated, let `E ∈ D(𝒪_X)` be perfect and `𝒢^•` a bounded complex of
> coherent `𝒪_X`-modules, flat over `Y`, with support proper over `Y` (the notation of Stacks
> 0DKK), and let `K = Rf_* RSheafHom(E, 𝒢^•)`.  Then there are isomorphisms
> `H^i(Y, K ⊗^L ℱ) ≅ Ext^i_{𝒪_X}(E, 𝒢^• ⊗ f^*ℱ)` for quasi-coherent `𝒪_Y`-modules `ℱ`,
> functorial in `ℱ`, and compatible with the boundary maps: for a short exact sequence
> `0 → ℱ₁ → ℱ₂ → ℱ₃ → 0` of quasi-coherent `𝒪_Y`-modules the boundary map
> `H^i(Y, K ⊗^L ℱ₃) → H^{i+1}(Y, K ⊗^L ℱ₁)` corresponds to the boundary map
> `Ext^i(E, 𝒢^• ⊗ f^*ℱ₃) → Ext^{i+1}(E, 𝒢^• ⊗ f^*ℱ₁)` of the short exact sequence of complexes
> `0 → 𝒢^• ⊗ f^*ℱ₁ → 𝒢^• ⊗ f^*ℱ₂ → 𝒢^• ⊗ f^*ℱ₃ → 0`.
>
> Here `K = Rf_* RSheafHom(E, 𝒢^•)` is formed with the internal hom
> `AlgebraicGeometry.Space.smallEtaleDerivedSheafHom` of `D(𝒪_X)` (the one adjoint to the derived
> tensor product of the small étale site, Stacks 08J8); it is perfect by
> `AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_smallEtaleDerivedSheafHom`.  Stacks
> 0DKK itself is registered, on the internal hom of the ringed site, as
> `AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_derivedSheafHom`.  `H^i(Y, -)` is the
> `i`-th cohomology of derived global sections, and `Ext^i(E, -) = Hom(E, -[i])` in `D(𝒪_X)`.

```lean
theorem exists_extPerfectCohomologyIso (hTop : B.Contains (⊤_ Scheme.{u})) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1)
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hG : FlatProperSupportComplex B S hS f hf G) :
    ∃ c : ∀ (F : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)),
        F.IsQuasicoherentOnSite → ∀ i : ℤ,
        extPerfectBaseCohomology B S hS f E G F i ≅ extPerfectExtGroup B S hS f E G F i,
      (∀ (F F' : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
          (hF : F.IsQuasicoherentOnSite) (hF' : F'.IsQuasicoherentOnSite) (q : F ⟶ F') (i : ℤ),
          (forget₂ (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS Y.1 Y.2))
              AddCommGrpCat.{u + 1}).map (((DerivedCategory.homologyFunctor
                (ModuleCat.{u + 1} (globalSectionRingSmallEtale B S hS Y.1 Y.2)) 0).shift i).map
              ((derivedModuleGlobalSectionsSmallEtaleAtModel B S hS Y.1 Y.2).map
                (((smallEtaleDerivedTensor B S hS Y).obj
                  (extPerfectDirectImageObj B S hS f E G)).map (extPerfectSingleMap B S hS q)))) ≫
            (c F' hF' i).hom =
          (c F hF i).hom ≫
            (preadditiveCoyoneda.obj (op E)).map ((extPerfectCoefficientMap B S hS f G q)⟦i⟧')) ∧
      (∀ (T : ShortComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)))
          (hT : T.ShortExact) (h₁ : T.X₁.IsQuasicoherentOnSite) (h₃ : T.X₃.IsQuasicoherentOnSite)
          (i j : ℤ) (h : i + 1 = j),
          extPerfectBaseDelta B S hS f E G T hT i j h ≫ (c T.X₁ h₁ j).hom =
          (c T.X₃ h₃ i).hom ≫ (preadditiveCoyoneda.obj (op E)).map
            ((DerivedCategory.triangleOfSESδ (shortExact_tensorPullbackComplex_map_single
                (hG.isFlatOverAtGeometricPoint B S hS) hT))⟦i⟧' ≫
              (shiftFunctorAdd' _ 1 i j (by omega)).inv.app
                (extPerfectCoefficientObj B S hS f G T.X₁)))
```

## Tag 08JR, a lemma

[Tag 08JR](https://stacks.math.columbia.edu/tag/08JR) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPseudoCoherent_extAddEquiv_tensorPullbackComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtPerfectDualTowerData.lean, line 705](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtPerfectDualTowerData.lean#L705). The attribute's comment: “(B)”.

> **Stacks 08JR, part (B).**  Let `S` be a scheme and `f : X ⟶ B` a morphism of algebraic spaces
> over `S` with `B` Noetherian and `f` locally of finite type and quasi-separated.  Let
> `E ∈ D^-_{Coh}(𝒪_X)` (coherent cohomology sheaves, bounded above) and let `𝒢^•` be a bounded
> complex of coherent `𝒪_X`-modules, flat over `B`, with support proper over `B`.  Then there is a
> pseudo-coherent `L ∈ D(𝒪_B)` with isomorphisms
> `Ext^i_{𝒪_B}(L, ℱ) ≅ Ext^i_{𝒪_X}(E, 𝒢^• ⊗_{𝒪_X} f^*ℱ)` for quasi-coherent `𝒪_B`-modules `ℱ`,
> functorial in `ℱ` and compatible with the boundary maps: for a short exact sequence
> `0 → ℱ₁ → ℱ₂ → ℱ₃ → 0` of quasi-coherent modules, the boundary map of the distinguished triangle
> of `ℱ₁[0] → ℱ₂[0] → ℱ₃[0]` on the left corresponds to the boundary map of the distinguished
> triangle of the short exact sequence of complexes
> `0 → 𝒢^• ⊗ f^*ℱ₁ → 𝒢^• ⊗ f^*ℱ₂ → 𝒢^• ⊗ f^*ℱ₃ → 0` on the right.
>
> Here `Ext^i(A, C) = Hom(A, C[i])` in the derived categories of the small étale ringed sites,
> `ℱ[0]` is `DerivedCategory.singleFunctor _ 0`, and `𝒢^• ⊗ f^*ℱ` is
> `AlgebraicGeometry.Space.tensorPullbackComplex` at `ℱ` placed in degree `0`; the sequence of
> complexes is written `ShortComplex.mk (ℱ₁[0] → ℱ₂[0]) (ℱ₂[0] → ℱ₃[0])` mapped by
> `𝒢^• ⊗ f^*(-)`, exact by `AlgebraicGeometry.Space.shortExact_tensorPullbackComplex_map_single`.

```lean
theorem exists_isPseudoCoherent_extAddEquiv_tensorPullbackComplex (hTop : B.Contains
    (⊤_ Scheme.{u}))
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1) (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hEcoh : ∀ q : ℤ, IsCoherent B S hS X.1 X.2 ((DerivedCategory.homologyFunctor _ q).obj E))
    (hEb : DerivedCategoryB.IsBoundedAbove E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hG : FlatProperSupportComplex B S hS f hf G) :
    ∃ (L : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
      (_ : (smallEtaleRingedSite B S hS Y.1 Y.2).IsPseudoCoherent L)
      (Φ : ∀ (F : Modules.{u, u} B S hS Y.1 Y.2) (_ : F.IsQuasicoherentOnSite) (i : ℤ),
        (L ⟶ ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y.1 Y.2) 0).obj F)⟦i⟧) ≃+
          ShiftedHom E (tensorPullbackComplexDerived f G ((HomologicalComplex.single
            (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
            (ComplexShape.up ℤ) 0).obj F)) i),
      (∀ {F F' : Modules.{u, u} B S hS Y.1 Y.2} (hF : F.IsQuasicoherentOnSite)
        (hF' : F'.IsQuasicoherentOnSite) (q : F ⟶ F') (i : ℤ)
        (e : L ⟶ ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y.1 Y.2) 0).obj F)⟦i⟧),
        Φ F' hF' i (e ≫ ((DerivedCategory.singleFunctor
          (Modules.{u, u} B S hS Y.1 Y.2) 0).map q)⟦i⟧') =
          Φ F hF i e ≫ (DerivedCategory.Q.map ((tensorPullbackComplex f G).map
            ((HomologicalComplex.single (SheafOfModules.{u}
            (ringedToposStructureRingSheaf B S hS Y)) (ComplexShape.up ℤ) 0).map q)))⟦i⟧') ∧
      (∀ (T : ShortComplex (Modules.{u, u} B S hS Y.1 Y.2)) (hT : T.ShortExact)
        (h₁ : T.X₁.IsQuasicoherentOnSite), T.X₂.IsQuasicoherentOnSite →
        ∀ (h₃ : T.X₃.IsQuasicoherentOnSite) (i : ℤ)
        (e : ShiftedHom L ((DerivedCategory.singleFunctor
          (Modules.{u, u} B S hS Y.1 Y.2) 0).obj T.X₃) i),
        Φ T.X₁ h₁ (i + 1) (e.comp hT.singleδ (add_comm 1 i)) =
          (Φ T.X₃ h₃ i e).comp (DerivedCategory.triangleOfSESδ
            (S := (ShortComplex.mk ((HomologicalComplex.single (SheafOfModules.{u}
            (ringedToposStructureRingSheaf B S hS Y)) (ComplexShape.up ℤ) 0).map T.f)
            ((HomologicalComplex.single (SheafOfModules.{u}
            (ringedToposStructureRingSheaf B S hS Y)) (ComplexShape.up ℤ) 0).map T.g)
            (single_map_comp_map_eq_zero B S hS T)).map (tensorPullbackComplex f G))
              (shortExact_tensorPullbackComplex_map_single
                (FlatProperSupportComplex.isFlatOverAtGeometricPoint B S hS hG) hT))
              (add_comm 1 i))
```

**`AlgebraicGeometry.Space.exists_isPerfect_tensorPullbackExtGroup_smallEtaleTensorCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtTensorPullbackPerfectApproximation.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtTensorPullbackPerfectApproximation.lean#L527). The attribute's comment: “(A)”.

> **Stacks 08JR, part (A).**  Let `S` be a scheme and `f : X ⟶ B` a morphism of algebraic spaces
> over `S` with `B` Noetherian and `f` locally of finite type and quasi-separated.  Let
> `E ∈ D^-_{Coh}(𝒪_X)` (coherent cohomology sheaves, bounded above) and let `𝒢^•` be a bounded
> complex of coherent `𝒪_X`-modules, flat over `B`, with support proper over `B`.  Then for every
> `m ∈ ℤ` there are a perfect `K ∈ D(𝒪_B)` and maps
> `α^i_ℱ : Ext^i_{𝒪_X}(E, 𝒢^• ⊗_{𝒪_X} f^*ℱ) ⟶ H^i(B, K ⊗^L_{𝒪_B} ℱ)` for quasi-coherent
> `𝒪_B`-modules `ℱ`, functorial in `ℱ`, compatible with the boundary maps of short exact sequences
> `0 → ℱ₁ → ℱ₂ → ℱ₃ → 0` of quasi-coherent modules (on the left the boundary map of the
> distinguished triangle of `0 → 𝒢^• ⊗ f^*ℱ₁ → 𝒢^• ⊗ f^*ℱ₂ → 𝒢^• ⊗ f^*ℱ₃ → 0`, on the right the
> connecting map of the cohomology of `RΓ(B, K ⊗^L -)` of the triangle of `ℱ₁[0] → ℱ₂[0] → ℱ₃[0]`),
> and invertible for `i ≤ m`.
>
> Here `Ext^i(E, -) = Hom(E, -[i])` in `D(𝒪_X)` (`AlgebraicGeometry.Space.tensorPullbackExtGroup`),
> `H^i(B, K ⊗^L ℱ)` is the `i`-th cohomology of derived global sections of `K ⊗^L ℱ[0]`
> (`AlgebraicGeometry.Space.smallEtaleTensorCohomology`), and the maps are morphisms of abelian
> groups.

```lean
theorem exists_isPerfect_tensorPullbackExtGroup_smallEtaleTensorCohomology
    (hTop : B.Contains (⊤_ Scheme.{u}))
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1) (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hEcoh : ∀ q : ℤ, IsCoherent B S hS X.1 X.2 ((DerivedCategory.homologyFunctor _ q).obj E))
    (hEb : DerivedCategoryB.IsBoundedAbove E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hG : FlatProperSupportComplex B S hS f hf G) (m : ℤ) :
    ∃ (K : smallEtaleModulesDerived B S hS Y) (_ : SmallEtaleIsPerfect B S hS K)
      (α : ∀ (F : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
        (_ : F.IsQuasicoherentOnSite) (i : ℤ),
        tensorPullbackExtGroup B S hS E f G F i ⟶ smallEtaleTensorCohomology B S hS K F i),
      (∀ (F : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
        (hF : F.IsQuasicoherentOnSite) (i : ℤ), i ≤ m → IsIso (α F hF i)) ∧
      (∀ {F F' : SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)}
        (hF : F.IsQuasicoherentOnSite) (hF' : F'.IsQuasicoherentOnSite) (q : F ⟶ F') (i : ℤ),
        tensorPullbackExtGroupMap B S hS E f G q i ≫ α F' hF' i =
          α F hF i ≫ smallEtaleTensorCohomologyMap B S hS K q i) ∧
      (∀ (T : ShortComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)))
        (hT : T.ShortExact) (h₁ : T.X₁.IsQuasicoherentOnSite) (h₃ : T.X₃.IsQuasicoherentOnSite)
        (i j : ℤ) (h : i + 1 = j),
        tensorPullbackExtGroupDelta B S hS E f G T (shortExact_tensorPullbackComplex_map_single
            (FlatProperSupportComplex.isFlatOverAtGeometricPoint B S hS hG) hT) i j h ≫
            α T.X₁ h₁ j =
          α T.X₃ h₃ i ≫ smallEtaleTensorCohomologyDelta B S hS K T hT i j h)
```

## Tag 0DKL, a remark

[Tag 0DKL](https://stacks.math.columbia.edu/tag/0DKL) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPseudoCoherent_extAddEquiv_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtRepresentingComplexBaseChange.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtRepresentingComplexBaseChange.lean#L126).

> **Stacks 0DKL.** Let `Y` be a Noetherian algebraic space, `f : X ⟶ Y` locally of finite type
> and quasi-separated, `E ∈ D^-_{Coh}(𝒪_X)` and `𝒢^•` a bounded complex of coherent `𝒪_X`-modules,
> flat over `Y`, with support proper over `Y`. The pseudo-coherent `L ∈ D(𝒪_Y)` of Stacks 08JR (B)
> has isomorphisms `Ext^i_Y(L, ℱ) ≅ Ext^i_X(E, 𝒢^• ⊗ f^*ℱ)`, natural in the quasi-coherent `ℱ` and
> compatible with boundary maps. It is compatible with base change: for every cartesian square
> `X' = X ×_Y Y'` (with `g : Y' ⟶ Y` arbitrary) there are isomorphisms
> `Ext^i_{Y'}(Lg^*L, ℱ') ≅ Ext^i_{X'}(L(g')^*E, (g')^*𝒢^• ⊗ (f')^*ℱ')` for `ℱ'` quasi-coherent on
> `Y'`, natural in `ℱ'`. Here `(g')^*𝒢^•` is the termwise, underived, pullback.

```lean
theorem exists_isPseudoCoherent_extAddEquiv_baseChange (hTop : B.Contains (⊤_ Scheme.{u}))
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hY : IsNoetherian B S hS hTop Y.1) (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hEcoh : ∀ q : ℤ, IsCoherent B S hS X.1 X.2 ((DerivedCategory.homologyFunctor _ q).obj E))
    (hEb : DerivedCategoryB.IsBoundedAbove E)
    (G : CochainComplex (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) ℤ)
    (hG : FlatProperSupportComplex B S hS f hf G) :
    ∃ (L : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
      (_ : (smallEtaleRingedSite B S hS Y.1 Y.2).IsPseudoCoherent L)
      (Φ : ∀ (F : Modules.{u, u} B S hS Y.1 Y.2) (_ : F.IsQuasicoherentOnSite) (i : ℤ),
        (L ⟶ ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y.1 Y.2) 0).obj F)⟦i⟧) ≃+
          ShiftedHom E (tensorPullbackComplexDerived f G ((HomologicalComplex.single
            (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)) (ComplexShape.up ℤ) 0).obj
              F)) i),
      (∀ {F F' : Modules.{u, u} B S hS Y.1 Y.2} (hF : F.IsQuasicoherentOnSite)
        (hF' : F'.IsQuasicoherentOnSite) (q : F ⟶ F') (i : ℤ)
        (e : L ⟶ ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y.1 Y.2) 0).obj F)⟦i⟧),
        Φ F' hF' i (e ≫ ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y.1 Y.2) 0).map
            q)⟦i⟧') =
          Φ F hF i e ≫ (DerivedCategory.Q.map ((tensorPullbackComplex f G).map
            ((HomologicalComplex.single
              (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
              (ComplexShape.up ℤ) 0).map q)))⟦i⟧') ∧
      (∀ (T : ShortComplex (Modules.{u, u} B S hS Y.1 Y.2)) (hT : T.ShortExact)
        (h₁ : T.X₁.IsQuasicoherentOnSite) (_h₂ : T.X₂.IsQuasicoherentOnSite)
        (h₃ : T.X₃.IsQuasicoherentOnSite) (i : ℤ)
        (e : ShiftedHom L ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y.1 Y.2) 0).obj
          T.X₃) i),
        Φ T.X₁ h₁ (i + 1) (e.comp hT.singleδ (add_comm 1 i)) =
          (Φ T.X₃ h₃ i e).comp (DerivedCategory.triangleOfSESδ (S := (ShortComplex.mk
            ((HomologicalComplex.single
              (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
              (ComplexShape.up ℤ) 0).map T.f)
            ((HomologicalComplex.single
              (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y))
              (ComplexShape.up ℤ) 0).map T.g) (single_map_comp_map_eq_zero B S hS T)).map
                (tensorPullbackComplex f G))
              (shortExact_tensorPullbackComplex_map_single
                (FlatProperSupportComplex.isFlatOverAtGeometricPoint B S hS hG) hT))
              (add_comm 1 i)) ∧
      ∀ {X' Y' : AlgebraicSpaces B S hS} {g : Y' ⟶ Y} {g' : X' ⟶ X} {f' : X' ⟶ Y'}
        (_ : IsPullback g' f' f g),
        ∃ Ψ : ∀ (F' : Modules.{u, u} B S hS Y'.1 Y'.2) (_ : F'.IsQuasicoherentOnSite) (i : ℤ),
            (asModulesObj Y' ((smallEtaleDerivedModulePullback B S hS g).obj L) ⟶
              ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y'.1 Y'.2) 0).obj F')⟦i⟧) ≃+
            (asModulesObj X' ((smallEtaleDerivedModulePullback B S hS g').obj E) ⟶
              (tensorPullbackComplexDerived f' ((pullbackComplexSmallEtale g').obj G)
                ((CochainComplex.singleFunctor _ 0).obj F'))⟦i⟧),
          ∀ {F' F'' : Modules.{u, u} B S hS Y'.1 Y'.2} (hF' : F'.IsQuasicoherentOnSite)
            (hF'' : F''.IsQuasicoherentOnSite) (q : F' ⟶ F'') (i : ℤ)
            (e : asModulesObj Y' ((smallEtaleDerivedModulePullback B S hS g).obj L) ⟶
              ((DerivedCategory.singleFunctor (Modules.{u, u} B S hS Y'.1 Y'.2) 0).obj F')⟦i⟧),
            Ψ F'' hF'' i (e ≫ ((DerivedCategory.singleFunctor _ 0).map q)⟦i⟧') =
              Ψ F' hF' i e ≫ (DerivedCategory.Q.map ((tensorPullbackComplex f'
                ((pullbackComplexSmallEtale g').obj G)).map
                  ((CochainComplex.singleFunctor _ 0).map q)))⟦i⟧'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.23, Tag 08JM](https://stacks.math.columbia.edu/tag/08JM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
