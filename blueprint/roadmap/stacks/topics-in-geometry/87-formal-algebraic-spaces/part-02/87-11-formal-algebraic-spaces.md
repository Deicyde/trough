---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.formalAlgebraicSpaces_discussion, AlgebraicGeometry.FormalSpace.IsFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.relativelyRepresentable_diag_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_diag_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_diag_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.relative_isSeparated_diag_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.relativelyRepresentable_diag_of_isAffineFormal, AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_diag_of_isAffineFormal
statement: formalized
proof: formalized
---

# 87.11 Formal algebraic spaces

Section 87.11 of the Stacks Project, [Tag 0AIL](https://stacks.math.columbia.edu/tag/0AIL). 6 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AIL, the section

[Tag 0AIL](https://stacks.math.columbia.edu/tag/0AIL) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.formalAlgebraicSpaces_discussion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalAlgebraicSpaceSanityChecks.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalAlgebraicSpaceSanityChecks.lean#L188). The attribute's comment: “the unnumbered discussion of Definition 0AIM in the section: an affine formal algebraic space is a formal algebraic space; the members of a family as in Definition 0AIM are representable by schemes; surjectivity of the map from the coproduct as a map of sheaves may be replaced by surjectivity (Bootstrap, Lemma 04S1). Also records that an affine formal algebraic space is quasi-compact”.

> **Stacks 0AIL**, the discussion following Definition 0AIM in Section 87.11, "Formal algebraic
> spaces". Over a scheme `S` contained in a big fppf site:
>
> 1. *(sanity check)* every affine formal algebraic space is a formal algebraic space;
> 2. in the situation of Definition 0AIM — a family of maps `fᵢ : Xᵢ ⟶ X` of fppf sheaves whose
>    sources are affine formal algebraic spaces and which are representable by algebraic spaces
>    and étale — every `fᵢ` is representable by schemes, that is, by objects of the site
>    (Lemma 0AIG);
> 3. *(Bootstrap, Lemma 04S1)* Definition 0AIM is unchanged if the requirement that `∐ Xᵢ ⟶ X` be
>    surjective as a map of sheaves is replaced by the requirement that it be surjective, meaning
>    that each of its base changes along a scheme of the site mapping to `X` is surjective.
>
> The last conjunct records that an affine formal algebraic space is moreover a quasi-compact
> formal algebraic space (Definition 0AJA, through condition (3) of Lemma 0AJ9), its identity being
> a surjective representable étale chart.

```lean
theorem formalAlgebraicSpaces_discussion :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    (∀ X : FppfSheaf B S hS,
      IsAffineFormalAlgebraicSpace B S hS X → IsFormalAlgebraicSpace B S hS X) ∧
    (∀ (X : FppfSheaf B S hS) (I : Type (u + 1)) (Xi : I → FppfSheaf B S hS)
      (f : ∀ i, Xi i ⟶ X), (∀ i, IsAffineFormalAlgebraicSpace B S hS (Xi i)) →
      (∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f i).hom,
        Space.HasPropertyULift.{u + 1} B S hS
          (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) (f i).hom hfi) →
      ∀ i, uliftYoneda.{u + 1}.relativelyRepresentable (f i).hom) ∧
    (∀ X : FppfSheaf B S hS,
      IsFormalAlgebraicSpace B S hS X ↔
        SatisfiesSetTheoreticCondition B S hS X ∧
          ∃ (I : Type (u + 1)) (Xi : I → FppfSheaf B S hS) (f : ∀ i, Xi i ⟶ X),
            (∀ i, IsAffineFormalAlgebraicSpace B S hS (Xi i)) ∧
            (∀ i, ∃ hfi : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (f i).hom,
              Space.HasPropertyULift.{u + 1} B S hS
                (fun _ _ g ↦ Space.IsEtaleULift.{u + 1} B S hS g.hom) (f i).hom hfi) ∧
            IsSurjectiveOnSchemeBaseChanges B S hS (Sigma.desc f)) ∧
    (∀ X : FppfSheaf B S hS,
      IsAffineFormalAlgebraicSpace B S hS X → IsQuasiCompactSpace B S hS X)
```

## Tag 0AIM, a definition

[Tag 0AIM](https://stacks.math.columbia.edu/tag/0AIM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsFormalAlgebraicSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Defs.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Defs.lean#L50).

> An fppf sheaf on the big fppf site of `S` is a *formal algebraic space* over `S` when it
> satisfies the set-theoretic condition of Stacks 0AIS and admits an atlas by affine formal
> algebraic spaces: a family of maps into it whose sources are affine formal algebraic spaces,
> each of which is representable by algebraic spaces and étale, and whose induced map from the
> coproduct is a surjection of sheaves.

```lean
abbrev IsFormalAlgebraicSpace (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : FppfSheaf B S hS) : Prop
```

## Tag 0AIP, a lemma

[Tag 0AIP](https://stacks.math.columbia.edu/tag/0AIP) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_diag_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1010). The attribute's comment: “representable by schemes, for an arbitrary formal algebraic space”.

> **Stacks 0AIP, representability, for an arbitrary formal algebraic space:** the absolute
> diagonal of a formal algebraic space over `S` is representable by objects of the big fppf site
> of `S`.
>
> The diagonal is representable exactly when every morphism into the space from a sheaf
> represented by an object of the site is, and that is
> `AlgebraicGeometry.FormalSpace.hasRepresentableRelativeProducts_of_isFormalAlgebraicSpace`.

```lean
theorem relativelyRepresentable_diag_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (diag X)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_diag_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1164). The attribute's comment: “locally of finite type, for an arbitrary formal algebraic space”.

> **Stacks 0AIP, local finite type, for an arbitrary formal algebraic space:** every
> represented base change of the absolute diagonal of a formal algebraic space over `S` is a
> locally of finite type morphism of objects of the big fppf site of `S`.
>
> This is the assertion on underlying presheaves,
> `…relative_locallyOfFiniteType_diag_hom_of_isFormalAlgebraicSpace`, transported to the sheaf
> category, which is where Stacks 0AIP and Stacks 0AN2 are stated.

```lean
theorem relative_locallyOfFiniteType_diag_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_diag_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1182). The attribute's comment: “locally quasi-finite, for an arbitrary formal algebraic space”.

> **Stacks 0AIP, local quasi-finiteness, for an arbitrary formal algebraic space:** every
> represented base change of the absolute diagonal of a formal algebraic space over `S` is a
> locally quasi-finite, locally of finite type morphism of schemes.
>
> The base change is locally of finite type by
> `…relative_locallyOfFiniteType_diag_of_isFormalAlgebraicSpace` and a monomorphism because the
> diagonal is, and a monomorphism of schemes locally of finite type is locally quasi-finite, which
> is **Stacks 0CT8**.

```lean
theorem relative_locallyQuasiFinite_diag_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

**`AlgebraicGeometry.FormalSpace.relative_isSeparated_diag_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 1205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L1205). The attribute's comment: “separated, for an arbitrary formal algebraic space”.

> **Stacks 0AIP, separatedness, for an arbitrary formal algebraic space:** every represented
> base change of the absolute diagonal of a formal algebraic space over `S` is a separated
> morphism of schemes.
>
> This one needs only the representability assertion: the base change is a monomorphism because
> the diagonal is, and a monomorphism of schemes is separated.

```lean
theorem relative_isSeparated_diag_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} (hX : IsFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_diag_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L199). The attribute's comment: “representable by schemes, for an affine formal algebraic space”.

> The absolute diagonal of an affine formal algebraic space is representable by objects of the
> site.

```lean
theorem relativelyRepresentable_diag_of_isAffineFormal {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable (diag X)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_diag_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L207). The attribute's comment: “locally quasi-finite, for an affine formal algebraic space”.

> Every represented base change of the absolute diagonal of an affine formal algebraic space is
> a locally quasi-finite, locally of finite type morphism of schemes.

```lean
theorem relative_locallyQuasiFinite_diag_of_isAffineFormal {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_diag_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L222). The attribute's comment: “locally of finite type, for an affine formal algebraic space”.

> Every represented base change of the absolute diagonal of an affine formal algebraic space is
> a locally of finite type morphism of schemes.

```lean
theorem relative_locallyOfFiniteType_diag_of_isAffineFormal {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

**`AlgebraicGeometry.FormalSpace.relative_isSeparated_diag_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L234). The attribute's comment: “separated, for an affine formal algebraic space”.

> Every represented base change of the absolute diagonal of an affine formal algebraic space is
> a separated morphism of schemes.

```lean
theorem relative_isSeparated_diag_of_isAffineFormal {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

**`AlgebraicGeometry.FormalSpace.mono_diag_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L247). The attribute's comment: “monomorphism, for an arbitrary formal algebraic space”.

> The absolute diagonal of a formal algebraic space over `S` is a monomorphism of fppf sheaves,
> which by **Stacks 0AQB** is what it is for a morphism of formal algebraic spaces to be a
> monomorphism.

```lean
theorem mono_diag_of_isFormalAlgebraicSpace {X : FppfSheaf B S hS}
    (_hX : IsFormalAlgebraicSpace B S hS X) : Mono (diag X)
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.instIsSplitMonoDiag`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.instIsSplitMonoDiag#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RelativeDiagonal.lean#L328) (StacksFrontier): “monomorphism”.

## Tag 0AIQ, a lemma

[Tag 0AIQ](https://stacks.math.columbia.edu/tag/0AIQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_isAlgebraicSpaceULift_of_isFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean, line 993](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DiagonalRepresentable.lean#L993). The attribute's comment: “for an arbitrary formal algebraic space target, carrying nothing: the representable-relative-products hypothesis is discharged by this module's own Stacks 0AIP”.

> **Stacks 0AIQ for an arbitrary formal algebraic space target.** A morphism of fppf sheaves
> whose source is an algebraic space over `S` and whose target is a formal algebraic space over `S`
> is representable by algebraic spaces.
>
> This carries nothing. `isRepresentableByAlgebraicSpacesULift_of_isAlgebraicSpaceULift`
> (`MapsFromAlgebraicSpace`) states the implication with the target's representable relative
> products as a hypothesis, and that hypothesis is the theorem above -- the representability
> assertion of **Stacks 0AIP**. It is stated here rather than beside that theorem because
> `MapsFromAlgebraicSpace` lies in this module's import closure and not conversely, so the
> discharge can only be written downstream.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_isAlgebraicSpaceULift_of_isFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : Space.IsAlgebraicSpaceULift.{u + 1} B S hS X.obj)
    (hY : IsFormalAlgebraicSpace B S hS Y) :
    Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom
```

**`AlgebraicGeometry.FormalSpace.isRepresentableByAlgebraicSpacesULift_of_isAlgebraicSpaceULift_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/MapsFromAlgebraicSpace.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/MapsFromAlgebraicSpace.lean#L134). The attribute's comment: “for a target which is an affine formal algebraic space, that being the case in which this library has Stacks 0AIP”.

> **Stacks 0AIQ** when the target is an affine formal algebraic space. A morphism of fppf
> sheaves from an algebraic space over `S` to an affine formal algebraic space over `S` is
> representable by algebraic spaces, the relative products of the target being representable by
> **Stacks 0AI8**.

```lean
theorem isRepresentableByAlgebraicSpacesULift_of_isAlgebraicSpaceULift_of_isAffineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : Space.IsAlgebraicSpaceULift.{u + 1} B S hS X.obj)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y) :
    Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom
```

## Tag 0AIR, a remark

[Tag 0AIR](https://stacks.math.columbia.edu/tag/0AIR) in the Stacks Project.

**`AlgebraicGeometry.full_formalSchemePointsFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean#L104). The attribute's comment: “fullness of the embedding by the functor of points, on all schemes”.

> The functor of points of formal schemes on the category of all schemes is full, with no size
> hypothesis.

```lean
instance full_formalSchemePointsFunctor : formalSchemePointsFunctor.{u}.Full
```

**`AlgebraicGeometry.fullyFaithfulFormalSchemePointsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean#L111). The attribute's comment: “the assignment 𝔛 ↦ h\_𝔛 is a fully faithful embedding of formal schemes into presheaves on schemes”.

> Taking the functor of points on the category of all schemes is a fully faithful embedding of
> the category of formal schemes into presheaves of sets on schemes.

```lean
noncomputable def fullyFaithfulFormalSchemePointsFunctor :
    formalSchemePointsFunctor.{u}.FullyFaithful
```

**`AlgebraicGeometry.faithful_formalSchemePointsFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean#L81). The attribute's comment: “faithfulness of the embedding by the functor of points, on all schemes”.

> The functor of points of formal schemes on the category of all schemes is faithful.

```lean
instance faithful_formalSchemePointsFunctor : formalSchemePointsFunctor.{u}.Faithful
```

**`AlgebraicGeometry.FormalSpace.relative_isOpenImmersion_openFormalSubschemePresheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean#L504). The attribute's comment: “the morphisms h\_\{𝔛ᵢ} ⟶ h\_𝔛 of an open covering are representable and open immersions”.

> **Stacks 0AIR, clause (4).** The morphism `h_{𝔛|_𝔘} ⟶ h_𝔛` of fppf sheaves on the big fppf
> site of `S` is representable and an open immersion: it is representable by morphisms of the
> site, and every morphism of the site representing a base change of it is an open immersion of
> schemes. Nothing is assumed of `𝔛`, of `𝔘` or of the base scheme `S`.
>
> The base change along a point `g` of `𝔛` over `T` is the inclusion of the open subscheme
> `g⁻¹(𝔘)` of `T`, which is `AlgebraicGeometry.FormalSpace.isPullback_chart`; any other morphism
> of the site representing the same base change differs from it by an isomorphism, the
> universe-lifted Yoneda embedding being fully faithful.

```lean
theorem relative_isOpenImmersion_openFormalSubschemePresheafHom :
    (MorphismProperty.inverseImage (@AlgebraicGeometry.IsOpenImmersion.{u} :
        MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS)).relative
      (uliftYoneda.{u + 1}) (openFormalSubschemePresheafHom B S hS X V hV)
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_openFormalSubschemePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean#L612). The attribute's comment: “the charts h\_\{𝔛ᵢ} of an affine open covering are affine formal algebraic spaces”.

> **Stacks 0AIR, clause (3).** For a member `𝔛|_𝔘` of an affine open covering of `𝔛` — an open
> of `𝔛` whose restriction is isomorphic to the formal spectrum of an admissible topological ring
> `A` — the functor of points `h_{𝔛|_𝔘}` is an affine formal algebraic space over `S`.
>
> This is Stacks 0AIE,
> `AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_formalSchemePointsFppfSheaf`,
> transported along the chart isomorphism, the functor of points being a functor of the formal
> scheme. The source's own hypotheses are kept: the base is terminal, as the source assumes it is
> `Spec(ℤ)`, and the quotient spectra of `A` and their coproduct belong to the chosen big fppf
> site, which is the datum `D` and the condition `hB`.

```lean
theorem isAffineFormalAlgebraicSpace_openFormalSubschemePoints (hterm : IsTerminal S)
    (hA : TopologicalRing.IsAdmissible A) (D : QuotientSystem B S hS A) (hB : D.HasLargeSite)
    (e : (X.obj.restrict V).toPresheafedSpace ≅ (spfLTRS A hA.1).toPresheafedSpace) :
    IsAffineFormalAlgebraicSpace B S hS
      (formalSchemePointsFppfSheaf B S hS (openFormalSubscheme X V hV))
```

**`AlgebraicGeometry.FormalSpace.fullyFaithfulFormalSchemePointsFppfSheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean#L735). The attribute's comment: “the assignment 𝔛 ↦ h\_𝔛 is a fully faithful embedding of formal schemes into the fppf sheaves on the big fppf site of the base”.

> **Stacks 0AIR, clause (2).** The assignment `𝔛 ↦ h_𝔛` is a fully faithful embedding of the
> category of formal schemes into the category `AlgebraicGeometry.FormalSpace.FppfSheaf B S hS`
> of fppf sheaves on the big fppf site of `S` — the category in which formal algebraic spaces over
> `S` live, and the one the comparison of Stacks 0AIR is about.
>
> The source's "modulo set theoretic issues" is the restriction of the source category to the
> formal schemes whose affine chart quotients belong to the big fppf site, which is the size
> condition of Stacks 0AI1 for the site's cutoff, and the source's assumption that the base is
> `Spec(ℤ)` is the hypothesis `hterm`. Both halves are Stacks 0AI1 read on the site:
> `AlgebraicGeometry.FormalSpace.injective_map_formalSchemePointsFppfSheafFunctor` and
> `AlgebraicGeometry.FormalSpace.exists_map_eq_formalSchemePointsFppfSheafFunctor`.

```lean
def fullyFaithfulFormalSchemePointsFppfSheafFunctor (hterm : IsTerminal S) :
    (sizeBoundedFormalSchemePointsFppfSheafFunctor B S hS).FullyFaithful
```

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpaceFormalSchemePoints_of_affineCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean, line 811](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean#L811). The attribute's comment: “the functor of points of a formal scheme with an affine open covering is a formal algebraic space”.

> **Stacks 0AIR, clause (5).** The functor of points of a formal scheme à la EGA is a formal
> algebraic space over `S`, for a formal scheme admitting an open covering `𝔛 = ⋃ 𝔘_i` whose
> charts have affine formal algebraic space functors of points and whose own functor of points
> satisfies the set-theoretic condition of Stacks 0AIS.
>
> This is the last sentence of the source's remark. The family `{h_{𝔛|_{𝔘_i}} ⟶ h_𝔛}` is a family
> as in Definition 0AIM: the sources are affine formal algebraic spaces, which is the hypothesis
> `haff` supplied by
> `AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_openFormalSubschemePoints`; the
> arrows are representable open immersions, hence representable étale, which is
> `AlgebraicGeometry.FormalSpace.isRepresentableEtale_openFormalSubschemeSheafHom`; and the
> family is jointly surjective, which is
> `AlgebraicGeometry.FormalSpace.isLocallySurjective_sigmaDesc_openFormalSubschemeSheafHom`. The
> conclusion is then Stacks 0AJ1,
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_etaleCover`.
>
> The hypothesis `hset` is the source's "modulo set theoretic issues" in the precise form of
> Stacks 0AIS, and it is the only thing the source leaves to the reader here.

```lean
theorem isFormalAlgebraicSpaceFormalSchemePoints_of_affineCover
    (hcov : ∀ p : X.obj, ∃ i, p ∈ U i)
    (haff : ∀ i, IsAffineFormalAlgebraicSpace B S hS
      (formalSchemePointsFppfSheaf B S hS (openFormalSubscheme X (U i) (hU i))))
    (hset : SatisfiesSetTheoreticCondition B S hS (formalSchemePointsFppfSheaf B S hS X)) :
    IsFormalAlgebraicSpaceFormalSchemePoints B S hS X
```

**`AlgebraicGeometry.FormalSpace.fullyFaithfulComparableFormalSchemePointsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean, line 864](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonAtlas.lean#L864). The attribute's comment: “the category of formal schemes is equivalent to a full subcategory of the category of formal algebraic spaces”.

> **Stacks 0AIR, the comparison.** The category of formal schemes à la EGA is equivalent to a
> full subcategory of the category of formal algebraic spaces over `S`: the functor `𝔛 ↦ h_𝔛`
> from the formal schemes the comparison applies to into the formal algebraic spaces over `S` is
> fully faithful, so it is an equivalence onto the full subcategory on its image.
>
> This is the opening sentence of the source's remark. Its "modulo set theoretic issues" is the
> restriction of the source category to
> `AlgebraicGeometry.FormalSpace.comparableFormalSchemes`, and the source's assumption that the
> base is `Spec(ℤ)` is the hypothesis `hterm`. Full faithfulness is clause (2),
> `AlgebraicGeometry.FormalSpace.fullyFaithfulFormalSchemePointsFppfSheafFunctor`, and the
> functor lands in formal algebraic spaces by clause (5).

```lean
def fullyFaithfulComparableFormalSchemePointsFunctor (hterm : IsTerminal S) :
    (comparableFormalSchemePointsFunctor B S hS).FullyFaithful
```

**`AlgebraicGeometry.FormalSpace.isFppfSheafFormalSchemePoints_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonSheaf.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonSheaf.lean#L133). The attribute's comment: “the functor of points is an fppf sheaf, for a formal scheme that is a scheme”.

> **Stacks 0AIR**, the sheaf clause, for a formal scheme isomorphic to a scheme: its functor
> of points satisfies the fppf sheaf condition on the big fppf site of `S`, with no hypothesis
> assumed.
>
> The functor of points of a scheme seen as a formal scheme is the presheaf it represents and the
> fpqc topology is subcanonical, which is
> `AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints_of_iso`.

```lean
theorem isFppfSheafFormalSchemePoints_of_iso {X : FormalScheme.{u}} {Z : Scheme.{u}}
    (e : X ≅ schemeToFormalScheme.obj Z) : IsFppfSheafFormalSchemePoints B S hS X
```

**`AlgebraicGeometry.FormalSpace.isFppfSheafFormalSchemePoints_formalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonSheaf.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonSheaf.lean#L164). The attribute's comment: “the functor of points of an arbitrary formal scheme is an fppf sheaf”.

> **Stacks 0AIR**, the sheaf clause, for an *arbitrary* formal scheme: the functor of points
> of a formal scheme à la EGA satisfies the fppf sheaf condition on the big fppf site of `S`, with
> no hypothesis assumed.
>
> This is the first sentence of the source's remark, "by Lemma 87.2.2 the functor of points
> `h_𝔛` associated to a formal scheme `𝔛` is a sheaf in the fppf topology". It is
> `AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints`, the full statement of Stacks 0AI2,
> read on the big fppf site of `S` by
> `AlgebraicGeometry.FormalSpace.isFppfSheafFormalSchemePoints_of_isSheaf_fpqcTopology`.

```lean
theorem isFppfSheafFormalSchemePoints_formalScheme (X : FormalScheme.{u}) :
    IsFppfSheafFormalSchemePoints B S hS X
```

## Tag 0AIS, a remark

[Tag 0AIS](https://stacks.math.columbia.edu/tag/0AIS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.SatisfiesSetTheoreticCondition`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine.lean#L73). The attribute's comment: “the set-theoretic condition”.

> An fppf sheaf satisfies the *set-theoretic condition* when there is a representable sheaf
> surjecting onto it and a representable sheaf surjecting onto the kernel pair of that surjection.
> Representability is recorded by an isomorphism of underlying presheaves with a universe-lifted
> Yoneda presheaf.

```lean
abbrev SatisfiesSetTheoreticCondition (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_bounded_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/BoundedColimit.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/BoundedColimit.lean#L123). The attribute's comment: “bounded\_colimit”.

> **Stacks 0AIS, bounded colimit.** A directed colimit of affine fppf sheaves along
> thickenings satisfies the set-theoretic condition as soon as one cardinal `μ` below the size
> cutoff of the site bounds both the index and the size of every stage.
>
> The coproduct of the stages is then an object of the site — a coproduct of at most `μ` schemes
> of size at most `μ` has size at most `μ`, by `AlgebraicGeometry.schemeSize_coproduct_le` — and
> its universe-lifted representable sheaf is the coproduct of those of the stages, which is the
> hypothesis of `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_colimit`.
>
> Nothing is asked of the cofinality of the cutoff, and the index may be uncountable: the uniform
> bound dominates the supremum of the stage sizes outright.

```lean
theorem satisfiesSetTheoreticCondition_of_bounded_colimit
    {I : Type (u + 1)} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ BigAffineFppf B S hS)
    (hD : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      Stacks.Thickenings.IsThickening ((BigAffineFppf.toScheme B S hS).map (D.map f)))
    {μ : Cardinal.{u}} (hμ : μ < B.cutoff) (hI : #I ≤ Cardinal.lift.{u + 1, u} μ)
    (hstage : ∀ i : I, ((BigAffineFppf.toScheme B S hS).obj (D.obj i)).size ≤ μ)
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (hX : Nonempty (X ≅ colimit
      (D ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)))) :
    SatisfiesSetTheoreticCondition B S hS X
```

**`AlgebraicGeometry.FormalSpace.exists_representable_epi_of_countable_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountableAtlas.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountableAtlas.lean#L174). The attribute's comment: “observation (3), countable atlas”.

> **Stacks 0AIS, observation (3), first half.** Let `{Xᵢ ⟶ X}` be a family of maps of fppf
> sheaves over `S` satisfying conditions (1), (2) and (3) of Definition 0AIM, with a *countable*
> index. Then there is an object `U` of the big fppf site of `S` and a surjection of fppf sheaves
> from the sheaf it represents onto `X`.
>
> The surjection `Uᵢ ⟶ Xᵢ` from an object of the site onto each member of the family is the
> first half of the set-theoretic condition of Stacks 0AIS, which the hypothesis that `Xᵢ` is an
> affine formal algebraic space carries; countability makes the coproduct `U = ∐ Uᵢ` an object of
> the site, the size cutoff of a big fppf site having uncountable cofinality.

```lean
theorem exists_representable_epi_of_countable_atlas (X : FppfSheaf B S hS)
    {I : Type (u + 1)} [Countable I] (Xi : I → FppfSheaf B S hS) (f : ∀ i, Xi i ⟶ X)
    (hatlas : IsFormalAtlas B S hS X Xi f) :
    ∃ (U : BigFppfOver B S hS)
      (t : (BigFppfOver.topology B S hS).uliftYoneda.{u + 1}.obj U ⟶ X), Epi t
```

**`AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_countable_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountableAtlas.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountableAtlas.lean#L405). The attribute's comment: “observation (3)”.

> **Stacks 0AIS, observation (3).** Let `{Xᵢ ⟶ X}` be a family of maps of fppf sheaves over
> `S` satisfying conditions (1), (2) and (3) of Definition 0AIM with a *countable* index. Then
> `X` satisfies the set-theoretic condition of Stacks 0AIS.
>
> Countability provides the object `U` of the site surjecting onto `X`
> (`AlgebraicGeometry.FormalSpace.exists_representable_epi_of_countable_atlas`). For the relation
> it provides the second half as well. The kernel pair `U ×_X U` is covered by the family of
> fibre products `(U ×_X Xᵢ) ×_{Xᵢ} (U ×_X Xᵢ)`, one for each member of the atlas: that family
> is the base change of `U ×_X U` along the surjection `∐ Xᵢ ⟶ X` of condition (3), decomposed
> along the coproduct, coproducts of sheaves of sets being stable under base change. Each member
> is an algebraic space over `S` — this is the step of Stacks 0AIP available unconditionally in
> this library, `AlgebraicGeometry.FormalSpace.isAlgebraicSpaceULift_pullback_snd_pullback_snd` —
> and an algebraic space over `S` receives a surjection of sheaves from an *object of the site*,
> that being what its étale scheme atlas is by Definition 025Y. The coproduct of those atlases,
> one for each index, is an object of the site because the index is countable and the size cutoff
> of a big fppf site has uncountable cofinality; it is the required `R`.

```lean
theorem satisfiesSetTheoreticCondition_of_countable_atlas (X : FppfSheaf B S hS)
    {I : Type (u + 1)} [Countable I] (Xi : I → FppfSheaf B S hS) (f : ∀ i, Xi i ⟶ X)
    (hatlas : IsFormalAtlas B S hS X Xi f) :
    SatisfiesSetTheoreticCondition B S hS X
```

**`AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_countable_atlas_of_hasQuasiCompactDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountableAtlas.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountableAtlas.lean#L518). The attribute's comment: “observation (3), the source's quasi-compact diagonal”.

> **Stacks 0AIS, observation (3), as the source states it.** Let `{Xᵢ ⟶ X}` be a family of
> maps of fppf sheaves over `S` satisfying conditions (1), (2) and (3) of Definition 0AIM with a
> *countable* index, and let the diagonal of `X` be quasi-compact, that is, let `X` be
> quasi-separated over `S`. Then `X` satisfies the set-theoretic condition of Stacks 0AIS.
>
> Quasi-separatedness of `X` over `S` is quasi-compactness of the relative diagonal of its
> structure morphism in the sense of Stacks 0ARN part (2), the structure morphism being the
> morphism to the terminal object of the category of fppf sheaves on the big fppf site of `S`,
> whose relative self-product is therefore `X ×_S X`. It is the source's hypothesis, and the
> source is right that it suffices; it is not needed, and
> `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_countable_atlas` proves the
> same conclusion from the countable atlas alone. The reason is that the source bounds the size
> of the relation `R` by that of `U ×_S U`, for which it needs the diagonal to be tame, whereas
> the argument here never leaves the site: the relation is assembled from the étale scheme
> atlases of the members of a countable cover of `U ×_X U`, and those are objects of the site by
> the definition of an algebraic space.

```lean
theorem satisfiesSetTheoreticCondition_of_countable_atlas_of_hasQuasiCompactDiagonal
    (X : FppfSheaf B S hS) {I : Type (u + 1)} [Countable I] (Xi : I → FppfSheaf B S hS)
    (f : ∀ i, Xi i ⟶ X) (hatlas : IsFormalAtlas B S hS X Xi f)
    (hdiag : HasQuasiCompactDiagonal B S hS (terminal.from X)) :
    SatisfiesSetTheoreticCondition B S hS X
```

**`AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_countable_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountableColimit.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountableColimit.lean#L264). The attribute's comment: “countable\_colimit”.

> **Stacks 0AIS, countable colimit.** A countable directed colimit of affine fppf sheaves
> along thickenings satisfies the set-theoretic condition.
>
> Countability replaces the representability hypothesis on the coproduct of the stages in
> `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_colimit`: a countable
> coproduct is itself represented by an object of the big fppf site. What the argument uses is
> only that a countable index is admissible for coproducts in the site, so this is the countable
> case of `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_admissible_colimit`.

```lean
theorem satisfiesSetTheoreticCondition_of_countable_colimit (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {I : Type (u + 1)} [Preorder I] [Nonempty I]
    [IsDirected I (· ≤ ·)] [Countable I] (D : I ⥤ BigAffineFppf B S hS)
    (hD : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      Stacks.Thickenings.IsThickening ((BigAffineFppf.toScheme B S hS).map (D.map f)))
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (hX : Nonempty (X ≅ colimit
      (D ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)))) :
    SatisfiesSetTheoreticCondition B S hS X
```

**`AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_representable_over_affineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableOverAffineSetCondition.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RepresentableOverAffineSetCondition.lean#L155). The attribute's comment: “the condition for the source of a morphism to an affine formal algebraic space which is representable by algebraic spaces, which is the first conjunct of the conclusion of Stacks 0AJH”.

> **The set-theoretic condition of Stacks 0AIS for the source of a morphism to an affine
> formal algebraic space representable by algebraic spaces.** This is the first conjunct of the
> conclusion of **Stacks 0AJH**, discharged.
>
> The condition on `Y` supplies one object `U` of the site with `h_U ⟶ Y` a surjection of
> sheaves. The fibre product `W = h_U ×_Y X` is then an algebraic space over `S`, and `W ⟶ X` is
> a surjection of sheaves, so the étale scheme atlas `h_V ⟶ W` of `W` composes to a surjection
> `a : h_V ⟶ X` from a representable. That atlas is representable by objects of the site and
> `W ⟶ X` is a base change of `h_U ⟶ Y`, which is representable by objects of the site because an
> affine formal algebraic space has representable relative products (Stacks 0AI8); so `a` is
> representable by algebraic spaces, `h_V ×_X h_V` is an algebraic space by Stacks 03XY, and the
> étale scheme atlas of `h_V ×_X h_V` is the second half of the condition.

```lean
theorem satisfiesSetTheoreticCondition_of_representable_over_affineFormal
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom) :
    SatisfiesSetTheoreticCondition B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAlgebraicSpace_of_affineSchemeAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SchemeAtlas.lean, line 736](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SchemeAtlas.lean#L736). The attribute's comment: “observation (2)”.

> **Stacks 0AIS, observation (2), the sanity check.** A family `{Xᵢ ⟶ X}` as in
> Definition 0AIM — the set-theoretic condition included — in which every `Xᵢ` is an affine
> scheme makes `X` an algebraic space.
>
> The affine schemes of the family need not be objects of the chosen site; each is presented by
> its restricted functor of points, sheafified. The scheme atlas of the conclusion is assembled
> inside the chosen site rather than by descent from a larger one: the set-theoretic condition
> gives an object `U` of the site surjecting onto `X`, each `Xᵢ` is then represented by an affine
> object of the site of size at most that of `U`, and the coproduct of one such for each point of
> `U` is an object of the site because the size cutoff is a strong prelimit.
>
> The diagonal is not a hypothesis: the atlas assembled here is representable by objects of the
> site, so Stacks 0BGR gives the algebraic-space condition outright.

```lean
public theorem isAlgebraicSpace_of_affineSchemeAtlas
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : Sheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) (Type (u + 1)))
    (hX : AlgebraicGeometry.FormalSpace.IsFormalAlgebraicSpace B S hS X)
    (hAtlas :
      let J := AlgebraicGeometry.BigFppfOver.topology B S hS
      letI : HasColimitsOfSize.{u + 1, u + 1} (Sheaf J (Type (u + 1))) :=
        Sheaf.instHasColimitsOfSize
      ∃ (I : Type (u + 1)) (Xi : I → Sheaf J (Type (u + 1)))
        (f : ∀ i, Xi i ⟶ X),
        (∀ i, AlgebraicGeometry.FormalSpace.IsAffineFormalAlgebraicSpace B S hS (Xi i)) ∧
        (∀ i, ∃ (U : Over S), IsAffine U.left ∧
          Nonempty (Xi i ≅
            (presheafToSheaf J (Type (u + 1))).obj
              (Stacks.Groupoids.points (Over.post B.inclusion) U ⋙
                uliftFunctor.{u + 1, u}))) ∧
        (∀ i, ∃ hfi : AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpacesULift.{u + 1}
            B S hS (f i).hom,
          AlgebraicGeometry.Space.HasPropertyULift.{u + 1} B S hS
            (fun _ _ g ↦ AlgebraicGeometry.Space.IsEtaleULift.{u + 1} B S hS g.hom)
            (f i).hom hfi) ∧
        Sheaf.IsLocallySurjective (Sigma.desc f)) :
    AlgebraicGeometry.Space.IsAlgebraicSpaceULift.{u + 1} B S hS X.obj
```

**`AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_of_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SetTheoreticColimit.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SetTheoreticColimit.lean#L213). The attribute's comment: “colimit\_condition”.

> A directed colimit of affine fppf sheaves along thickenings satisfies the set-theoretic
> condition if the coproduct of its stages is representable in the big site.

```lean
public theorem satisfiesSetTheoreticCondition_of_colimit
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type (u + 1)} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ BigAffineFppf B S hS)
    (hD : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      Stacks.Thickenings.IsThickening
        ((BigAffineFppf.toScheme B S hS).map (D.map f)))
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (hX : Nonempty (X ≅ colimit
      (D ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))))
    (hU : ∃ (U : BigFppfOver B S hS)
      (F : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))),
      Nonempty (F.obj ≅ (uliftYoneda.{u + 1}).obj U) ∧
        Nonempty (F ≅ ∐ fun i : I ↦
          (Sheaf.sheafifiedYoneda
            (BigFppfOver.topology B S hS)).obj
              ((BigAffineFppf.inclusion B S hS).obj (D.obj i)))) :
    SatisfiesSetTheoreticCondition B S hS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.11, Tag 0AIL](https://stacks.math.columbia.edu/tag/0AIL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
