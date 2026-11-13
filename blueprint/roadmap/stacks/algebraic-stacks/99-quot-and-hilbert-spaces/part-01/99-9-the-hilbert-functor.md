---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HilbertFamily, AlgebraicGeometry.Space.hilbertFunctor, AlgebraicGeometry.Space.hilbertFunctor_map_obj, AlgebraicGeometry.Space.HilbertFamilyOver, AlgebraicGeometry.Space.hilbertPresheaf, AlgebraicGeometry.Space.hilbertPresheafToBase, AlgebraicGeometry.Space.hasProperSupport_pushforwardStructureSheaf_iff, AlgebraicGeometry.Space.hilbertFamilyOfQuotConditions
statement: formalized
proof: formalized
---

# 99.9 The Hilbert functor

Section 99.9 of the Stacks Project, [Tag 0CZX](https://stacks.math.columbia.edu/tag/0CZX). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CZY, a situation

[Tag 0CZY](https://stacks.math.columbia.edu/tag/0CZY) in the Stacks Project.

**`AlgebraicGeometry.Space.HilbertFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean#L186). The attribute's comment: “families classified by the functor”.

> **Stacks 0CZY.** A family classified by the Hilbert functor of `f : X ⟶ Y` over a scheme `T`
> over `Y`: a closed subspace of the base change `X_T` which is of finite presentation, flat and
> proper over `T`.

```lean
structure HilbertFamily (f : X ⟶ Y) (T : SchemesOverPresheaf B S hS Y)
```

**`AlgebraicGeometry.Space.hilbertFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean#L289). The attribute's comment: “the Hilbert functor”.

> **Stacks 0CZY.** The *Hilbert functor* of `f : X ⟶ Y`: it sends a scheme `T` over `Y` to the
> set of closed subspaces of `X_T` which are of finite presentation, flat and proper over `T`, and a
> morphism of schemes over `Y` to base change of those subspaces.

```lean
def hilbertFunctor (f : X ⟶ Y) : (SchemesOverPresheaf B S hS Y)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.hilbertFunctor_map_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean#L302). The attribute's comment: “base change in the Hilbert functor”.

> **Stacks 0CZY.** The Hilbert functor acts by inverse image of closed subspaces along the
> transition maps of base changes.

```lean
theorem hilbertFunctor_map_obj (f : X ⟶ Y) {T T' : SchemesOverPresheaf B S hS Y} (g : T' ⟶ T)
    (z : HilbertFamily f T) :
    ((hilbertFunctor f).map g.op z).Z = z.Z.preimage (schemeBaseChangeMap f g)
```

**`AlgebraicGeometry.Space.HilbertFamilyOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean#L310). The attribute's comment: “families over the schemes of the site”.

> **Stacks 0CZY.** A family classified by the Hilbert functor, over a scheme of the big fppf site
> rather than over a scheme of `Y`: the morphism to `Y` it lies over, together with a family over the
> resulting scheme over `Y`.

```lean
structure HilbertFamilyOver (f : X ⟶ Y) (T : BigFppfOver B S hS)
```

**`AlgebraicGeometry.Space.hilbertPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean#L391). The attribute's comment: “the presheaf on the schemes of the site”.

> **Stacks 0CZY.** The Hilbert functor read as a presheaf on the schemes of the big fppf site: a
> section over `T` is a morphism `T ⟶ Y` together with a family over `T` for the resulting scheme
> over `Y`, and restriction pulls back both.

```lean
def hilbertPresheaf (f : X ⟶ Y) : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.hilbertPresheafToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctor.lean#L401). The attribute's comment: “the canonical morphism to the base”.

> **Stacks 0CZY.** The canonical morphism from the Hilbert presheaf to the base algebraic space
> `Y`, sending a family to the morphism to `Y` it lies over. Its target is the universe lift of `Y`
> because subfunctors of a presheaf on the site live one universe up.

```lean
def hilbertPresheafToBase (f : X ⟶ Y) : hilbertPresheaf f ⟶ Y.obj ⋙ uliftFunctor.{u + 1, u}
```

## Tag 0D00, a lemma

[Tag 0D00](https://stacks.math.columbia.edu/tag/0D00) in the Stacks Project.

**`AlgebraicGeometry.Space.hasProperSupport_pushforwardStructureSheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean#L168). The attribute's comment: “the proper-support entry of the dictionary, both directions”.

> **The proper-support entry of the dictionary of Stacks 0D00, in both directions.**  Let
> `g : X ⟶ T` be locally of finite type and let `Z ⊆ X` be a closed subspace with inclusion `i`.
> The module `i_*𝒪_Z` has support proper over `T` in the sense of Stacks 0CZD exactly when the
> composite `Z ⟶ T` is proper.

```lean
theorem hasProperSupport_pushforwardStructureSheaf_iff (g : X ⟶ T)
    (hg : IsLocallyOfFiniteType B S hS g.hom) :
    HasProperSupport B S hS X.property T.property g.hom hg
        ((SheafOfModules.toSheaf _).obj (pushforwardStructureSheaf B S hS X Z)) ↔
      IsProper B S hS (Z.1.ι ≫ g.hom)
```

**`AlgebraicGeometry.Space.hilbertFamilyOfQuotConditions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean#L388). The attribute's comment: “the converse construction: a quotient of the structure sheaf is a Hilbert family”.

> **Stacks 0D00, the converse construction.**  Let `f : X ⟶ Y` be a morphism of algebraic
> spaces of finite presentation, let `T` be a scheme of the site over `Y`, and let `W` be a closed
> subspace of the base change `X_T` with inclusion `i`.  If the quotient `𝒪_{X_T} ⟶ i_*𝒪_W` it
> determines is of finite presentation, is flat over `T` and has support proper over `T`, then `W`
> is a family classified by the Hilbert functor of `f` over `T`.

```lean
def hilbertFamilyOfQuotConditions (f : X ⟶ Y) (hf : IsFinitePresentation B S hS f.hom)
    (T : SchemesOverPresheaf B S hS Y)
    (W : ClosedSubspaces B S hS (schemeBaseChange f T))
    (hfpq : (pushforwardStructureSheaf B S hS
      (schemeBaseChangeSpace f T) W).IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS (schemeBaseChangeSpace f T).property
      (schemeBaseChangeProjectionHom B S hS f T).hom
      (pushforwardStructureSheaf B S hS (schemeBaseChangeSpace f T) W))
    (hproper : HasProperSupport B S hS (schemeBaseChangeSpace f T).property
      (schemeOverSpace T).property (schemeBaseChangeProjectionHom B S hS f T).hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS
        (isFinitePresentation_schemeBaseChangeProjection f hf T).1)
      ((SheafOfModules.toSheaf _).obj
        (pushforwardStructureSheaf B S hS (schemeBaseChangeSpace f T) W))) :
    HilbertFamily f T
```

**`AlgebraicGeometry.Space.exists_hilbertFamily_definingIdealSheaf_eq_of_quotConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean#L433). The attribute's comment: “the converse construction, from a quasi-coherent sheaf of ideals”.

> **Stacks 0D00, the converse construction from the sheaf of ideals.**  A sheaf of ideals
> `𝓘 ⊆ 𝒪_{X_T}` whose quotient `𝒪_{X_T}/𝓘` is of finite presentation, flat over `T` and with
> support proper over `T` is the defining ideal sheaf of a family classified by the Hilbert functor
> of `f` over `T`.

```lean
theorem exists_hilbertFamily_definingIdealSheaf_eq_of_quotConditions (f : X ⟶ Y)
    (hf : IsFinitePresentation B S hS f.hom) (T : SchemesOverPresheaf B S hS Y)
    (I : (SheafOfModules.unit
      (structureRingSheaf B S hS (schemeBaseChangeSpace f T))).Submodule)
    (hfpq : (cokernel I.ι : Modules.{u, u} B S hS (schemeBaseChangeSpace f T).1
      (schemeBaseChangeSpace f T).2).IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS (schemeBaseChangeSpace f T).property
      (schemeBaseChangeProjectionHom B S hS f T).hom
      (cokernel I.ι : Modules.{u, u} B S hS (schemeBaseChangeSpace f T).1
        (schemeBaseChangeSpace f T).2))
    (hproper : HasProperSupport B S hS (schemeBaseChangeSpace f T).property
      (schemeOverSpace T).property (schemeBaseChangeProjectionHom B S hS f T).hom
      (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS
        (isFinitePresentation_schemeBaseChangeProjection f hf T).1)
      ((SheafOfModules.toSheaf _).obj (cokernel I.ι :
        Modules.{u, u} B S hS (schemeBaseChangeSpace f T).1
          (schemeBaseChangeSpace f T).2))) :
    ∃ z : HilbertFamily f T,
      definingIdealSheaf B S hS (schemeBaseChangeSpace f T) ⟨z.Z, z.closed⟩ = I
```

**`AlgebraicGeometry.Space.exists_hilbertPresheafIso_quotSitePresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotFunctorEquality.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotFunctorEquality.lean#L279).

> In Situation 0CZY we have `Hilb_{X/B} = Quot_{𝒪_X/X/B}`: the Hilbert functor of `f` and the
> Quot functor of its structure sheaf are isomorphic presheaves on the schemes of the big fppf site,
> by an isomorphism over `Y`.

```lean
theorem exists_hilbertPresheafIso_quotSitePresheaf :
    ∃ e : hilbertPresheaf f ≅ (structureSheafQuotSituation f hf).quotSitePresheaf,
      e.hom ≫ (structureSheafQuotSituation f hf).quotSitePresheafToBase =
        hilbertPresheafToBase f
```

**`AlgebraicGeometry.Space.hilbertFamilySubobject_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotObjectwise.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotObjectwise.lean#L240). The attribute's comment: “the forward construction: a Hilbert family is a quotient of the structure sheaf”.

> The quotient of `F_T` that a family classified by the Hilbert functor of `f` over `T`
> determines lies in `Quot_{𝒪_X/X/B}(T)`: it is quasi-coherent, of finite presentation, flat over
> `T` and has support proper over `T`.

```lean
theorem hilbertFamilySubobject_mem (z : HilbertFamily f T) :
    hilbertFamilySubobject f hf T z ∈
      (structureSheafQuotSituation f hf).properlySupportedQuotients
        (structureSheafTestScheme T)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isFlatOver_pushforwardStructureSheaf_iff`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFamilyStructureSheafDictionary.lean#L258), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotObjectwise.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotObjectwise.lean#L76) (StacksFrontier): “the flatness entry of the dictionary, both directions”.
- [`isFinitePresentationOnSite_pushforwardStructureSheaf_hilbertFamily_unconditional`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isFinitePresentationOnSite_pushforwardStructureSheaf_hilbertFamily_unconditional#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotObjectwise.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertQuotObjectwise.lean#L79) (StacksFrontier): “the finite-presentation entry of the dictionary, for a Hilbert family”.

## Tag 0D3W, a lemma

[Tag 0D3W](https://stacks.math.columbia.edu/tag/0D3W) in the Stacks Project.

**`AlgebraicGeometry.Space.morEquivSpaceHilbertFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorPoints.lean, line 754](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorPoints.lean#L754). The attribute's comment: “the identification as a bijection, for an arbitrary algebraic space”.

> **Stacks 0D3W.** For an algebraic space `T` over `S` the morphisms of sheaves on the big fppf
> site of `S` from `T` into the Hilbert presheaf `Hilb_{X/Y}` of Stacks 0CZY are the pairs `(h, Z)`
> consisting of a morphism `h : T ⟶ Y` of algebraic spaces and a closed subspace `Z` of
> `X_T = X ×_{Y, h} T` which is of finite presentation, flat and proper over `T`.
>
> The source writes `=` between a set of morphisms of sheaves and a set of pairs; those are two
> different types here, so the honest reading is a bijection, and it is given as an `Equiv`, that
> is as data. Both directions are constructed: the forward map is
> `AlgebraicGeometry.Space.hilbertMorFamily`, which reads the morphism `h` off the canonical
> morphism to `Y` and glues the closed subspaces of the charts, and the inverse is
> `AlgebraicGeometry.Space.SpaceHilbertFamily.toMor`, which restricts a pair to every chart;
> nothing is chosen from an existence statement.
>
> The hypothesis `hloc` is the descent input `AlgebraicGeometry.Space.IsHilbertLocalOnBase`, which
> is all that the general case needs beyond the gluing proved here; it holds unconditionally when
> `T` is a scheme of the site.

```lean
def morEquivSpaceHilbertFamily (f : X ⟶ Y) (T : AlgebraicSpaces B S hS)
    (hloc : IsHilbertLocalOnBase f T) :
    (T.obj ⋙ uliftFunctor.{u + 1, u} ⟶ hilbertPresheaf f) ≃ SpaceHilbertFamily f T
```

**`AlgebraicGeometry.Space.morEquivSpaceHilbertFamilyOfScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorPoints.lean, line 781](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorPoints.lean#L781). The attribute's comment: “the identification for a scheme of the big fppf site, unconditionally”.

> **Stacks 0D3W for a scheme of the big fppf site.** The morphisms of sheaves from a scheme `U`
> of the site into the Hilbert presheaf `Hilb_{X/Y}` of Stacks 0CZY are the pairs `(h, Z)`
> consisting of a morphism `h : U ⟶ Y` of algebraic spaces and a closed subspace `Z` of
> `X_U = X ×_{Y, h} U` which is of finite presentation, flat and proper over `U`.
>
> This is `AlgebraicGeometry.Space.morEquivSpaceHilbertFamily` at the algebraic space of `U`, where
> the descent input is discharged by the identity chart, so nothing is assumed.

```lean
def morEquivSpaceHilbertFamilyOfScheme (f : X ⟶ Y) (U : BigFppfOver B S hS) :
    (uliftYoneda.{u + 1}.obj U ⟶ hilbertPresheaf f) ≃
      SpaceHilbertFamily f ⟨yoneda.obj U, isAlgebraicSpace_yoneda B S hS U⟩
```

**`AlgebraicGeometry.Space.morEquivSpaceHilbertFamilyOfAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorPointsDescent.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorPointsDescent.lean#L188). The attribute's comment: “the identification as a bijection, for an arbitrary algebraic space, unconditionally”.

> **The points of the Hilbert functor with values in an algebraic space.** In Situation 0CZY,
> for an algebraic space `T` over `S` the morphisms of sheaves on the big fppf site of `S` from `T`
> into the Hilbert presheaf `Hilb_{X/Y}` are the pairs `(h, Z)` consisting of a morphism `h : T ⟶ Y`
> of algebraic spaces and a closed subspace `Z` of `X_T = X ×_{Y, h} T` which is of finite
> presentation, flat and proper over `T`.
>
> The identification is a bijection, given as an `Equiv`; the finite presentation of `f` imposed by
> Situation 0CZY is not needed. The sheaf of `T` is lifted to the universe of `Hilb_{X/Y}`, which
> adds or loses no morphism.

```lean
def morEquivSpaceHilbertFamilyOfAlgebraicSpace (f : X ⟶ Y) (T : AlgebraicSpaces B S hS) :
    (T.obj ⋙ uliftFunctor.{u + 1, u} ⟶ hilbertPresheaf f) ≃ SpaceHilbertFamily f T
```

## Tag 0D01, a proposition

[Tag 0D01](https://stacks.math.columbia.edu/tag/0D01) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_hilbertPresheafModel_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorAlgebraicSpace.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorAlgebraicSpace.lean#L115).

> **Stacks 0D01.** For a morphism `f : X ⟶ B` of algebraic spaces over `S` which is of finite
> presentation and separated, the Hilbert functor `Hilb_{X/B}` of Stacks 0CZY is an algebraic space
> locally of finite presentation over `B`: there is a model of the Hilbert presheaf in the universe
> of the site which is an algebraic space and whose canonical morphism to `B` is locally of finite
> presentation.
>
> This is the source's deduction from Stacks 0D00 and Stacks 09TU, both of which are carried as
> hypotheses because neither is in the library. Stacks 09TU is `N` together with `halg` and `hlfp`:
> a model of the Quot presheaf of a situation on `f` which is an algebraic space whose morphism to
> `B` is locally of finite presentation. Stacks 0D00 is `e` together with `he`: an isomorphism of
> the Hilbert presheaf with that Quot presheaf, compatible with the two canonical morphisms to `B`.
> The source's standing hypotheses that `f` be of finite presentation and separated are recorded as
> `_hfp` and `_hsep`; the deduction itself does not consume them, since they enter through
> Stacks 09TU, which is carried. The content delivered is the transport: the Quot model is already a
> model of the Hilbert presheaf through `e`, and its morphism to `B` is the Hilbert one by
> `AlgebraicGeometry.Space.HilbertPresheafModel.toBase_eq_of_iso`.

```lean
theorem exists_hilbertPresheafModel_isAlgebraicSpace {X : AlgebraicSpaces B S hS}
    (D : QuotSituation B S hS) (f : X ⟶ D.Y)
    (_hfp : IsFinitePresentation B S hS f.hom) (_hsep : IsSeparated B S hS f.hom)
    (N : QuotSitePresheafModel D) (halg : IsAlgebraicSpace B S hS N.presheaf)
    (hlfp : IsLocallyOfFinitePresentation B S hS N.toBase)
    (e : hilbertPresheaf f ≅ D.quotSitePresheaf)
    (he : e.hom ≫ D.quotSitePresheafToBase = hilbertPresheafToBase f) :
    ∃ M : HilbertPresheafModel f,
      IsAlgebraicSpace B S hS M.presheaf ∧
        IsLocallyOfFinitePresentation B S hS M.toBase
```

**`AlgebraicGeometry.Space.exists_hilbertPresheafModel_isAlgebraicSpace_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorAlgebraicSpaceOfSeparated.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorAlgebraicSpaceOfSeparated.lean#L52).

> Let `S` be a scheme and `f : X ⟶ Y` a morphism of algebraic spaces over `S`. If `f` is of
> finite presentation and separated, then the Hilbert functor `Hilb_{X/Y}` of Stacks 0CZY is an
> algebraic space locally of finite presentation over `Y`: it has a model in the universe of the
> site which is an algebraic space whose canonical morphism to `Y` is locally of finite
> presentation.

```lean
theorem exists_hilbertPresheafModel_isAlgebraicSpace_of_isSeparated
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hfp : IsFinitePresentation B S hS f.hom) (hsep : IsSeparated B S hS f.hom) :
    ∃ M : HilbertPresheafModel f,
      IsAlgebraicSpace B S hS M.presheaf ∧ IsLocallyOfFinitePresentation B S hS M.toBase
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.9, Tag 0CZX](https://stacks.math.columbia.edu/tag/0CZX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
