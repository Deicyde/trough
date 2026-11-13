---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpace, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isRepresentableCFG, AlgebraicGeometry.isRepresentableByAlgebraicSpace_iff, AlgebraicGeometry.Stack.morphismSpaceEquiv, AlgebraicGeometry.Stack.existsUnique_twoIso_of_morphismSpaceEquiv_eq, AlgebraicGeometry.Stack.morphismSpaceEquiv_map, AlgebraicGeometry.Space.eq_inducedSpacesHom_iff_forall_sectionOfObj, AlgebraicGeometry.Stack.morphismSpaceEquiv_eq_inducedSpaceMap
statement: formalized
proof: formalized
---

# 94.8 Categories fibred in groupoids representable by algebraic spaces

Section 94.8 of the Stacks Project, [Tag 02ZV](https://stacks.math.columbia.edu/tag/02ZV). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02ZV, the section

[Tag 02ZV](https://stacks.math.columbia.edu/tag/02ZV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Representability.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean#L35) (StacksFrontier): “representable by an algebraic space”.
- [`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isRepresentableCFG`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaAlgebraicSpaceSources.lean#L120), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean#L37) (StacksFrontier): “a representable category fibred in groupoids is representable by an algebraic space”.
- [`AlgebraicGeometry.isRepresentableByAlgebraicSpace_iff`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableBySpace/Characterization.lean#L600), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean#L39) (StacksFrontier): “characterization by setoid fibres”.
- [`AlgebraicGeometry.Stack.morphismSpaceEquiv`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean#L41) (StacksFrontier): “1-morphisms up to 2-isomorphism are morphisms of algebraic spaces”.
- [`AlgebraicGeometry.Stack.existsUnique_twoIso_of_morphismSpaceEquiv_eq`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean#L177), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableByAlgebraicSpacesSection.lean#L43) (StacksFrontier): “uniqueness of the 1-morphism up to unique 2-isomorphism”.

## Tag 04SV, a definition

[Tag 04SV](https://stacks.math.columbia.edu/tag/04SV) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Representability.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Representability.lean#L66).

> **Stacks 04SV.** A category fibred in groupoids over the big fppf site of `S` is
> *represented by an algebraic space* over `S` if it is equivalent, over that site, to the
> category of elements of the sheaf of points of an algebraic space over `S`.

```lean
abbrev IsRepresentableByAlgebraicSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)) : Prop
```

## Tag 02ZX, a lemma

[Tag 02ZX](https://stacks.math.columbia.edu/tag/02ZX) in the Stacks Project.

**`AlgebraicGeometry.isRepresentableByAlgebraicSpace_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableBySpace/Characterization.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableBySpace/Characterization.lean#L600).

> **Stacks 02ZX.** A category fibred in groupoids over the big fppf site
> is represented by an algebraic space precisely when its fibres are setoids
> and its presheaf of isomorphism classes is an algebraic space.

```lean
public theorem isRepresentableByAlgebraicSpace_iff
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, v, u + 1, w} (AlgebraicGeometry.BigFppfOver B S hS)) :
    AlgebraicGeometry.IsRepresentableByAlgebraicSpace B S hS 𝒳 ↔
      (𝒳.val.p.IsFiberedInSetoids ∧ IsAlgebraicSpaceIsoClassPresheaf B S hS 𝒳)
```

## Tag 04SW, an equation

[Tag 04SW](https://stacks.math.columbia.edu/tag/04SW) in the Stacks Project.

**`AlgebraicGeometry.Stack.morphismSpaceEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean#L72). The attribute's comment: “equivalence of morphism spaces”.

> **Stacks 04SW.** One-morphisms of categories fibred in groupoids represented by `F` and `G`,
> modulo two-isomorphism, are morphisms `F ⟶ G` of the representing presheaves.

```lean
noncomputable def morphismSpaceEquiv
    (eX : StacksRepresentableCFG.EquivalenceOver
      𝒳.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
    (eY : StacksRepresentableCFG.EquivalenceOver
      𝒴.val.p (presheafOfCategories (G ⋙ typeToCat)).p) :
    Quotient (Functor.twoIsoSetoid 𝒳.val.p 𝒴.val.p) ≃ (F ⟶ G)
```

**`AlgebraicGeometry.Stack.morphismSpaceEquiv_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean#L109). The attribute's comment: “induced map on fibre isomorphism classes”.

> **Stacks 04SW.** On every fibre, the forward direction of
> `AlgebraicGeometry.Stack.morphismSpaceEquiv` is the map induced by the given one-morphism on
> isomorphism classes of objects.

```lean
theorem morphismSpaceEquiv_map
    (eX : StacksRepresentableCFG.EquivalenceOver
      𝒳.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
    (eY : StacksRepresentableCFG.EquivalenceOver
      𝒴.val.p (presheafOfCategories (G ⋙ typeToCat)).p)
    (f : {H : 𝒳.val.obj ⥤ 𝒴.val.obj // H ⋙ 𝒴.val.p = 𝒳.val.p})
    (U : BigFppfOver B S hS) (a : F.obj (op U)) :
    letI : 𝒳.val.p.IsFibered := 𝒳.2.isFibered
    letI : 𝒴.val.p.IsFibered := 𝒴.2.isFibered
    ((Functor.isoClassMap
      (Functor.isFibredOneMorphism_of_isFiberedInGroupoids 𝒴.2 f.2)).app (op U))
      (Functor.isoClassMk 𝒳.val.p
        ((Functor.fiberFunctorOfCompEq eX.inv.w U).obj
          (⟨⟨U, Discrete.mk a⟩, rfl⟩ :
            (presheafOfCategories (F ⋙ typeToCat)).p.Fiber U))) =
    Functor.isoClassMk 𝒴.val.p
      ((Functor.fiberFunctorOfCompEq eY.inv.w U).obj
        (⟨⟨U, Discrete.mk
          ((morphismSpaceEquiv B S hS 𝒳 𝒴 F G eX eY (Quotient.mk _ f)).app
            (op U) a)⟩, rfl⟩ :
          (presheafOfCategories (G ⋙ typeToCat)).p.Fiber U))
```

**`AlgebraicGeometry.Stack.existsUnique_twoIso_of_morphismSpaceEquiv_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpace.lean#L177). The attribute's comment: “uniqueness up to unique two-isomorphism”.

> **Stacks 04SW.** Two one-morphisms inducing the same morphism of representing presheaves
> admit a unique two-isomorphism over the site.

```lean
theorem existsUnique_twoIso_of_morphismSpaceEquiv_eq
    (eX : StacksRepresentableCFG.EquivalenceOver
      𝒳.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
    (eY : StacksRepresentableCFG.EquivalenceOver
      𝒴.val.p (presheafOfCategories (G ⋙ typeToCat)).p)
    (f g : {H : 𝒳.val.obj ⥤ 𝒴.val.obj // H ⋙ 𝒴.val.p = 𝒳.val.p})
    (h : morphismSpaceEquiv B S hS 𝒳 𝒴 F G eX eY (Quotient.mk _ f) =
      morphismSpaceEquiv B S hS 𝒳 𝒴 F G eX eY (Quotient.mk _ g)) :
    ∃! α : f.1 ≅ g.1,
      ∀ x : 𝒳.val.obj, 𝒴.val.p.IsHomLift (𝟙 (𝒳.val.p.obj x)) (α.hom.app x)
```

**`AlgebraicGeometry.Space.eq_inducedSpacesHom_iff_forall_sectionOfObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpaceInduced.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpaceInduced.lean#L199). The attribute's comment: “the morphism of algebraic spaces determined by a 1-morphism, characterised on named sections”.

> **Stacks 04SW.** A morphism `g : X ⟶ Y` of algebraic spaces is the one determined by a
> 1-morphism `f : 𝒳 ⥤ 𝒴` over the site if and only if it carries the section of `X` named by every
> object `z` of `𝒳` to the section of `Y` named by `f z`.
>
> This is the identification of Stacks 04SW stated as a property of a *given* morphism of algebraic
> spaces: it is what pins a morphism of algebraic spaces appearing as a free parameter against a
> 1-morphism appearing as another, which is the compatibility a statement about "the induced
> morphism of algebraic spaces" presupposes. The right-hand condition is the recipe of the source —
> an object of `𝒳` over `U` is a section of `X` over `U`, and `f` of it is a section of `Y` over
> `U` — and the left-hand side is
> `AlgebraicGeometry.Space.inducedSpacesHom`, the morphism of algebraic spaces that recipe
> defines.
>
> The hypotheses are those of the source: `X` and `Y` are algebraic spaces, and `eF`, `eG` are the
> equivalences over the site exhibiting `𝒳` and `𝒴` as representable by them. Being equivalent
> over the site to a category of elements already makes `p` and `q` fibred in groupoids, so no
> such hypothesis is carried.

```lean
theorem eq_inducedSpacesHom_iff_forall_sectionOfObj
    (eF : StacksRepresentableCFG.EquivalenceOver p
      (presheafOfCategories (X.1 ⋙ typeToCat)).p)
    (eG : StacksRepresentableCFG.EquivalenceOver q
      (presheafOfCategories (Y.1 ⋙ typeToCat)).p)
    (f : 𝒳 ⥤ 𝒴) (hf : f ⋙ q = p) (g : X ⟶ Y) :
    g = inducedSpacesHom B S hS p q eF eG f hf ↔
      ∀ (z : 𝒳) (W : BigFppfOver B S hS) (h : p.obj z = W),
        g.hom.app (op W) (PresheafOfCategories.sectionOfObj eF z h) =
          PresheafOfCategories.sectionOfObj eG (f.obj z)
            ((Functor.congr_obj hf z).trans h)
```

**`AlgebraicGeometry.Stack.morphismSpaceEquiv_eq_inducedSpaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpaceInduced.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpaceInduced.lean#L241). The attribute's comment: “the bijection is the morphism of representing presheaves induced by the 1-morphism”.

> **Stacks 04SW.** The bijection of morphism spaces takes the 2-isomorphism class of a
> 1-morphism `Φ : 𝒳 ⥤ 𝒴` over the site to the morphism of representing presheaves that `Φ`
> induces: the section of `G` attached to a section of `F` is the one named by the image under `Φ`
> of the object naming it.
>
> So the abstract identification `AlgebraicGeometry.Stack.morphismSpaceEquiv` and the explicit
> construction `AlgebraicGeometry.Space.inducedSpaceMap` of Stacks 0GQA are the same map, and a
> compatibility expressed through the latter — as
> `AlgebraicGeometry.Space.eq_inducedSpacesHom_iff_forall_sectionOfObj` expresses it — is a
> compatibility with the former.
>
> Both sides are computed on named sections: the left by
> `AlgebraicGeometry.Stack.morphismSpaceEquiv_app_sectionOfObj`, the right by
> `AlgebraicGeometry.Space.inducedSpaceMap_app_sectionOfObj`, and a morphism of representing
> presheaves is determined by those values.

```lean
theorem morphismSpaceEquiv_eq_inducedSpaceMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, w} (BigFppfOver B S hS))
    (F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (eX : StacksRepresentableCFG.EquivalenceOver
      𝒳.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
    (eY : StacksRepresentableCFG.EquivalenceOver
      𝒴.val.p (presheafOfCategories (G ⋙ typeToCat)).p)
    (Φ : {H : 𝒳.val.obj ⥤ 𝒴.val.obj // H ⋙ 𝒴.val.p = 𝒳.val.p}) :
    morphismSpaceEquiv B S hS 𝒳 𝒴 F G eX eY (Quotient.mk _ Φ) =
      Space.inducedSpaceMap B S hS F G 𝒳.val.p 𝒴.val.p eX eY Φ.1 Φ.2
```

**`AlgebraicGeometry.Stack.morphismSpaceEquiv_app_sectionOfObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpaceSections.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/MorphismSpaceSections.lean#L68). The attribute's comment: “value of the induced morphism on a named section”.

> **Stacks 04SW.** The morphism `F ⟶ G` of representing presheaves induced by a 1-morphism `Φ`
> over the site carries the section of `F` named by an object `z` of `𝒳` to the section of `G`
> named by `Φ z`.

```lean
theorem morphismSpaceEquiv_app_sectionOfObj
    (Φ : {H : 𝒳.val.obj ⥤ 𝒴.val.obj // H ⋙ 𝒴.val.p = 𝒳.val.p})
    (z : 𝒳.val.obj) {W : BigFppfOver B S hS} (h : 𝒳.val.p.obj z = W) :
    (morphismSpaceEquiv B S hS 𝒳 𝒴 F G eX eY (Quotient.mk _ Φ)).app (op W)
        (PresheafOfCategories.sectionOfObj eX z h) =
      PresheafOfCategories.sectionOfObj eY (Φ.1.obj z) ((Functor.congr_obj Φ.2 z).trans h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.8, Tag 02ZV](https://stacks.math.columbia.edu/tag/02ZV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
