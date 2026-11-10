---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsElementaryDistinguishedSquare, AlgebraicGeometry.Space.isElementaryDistinguishedSquare_iff, AlgebraicGeometry.Space.isElementaryDistinguishedSquare_preimage, AlgebraicGeometry.Space.isElementaryDistinguishedSquare_openRestriction, AlgebraicGeometry.Space.isElementaryDistinguishedSquare_relocalizeRestrict, AlgebraicGeometry.Space.qcqs_induction_on, AlgebraicGeometry.Space.qcqs_induction_on_self, AlgebraicGeometry.Space.qcqs_induction_on_collection
statement: formalized
proof: formalized
---

# 75.9 Induction principle

Section 75.9 of the Stacks Project, [Tag 08GL](https://stacks.math.columbia.edu/tag/08GL). 6 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08GM, a definition

[Tag 08GM](https://stacks.math.columbia.edu/tag/08GM) in the Stacks Project.

**`AlgebraicGeometry.Space.IsElementaryDistinguishedSquare`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean#L100).

> **Stacks 08GM.** An open subspace `U` of an algebraic space `W` together with an étale
> morphism `f : V ⟶ W` which is an isomorphism over the reduced closed subspace on the
> complement of `U` form an *elementary distinguished square*.

```lean
structure IsElementaryDistinguishedSquare (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {W V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hW : IsAlgebraicSpace B S hS W) (U : Subfunctor W) (f : V ⟶ W) : Prop
```

**`AlgebraicGeometry.Space.isElementaryDistinguishedSquare_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean#L121). The attribute's comment: “characterization”.

> An elementary distinguished square is exactly an open subspace together with an étale
> morphism which is an isomorphism over the reduced closed complement of that subspace.

```lean
theorem isElementaryDistinguishedSquare_iff (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {W V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hW : IsAlgebraicSpace B S hS W) (U : Subfunctor W) (f : V ⟶ W) :
    IsElementaryDistinguishedSquare B S hS hW U f ↔
      (IsAlgebraicSpace B S hS V ∧ IsOpenSubspace B S hS U ∧ IsEtale B S hS f ∧
        ∃ hT : IsClosed (Set.range (pointsMap B S hS U.toFunctor U.ι))ᶜ,
          IsIso ((reducedClosedSubspace B S hS W hW
            (Set.range (pointsMap B S hS U.toFunctor U.ι))ᶜ hT).fromPreimage f))
```

## Tag 08GN, a lemma

[Tag 08GN](https://stacks.math.columbia.edu/tag/08GN) in the Stacks Project.

**`AlgebraicGeometry.Space.isElementaryDistinguishedSquare_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean#L165). The attribute's comment: “base_change”.

> **Stacks 08GN, part (2).** An elementary distinguished square stays elementary
> distinguished after base change along any morphism of algebraic spaces: the open subspace is
> replaced by its preimage and the étale morphism by its base change.

```lean
theorem isElementaryDistinguishedSquare_preimage (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    {W V W' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hW : IsAlgebraicSpace B S hS W)
    (hW' : IsAlgebraicSpace B S hS W') (U : Subfunctor W) (f : V ⟶ W)
    (h : IsElementaryDistinguishedSquare B S hS hW U f) (p : W' ⟶ W) :
    IsElementaryDistinguishedSquare B S hS hW' (U.preimage p) (Limits.pullback.snd f p)
```

**`AlgebraicGeometry.Space.isElementaryDistinguishedSquare_openRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean#L267). The attribute's comment: “open_restriction”.

> **Stacks 08GN, restriction to open subspaces.** Let `U ⊆ U'` be open subspaces of `W` and
> let `V'` be an open subspace of `V`. The union of the point set of `U'` with the image of the
> point set of `V'` is the point set of an open subspace `W'` of `W`; the morphism `V' ⟶ W`
> factors through `W'`, and the square formed by `U'` inside `W'` and that factorisation is
> again elementary distinguished.
>
> The union is described by its set of points rather than as the range of `V'.ι ≫ f`, which
> need not be an open subspace, and `U'` is presented inside `W'` as the range of the canonical
> inclusion `U' ⟶ W'`.

```lean
theorem isElementaryDistinguishedSquare_openRestriction (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    {W V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hW : IsAlgebraicSpace B S hS W)
    (U : Subfunctor W) (f : V ⟶ W)
    (hsq : IsElementaryDistinguishedSquare B S hS hW U f)
    (V' : Subfunctor V) (hV' : IsOpenSubspace B S hS V')
    (U' : Subfunctor W) (hU' : IsOpenSubspace B S hS U') (hUU' : U ≤ U') :
    ∃ (W' : Subfunctor W) (hW' : IsOpenSubspace B S hS W') (hU'W' : U' ≤ W')
      (f' : V'.toFunctor ⟶ W'.toFunctor),
      (Set.range (pointsMap B S hS W'.toFunctor W'.ι) =
        Set.range (pointsMap B S hS U'.toFunctor U'.ι) ∪
          Set.range (pointsMap B S hS V'.toFunctor (V'.ι ≫ f))) ∧
      (f' ≫ W'.ι = V'.ι ≫ f) ∧
      IsElementaryDistinguishedSquare B S hS hW'.1
        (Subfunctor.range (Subfunctor.homOfLe hU'W')) f'
```

**`AlgebraicGeometry.Space.isElementaryDistinguishedSquare_relocalizeRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ElementaryDistinguishedSquare.lean#L701). The attribute's comment: “scheme_change”.

> **Stacks 08GN, change of base scheme.** An elementary distinguished square over `S` stays
> elementary distinguished after restriction along a morphism `g : S' ⟶ S` of the site: the open
> subspace is replaced by the image of the restricted inclusion and the étale morphism by its
> restriction.

```lean
theorem isElementaryDistinguishedSquare_relocalizeRestrict (B : BigFppfSite.{u})
    (S S' : Scheme.{u}) (hS : B.Contains S) (hS' : B.Contains S')
    (g : B.obj hS' ⟶ B.obj hS) {W V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hW : IsAlgebraicSpace B S hS W) (U : Subfunctor W) (f : V ⟶ W)
    (h : IsElementaryDistinguishedSquare B S hS hW U f) :
    IsElementaryDistinguishedSquare B S' hS'
      (isAlgebraicSpace_relocalizeRestrict B S' S hS' hS g W hW)
      (Subfunctor.range ((OverShriek.relocalizeRestrict g).map U.ι))
      ((OverShriek.relocalizeRestrict g).map f)
```

## Tag 08GP, a lemma

[Tag 08GP](https://stacks.math.columbia.edu/tag/08GP) in the Stacks Project.

**`AlgebraicGeometry.Space.qcqs_induction_on`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/QcqsInduction.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/QcqsInduction.lean#L333). The attribute's comment: “every quasi-compact quasi-separated étale object”.

> **Stacks 08GP.** Induction on the quasi-compact quasi-separated objects of the
> spaces-étale site of a quasi-compact quasi-separated algebraic space `X`: a property of
> algebraic spaces étale over `X` which holds on the affine ones and is inherited across an
> elementary distinguished square with affine étale member holds on all of them.

```lean
public theorem qcqs_induction_on
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (P : (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) →
      (Y ⟶ X.1) → Prop)
    (haff : ∀ V : SpacesEtale B S hS X,
      IsAffineSpace B S hS V.1.left.1 →
        P V.1.left.1 V.1.hom.hom)
    (hstep : ∀ (W V : SpacesEtale B S hS X)
      (U : Subfunctor W.1.left.1)
      (f : V.1.left.1 ⟶ W.1.left.1),
      (f ≫ W.1.hom.hom = V.1.hom.hom) →
      IsElementaryDistinguishedSquare B S hS W.1.left.property U f →
      IsQuasiCompactSpace B S hS W.1.left.1 →
      IsAbsolutelyQuasiSeparated B S hS hZ W.1.left.1 →
      IsQuasiCompactSpace B S hS U.toFunctor →
      IsAffineSpace B S hS V.1.left.1 →
      P U.toFunctor (U.ι ≫ W.1.hom.hom) →
      P V.1.left.1 V.1.hom.hom →
      P (pullback U.ι f)
        (pullback.fst U.ι f ≫ U.ι ≫ W.1.hom.hom) →
      P W.1.left.1 W.1.hom.hom) :
    ∀ Y : SpacesEtale B S hS X,
      IsQuasiCompactSpace B S hS Y.1.left.1 →
      IsAbsolutelyQuasiSeparated B S hS hZ Y.1.left.1 →
      P Y.1.left.1 Y.1.hom.hom
```

**`AlgebraicGeometry.Space.qcqs_induction_on_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/QcqsInduction.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/QcqsInduction.lean#L454). The attribute's comment: “the base space”.

> **Stacks 08GP** for the base space: a property of algebraic spaces étale over a
> quasi-compact quasi-separated algebraic space `X` which holds on the affine ones and is
> inherited across an elementary distinguished square with affine étale member holds for `X`
> itself, taken with its identity morphism.

```lean
public theorem qcqs_induction_on_self
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (P : (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) →
      (Y ⟶ X.1) → Prop)
    (haff : ∀ V : SpacesEtale B S hS X,
      IsAffineSpace B S hS V.1.left.1 →
        P V.1.left.1 V.1.hom.hom)
    (hstep : ∀ (W V : SpacesEtale B S hS X)
      (U : Subfunctor W.1.left.1)
      (f : V.1.left.1 ⟶ W.1.left.1),
      (f ≫ W.1.hom.hom = V.1.hom.hom) →
      IsElementaryDistinguishedSquare B S hS W.1.left.property U f →
      IsQuasiCompactSpace B S hS W.1.left.1 →
      IsAbsolutelyQuasiSeparated B S hS hZ W.1.left.1 →
      IsQuasiCompactSpace B S hS U.toFunctor →
      IsAffineSpace B S hS V.1.left.1 →
      P U.toFunctor (U.ι ≫ W.1.hom.hom) →
      P V.1.left.1 V.1.hom.hom →
      P (pullback U.ι f)
        (pullback.fst U.ι f ≫ U.ι ≫ W.1.hom.hom) →
      P W.1.left.1 W.1.hom.hom) :
    P X.1 (𝟙 X.1)
```

## Tag 08GQ, a lemma

[Tag 08GQ](https://stacks.math.columbia.edu/tag/08GQ) in the Stacks Project.

**`AlgebraicGeometry.Space.qcqs_induction_on_collection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/QcqsInduction.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/QcqsInduction.lean#L491).

> **Stacks 08GQ.** Induction inside a collection `𝓑` of objects of the spaces-étale site of
> a quasi-compact quasi-separated algebraic space `X`: a property of the members of `𝓑` holds
> throughout `𝓑` as soon as `𝓑` consists of quasi-compact quasi-separated objects, is closed
> under quasi-compact open subspaces and contains every affine object, the property holds on
> the affine objects, and it is inherited across an elementary distinguished square whose
> ambient object lies in `𝓑` and whose étale member is affine.

```lean
public theorem qcqs_induction_on_collection
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (𝓑 P : (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) →
      (Y ⟶ X.1) → Prop)
    (hBqcqs : ∀ W : SpacesEtale B S hS X,
      𝓑 W.1.left.1 W.1.hom.hom →
      IsQuasiCompactSpace B S hS W.1.left.1 ∧
        IsAbsolutelyQuasiSeparated B S hS hZ W.1.left.1)
    (hBopen : ∀ (W : SpacesEtale B S hS X)
      (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (i : U ⟶ W.1.left.1),
      𝓑 W.1.left.1 W.1.hom.hom →
      IsAlgebraicSpace B S hS U →
      IsOpenImmersion B S hS i →
      IsQuasiCompactSpace B S hS U →
      𝓑 U (i ≫ W.1.hom.hom))
    (hBaff : ∀ V : SpacesEtale B S hS X,
      IsAffineSpace B S hS V.1.left.1 →
        𝓑 V.1.left.1 V.1.hom.hom)
    (hPaff : ∀ V : SpacesEtale B S hS X,
      IsAffineSpace B S hS V.1.left.1 →
        P V.1.left.1 V.1.hom.hom)
    (hstep : ∀ (W V : SpacesEtale B S hS X)
      (U : Subfunctor W.1.left.1)
      (f : V.1.left.1 ⟶ W.1.left.1),
      (f ≫ W.1.hom.hom = V.1.hom.hom) →
      IsElementaryDistinguishedSquare B S hS W.1.left.property U f →
      𝓑 W.1.left.1 W.1.hom.hom →
      IsQuasiCompactSpace B S hS U.toFunctor →
      IsAffineSpace B S hS V.1.left.1 →
      P U.toFunctor (U.ι ≫ W.1.hom.hom) →
      P V.1.left.1 V.1.hom.hom →
      P (pullback U.ι f)
        (pullback.fst U.ι f ≫ U.ι ≫ W.1.hom.hom) →
      P W.1.left.1 W.1.hom.hom) :
    ∀ W : SpacesEtale B S hS X,
      𝓑 W.1.left.1 W.1.hom.hom →
      P W.1.left.1 W.1.hom.hom
```

## Tag 08GR, a remark

[Tag 08GR](https://stacks.math.columbia.edu/tag/08GR) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiCompactSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L228). The attribute's comment: “separated_objects”.

> The quasi-compact separated algebraic spaces in the spaces-étale site.

```lean
public abbrev IsQuasiCompactSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.isQuasiCompactSeparated_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L237). The attribute's comment: “separated_objects”.

> The base algebraic space belongs to the collection.

```lean
public theorem isQuasiCompactSeparated_base
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXsep : IsAbsolutelySeparated B S hS hZ X.1) :
    IsQuasiCompactSeparated B S hS hZ X.1
```

**`AlgebraicGeometry.Space.IsQuasiCompactSeparated.isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L247). The attribute's comment: “separated_objects”.

> Every member of the collection is quasi-separated.

```lean
public theorem IsQuasiCompactSeparated.isAbsolutelyQuasiSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hY : IsQuasiCompactSeparated B S hS hZ Y) :
    IsAbsolutelyQuasiSeparated B S hS hZ Y
```

**`AlgebraicGeometry.Space.IsQuasiCompactSeparated.of_openImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L257). The attribute's comment: “separated_objects”.

> A quasi-compact open subspace of a member is again a member.

```lean
public theorem IsQuasiCompactSeparated.of_openImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (W : SpacesEtale B S hS X)
    (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (i : U ⟶ W.1.left.1)
    (hW : IsQuasiCompactSeparated B S hS hZ W.1.left.1)
    (hUspace : IsAlgebraicSpace B S hS U)
    (hi : IsOpenImmersion B S hS i)
    (hUqc : IsQuasiCompactSpace B S hS U) :
    IsQuasiCompactSeparated B S hS hZ U
```

**`AlgebraicGeometry.Space.isQuasiCompactSeparated_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L284). The attribute's comment: “separated_objects”.

> Every affine object of the spaces-étale site belongs to the collection.

```lean
public theorem isQuasiCompactSeparated_of_isAffineSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (V : SpacesEtale B S hS X)
    (hV : IsAffineSpace B S hS V.1.left.1) :
    IsQuasiCompactSeparated B S hS hZ V.1.left.1
```

**`AlgebraicGeometry.Space.qcqs_induction_on_quasiCompactSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L296). The attribute's comment: “separated_objects”.

> Induction on quasi-compact separated objects of the spaces-étale site.

```lean
public theorem qcqs_induction_on_quasiCompactSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXsep : IsAbsolutelySeparated B S hS hZ X.1)
    (P : (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) →
      (Y ⟶ X.1) → Prop)
    (hPaff : ∀ V : SpacesEtale B S hS X,
      IsAffineSpace B S hS V.1.left.1 →
        P V.1.left.1 V.1.hom.hom)
    (hstep : ∀ (W V : SpacesEtale B S hS X)
      (U : Subfunctor W.1.left.1)
      (f : V.1.left.1 ⟶ W.1.left.1),
      (f ≫ W.1.hom.hom = V.1.hom.hom) →
      IsElementaryDistinguishedSquare B S hS W.1.left.property U f →
      IsQuasiCompactSeparated B S hS hZ W.1.left.1 →
      IsQuasiCompactSpace B S hS U.toFunctor →
      IsAffineSpace B S hS V.1.left.1 →
      P U.toFunctor (U.ι ≫ W.1.hom.hom) →
      P V.1.left.1 V.1.hom.hom →
      P (pullback U.ι f)
        (pullback.fst U.ι f ≫ U.ι ≫ W.1.hom.hom) →
      P W.1.left.1 W.1.hom.hom) :
    ∀ W : SpacesEtale B S hS X,
      IsQuasiCompactSeparated B S hS hZ W.1.left.1 →
        P W.1.left.1 W.1.hom.hom
```

**`AlgebraicGeometry.Space.IsQuasiCompactWithAffineDiagonal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L406). The attribute's comment: “affine_diagonal_objects”.

> A quasi-compact algebraic space with affine absolute diagonal.

```lean
public abbrev IsQuasiCompactWithAffineDiagonal
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

**`AlgebraicGeometry.Space.isQuasiCompactWithAffineDiagonal_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L417). The attribute's comment: “affine_diagonal_objects”.

> The base algebraic space belongs to the collection.

```lean
public theorem isQuasiCompactWithAffineDiagonal_base
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXdiag : IsAffineHom B (⊤_ Scheme.{u}) hZ
      (diag (viewOverIntegers B S hS hZ X.1))) :
    IsQuasiCompactWithAffineDiagonal B S hS hZ X.1
```

**`AlgebraicGeometry.Space.IsQuasiCompactWithAffineDiagonal.isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L428). The attribute's comment: “affine_diagonal_objects”.

> Every member of the collection is quasi-separated.

```lean
public theorem IsQuasiCompactWithAffineDiagonal.isAbsolutelyQuasiSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (W : SpacesEtale B S hS X)
    (hW : IsQuasiCompactWithAffineDiagonal B S hS hZ W.1.left.1) :
    IsAbsolutelyQuasiSeparated B S hS hZ W.1.left.1
```

**`AlgebraicGeometry.Space.IsQuasiCompactWithAffineDiagonal.of_openImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L448). The attribute's comment: “affine_diagonal_objects”.

> A quasi-compact open subspace of a member is again a member.

```lean
public theorem IsQuasiCompactWithAffineDiagonal.of_openImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (W : SpacesEtale B S hS X)
    (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (i : U ⟶ W.1.left.1)
    (hW : IsQuasiCompactWithAffineDiagonal B S hS hZ W.1.left.1)
    (_hUspace : IsAlgebraicSpace B S hS U)
    (hi : IsOpenImmersion B S hS i)
    (hUqc : IsQuasiCompactSpace B S hS U) :
    IsQuasiCompactWithAffineDiagonal B S hS hZ U
```

**`AlgebraicGeometry.Space.isQuasiCompactWithAffineDiagonal_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L469). The attribute's comment: “affine_diagonal_objects”.

> Every affine object of the spaces-étale site belongs to the collection.

```lean
public theorem isQuasiCompactWithAffineDiagonal_of_isAffineSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (V : SpacesEtale B S hS X)
    (hV : IsAffineSpace B S hS V.1.left.1) :
    IsQuasiCompactWithAffineDiagonal B S hS hZ V.1.left.1
```

**`AlgebraicGeometry.Space.IsBasicEtaleObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L511). The attribute's comment: “smallest_collection”.

> A quasi-compact open subspace of `X` or of an affine étale object over `X`.

```lean
public def IsBasicEtaleObject
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (g : Y ⟶ X.1) : Prop
```

**`AlgebraicGeometry.Space.isBasicEtaleObject_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L551). The attribute's comment: “smallest_collection”.

> The base belongs to the basic collection.

```lean
public theorem isBasicEtaleObject_base
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1) :
    IsBasicEtaleObject B S hS X X.1 (𝟙 X.1)
```

**`AlgebraicGeometry.Space.IsBasicEtaleObject.isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L560). The attribute's comment: “smallest_collection”.

> A basic étale object is quasi-compact.

```lean
public theorem IsBasicEtaleObject.isQuasiCompactSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (W : SpacesEtale B S hS X)
    (hW : IsBasicEtaleObject B S hS X W.1.left.1 W.1.hom.hom) :
    IsQuasiCompactSpace B S hS W.1.left.1
```

**`AlgebraicGeometry.Space.IsBasicEtaleObject.isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L569). The attribute's comment: “smallest_collection”.

> A basic étale object is quasi-separated when `X` is.

```lean
public theorem IsBasicEtaleObject.isAbsolutelyQuasiSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (W : SpacesEtale B S hS X)
    (hW : IsBasicEtaleObject B S hS X W.1.left.1 W.1.hom.hom) :
    IsAbsolutelyQuasiSeparated B S hS hZ W.1.left.1
```

**`AlgebraicGeometry.Space.IsBasicEtaleObject.of_openImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L586). The attribute's comment: “smallest_collection”.

> Quasi-compact open subspaces of basic objects are basic.

```lean
public theorem IsBasicEtaleObject.of_openImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (W : SpacesEtale B S hS X)
    (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (i : U ⟶ W.1.left.1)
    (hW : IsBasicEtaleObject B S hS X W.1.left.1 W.1.hom.hom)
    (hUspace : IsAlgebraicSpace B S hS U)
    (hi : IsOpenImmersion B S hS i)
    (hUqc : IsQuasiCompactSpace B S hS U) :
    IsBasicEtaleObject B S hS X U (i ≫ W.1.hom.hom)
```

**`AlgebraicGeometry.Space.isBasicEtaleObject_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L606). The attribute's comment: “smallest_collection”.

> Every affine object of the étale site is basic.

```lean
public theorem isBasicEtaleObject_of_isAffineSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS)
    (V : SpacesEtale B S hS X)
    (hV : IsAffineSpace B S hS V.1.left.1) :
    IsBasicEtaleObject B S hS X V.1.left.1 V.1.hom.hom
```

**`AlgebraicGeometry.Space.IsAdmissibleCollection.mem_of_isBasicEtaleObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionCollections.lean#L630). The attribute's comment: “smallest_collection”.

> Every admissible collection contains all basic objects.

```lean
public theorem IsAdmissibleCollection.mem_of_isBasicEtaleObject
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (C : (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) →
      (Y ⟶ X.1) → Prop)
    (hC : IsAdmissibleCollection B S hS hZ X C)
    (W : SpacesEtale B S hS X)
    (hW : IsBasicEtaleObject B S hS X W.1.left.1 W.1.hom.hom) :
    C W.1.left.1 W.1.hom.hom
```

## Tag 09IT, a lemma

[Tag 09IT](https://stacks.math.columbia.edu/tag/09IT) in the Stacks Project.

**`AlgebraicGeometry.Space.qcqs_induction_on_enlargement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/EnlargementInduction.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/InductionPrinciple/EnlargementInduction.lean#L34).

> **Stacks 09IT.** Let `X` be a quasi-compact quasi-separated algebraic space and let
> `W ⊆ X` be a quasi-compact open subspace. A property `P` of the quasi-compact open subspaces
> of `X` which holds for `W`, and which for every elementary distinguished square
> `(W₁ ⊆ W₂, f : V ⟶ W₂)` with `W₁`, `W₂` quasi-compact open subspaces of `X` containing `W`
> and `V` affine passes from `W₁` to `W₂`, holds for `X`.

```lean
public theorem qcqs_induction_on_enlargement
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS)
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (W : Subfunctor X.1) (hWopen : IsOpenSubspace B S hS W)
    (hWqc : IsQuasiCompactSpace B S hS W.toFunctor)
    (P : Subfunctor X.1 → Prop) (hPW : P W)
    (hstep : ∀ (W₁ W₂ : Subfunctor X.1) (hW₁ : IsOpenSubspace B S hS W₁)
      (hW₂ : IsOpenSubspace B S hS W₂),
      IsQuasiCompactSpace B S hS W₁.toFunctor →
      IsQuasiCompactSpace B S hS W₂.toFunctor →
      ∀ hle : W₁ ≤ W₂, W ≤ W₁ →
      ∀ {V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : V ⟶ W₂.toFunctor),
        IsAffineSpace B S hS V →
        IsElementaryDistinguishedSquare B S hS hW₂.1
          (Subfunctor.range (Subfunctor.homOfLe hle)) f →
        P W₁ → P W₂) :
    P (⊤ : Subfunctor X.1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.9, Tag 08GL](https://stacks.math.columbia.edu/tag/08GL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
