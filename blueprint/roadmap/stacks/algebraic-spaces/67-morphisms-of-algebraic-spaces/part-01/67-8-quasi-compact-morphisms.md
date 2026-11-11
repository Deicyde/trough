---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsQuasiCompact, AlgebraicGeometry.Space.presheaf_quasiCompact_iff_isQuasiCompact, AlgebraicGeometry.Space.isQuasiCompact_of_isQuasiCompactSpace, AlgebraicGeometry.Space.isQuasiCompact_of_presheaf_quasiCompact, AlgebraicGeometry.Space.isQuasiCompactMap_pointsMap, AlgebraicGeometry.Space.isQuasiCompact_of_isPullback, AlgebraicGeometry.Space.IsQuasiCompact.comp, AlgebraicGeometry.Space.isQuasiCompactSpaceULift_of_isSurjectiveULift
statement: formalized
proof: formalized
---

# 67.8 Quasi-compact morphisms

Section 67.8 of the Stacks Project, [Tag 03HC](https://stacks.math.columbia.edu/tag/03HC). 11 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03HC, the section

[Tag 03HC](https://stacks.math.columbia.edu/tag/03HC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.IsQuasiCompact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L262), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactMorphisms.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactMorphisms.lean#L32) (StacksFrontier): “quasi-compact morphisms of algebraic spaces”.
- [`AlgebraicGeometry.Space.presheaf_quasiCompact_iff_isQuasiCompact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L128), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactMorphisms.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactMorphisms.lean#L34) (StacksFrontier): “agreement with the notion for representable morphisms”.
- [`AlgebraicGeometry.Space.isQuasiCompact_of_isQuasiCompactSpace`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSupport.lean#L171), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactMorphisms.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactMorphisms.lean#L36) (StacksFrontier): “a morphism from a quasi-compact space to a quasi-separated one is quasi-compact”.

## Tag 03HD, a lemma

[Tag 03HD](https://stacks.math.columbia.edu/tag/03HD) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_quasiCompact_iff_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L128).

> For a representable morphism of algebraic spaces over `S` the two readings of
> quasi-compactness agree: every represented base change of it is a quasi-compact morphism of
> schemes exactly when every base change of it along a morphism from a quasi-compact algebraic
> space has quasi-compact source.

```lean
theorem presheaf_quasiCompact_iff_isQuasiCompact {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : F ⟶ G} (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage (@AlgebraicGeometry.QuasiCompact.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      IsQuasiCompact B S hS f
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_presheaf_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactComposition.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactComposition.lean#L56). The attribute's comment: “part (1) implies part (2)”.

> A morphism of presheaves on the big fppf site of `S` which is representable and
> quasi-compact after every representable base change is quasi-compact: every base change of it
> along a morphism from a quasi-compact algebraic space has quasi-compact source.

```lean
theorem isQuasiCompact_of_presheaf_quasiCompact
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.QuasiCompact.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f) :
    IsQuasiCompact B S hS f
```

## Tag 03HE, a definition

[Tag 03HE](https://stacks.math.columbia.edu/tag/03HE) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiCompact`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L262).

> **Stacks 03HE.** A morphism of algebraic spaces over `S` is *quasi-compact* when every
> base change of it along a morphism from a quasi-compact algebraic space has quasi-compact
> source.

```lean
abbrev IsQuasiCompact (f : F ⟶ G) : Prop
```

## Tag 0EMK, a lemma

[Tag 0EMK](https://stacks.math.columbia.edu/tag/0EMK) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompactMap_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOnPoints.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactOnPoints.lean#L52).

> A quasi-compact morphism `f : X ⟶ Y` of algebraic spaces over `S`
> induces a quasi-compact map `|X| → |Y|` of point spaces: the preimage of a quasi-compact
> open subset of `|Y|` is quasi-compact.

```lean
theorem isQuasiCompactMap_pointsMap {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f) :
    ∀ ⦃U : Set (points B S hS Y)⦄, IsOpen U → IsCompact U →
      IsCompact (pointsMap B S hS X f ⁻¹' U)
```

## Tag 03HF, a lemma

[Tag 03HF](https://stacks.math.columbia.edu/tag/03HF) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L137).

> Quasi-compactness of a morphism of algebraic spaces is stable under base change: in a
> cartesian square, the base change `b` of a quasi-compact `p` is quasi-compact.

```lean
theorem isQuasiCompact_of_isPullback {F G F' G' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {a : F ⟶ F'} {b : F ⟶ G} {p : F' ⟶ G'} {q : G ⟶ G'}
    (sq : IsPullback a b p q) (hp : IsQuasiCompact B S hS p) : IsQuasiCompact B S hS b
```

## Tag 03HG, a lemma

[Tag 03HG](https://stacks.math.columbia.edu/tag/03HG) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiCompact.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactComposition.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactComposition.lean#L80).

> The composition of a pair of quasi-compact morphisms of algebraic spaces over `S` is
> quasi-compact.

```lean
theorem IsQuasiCompact.comp
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (hf : IsQuasiCompact B S hS f) (hg : IsQuasiCompact B S hS g) :
    IsQuasiCompact B S hS (f ≫ g)
```

## Tag 040W, a lemma

[Tag 040W](https://stacks.math.columbia.edu/tag/040W) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompactSpaceULift_of_isSurjectiveULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedQuasiCompactPoints.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedQuasiCompactPoints.lean#L208). The attribute's comment: “part (1), for a value universe independent of the universe of the schemes”.

> **Stacks 040W**, part (1), for a value universe `max w u` independent of the universe `u` of
> the schemes: if `f : F ⟶ G` is a surjective morphism of algebraic spaces over `S` and `F` is
> quasi-compact, then `G` is quasi-compact. The point space of `G` is the image of the
> quasi-compact point space of `F` under a continuous surjection.

```lean
theorem isQuasiCompactSpaceULift_of_isSurjectiveULift
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    (hF : IsAlgebraicSpaceULift.{w} B S hS F) (hG : IsAlgebraicSpaceULift.{w} B S hS G)
    (f : F ⟶ G) (hf : IsSurjectiveULift.{w} B S hS f)
    (h : IsQuasiCompactSpaceULift.{w} B S hS F) :
    IsQuasiCompactSpaceULift.{w} B S hS G
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L178). The attribute's comment: “part (1)”.

> The image of a quasi-compact algebraic space over `S` under a surjective morphism of
> algebraic spaces over `S` is quasi-compact.

```lean
theorem isQuasiCompactSpace_of_isSurjective {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hf : IsSurjective B S hS f) (hFqc : IsQuasiCompactSpace B S hS F) :
    IsQuasiCompactSpace B S hS G
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_comp_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L189). The attribute's comment: “part (2)”.

> In a commuting triangle `p = f ≫ q` of morphisms of algebraic
> spaces over `S` whose horizontal morphism `f` is surjective, quasi-compactness of `p` implies
> quasi-compactness of `q`.

```lean
theorem isQuasiCompact_of_comp_surjective {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H) (f : F ⟶ G) (p : F ⟶ H) (q : G ⟶ H) (hcomm : p = f ≫ q)
    (hf : IsSurjective B S hS f) (hp : IsQuasiCompact B S hS p) :
    IsQuasiCompact B S hS q
```

**`AlgebraicGeometry.Space.IsQuasiCompactSpace.of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSurjection.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSurjection.lean#L60). The attribute's comment: “part (1): quasi-compactness of the target”.

> **Stacks 040W, part (1).** The image of a quasi-compact algebraic space under a
> surjective morphism of algebraic spaces over `S` is quasi-compact: if `f : X ⟶ Y` is
> surjective on points and `X` is quasi-compact, then `Y` is quasi-compact.

```lean
theorem IsQuasiCompactSpace.of_isSurjective {f : X ⟶ Y}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsSurjective B S hS f) (h : IsQuasiCompactSpace B S hS X) :
    IsQuasiCompactSpace B S hS Y
```

**`AlgebraicGeometry.Space.IsQuasiCompact.of_isSurjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSurjection.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSurjection.lean#L72). The attribute's comment: “part (2): quasi-compactness of a morphism”. References: EGA IV (1.1.3).

> **Stacks 040W, part (2).** In a commuting triangle `f ≫ q = p` of morphisms of algebraic
> spaces over `S` whose horizontal arrow `f` is surjective, quasi-compactness of `p` implies
> quasi-compactness of `q`.

```lean
theorem IsQuasiCompact.of_isSurjective_comp {f : X ⟶ Y} {p : X ⟶ Z} {q : Y ⟶ Z}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (hcomm : f ≫ q = p)
    (hf : IsSurjective B S hS f) (hp : IsQuasiCompact B S hS p) :
    IsQuasiCompact B S hS q
```

## Tag 04ZJ, a lemma

[Tag 04ZJ](https://stacks.math.columbia.edu/tag/04ZJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_of_universallyOpen_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L322).

> Let `g : G' ⟶ G` be a universally open surjective morphism of algebraic spaces over `S`.
> If the base change of `f : F ⟶ G` along `g` is quasi-compact, then so is `f`.

```lean
theorem isQuasiCompact_of_universallyOpen_isSurjective
    {F G G' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (hG' : IsAlgebraicSpace B S hS G') (f : F ⟶ G)
    (g : G' ⟶ G) (hgopen : UniversallyOpen B S hS g) (hgsurj : IsSurjective B S hS g)
    (hf : IsQuasiCompact B S hS (pullback.fst g f)) :
    IsQuasiCompact B S hS f
```

## Tag 03KG, a lemma

[Tag 03KG](https://stacks.math.columbia.edu/tag/03KG) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L248).

> For a morphism `f : F ⟶ G` of algebraic spaces over `S` the following six
> conditions are equivalent: `f` is quasi-compact; the base change of `f` along every morphism
> to `G` from a presheaf represented by an object of the site is quasi-compact; for every such
> object with affine underlying scheme the fibre product is a quasi-compact algebraic space;
> the base change of `f` along some surjective étale morphism to `G` from a represented
> presheaf is quasi-compact; the same for some surjective étale morphism from an arbitrary
> algebraic space; and there is a Zariski covering of `G` along each member of which the base
> change of `f` is quasi-compact.

```lean
theorem isQuasiCompact_tfae {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    List.TFAE
      [IsQuasiCompact B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
          IsQuasiCompact B S hS (pullback.fst g f),
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
          IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
            IsQuasiCompactSpace B S hS (pullback g f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ G),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            IsQuasiCompact B S hS (pullback.fst g f),
        ∃ (G' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS G')
          (g : G' ⟶ G), IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            IsQuasiCompact B S hS (pullback.fst g f),
        ∃ (I : Type u) (U : I → Subfunctor G) (_ : IsZariskiCover B S hS I U),
          ∀ i, IsQuasiCompact B S hS (pullback.fst (U i).ι f)]
```

**`AlgebraicGeometry.Space.isQuasiCompact_pullback_snd_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L319). The attribute's comment: “part (1) implies part (2)”.

> **Stacks 03KG, part (1) implies part (2).** If `f : X ⟶ Y` is a quasi-compact morphism of
> algebraic spaces over `S`, then for every object `Z` of the site and every `g : h_Z ⟶ Y` the
> projection `Z ×_Y X ⟶ h_Z` is quasi-compact.
>
> This is Stacks 03HF, `AlgebraicGeometry.Space.isQuasiCompact_of_isPullback`, read at the
> cartesian square of the chosen fibre product; no representability of `Z` is used.

```lean
theorem isQuasiCompact_pullback_snd_of_isQuasiCompact
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y} (hf : IsQuasiCompact B S hS f)
    (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y) :
    IsQuasiCompact B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_pullback_of_isQuasiCompact_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L335). The attribute's comment: “part (2) implies part (3)”.

> **Stacks 03KG, part (2) implies part (3).** If every projection `Z ×_Y X ⟶ h_Z` of
> `f : X ⟶ Y` along a morphism from a represented presheaf is quasi-compact, then `Z ×_Y X` is a
> quasi-compact algebraic space whenever the scheme underlying `Z` is affine.
>
> An affine object of the site represents a quasi-compact algebraic space, and
> `AlgebraicGeometry.Space.isQuasiCompactSpace_source_of_isQuasiCompact` then transfers
> quasi-compactness from the target of the projection to its source. Only the single instance
> `g` of part (2) is used, not the whole of it, and the algebraic-space hypotheses `_hX` and
> `_hY` are retained from the source but are not needed.

```lean
theorem isQuasiCompactSpace_pullback_of_isQuasiCompact_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y)
    (h : ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
      IsQuasiCompact B S hS (pullback.snd f g))
    (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y)
    (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z)) :
    IsQuasiCompactSpace B S hS (pullback f g)
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_isQuasiCompactSpace_pullback_affine'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L362). The attribute's comment: “part (3) implies part (1)”.

> **Stacks 03KG, part (3) implies part (1): quasi-compactness of a morphism of algebraic
> spaces may be tested on affine schemes.** If `Z ×_Y X` is a quasi-compact algebraic space for
> every object `Z` of the site with affine underlying scheme and every `g : h_Z ⟶ Y`, then
> `f : X ⟶ Y` is quasi-compact.
>
> A quasi-compact algebraic space has a surjective étale morphism from an affine scheme by
> Stacks 03H6, and `AlgebraicGeometry.Space.isQuasiCompactSpace_pullback_of_isSurjective`
> replaces the test object by that affine scheme.
>
> `AlgebraicGeometry.Space.isQuasiCompact_of_isQuasiCompactSpace_pullback_affine` is the same
> assertion with the fibre product of the hypothesis taken in the other order and the two
> algebraic-space hypotheses in front of the morphism.

```lean
theorem isQuasiCompact_of_isQuasiCompactSpace_pullback_affine'
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (h : ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
      IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
        IsQuasiCompactSpace B S hS (pullback f g)) :
    IsQuasiCompact B S hS f
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_surjectiveEtale_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L389). The attribute's comment: “part (4) implies part (1)”.

> **Stacks 03KG, part (4) implies part (1): quasi-compactness of a morphism of algebraic
> spaces is étale-local on the target.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over
> `S`. If there are an object `V` of the site and a surjective étale morphism `φ : h_V ⟶ Y` such
> that the projection `V ×_Y X ⟶ h_V` is quasi-compact, then `f` is quasi-compact.
>
> This is the leg of Stacks 03KG that the proof of Stacks 03JV uses in passing from its
> condition (3) to its condition (4). Quasi-compactness of an arbitrary test object is reduced
> in two steps — to an affine scheme chart of it, which is part (3) implies part (1), and from
> there to a quasi-compact object factoring through `φ` by
> `AlgebraicGeometry.Space.exists_compactSpace_factoring_of_isSurjective_isEtale` — after which
> the hypothesis applies directly.

```lean
theorem isQuasiCompact_of_surjectiveEtale_atlas
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (V : BigFppfOver B S hS) (φ : yoneda.obj V ⟶ Y)
    (hsurj : IsSurjective B S hS φ) (hφ : IsEtale B S hS φ)
    (h : IsQuasiCompact B S hS (pullback.snd f φ)) :
    IsQuasiCompact B S hS f
```

**`AlgebraicGeometry.Space.exists_surjectiveEtale_atlas_isQuasiCompact_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L423). The attribute's comment: “part (1) implies part (4)”.

> **Stacks 03KG, part (1) implies part (4).** A quasi-compact morphism `f : X ⟶ Y` of
> algebraic spaces over `S` has a surjective étale chart `φ : h_V ⟶ Y` of its target along
> which its base change `V ×_Y X ⟶ h_V` is quasi-compact.
>
> Any scheme atlas of `Y` will do: it is surjective and étale by Stacks 03H5 and by
> multiplicativity of the represented étale morphisms, and the base change of `f` along it is
> quasi-compact by Stacks 03HF. Together with
> `AlgebraicGeometry.Space.isQuasiCompact_of_surjectiveEtale_atlas` this makes conditions (1) and
> (4) of Stacks 03KG equivalent, and it exhibits the hypothesis of that statement as
> satisfiable.

```lean
theorem exists_surjectiveEtale_atlas_isQuasiCompact_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hY : IsAlgebraicSpace B S hS Y) (hf : IsQuasiCompact B S hS f) :
    ∃ (V : BigFppfOver B S hS) (φ : yoneda.obj V ⟶ Y),
      IsSurjective B S hS φ ∧ IsEtale B S hS φ ∧
      IsQuasiCompact B S hS (pullback.snd f φ)
```

**`AlgebraicGeometry.Space.exists_isAlgebraicSpace_surjectiveEtale_isQuasiCompact_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L441). The attribute's comment: “part (4) implies part (5)”.

> **Stacks 03KG, part (4) implies part (5).** A surjective étale chart of `Y` by an object
> of the site is in particular a surjective étale morphism of algebraic spaces onto `Y`.
>
> The presheaf represented by an object of the site is an algebraic space, so this is a
> repackaging; it is stated so that the implications recorded for Tag 03KG reach condition (5)
> in the shape the source gives it.

```lean
theorem exists_isAlgebraicSpace_surjectiveEtale_isQuasiCompact_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (V : BigFppfOver B S hS) (φ : yoneda.obj V ⟶ Y)
    (hsurj : IsSurjective B S hS φ) (hφ : IsEtale B S hS φ)
    (h : IsQuasiCompact B S hS (pullback.snd f φ)) :
    ∃ (Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hY' : IsAlgebraicSpace B S hS Y')
      (g : Y' ⟶ Y), IsSurjective B S hS g ∧ IsEtale B S hS g ∧
        IsQuasiCompact B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.exists_surjectiveEtale_atlas_of_isAlgebraicSpace_surjectiveEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactEtaleLocalTarget.lean#L462). The attribute's comment: “part (5) implies part (4)”.

> **Stacks 03KG, part (5) implies part (4): an algebraic-space chart may be replaced by a
> scheme chart.** If `g : Y' ⟶ Y` is a surjective étale morphism of algebraic spaces over `S`
> along which the base change of `f : X ⟶ Y` is quasi-compact, then the same holds for a chart
> of `Y` by an object of the site.
>
> Compose `g` with a scheme atlas `a : h_V ⟶ Y'` of `Y'`. The composite is surjective on points
> because `AlgebraicGeometry.Space.pointsMap` is functorial, étale because
> `AlgebraicGeometry.Space.IsEtale g` tests exactly the étale charts of `Y'`, and the base change
> of `f` along it is a base change of the base change along `g`, hence quasi-compact by
> Stacks 03HF. Note that `Y` itself need not be assumed an algebraic space.

```lean
theorem exists_surjectiveEtale_atlas_of_isAlgebraicSpace_surjectiveEtale
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    {Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hY' : IsAlgebraicSpace B S hS Y')
    (g : Y' ⟶ Y) (hsurj : IsSurjective B S hS g) (hg : IsEtale B S hS g)
    (h : IsQuasiCompact B S hS (pullback.snd f g)) :
    ∃ (V : BigFppfOver B S hS) (φ : yoneda.obj V ⟶ Y),
      IsSurjective B S hS φ ∧ IsEtale B S hS φ ∧
      IsQuasiCompact B S hS (pullback.snd f φ)
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_zariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactZariskiLocalTarget.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactZariskiLocalTarget.lean#L218). The attribute's comment: “part (6) implies part (1)”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`. If there is a Zariski covering
> of `Y` by open subspaces `W i`, that is one whose point sets cover the space of points of `Y`,
> such that each of the morphisms `f⁻¹(W i) ⟶ W i`, that is `pullback.snd f (W i).ι`, is
> quasi-compact, then `f` is quasi-compact.

```lean
theorem isQuasiCompact_of_zariskiCover
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    {I : Type u} (W : I → Subfunctor Y) (hW : ∀ i, IsOpenSubspace B S hS (W i))
    (hcov : ∀ y : points B S hS Y, ∃ i,
      y ∈ Set.range (pointsMap B S hS (W i).toFunctor (W i).ι))
    (h : ∀ i, IsQuasiCompact B S hS (pullback.snd f (W i).ι)) :
    IsQuasiCompact B S hS f
```

**`AlgebraicGeometry.Space.exists_zariskiCover_isQuasiCompact_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactZariskiLocalTarget.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactZariskiLocalTarget.lean#L232). The attribute's comment: “part (1) implies part (6)”.

> A quasi-compact morphism `f : X ⟶ Y` of algebraic spaces over `S` admits a Zariski
> covering of `Y` over each member of which its restriction is quasi-compact.

```lean
theorem exists_zariskiCover_isQuasiCompact_pullback_snd
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hY : IsAlgebraicSpace B S hS Y) (hf : IsQuasiCompact B S hS f) :
    ∃ (I : Type u) (W : I → Subfunctor Y), (∀ i, IsOpenSubspace B S hS (W i)) ∧
      (∀ y : points B S hS Y, ∃ i,
        y ∈ Set.range (pointsMap B S hS (W i).toFunctor (W i).ι)) ∧
      ∀ i, IsQuasiCompact B S hS (pullback.snd f (W i).ι)
```

## Tag 03KS, a lemma

[Tag 03KS](https://stacks.math.columbia.edu/tag/03KS) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_of_comp_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L148). References: EGA IV (1.2.4).

> If a composite of morphisms of algebraic spaces over `S` is quasi-compact and its second
> factor is quasi-separated, then its first factor is quasi-compact.

```lean
theorem isQuasiCompact_of_comp_of_isQuasiSeparated {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) (g : G ⟶ H) (hF : IsAlgebraicSpace B S hS F)
    (hH : IsAlgebraicSpace B S hS H) (hgf : IsQuasiCompact B S hS (f ≫ g))
    (hg : IsQuasiSeparated B S hS g) :
    IsQuasiCompact B S hS f
```

## Tag 073B, a lemma

[Tag 073B](https://stacks.math.columbia.edu/tag/073B) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L401). The attribute's comment: “part (2): quasi-separated”.

> Every morphism of algebraic spaces over `S` out of a quasi-separated algebraic space is
> quasi-separated.

```lean
theorem isQuasiSeparated_of_isAbsolutelyQuasiSeparated_source
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hFqs : IsAbsolutelyQuasiSeparated B S hS hZ F) (f : F ⟶ G) :
    IsQuasiSeparated B S hS f
```

**`AlgebraicGeometry.Space.isQuasiCompactSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L411). The attribute's comment: “part (3): quasi-compact”.

> A fibre product of quasi-compact algebraic spaces over `S` over a quasi-separated
> algebraic space is quasi-compact.

```lean
theorem isQuasiCompactSpace_pullback {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ H)
    (g : G ⟶ H) (hF : IsAlgebraicSpace B S hS F) (hH : IsAlgebraicSpace B S hS H)
    (hFqc : IsQuasiCompactSpace B S hS F) (hGqc : IsQuasiCompactSpace B S hS G)
    (hHqs : IsAbsolutelyQuasiSeparated B S hS hZ H) :
    IsQuasiCompactSpace B S hS (pullback f g)
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompact.lean#L420). The attribute's comment: “part (3): quasi-separated”.

> A fibre product of quasi-separated algebraic spaces over `S` is quasi-separated.

```lean
theorem isAbsolutelyQuasiSeparated_pullback {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ H) (g : G ⟶ H) (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (hH : IsAlgebraicSpace B S hS H)
    (hFqs : IsAbsolutelyQuasiSeparated B S hS hZ F)
    (hGqs : IsAbsolutelyQuasiSeparated B S hS hZ G) :
    IsAbsolutelyQuasiSeparated B S hS hZ (pullback f g)
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSupport.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactSupport.lean#L171). The attribute's comment: “part (1)”. References: SGA 4 VI (1.14), “(i), algebraic spaces”.

> A morphism from a quasi-compact algebraic space into a quasi-separated algebraic space is
> quasi-compact.

```lean
theorem isQuasiCompact_of_isQuasiCompactSpace
    {X U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hUqc : IsQuasiCompactSpace B S hS U) (ι : U ⟶ X) :
    IsQuasiCompact B S hS ι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.8, Tag 03HC](https://stacks.math.columbia.edu/tag/03HC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
