---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFinitePresentationOnSite_iff_isFinitePresentationOnCharts, AlgebraicGeometry.Space.isFiniteTypeOnSite_of_epi, AlgebraicGeometry.Space.isCoherentOnSite_modulePullback_of_isEtale, AlgebraicGeometry.Space.isLocallyFreeOnSite_modulePullback, AlgebraicGeometry.Space.isLocallyGeneratedBySectionsOnSite_modulePullback, AlgebraicGeometry.Space.exists_isGeneratedByGlobalSectionsOfCard_modulePullback, AlgebraicGeometry.Space.isPresentedByGlobalSections_modulePullback, AlgebraicGeometry.Space.isFinitelyPresentedByGlobalSections_modulePullback
statement: formalized
proof: formalized
---

# 66.30 Properties of modules

Section 66.30 of the Stacks Project, [Tag 05VR](https://stacks.math.columbia.edu/tag/05VR). 1 tag here is carried by 17 declarations of the repository (all in StacksFrontier) and 22 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05VR, the section

[Tag 05VR](https://stacks.math.columbia.edu/tag/05VR) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_iff_isFinitePresentationOnCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationOnSiteAffineCharts.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationOnSiteAffineCharts.lean#L269). The attribute's comment: “of finite presentation: for a quasi-coherent module on an algebraic space, finite presentation on the small etale site is finite presentation of its restriction to every etale scheme chart, read on the Zariski site of the chart (items (2) and (4) of the section)”.

> **For a quasi-coherent module, finite presentation on the small étale site is finite
> presentation on the étale scheme charts.**  This is the property "of finite presentation" of the
> section of Stacks 05VR on properties of modules on an algebraic space: it may be read on the
> small étale site, or on every étale scheme chart, where for a quasi-coherent module it is the
> property of the corresponding module on the scheme (the scheme case being Stacks 05VG).

```lean
theorem isFinitePresentationOnSite_iff_isFinitePresentationOnCharts
    (M : Modules.{u, u} B S hS X.1 X.2) (hqc : M.IsQuasicoherentOnSite) :
    SheafOfModules.IsFinitePresentationOnSite M ↔ IsFinitePresentationOnCharts B S hS X.2 M
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleFiniteTypeQuotient.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModuleFiniteTypeQuotient.lean#L94). The attribute's comment: “finite type, quotients”.

> **Properties of Spaces, Section 66.30, the finite type clause for a quotient.**  A quotient
> of an `𝒪_X`-module of finite type on the small étale site of an algebraic space `X` is again of
> finite type.
>
> On each member of a covering witnessing finite type for the source, the restricted epimorphism
> composes with the finite coproduct presenting the source to present the target.

```lean
theorem isFiniteTypeOnSite_of_epi {M N : Modules.{u, u} B S hS X hX} (p : M ⟶ N) [Epi p]
    (hM : SheafOfModules.IsFiniteTypeOnSite M) :
    SheafOfModules.IsFiniteTypeOnSite N
```

**`AlgebraicGeometry.Space.isCoherentOnSite_modulePullback_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/EtalePullbackCoherent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/EtalePullbackCoherent.lean#L84). The attribute's comment: “consequence (2), property 'coherent': for an étale morphism f of algebraic spaces, the pullback f^*𝓕 of a coherent module 𝓕 is coherent”.

> **The pullback of a coherent module along an étale morphism is coherent.**  For an étale
> morphism `f : X ⟶ Y` of algebraic spaces, the inverse image `f^*M` of Stacks 03LU of a coherent
> `𝒪_Y`-module is coherent: it is isomorphic to the étale restriction of `M` (Stacks 03LW), which
> is coherent by `AlgebraicGeometry.Space.isCoherentOnSite_etaleModulePullback`.

```lean
theorem isCoherentOnSite_modulePullback_of_isEtale (f : X ⟶ Y) (hf : IsEtale B S hS f.hom)
    (M : Modules.{u, u} B S hS Y.1 Y.2) (hM : M.IsCoherentOnSite) :
    ((modulePullback B S hS f).obj M).IsCoherentOnSite
```

**`AlgebraicGeometry.Space.isLocallyFreeOnSite_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/LocalFreenessPullback.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/LocalFreenessPullback.lean#L133). The attribute's comment: “consequences (1) and (2), property 'locally free': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a locally free module is locally free”.

> **The inverse image of a locally free module is locally free.**  For a morphism `f : X ⟶ Y`
> of algebraic spaces over `S` and a locally free `𝒪_Y`-module `N` (Stacks 03DL (1)), the inverse
> image `f^*N` of Stacks 03LU is locally free.  This is the locally free clause of Stacks 03DO along
> the morphism of small étale ringed topoi of `f`, consequence (1) of Stacks 05VR.

```lean
theorem isLocallyFreeOnSite_modulePullback {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (N : Modules.{u, u} B S hS Y.1 Y.2) (hN : N.IsLocallyFreeOnSite) :
    ((modulePullback B S hS f).obj N).IsLocallyFreeOnSite
```

**`AlgebraicGeometry.Space.isLocallyGeneratedBySectionsOnSite_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/LocalFreenessPullback.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/LocalFreenessPullback.lean#L207). The attribute's comment: “consequences (1) and (2), property 'locally generated by sections': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module locally generated by sections is locally generated by sections”.

> **The inverse image of a module locally generated by sections is locally generated by
> sections.**  For a morphism `f : X ⟶ Y` of algebraic spaces over `S` and an `𝒪_Y`-module `N`
> locally generated by sections (Stacks 03DL (3)), the inverse image `f^*N` of Stacks 03LU is
> locally generated by sections.  This is that clause of Stacks 03DO along the morphism of small
> étale ringed topoi of `f`, consequence (1) of Stacks 05VR.

```lean
theorem isLocallyGeneratedBySectionsOnSite_modulePullback {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (N : Modules.{u, u} B S hS Y.1 Y.2) (hN : N.IsLocallyGeneratedBySectionsOnSite) :
    ((modulePullback B S hS f).obj N).IsLocallyGeneratedBySectionsOnSite
```

**`AlgebraicGeometry.Space.exists_isGeneratedByGlobalSectionsOfCard_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L85). The attribute's comment: “consequences (1) and (2), property 'generated by finitely many global sections': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module generated by finitely many global sections is generated by finitely many global sections”.

> **Generation by finitely many global sections is preserved by pullback.**  For a morphism
> `f : X ⟶ Y` of algebraic spaces and an `𝒪_Y`-module `G` generated by finitely many global
> sections, `f^*G` is generated by finitely many global sections (Stacks 03DF).

```lean
theorem exists_isGeneratedByGlobalSectionsOfCard_modulePullback (f : X ⟶ Y)
    {G : Modules.{u, u} B S hS Y.1 Y.2} (hG : ∃ r : ℕ, G.IsGeneratedByGlobalSectionsOfCard r) :
    ∃ r : ℕ, ((modulePullback B S hS f).obj G).IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.Space.isPresentedByGlobalSections_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L96). The attribute's comment: “consequences (1) and (2), property 'having a global presentation': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module with a global presentation is a module with a global presentation”.

> **Having a global presentation is preserved by pullback.**  For a morphism `f : X ⟶ Y` of
> algebraic spaces and an `𝒪_Y`-module `G` with a global presentation, `f^*G` has a global
> presentation (Stacks 03DF).

```lean
theorem isPresentedByGlobalSections_modulePullback (f : X ⟶ Y)
    {G : Modules.{u, u} B S hS Y.1 Y.2} (hG : G.IsPresentedByGlobalSections) :
    ((modulePullback B S hS f).obj G).IsPresentedByGlobalSections
```

**`AlgebraicGeometry.Space.isFinitelyPresentedByGlobalSections_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L110). The attribute's comment: “consequences (1) and (2), property 'having a global finite presentation': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module with a global finite presentation is a module with a global finite presentation”.

> **Having a global finite presentation is preserved by pullback.**  For a morphism
> `f : X ⟶ Y` of algebraic spaces and an `𝒪_Y`-module `G` with a global finite presentation, `f^*G`
> has a global finite presentation (Stacks 03DF).

```lean
theorem isFinitelyPresentedByGlobalSections_modulePullback (f : X ⟶ Y)
    {G : Modules.{u, u} B S hS Y.1 Y.2} (hG : G.IsFinitelyPresentedByGlobalSections) :
    ((modulePullback B S hS f).obj G).IsFinitelyPresentedByGlobalSections
```

**`AlgebraicGeometry.Space.isLocallyGeneratedByOnSite_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L124). The attribute's comment: “consequences (1) and (2), property 'locally generated by r sections': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module locally generated by r sections is locally generated by r sections”.

> **Local generation by `r` sections is preserved by pullback.**  For a morphism `f : X ⟶ Y` of
> algebraic spaces and an `𝒪_Y`-module `G` locally generated by `r` sections, `f^*G` is locally
> generated by `r` sections (Stacks 03DO).

```lean
theorem isLocallyGeneratedByOnSite_modulePullback (f : X ⟶ Y)
    (G : Modules.{u, u} B S hS Y.1 Y.2) (r : ℕ) (hG : G.IsLocallyGeneratedByOnSite r) :
    ((modulePullback B S hS f).obj G).IsLocallyGeneratedByOnSite r
```

**`AlgebraicGeometry.Space.isFlat_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L134). The attribute's comment: “consequences (1) and (2), property 'flat': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a flat module is flat”.

> **Flatness is preserved by pullback.**  For a morphism `f : X ⟶ Y` of algebraic spaces and a
> flat `𝒪_Y`-module `G`, the inverse image `f^*G` is a flat `𝒪_X`-module (Stacks 05VD).

```lean
theorem isFlat_modulePullback (f : X ⟶ Y) (G : Modules.{u, u} B S hS Y.1 Y.2)
    (hG : AlgebraicGeometry.SheafOfModules.IsFlat.{u, u + 1, u, u}
      (O := (smallEtaleRingedTopos B S hS Y).O) G) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{u, u + 1, u, u}
      (O := (smallEtaleRingedTopos B S hS X).O) ((modulePullback B S hS f).obj G)
```

**`AlgebraicGeometry.Space.isLocallyFreeOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L208). The attribute's comment: “consequence (3), property 'locally free': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is locally free then 𝓕 is locally free”.

> **Local freeness descends along a surjective étale morphism** (Stacks 05VR, with Stacks 03DN):
> if the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on points is locally
> free, so is `M`.

```lean
theorem isLocallyFreeOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2)
    (h : SheafOfModules.IsLocallyFreeOnSite ((modulePullback B S hS f).obj M)) :
    SheafOfModules.IsLocallyFreeOnSite M
```

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L230). The attribute's comment: “consequence (3), property 'finite locally free': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is finite locally free then 𝓕 is finite locally free”.

> **Finite local freeness descends along a surjective étale morphism** (Stacks 05VR, with
> Stacks 03DN): if the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on
> points is finite locally free, so is `M`.

```lean
theorem isFiniteLocallyFreeOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2)
    (h : SheafOfModules.IsFiniteLocallyFreeOnSite ((modulePullback B S hS f).obj M)) :
    SheafOfModules.IsFiniteLocallyFreeOnSite M
```

**`AlgebraicGeometry.Space.isLocallyGeneratedBySectionsOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L258). The attribute's comment: “consequence (3), property 'locally generated by sections': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is locally generated by sections then 𝓕 is locally generated by sections”.

> **Local generation by sections descends along a surjective étale morphism** (Stacks 05VR,
> with Stacks 03DN): if the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on
> points is locally generated by sections, so is `M`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2)
    (h : SheafOfModules.IsLocallyGeneratedBySectionsOnSite ((modulePullback B S hS f).obj M)) :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite M
```

**`AlgebraicGeometry.Space.isLocallyGeneratedByOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L287). The attribute's comment: “consequence (3), property 'locally generated by r sections': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is locally generated by r sections then 𝓕 is locally generated by r sections”.

> **Local generation by `r` sections descends along a surjective étale morphism** (Stacks 05VR,
> with Stacks 03DN): if the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on
> points is locally generated by `r` sections, so is `M`.

```lean
theorem isLocallyGeneratedByOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2) (r : ℕ)
    (h : SheafOfModules.IsLocallyGeneratedByOnSite ((modulePullback B S hS f).obj M) r) :
    SheafOfModules.IsLocallyGeneratedByOnSite M r
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L309). The attribute's comment: “consequence (3), property 'of finite type': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is of finite type then 𝓕 is of finite type”.

> **Finite type descends along a surjective étale morphism** (Stacks 05VR, with Stacks 03DN):
> if the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on points is of
> finite type, so is `M`.

```lean
theorem isFiniteTypeOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2)
    (h : ((modulePullback B S hS f).obj M).IsFiniteTypeOnSite) :
    M.IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L331). The attribute's comment: “consequence (3), property 'quasi-coherent': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is quasi-coherent then 𝓕 is quasi-coherent”.

> **Quasi-coherence descends along a surjective étale morphism** (Stacks 05VR, with
> Stacks 03DN): if the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on
> points is quasi-coherent, so is `M`.

```lean
theorem isQuasicoherentOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2)
    (h : ((modulePullback B S hS f).obj M).IsQuasicoherentOnSite) :
    M.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isCoherentOnSite_of_modulePullback_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L347). The attribute's comment: “consequence (3), property 'coherent': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is coherent then 𝓕 is coherent”.

> **Coherence descends along a surjective étale morphism** (Stacks 05VR, with Stacks 03DN): if
> the inverse image `f^*M` along an étale morphism `f : Y ⟶ X` surjective on points is coherent,
> so is `M`.  Coherence of `f^*M` restricts to the slice at an étale chart `V₀` of `Y` surjective
> on points, crosses the slice comparison of Stacks 04M0 to the slice of `X` at the composite
> chart, and descends from that surjective chart to `X`.

```lean
theorem isCoherentOnSite_of_modulePullback_of_isSurjective (f : Y ⟶ X)
    (hf : IsEtale B S hS f.hom) (hsurj : IsSurjective B S hS f.hom)
    (M : Modules.{u, u} B S hS X.1 X.2)
    (h : SheafOfModules.IsCoherentOnSite ((modulePullback B S hS f).obj M)) :
    SheafOfModules.IsCoherentOnSite M
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isFreeModule_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackIsFreeModule.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L148) (StacksFrontier): “consequences (1) and (2), property 'free': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a free module is free”.
- [`AlgebraicGeometry.Space.isFiniteFreeModule_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricFibreEtaleFreeLocus.lean#L150), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L152) (StacksFrontier): “consequences (1) and (2), property 'finite free': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a finite free module is finite free”.
- [`AlgebraicGeometry.C1764Prereq.isGeneratedByGlobalSections_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/C1764Prereq/SchemeGlobalGeneration.lean#L146), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L157) (StacksFrontier): “consequences (1) and (2), property 'generated by global sections': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module generated by global sections is generated by global sections”.
- [`AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_modulePullback'`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyLimitStageDescent.lean#L94), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L162) (StacksFrontier): “consequences (1) and (2), property 'finite locally free': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a finite locally free module is finite locally free”.
- [`AlgebraicGeometry.Space.isFiniteTypeOnSite_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackSupport.lean#L129), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L167) (StacksFrontier): “consequences (1) and (2), property 'finite type': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module of finite type is of finite type”.
- [`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModulePullbackQuasicoherentFromChartDiagrams.lean#L109), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L172) (StacksFrontier): “consequences (1) and (2), property 'quasi-coherent': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a quasi-coherent module is quasi-coherent”.
- [`AlgebraicGeometry.Space.isFinitePresentationOnSite_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPullbackStability.lean#L91), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/Pullback.lean#L177) (StacksFrontier): “consequences (1) and (2), property 'of finite presentation': for a morphism f of algebraic spaces, in particular an étale one, the pullback f^*𝓕 of a module of finite presentation is of finite presentation”.
- [`AlgebraicGeometry.Scheme.Modules.isFree_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L32) (StacksFrontier): “consequence (4), property 'free': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isFiniteFree_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L161), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L37) (StacksFrontier): “consequence (4), property 'finite free': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isGeneratedByGlobalSections_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L184), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L42) (StacksFrontier): “consequence (4), property 'generated by global sections': for a quasi- coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.exists_isGeneratedByGlobalSectionsOfCard_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L241), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L47) (StacksFrontier): “consequence (4), property 'generated by finitely many global sections': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isPresentedByGlobalSections_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L273), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L52) (StacksFrontier): “consequence (4), property 'having a global presentation': for a quasi- coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isFinitelyPresentedByGlobalSections_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L299), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L57) (StacksFrontier): “consequence (4), property 'having a global finite presentation': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isFiniteLocallyFreeOnSite_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L329), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L62) (StacksFrontier): “consequence (4), property 'finite locally free': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isLocallyGeneratedBySectionsOnSite_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L355), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L67) (StacksFrontier): “consequence (4), property 'locally generated by sections': for a quasi- coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isLocallyGeneratedByOnSite_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L384), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L72) (StacksFrontier): “consequence (4), property 'locally generated by r sections': for a quasi- coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isFiniteType_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L410), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L77) (StacksFrontier): “consequence (4), property 'finite type': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isFinitePresentation_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L432), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L82) (StacksFrontier): “consequence (4), property 'of finite presentation': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.Scheme.Modules.isFlat_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L453), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L87) (StacksFrontier): “consequence (4), property 'flat': for a quasi-coherent module 𝓕 on a scheme X, 𝓕 has the property exactly when the corresponding module 𝓕ᵃ on X\_étale has it, and exactly when 𝓕ᵃ on X\_Zar has it”.
- [`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleOpenCoverQuasicoherence.lean#L262), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L92) (StacksFrontier): “consequence (4), property 'quasi-coherent': for a quasi-coherent module 𝓕 on a scheme X, the corresponding module 𝓕ᵃ on X\_étale is quasi-coherent”.
- [`AlgebraicGeometry.Scheme.Modules.isCoherent_iff_associatedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/PropertiesOfModulesComparison.lean#L481), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SchemeComparison.lean#L96) (StacksFrontier): “consequence (5): for a quasi-coherent module 𝓕 on a locally Noetherian scheme X, 𝓕 is coherent exactly when the corresponding module 𝓕ᵃ on X\_étale is coherent, and exactly when 𝓕ᵃ on X\_Zar is coherent”.
- [`AlgebraicGeometry.Space.isFinitePresentationOnSite_of_modulePullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationSurjectiveEtaleDescent.lean#L174), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/PropertiesOfModules/SurjectiveEtaleDescent.lean#L386) (StacksFrontier): “consequence (3), property 'of finite presentation': for a surjective étale morphism f : Y → X of algebraic spaces and a module 𝓕 on X, if f^*𝓕 is of finite presentation then 𝓕 is of finite presentation”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.30, Tag 05VR](https://stacks.math.columbia.edu/tag/05VR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
