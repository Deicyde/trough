---
declaration: section
origin: cited
lean: RingHom.Flat.faithfullyFlat_of_isLocalHom, AlgebraicGeometry.Space.faithfullyFlat_etaleLocalRingMap, AlgebraicGeometry.Space.IsFlat, AlgebraicGeometry.Space.IsFlatAt, AlgebraicGeometry.Space.isFlat_tfae, AlgebraicGeometry.Space.isFlat_comp, AlgebraicGeometry.Space.isFlat_isStableUnderBaseChange, AlgebraicGeometry.Space.universallyOpen_of_isFlat_of_isLocallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 67.30 Flat morphisms

Section 67.30 of the Stacks Project, [Tag 03MK](https://stacks.math.columbia.edu/tag/03MK). 13 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03MK, the section

[Tag 03MK](https://stacks.math.columbia.edu/tag/03MK) in the Stacks Project.

**`RingHom.Flat.faithfullyFlat_of_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FaithfullyFlatLocalHom.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FaithfullyFlatLocalHom.lean#L47). The attribute's comment: “section tag: a flat local homomorphism of local rings is faithfully flat”. References: EGA 0 (6.6.1), “(e) ⇒ (a), special case”; EGA 0 (6.6.2), “partial, special case”; SGA 1 IV (2.2), “special case”; SGA 1 IV (2.6), “(i), special case”.

> A flat local homomorphism of local rings is faithfully flat.

```lean
theorem faithfullyFlat_of_isLocalHom {R S : Type*} [CommRing R] [CommRing S] [IsLocalRing R]
    [IsLocalRing S] {f : R →+* S} (hf : f.Flat) [IsLocalHom f] : f.FaithfullyFlat
```

**`AlgebraicGeometry.Space.faithfullyFlat_etaleLocalRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FaithfullyFlatLocalHom.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FaithfullyFlatLocalHom.lean#L64). The attribute's comment: “section tag: the étale local ring map of a flat morphism is faithfully flat”.

> The canonical homomorphism of étale local rings `𝒪_{G, f ∘ x} ⟶ 𝒪_{F, x}` induced by a flat
> morphism `f : F ⟶ G` of algebraic spaces at a geometric point `x` of its source is faithfully
> flat.

```lean
theorem faithfullyFlat_etaleLocalRingMap {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hf : IsFlat B S hS f) (x : GeometricPoint B S hS F) :
    (etaleLocalRingMap hF f x).FaithfullyFlat
```

## Tag 03ML, a definition

[Tag 03ML](https://stacks.math.columbia.edu/tag/03ML) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat.lean#L40). The attribute's comment: “part (1)”.

> A morphism of algebraic spaces over `S` is *flat* when the morphism of schemes underlying every
> commuting square of étale scheme charts of it is flat.

```lean
abbrev IsFlat (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.IsFlatAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/AtAPoint.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/AtAPoint.lean#L54). The attribute's comment: “part (2)”.

> **Stacks 03ML, part (2).** A morphism of algebraic spaces over `S` is *flat at* a point `x`
> of its source when the morphism of germs it induces in every pointed étale scheme chart at `x`
> is flat on local rings.

```lean
abbrev IsFlatAt (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) (x : points B S hS F) : Prop
```

## Tag 08EW, a lemma

[Tag 08EW](https://stacks.math.columbia.edu/tag/08EW) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean#L723). The attribute's comment: “the equivalence of (1) and (2): flat iff flat at every point of |X|”.

> Nine criteria for a morphism of algebraic spaces over `S` to be flat: pointwise flatness,
> flatness of every base change to a scheme or to an affine scheme or to one surjective étale chart
> of the target, flatness of the composite with one surjective étale chart of the source, flatness
> of the morphism of schemes in every — or in one surjective — commuting square of étale charts, or
> over a pair of Zariski coverings.

```lean
theorem isFlat_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      IsFlat B S hS f,
      ∀ x : points B S hS X, IsFlatAt B S hS f x,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsFlat B S hS (pullback.fst g f),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) → IsFlat B S hS (pullback.fst g f),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧ IsFlat B S hS (pullback.fst g f),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧ IsFlat B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          IsFlat B S hS (yoneda.map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧ IsFlat B S hS (yoneda.map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsFlat B S hS ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 03MN, a lemma

[Tag 03MN](https://stacks.math.columbia.edu/tag/03MN) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatComposition.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatComposition.lean#L63).

> **Stacks 03MN.** A composition of flat morphisms of algebraic spaces over `S` is flat.

```lean
theorem isFlat_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsFlat B S hS f) (hg : IsFlat B S hS g) :
    IsFlat B S hS (f ≫ g)
```

## Tag 03MO, a lemma

[Tag 03MO](https://stacks.math.columbia.edu/tag/03MO) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FlatLocalAtSource.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/FlatLocalAtSource.lean#L104).

> **Stacks Project, Tag 03MO.** Flatness of morphisms of algebraic spaces over `S` is stable
> under base change.

```lean
theorem isFlat_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsFlat B S hS f.hom)
```

## Tag 03MM, a lemma

[Tag 03MM](https://stacks.math.columbia.edu/tag/03MM) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean#L723).

> Nine criteria for a morphism of algebraic spaces over `S` to be flat: pointwise flatness,
> flatness of every base change to a scheme or to an affine scheme or to one surjective étale chart
> of the target, flatness of the composite with one surjective étale chart of the source, flatness
> of the morphism of schemes in every — or in one surjective — commuting square of étale charts, or
> over a pair of Zariski coverings.

```lean
theorem isFlat_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      IsFlat B S hS f,
      ∀ x : points B S hS X, IsFlatAt B S hS f x,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsFlat B S hS (pullback.fst g f),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) → IsFlat B S hS (pullback.fst g f),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧ IsFlat B S hS (pullback.fst g f),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧ IsFlat B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          IsFlat B S hS (yoneda.map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧ IsFlat B S hS (yoneda.map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsFlat B S hS ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 042S, a lemma

[Tag 042S](https://stacks.math.columbia.edu/tag/042S) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_of_isFlat_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean, line 772](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Flat.lean#L772). References: EGA IV (2.4.6), “in particular clause”; EGA IV (15.2.1), “flat+lfp ⇒ univ open”; SGA 3 XVI (2.1), “more general”.

> A flat morphism of algebraic spaces over `S` which is locally of finite presentation is
> universally open in the sense of Stacks 03Z2.

```lean
theorem universallyOpen_of_isFlat_of_isLocallyOfFinitePresentation
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f) :
    UniversallyOpen B S hS f
```

## Tag 0413, a lemma

[Tag 0413](https://stacks.math.columbia.edu/tag/0413) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_iff_isOpen_preimage_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L370). The attribute's comment: “open subsets”. References: EGA IV (2.3.12), “open case”; SGA 1 VIII (4.3), “open subsets”; SGA 1 IX (2.2), “flat qc case, open”.

> **Stacks 0413, open subsets.** A subset of the points of the target of a flat,
> quasi-compact, surjective morphism of algebraic spaces over `S` is open exactly when its
> inverse image on points is open.
>
> Openness in the point topology is tested on the presheaves represented by the objects of the
> site, and openness there is openness in the representing scheme, hence local on its affine
> opens; those affine opens are objects of the site with affine underlying scheme, so
> `AlgebraicGeometry.Space.isOpen_preimage_pointsMap_of_isAffine` applies to each.

```lean
theorem isOpen_iff_isOpen_preimage_pointsMap
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hqc : IsQuasiCompact B S hS f) (hsurj : IsSurjective B S hS f)
    (T : Set (points B S hS Y)) :
    IsOpen T ↔ IsOpen (pointsMap B S hS X f ⁻¹' T)
```

**`AlgebraicGeometry.Space.isClosed_iff_isClosed_preimage_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L412). The attribute's comment: “closed subsets”. References: EGA IV (2.3.12), “closed case”; SGA 1 VIII (4.3), “closed subsets”; SGA 1 IX (2.2), “flat qc case, closed”.

> **Stacks 0413, closed subsets.** A subset of the points of the target of a flat,
> quasi-compact, surjective morphism of algebraic spaces over `S` is closed exactly when its
> inverse image on points is closed. This is
> `AlgebraicGeometry.Space.isOpen_iff_isOpen_preimage_pointsMap` at the complement.

```lean
theorem isClosed_iff_isClosed_preimage_pointsMap
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hqc : IsQuasiCompact B S hS f) (hsurj : IsSurjective B S hS f)
    (T : Set (points B S hS Y)) :
    IsClosed T ↔ IsClosed (pointsMap B S hS X f ⁻¹' T)
```

**`AlgebraicGeometry.Space.isSubmersive_of_isFlat_of_isQuasiCompact_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L428). The attribute's comment: “submersive”. References: EGA IV (15.7.8), “fppf ⇒ submersive”; EGA IV (2.3.12); SGA 1 VIII (4.3); SGA 1 IX (2.2), “flat qc submersive”.

> **Stacks 0413, submersiveness.** A flat, quasi-compact, surjective morphism of algebraic
> spaces over `S` is submersive: it is surjective on points, and openness of a subset of the
> points of its target is openness of the inverse image.

```lean
theorem isSubmersive_of_isFlat_of_isQuasiCompact_of_isSurjective
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hqc : IsQuasiCompact B S hS f) (hsurj : IsSurjective B S hS f) :
    IsSubmersive B S hS f
```

**`AlgebraicGeometry.Space.universallySubmersive_of_isFlat_of_isQuasiCompact_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Submersive.lean#L440). The attribute's comment: “universally submersive”.

> **Stacks 0413, universal submersiveness.** A flat, quasi-compact, surjective morphism of
> algebraic spaces over `S` is universally submersive: each of the three hypotheses is stable
> under base change, by Stacks 03MO, Stacks 03HF and Stacks 03MH.

```lean
theorem universallySubmersive_of_isFlat_of_isQuasiCompact_of_isSurjective
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hqc : IsQuasiCompact B S hS f) (hsurj : IsSurjective B S hS f) :
    UniversallySubmersive B S hS f
```

## Tag 04NG, a lemma

[Tag 04NG](https://stacks.math.columbia.edu/tag/04NG) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_etaleLocalRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatEtaleLocalRing.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatEtaleLocalRing.lean#L406). The attribute's comment: “the canonical homomorphism of étale local rings”.

> **Stacks 04NG.** A morphism `f` of algebraic spaces over `S` induces at a geometric point
> `x` of its source a unique homomorphism of étale local rings
> `𝒪_{G, f ∘ x} ⟶ 𝒪_{F, x}` compatible with the germ maps in every commuting diagram of pointed
> étale scheme charts over `f`.

```lean
theorem existsUnique_etaleLocalRingMap (hF : IsAlgebraicSpace B S hS F) (f : F ⟶ G)
    (x : GeometricPoint B S hS F) :
    ∃! φ : etaleLocalRing B S hS G (geometricPointMap f x) →+* etaleLocalRing B S hS F x,
      IsEtaleLocalRingMap f x φ
```

**`AlgebraicGeometry.Space.isFlatAt_iff_etaleLocalRingMap_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatEtaleLocalRing.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatEtaleLocalRing.lean#L581). The attribute's comment: “the flatness criterion”.

> **Stacks 04NG.** A morphism `f` of algebraic spaces over `S` is flat at the image of a
> geometric point `x` of its source exactly when the canonical homomorphism of étale local rings
> `𝒪_{G, f ∘ x} ⟶ 𝒪_{F, x}` is flat.
>
> For a point `x₀` of `F` with `x.LiesOver x₀` the statement for `x₀` follows by rewriting along
> that equality.

```lean
theorem isFlatAt_iff_etaleLocalRingMap_flat (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (x : GeometricPoint B S hS F) :
    IsFlatAt B S hS f x.image ↔ (etaleLocalRingMap hF f x).Flat
```

## Tag 073C, a lemma

[Tag 073C](https://stacks.math.columbia.edu/tag/073C) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_iff_smallEtaleRingedToposHom_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleFlatTopos.lean, line 596](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleFlatTopos.lean#L596).

> **Stacks 073C.** A morphism of algebraic spaces over `S` is flat if and only if the
> morphism of small étale ringed topoi `(f_small, f♯) : (X_étale, 𝒪_X) ⟶ (Y_étale, 𝒪_Y)`
> associated to it is flat.

```lean
theorem isFlat_iff_smallEtaleRingedToposHom_isFlat :
    IsFlat B S hS f.hom ↔
      RingedToposHom.IsFlat (smallEtaleRingedToposHom B S hS f)
```

## Tag 089C, a lemma

[Tag 089C](https://stacks.math.columbia.edu/tag/089C) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticSupport_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportFlatPullback.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SchemeTheoreticSupportFlatPullback.lean#L245). The attribute's comment: “flatness of the morphism, quasi-coherence of the module and finiteness of its type are the hypotheses of the tag and are all consumed; the affine-chart description of the pullback of modules, Descent Proposition 03DX(2) read across the morphism, is proved, not carried”.

> **[Stacks, Tag 089C].**  Let `f : Y ⟶ X` be a flat morphism of algebraic spaces over `S` and
> let `F` be a quasi-coherent `𝒪_X`-module of finite type with scheme-theoretic support `Z ⊆ X`.
> Then the inverse image `f⁻¹(Z)` is the scheme-theoretic support of `f^*F`.

```lean
theorem schemeTheoreticSupport_modulePullback {f : Y ⟶ X} (hf : IsFlat B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hft : PresheafOfModules.IsFiniteType (smallEtaleRingedSite B S hS X.1 X.2).J F.val) :
    schemeTheoreticSupport B S hS Y ((modulePullback B S hS f).obj F) =
      (schemeTheoreticSupport B S hS X F).preimage f.hom
```

## Tag 089D, a lemma

[Tag 089D](https://stacks.math.columbia.edu/tag/089D) in the Stacks Project.

**`AlgebraicGeometry.Space.isSchemeTheoreticallyDense_preimage_of_isFlat_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticDensity.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticDensity.lean#L149).

> Let `S` be a scheme contained in a big fppf site `B`, let `f : X ⟶ Y` be a flat morphism of
> algebraic spaces over `S` and let `V ⊆ Y` be an open subspace whose inclusion is quasi-compact.
> If `V` is scheme-theoretically dense in `Y`, then `f⁻¹V` is scheme-theoretically dense in
> `X`.

```lean
theorem isSchemeTheoreticallyDense_preimage_of_isFlat_of_isQuasiCompact
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsFlat B S hS f) (V : Subfunctor Y) (hV : IsOpenSubspace B S hS V)
    (hqc : IsQuasiCompact B S hS V.ι)
    (hdense : IsSchemeTheoreticallyDense B S hS V) :
    IsSchemeTheoreticallyDense B S hS (V.preimage f)
```

## Tag 089E, a lemma

[Tag 089E](https://stacks.math.columbia.edu/tag/089E) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_pullback_snd_of_isFlat_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImageFlatBaseChange.lean, line 642](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImageFlatBaseChange.lean#L642). References: EGA IV (2.3.2).

> The scheme-theoretic image of a quasi-compact morphism `g : V ⟶ Y` of
> algebraic spaces over `S` commutes with flat base change: for a flat `f : X ⟶ Y`, the
> scheme-theoretic image of `V ×_Y X ⟶ X` is the inverse image along `f` of the scheme-theoretic
> image of `g`.

```lean
theorem schemeTheoreticImageSubfunctor_pullback_snd_of_isFlat_of_isQuasiCompact
    {X Y V : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : V ⟶ Y)
    (hf : IsFlat B S hS f.hom) (hg : IsQuasiCompact B S hS g.hom) :
    schemeTheoreticImageSubfunctor B S hS (pullback.snd g.hom f.hom) =
      (schemeTheoreticImageSubfunctor B S hS g.hom).preimage f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.30, Tag 03MK](https://stacks.math.columbia.edu/tag/03MK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
