---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsProper, AlgebraicGeometry.FormalSpace.isProper_of_forall_surjective_etale_cover, AlgebraicGeometry.FormalSpace.isProper_of_isRepresentable_of_forall_fppfFamily, AlgebraicGeometry.FormalSpace.IsProper.isProperOnSchemeBaseChanges, AlgebraicGeometry.FormalSpace.isProper_of_isProperOnSchemeBaseChanges, AlgebraicGeometry.FormalSpace.isProper_iff_isProperOnSchemeBaseChanges, AlgebraicGeometry.FormalSpace.IsProperOnSchemeBaseChanges.isProperOnAffineBaseChanges, AlgebraicGeometry.FormalSpace.IsProperOnAffineBaseChanges.isAlgebraicAndProper
statement: formalized
proof: formalized
---

# 87.31 Proper morphisms

Section 87.31 of the Stacks Project, [Tag 0AM5](https://stacks.math.columbia.edu/tag/0AM5). 3 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AM6, a definition

[Tag 0AM6](https://stacks.math.columbia.edu/tag/0AM6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsProper`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L111).

> **Stacks 0AM6.** A morphism of formal algebraic spaces over `S` is *proper* when it is
> representable by algebraic spaces and every base change of it along a scheme-valued point of
> its target is a morphism of algebraic spaces which is proper, that is, separated, of finite
> type and universally closed. The condition makes sense, and is stated, for an arbitrary
> morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev IsProper {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.isProper_of_forall_surjective_etale_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperEtaleLocal.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperEtaleLocal.lean#L85). The attribute's comment: “local on the target”.

> **Properness of morphisms of formal algebraic spaces is local on the target.** A morphism
> `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` is proper in the sense of
> **Stacks 0AM6** as soon as every scheme-valued point `ξ : U ⟶ Y` of its target admits a
> morphism `q : U' ⟶ U` of the site, surjective and étale on underlying schemes, such that the
> base change of `f` along `U' ⟶ U ⟶ Y` is an algebraic space over `S` proper over `U'`.
>
> Being an algebraic space descends along `q` by **Stacks 0BGR** and properness by
> **Stacks 0422**, both applied to the base change of the universe-lifted Yoneda image of `q`
> along the projection of the base change of `f` along `ξ`.

```lean
theorem isProper_of_forall_surjective_etale_cover {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (h : ∀ (U : BigFppfOver B S hS) (ξ : (uliftYoneda.{u + 1}).obj U ⟶ Y.obj),
      ∃ (U' : BigFppfOver B S hS) (q : U' ⟶ U),
        Surjective ((BigFppfOver.toScheme B S hS).map q) ∧
        Etale ((BigFppfOver.toScheme B S hS).map q) ∧
        Space.IsAlgebraicSpaceULift.{u + 1} B S hS
          (pullback ((uliftYoneda.{u + 1}).map q ≫ ξ) f.hom) ∧
        Space.IsProperULift.{u + 1} B S hS
          (pullback.fst ((uliftYoneda.{u + 1}).map q ≫ ξ) f.hom)) :
    IsProper B S hS f
```

**`AlgebraicGeometry.FormalSpace.isProper_of_isRepresentable_of_forall_fppfFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperEtaleLocal.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperEtaleLocal.lean#L152). The attribute's comment: “local on the target for a covering family, given representability”.

> **Properness of a morphism representable by algebraic spaces is local on the target for a
> covering family of the site.** Let `f : X ⟶ Y` be a morphism of fppf sheaves on the big fppf
> site of `S` which is representable by algebraic spaces, and suppose every scheme-valued point
> `ξ : U ⟶ Y` of its target admits a family `{qᵢ : Vᵢ ⟶ U}` of morphisms of the site whose Yoneda
> images form an fppf covering family of `U`, such that the base change of `f` along each
> `Vᵢ ⟶ U ⟶ Y` is proper as a morphism of algebraic spaces. Then `f` is proper in the sense of
> **Stacks 0AM6**.
>
> Unlike `AlgebraicGeometry.FormalSpace.isProper_of_forall_surjective_etale_cover` this takes a
> *family* and not one morphism, so it needs no coproduct of the members inside the site; what it
> asks instead is that `f` be representable by algebraic spaces, since being an algebraic space is
> the half of properness which the family form of **Stacks 0422** does not descend. The base
> change of `f` along `Vᵢ ⟶ U ⟶ Y` is compared with the base change along `qᵢ` of the base change
> along `ξ` by `CategoryTheory.Limits.pullbackRightPullbackFstIso`.

```lean
theorem isProper_of_isRepresentable_of_forall_fppfFamily {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (h : ∀ (U : BigFppfOver B S hS) (ξ : (uliftYoneda.{u + 1}).obj U ⟶ Y.obj),
      ∃ (Idx : Type (u + 1)) (V : Idx → BigFppfOver B S hS) (q : ∀ i, V i ⟶ U),
        Space.IsFppfCovering B S hS (fun i => yoneda.obj (V i))
          (fun i => yoneda.map (q i)) ∧
        ∀ i, Space.IsProperULift.{u + 1} B S hS
          (pullback.fst ((uliftYoneda.{u + 1}).map (q i) ≫ ξ) f.hom)) :
    IsProper B S hS f
```

## Tag 0ART, a lemma

[Tag 0ART](https://stacks.math.columbia.edu/tag/0ART) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsProper.isProperOnSchemeBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L254). The attribute's comment: “(1) implies (2)”.

> **Stacks 0ART, (1) implies (2).** A base change of a proper morphism of formal algebraic
> spaces over `S` along a scheme over `S` in the site is proper. This is the base change
> stability of properness, which needs no hypothesis on the base.

```lean
theorem IsProper.isProperOnSchemeBaseChanges {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (hf : IsProper B S hS f) : IsProperOnSchemeBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.isProper_of_isProperOnSchemeBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L263). The attribute's comment: “(2) implies (1)”.

> **Stacks 0ART, (2) implies (1).** A morphism of formal algebraic spaces over `S` all of
> whose base changes along schemes over `S` in the site are proper is proper: the base change
> along a scheme-valued point of the target, read at the identity point of its own target, is
> that base change itself.

```lean
theorem isProper_of_isProperOnSchemeBaseChanges {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsProperOnSchemeBaseChanges B S hS f) : IsProper B S hS f
```

**`AlgebraicGeometry.FormalSpace.isProper_iff_isProperOnSchemeBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L276). The attribute's comment: “(1) is equivalent to (2)”.

> **Stacks 0ART, (1) is equivalent to (2).** A morphism of formal algebraic spaces over `S`
> is proper exactly when each of its base changes along a scheme over `S` in the site is
> proper.

```lean
theorem isProper_iff_isProperOnSchemeBaseChanges {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsProper B S hS f ↔ IsProperOnSchemeBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsProperOnSchemeBaseChanges.isProperOnAffineBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L284). The attribute's comment: “(2) implies (3)”.

> **Stacks 0ART, (2) implies (3).** The base change condition over all schemes over `S` in
> the site restricts to the affine ones.

```lean
theorem IsProperOnSchemeBaseChanges.isProperOnAffineBaseChanges {X Y : FppfSheaf B S hS}
    {f : X ⟶ Y} (h : IsProperOnSchemeBaseChanges B S hS f) :
    IsProperOnAffineBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsProperOnAffineBaseChanges.isAlgebraicAndProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L295). The attribute's comment: “(3) implies (4)”.

> **Stacks 0ART, (3) implies (4).** If every base change of a morphism of formal algebraic
> spaces over `S` along an affine scheme `Z` over `S` in the site is proper, then every such
> base change is an algebraic space over `S` and its projection to `Z` is proper as a morphism of
> algebraic spaces: both are the content of properness of that base change read at the identity
> point of `Z`.

```lean
theorem IsProperOnAffineBaseChanges.isAlgebraicAndProper {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsProperOnAffineBaseChanges B S hS f) :
    IsAlgebraicAndProperOnAffineBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsProper.hasProperFormalAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L307). The attribute's comment: “(1) implies (5)”.

> **Stacks 0ART, (1) implies (5).** A proper morphism of formal algebraic spaces over `S`
> has a covering of its target as in Definition 0AIM all of whose base changes of the morphism
> are proper: any atlas of the target witnessing that it is a formal algebraic space will do,
> properness being stable under base change.

```lean
theorem IsProper.hasProperFormalAtlas {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (hY : IsFormalAlgebraicSpace B S hS Y) (hf : IsProper B S hS f) :
    HasProperFormalAtlas B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsAlgebraicAndProperOnAffineBaseChanges.isProperOnAffineBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineCriterion.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineCriterion.lean#L251). The attribute's comment: “(4) implies (3)”.

> **Stacks 0ART, (4) implies (3).** If every base change of a morphism of formal algebraic
> spaces over `S` along an affine scheme `Z` over `S` in the site is an algebraic space over `S`
> whose projection to `Z` is proper as a morphism of algebraic spaces, then every such base
> change is proper as a morphism of formal algebraic spaces: over a scheme of the site the two
> conditions agree, properness of morphisms of algebraic spaces being stable under base change
> along a scheme-valued point.

```lean
theorem IsAlgebraicAndProperOnAffineBaseChanges.isProperOnAffineBaseChanges
    {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsAlgebraicAndProperOnAffineBaseChanges B S hS f) :
    IsProperOnAffineBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.isProperOnAffineBaseChanges_iff_isAlgebraicAndProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineCriterion.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineCriterion.lean#L262). The attribute's comment: “(3) is equivalent to (4)”.

> **Stacks 0ART, (3) is equivalent to (4).** Over an affine scheme of the site, properness
> of the base change as a morphism of formal algebraic spaces and the conjunction of being an
> algebraic space with properness of the projection as a morphism of algebraic spaces are the
> same condition.

```lean
theorem isProperOnAffineBaseChanges_iff_isAlgebraicAndProper {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) :
    IsProperOnAffineBaseChanges B S hS f ↔
      IsAlgebraicAndProperOnAffineBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsProperOnAffineBaseChanges.isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineLocal.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineLocal.lean#L225). The attribute's comment: “(3) implies (1)”.

> **Stacks 0ART, (3) implies (1).** A morphism of formal algebraic spaces over `S` all of
> whose base changes along affine schemes over `S` in the site are proper is proper.
>
> Condition (3) gives, at an affine point `Z ⟶ Y`, properness of the chosen base change as a
> morphism of formal algebraic spaces; read at the identity point of `Z`
> (**Stacks 0ART, (3) implies (4)**) that is exactly the hypothesis of
> `AlgebraicGeometry.FormalSpace.isProper_of_affine_base_changes`, namely that the base change is
> an algebraic space over `S` proper over `Z`.

```lean
theorem IsProperOnAffineBaseChanges.isProper {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : IsProperOnAffineBaseChanges B S hS f) : IsProper B S hS f
```

**`AlgebraicGeometry.FormalSpace.isProper_iff_isProperOnAffineBaseChanges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineLocal.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperAffineLocal.lean#L242). The attribute's comment: “(1) is equivalent to (3)”.

> **Stacks 0ART, (1) is equivalent to (3).** A morphism of formal algebraic spaces over `S`
> is proper exactly when each of its base changes along an affine scheme over `S` in the site is
> proper.

```lean
theorem isProper_iff_isProperOnAffineBaseChanges {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsProper B S hS f ↔ IsProperOnAffineBaseChanges B S hS f
```

**`AlgebraicGeometry.FormalSpace.HasProperFormalAtlas.isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperFormalAtlas.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperFormalAtlas.lean#L371). The attribute's comment: “(5) implies (1)”.

> **Stacks 0ART, (5) implies (1).** A morphism of formal algebraic spaces over `S` admitting
> *one* covering of its target as in Definition 0AIM all of whose base changes of the morphism are
> proper is itself proper.
>
> Properness is local on the target for a surjective étale covering by one object of the site, and
> such a covering of each scheme-valued point of `Y` is assembled from the given covering: its
> joint surjectivity puts every point of the scheme-valued point inside an affine étale
> neighbourhood over which the point factors through one member of the covering, and the
> coproduct of a `u`-small refinement of those neighbourhoods is the covering object.

```lean
theorem HasProperFormalAtlas.isProper {X Y : FppfSheaf B S hS} {f : X ⟶ Y}
    (h : HasProperFormalAtlas B S hS f) : IsProper B S hS f
```

**`AlgebraicGeometry.FormalSpace.isProper_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperTfae.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperTfae.lean#L76). The attribute's comment: “(1), (2), (3) and (4) are equivalent”.

> **Stacks 0ART, conditions (1), (2), (3) and (4) are equivalent.** For a morphism of fppf
> sheaves on the big fppf site of `S`: being proper, having every base change along a scheme of
> the site proper, having every base change along an affine scheme of the site proper, and having
> every base change along an affine scheme `Z` of the site be an algebraic space over `S` proper
> over `Z`, are the same condition.
>
> The cycle is closed by (3) ⇒ (1). Condition (5) of the source asks nothing of `X` or `Y` in
> `AlgebraicGeometry.FormalSpace.HasProperFormalAtlas.isProper` but needs `Y` to be a formal
> algebraic space to follow from the others, so it is added to the list separately in
> `AlgebraicGeometry.FormalSpace.isProper_tfae_of_isFormalAlgebraicSpace`.

```lean
theorem isProper_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    List.TFAE
      [IsProper B S hS f,
        IsProperOnSchemeBaseChanges B S hS f,
        IsProperOnAffineBaseChanges B S hS f,
        IsAlgebraicAndProperOnAffineBaseChanges B S hS f]
```

**`AlgebraicGeometry.FormalSpace.isProper_tfae_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperTfae.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperTfae.lean#L100). The attribute's comment: “all five conditions are equivalent”.

> **Stacks 0ART.** For a morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S`
> whose target is a formal algebraic space over `S`, the five conditions of the source are
> equivalent: `f` is proper; every base change of `f` along a scheme of the site is proper; every
> base change of `f` along an affine scheme of the site is proper; every base change of `f` along
> an affine scheme `Z` of the site is an algebraic space over `S` proper over `Z`; and there is
> one covering of `Y` as in Definition 0AIM all of whose base changes of `f` are proper.
>
> The first four are `AlgebraicGeometry.FormalSpace.isProper_tfae`, which needs no hypothesis on
> `Y`; the fifth is attached by `AlgebraicGeometry.FormalSpace.IsProper.hasProperFormalAtlas`,
> which reads an atlas of `Y` off the hypothesis, and by
> `AlgebraicGeometry.FormalSpace.HasProperFormalAtlas.isProper`.

```lean
theorem isProper_tfae_of_isFormalAlgebraicSpace {X Y : FppfSheaf B S hS}
    (hY : IsFormalAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [IsProper B S hS f,
        IsProperOnSchemeBaseChanges B S hS f,
        IsProperOnAffineBaseChanges B S hS f,
        IsAlgebraicAndProperOnAffineBaseChanges B S hS f,
        HasProperFormalAtlas B S hS f]
```

## Tag 0GBT, a lemma

[Tag 0GBT](https://stacks.math.columbia.edu/tag/0GBT) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsProper.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Proper.lean#L146).

> **Stacks 0GBT.** A base change of a proper morphism of formal algebraic spaces over `S` is
> proper: representability by algebraic spaces is stable under base change, and so is the Bootstrap
> condition of Stacks 03XZ, properness of morphisms of algebraic spaces being invariant under
> isomorphism.

```lean
theorem IsProper.of_isPullback {W X Z Y : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsProper B S hS f) : IsProper B S hS p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.31, Tag 0AM5](https://stacks.math.columbia.edu/tag/0AM5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
