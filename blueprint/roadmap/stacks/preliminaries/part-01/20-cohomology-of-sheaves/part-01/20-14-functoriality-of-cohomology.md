---
declaration: section
origin: cited
lean: Stacks.Cohomology.toDerivedPushforwardPlus, Stacks.Cohomology.toDerivedPushforwardPlus_comp_left, Stacks.Cohomology.toDerivedPushforwardPlus_comp_right, Stacks.Cohomology.derivedGlobalSectionsMap, Stacks.Cohomology.moduleCohomologyMap, Stacks.Cohomology.exists_pushforwardInjectiveResolutionLift, Stacks.Cohomology.quasiIso_moduleGlobalSections_map_pushforwardResolution, Stacks.Cohomology.injectiveResolutionGlobalSectionsMap
statement: formalized
proof: formalized
---

# 20.14 Functoriality of cohomology

Section 20.14 of the Stacks Project, [Tag 01F7](https://stacks.math.columbia.edu/tag/01F7). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01F8, a lemma

[Tag 01F8](https://stacks.math.columbia.edu/tag/01F8) in the Stacks Project.

**`Stacks.Cohomology.toDerivedPushforwardPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean#L115). References: EGA 0 (12.4.8), “(12.4.8.1)”.

> **Stacks 01F8.**  A morphism of complexes `φ : 𝒢^• ⟶ f_* ℱ^•` from a bounded below complex
> of `𝒪_Y`-modules to the termwise pushforward of a bounded below complex of `𝒪_X`-modules
> induces a canonical morphism `𝒢^• ⟶ Rf_*(ℱ^•)` in `D⁺(Mod 𝒪_Y)`, namely `φ` read in the derived
> category followed by the unit of the right derived functor of `f_*`.

```lean
noncomputable def toDerivedPushforwardPlus {G : CochainComplex.Plus (Modules Y)}
    {F : CochainComplex.Plus (Modules X)}
    (phi : G ⟶ (pushforward f).mapCochainComplexPlus.obj F) :
    DerivedCategory.Plus.Q.obj G ⟶
      (pushforward f).rightDerivedFunctorPlus.obj (DerivedCategory.Plus.Q.obj F)
```

**`Stacks.Cohomology.toDerivedPushforwardPlus_comp_left`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean#L127).

> **Functoriality in the complex downstairs.**  Precomposing the morphism of complexes with
> `g : 𝒢'^• ⟶ 𝒢^•` precomposes the morphism of [Stacks, Tag 01F8] with `g` read in the derived
> category.

```lean
lemma toDerivedPushforwardPlus_comp_left {G G' : CochainComplex.Plus (Modules Y)}
    {F : CochainComplex.Plus (Modules X)} (g : G' ⟶ G)
    (phi : G ⟶ (pushforward f).mapCochainComplexPlus.obj F) :
    DerivedCategory.Plus.Q.map g ≫ toDerivedPushforwardPlus f phi =
      toDerivedPushforwardPlus f (g ≫ phi)
```

**`Stacks.Cohomology.toDerivedPushforwardPlus_comp_right`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean#L138).

> **Functoriality in the complex upstairs.**  Postcomposing the morphism of complexes with the
> termwise pushforward of `k : ℱ^• ⟶ ℱ'^•` postcomposes the morphism of [Stacks, Tag 01F8] with
> `Rf_*(k)`.

```lean
lemma toDerivedPushforwardPlus_comp_right {G : CochainComplex.Plus (Modules Y)}
    {F F' : CochainComplex.Plus (Modules X)}
    (phi : G ⟶ (pushforward f).mapCochainComplexPlus.obj F) (k : F ⟶ F') :
    toDerivedPushforwardPlus f phi ≫
        (pushforward f).rightDerivedFunctorPlus.map (DerivedCategory.Plus.Q.map k) =
      toDerivedPushforwardPlus f (phi ≫ (pushforward f).mapCochainComplexPlus.map k)
```

## Tag 01F9, an equation

[Tag 01F9](https://stacks.math.columbia.edu/tag/01F9) in the Stacks Project.

**`Stacks.Cohomology.derivedGlobalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedGlobalSectionsMap.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/DerivedGlobalSectionsMap.lean#L228).

> **Stacks 01F9.**  An `f`-map `φ : 𝒢 ⟶ f_* ℱ` from an `𝒪_Y`-module `𝒢` to an `𝒪_X`-module
> `ℱ` induces the morphism
>
> ```
> φ : RΓ(Y, 𝒢) ⟶ RΓ(X, ℱ)
> ```
>
> of `D⁺(Γ(Y, 𝒪_Y))`, the target carrying its `Γ(Y, 𝒪_Y)`-module structure by restriction of
> scalars along `Γ(Y, 𝒪_Y) ⟶ Γ(X, 𝒪_X)`.  It is `RΓ(Y, -)` applied to the morphism
> `𝒢[0] ⟶ Rf_*(ℱ[0])` of [Stacks, Tag 01F8], followed by the identification
> `RΓ(Y, Rf_* ℱ) ≅ RΓ(X, ℱ)` of [Stacks, Tag 01EZ].

```lean
noncomputable def derivedGlobalSectionsMap {G : Modules Y} {F : Modules X}
    (phi : G ⟶ (pushforward f).obj F) :
    (derivedModuleGlobalSections Y).obj
        ((DerivedCategory.Plus.singleFunctor (Modules Y) 0).obj G) ⟶
      (derivedModuleGlobalSectionsAlong f).obj
        ((DerivedCategory.Plus.singleFunctor (Modules X) 0).obj F)
```

## Tag 01FA, an equation

[Tag 01FA](https://stacks.math.columbia.edu/tag/01FA) in the Stacks Project.

**`Stacks.Cohomology.moduleCohomologyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/FunctorialityOfCohomology.lean#L196).

> **Stacks 01FA.**  An `f`-map `φ : 𝒢 ⟶ f_* ℱ` from an `𝒪_Y`-module `𝒢` to an `𝒪_X`-module
> `ℱ` induces the map on cohomology
>
> ```
> φ : H^i(Y, 𝒢) ⟶ H^i(X, ℱ)
> ```
>
> for every `i`, the target carrying its `Γ(Y, 𝒪_Y)`-module structure by restriction of scalars.
> It is `H^i` applied to the arrow `RΓ(Y, 𝒢) ⟶ RΓ(X, ℱ)` of [Stacks, Tag 01F9].

```lean
noncomputable def moduleCohomologyMap (i : ℤ) {G : Modules Y} {F : Modules X}
    (phi : G ⟶ (pushforward f).obj F) :
    (spaceModuleCohomology Y i).obj G ⟶ (moduleCohomologyAlong f i).obj F
```

## Tag 01FB, a remark

[Tag 01FB](https://stacks.math.columbia.edu/tag/01FB) in the Stacks Project.

**`Stacks.Cohomology.exists_pushforwardInjectiveResolutionLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean#L151). The attribute's comment: “the lift between injective resolutions”.

> **The commutative square labelled `(choice)` in [Stacks, Tag 01FB].** Given injective
> resolutions of `F[0]`, of `G[0]` and of the pushforward of the resolution of `F[0]`, the adjoint
> of an `f`-map lifts to a morphism between the latter two resolutions.

```lean
theorem exists_pushforwardInjectiveResolutionLift {G : Modules Y} {F : Modules X}
    (φ : (RingedSpaceModuleAdjunction.modulePullback f).obj G ⟶ F)
    (I : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules X) 0).obj F))
    (J : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules Y) 0).obj G))
    (J' : CochainComplex.InjectiveResolution (modulePushforwardComplex f I.cocomplex))
    [∀ n, Mono (J.ι.f n)] :
    ∃ β : J.cocomplex ⟶ J'.cocomplex,
      J.ι ≫ β =
        (CochainComplex.singleFunctor (Modules Y) 0).map
            (RingedSpaceModuleAdjunction.homEquiv f F G φ) ≫
          (HomologicalComplex.singleMapHomologicalComplex
              (RingedSpaceModuleAdjunction.modulePushforward f)
              (ComplexShape.up ℤ) 0).inv.app F ≫
          ((RingedSpaceModuleAdjunction.modulePushforward f).mapHomologicalComplex
              (ComplexShape.up ℤ)).map I.ι ≫ J'.ι
```

**`Stacks.Cohomology.quasiIso_moduleGlobalSections_map_pushforwardResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean#L178). The attribute's comment: “the quasi-isomorphism after taking sections”.

> **The right leg of the roof of [Stacks, Tag 01FB] is a quasi-isomorphism.** If `I⁼` is a
> complex of injective sheaves of modules on `X` and `J'⁼` is an injective resolution of its
> pushforward, then global sections on `Y` carry the resolution map to a quasi-isomorphism, hence
> to an isomorphism in the derived category.

```lean
theorem quasiIso_moduleGlobalSections_map_pushforwardResolution {F : Modules X}
    (I : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules X) 0).obj F))
    (J' : CochainComplex.InjectiveResolution (modulePushforwardComplex f I.cocomplex)) :
    QuasiIso (((moduleGlobalSections Y).mapHomologicalComplex (ComplexShape.up ℤ)).map J'.ι)
```

**`Stacks.Cohomology.injectiveResolutionGlobalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean#L211). The attribute's comment: “the roof representing the functorial map”. References: EGA 0 (12.1.4), “inj. resolution constr.”.

> **The representative of the functorial map on derived global sections afforded by choices
> of injective resolutions and a lift `β`**: it is the lower horizontal map of [Stacks, Tag 01FB]
> followed by the inverse of the vertical quasi-isomorphism.

```lean
noncomputable def injectiveResolutionGlobalSectionsMap {G : Modules Y} {F : Modules X}
    (φ : (RingedSpaceModuleAdjunction.modulePullback f).obj G ⟶ F)
    (I : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules X) 0).obj F))
    (J : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules Y) 0).obj G))
    (J' : CochainComplex.InjectiveResolution (modulePushforwardComplex f I.cocomplex))
    (β : J.cocomplex ⟶ J'.cocomplex)
    (_hβ : J.ι ≫ β =
      (CochainComplex.singleFunctor (Modules Y) 0).map
          (RingedSpaceModuleAdjunction.homEquiv f F G φ) ≫
        (HomologicalComplex.singleMapHomologicalComplex
            (RingedSpaceModuleAdjunction.modulePushforward f)
            (ComplexShape.up ℤ) 0).inv.app F ≫
        ((RingedSpaceModuleAdjunction.modulePushforward f).mapHomologicalComplex
            (ComplexShape.up ℤ)).map I.ι ≫ J'.ι) :
    DerivedCategory.Q.obj (moduleGlobalSectionsComplex Y J.cocomplex) ⟶
      DerivedCategory.Q.obj
        (moduleGlobalSectionsComplex Y (modulePushforwardComplex f I.cocomplex))
```

**`Stacks.Cohomology.derivedModuleGlobalSectionsMap_eq_injectiveResolutionGlobalSectionsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/DerivedGlobalSectionsViaResolutions.lean#L759). The attribute's comment: “identification with the canonical functorial map”. References: EGA 0 (12.1.4), “inj. resolution descr.”.

> **The roof of [Stacks, Tag 01FB] represents the canonical functorial map of
> [Stacks, Tag 01F9].** Read through the canonical identifications of `RΓ(Y, G)` with
> `Γ(Y, J⁼)` and of `RΓ(X, F)`, over `Γ(Y, 𝒪_Y)`, with `Γ(Y, f_* I⁼)`, the morphism
> `Stacks.Cohomology.derivedModuleGlobalSectionsMap` attached to the `f`-map `φ` is the roof
> `Stacks.Cohomology.injectiveResolutionGlobalSectionsMap` built from a lift `β` and the inverse
> of the quasi-isomorphism `Γ(Y, f_* I⁼) ⟶ Γ(Y, J'⁼)`. Both comparisons are built from `I.ι`,
> `J.ι` and the derived-functor units, so neither can be replaced by an arbitrary isomorphism,
> and `CategoryTheory.DerivedCategory.Plus.ι` displays the bounded-below objects in the
> unbounded derived category in which the roof was defined.

```lean
theorem derivedModuleGlobalSectionsMap_eq_injectiveResolutionGlobalSectionsMap
    {G : Modules Y} {F : Modules X}
    (φ : (RingedSpaceModuleAdjunction.modulePullback f).obj G ⟶ F)
    (I : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules X) 0).obj F))
    (J : CochainComplex.InjectiveResolution
      ((CochainComplex.singleFunctor (Modules Y) 0).obj G))
    (J' : CochainComplex.InjectiveResolution (modulePushforwardComplex f I.cocomplex))
    (β : J.cocomplex ⟶ J'.cocomplex)
    (hβ : J.ι ≫ β =
      (CochainComplex.singleFunctor (Modules Y) 0).map
          (RingedSpaceModuleAdjunction.homEquiv f F G φ) ≫
        (HomologicalComplex.singleMapHomologicalComplex
            (RingedSpaceModuleAdjunction.modulePushforward f)
            (ComplexShape.up ℤ) 0).inv.app F ≫
        ((RingedSpaceModuleAdjunction.modulePushforward f).mapHomologicalComplex
            (ComplexShape.up ℤ)).map I.ι ≫ J'.ι) :
    ((moduleGlobalSections Y).rightDerivedFunctorPlusInjectiveResolutionIso G J).hom ≫
        injectiveResolutionGlobalSectionsMap f φ I J J' β hβ =
      DerivedCategory.Plus.ι.map (derivedModuleGlobalSectionsMap f φ) ≫
        (derivedModuleGlobalSectionsAlongResolutionIso f I).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.14, Tag 01F7](https://stacks.math.columbia.edu/tag/01F7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
