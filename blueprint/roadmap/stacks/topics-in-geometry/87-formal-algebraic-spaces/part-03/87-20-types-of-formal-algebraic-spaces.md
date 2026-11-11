---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isCountablyIndexed_of_surjective_flat, AlgebraicGeometry.FormalSpace.isCountablyIndexed_iff_of_surjective_flat, AlgebraicGeometry.FormalSpace.isCountablyIndexed_iff_of_surjective_flat', AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_iff_of_isSurjective_of_isRepresentableFlat, AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_iff_of_surjective_flat, AlgebraicGeometry.FormalSpace.isWeaklyAdic_iff_of_surjective_flat, AlgebraicGeometry.FormalSpace.isWeaklyAdic_iff_of_surjective_flat', AlgebraicGeometry.FormalSpace.isAdicStar_iff_of_surjective_flat
statement: formalized
proof: formalized
---

# 87.20 Types of formal algebraic spaces

Section 87.20 of the Stacks Project, [Tag 0AKR](https://stacks.math.columbia.edu/tag/0AKR). 11 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AKS, a lemma

[Tag 0AKS](https://stacks.math.columbia.edu/tag/0AKS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isCountablyIndexed_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedDescent.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedDescent.lean#L165). The attribute's comment: “the implication from the source being countably indexed to the target being countably indexed, which is the content of the source's proof; the converse is clause (1) of Stacks 0AKQ”.

> **Stacks 0AKS, the forward implication.** Let `f : X ⟶ Y` be a morphism of affine formal
> algebraic spaces over `S` which is representable by algebraic spaces, surjective and flat. If
> `X` is countably indexed then so is `Y`.

```lean
theorem isCountablyIndexed_of_isCountablyIndexed_of_surjective_flat
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hfrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsurj : IsSurjective B S hS f)
    (hflat : ∃ hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ g ↦ Space.HoldsOnEveryEtaleChartULift.{u + 1} B S hS
          (@AlgebraicGeometry.Flat.{u} : MorphismProperty Scheme.{u}) g.hom) f.hom hf)
    (hXc : IsCountablyIndexed B S hS X) :
    IsCountablyIndexed B S hS Y
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_iff_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L484). The attribute's comment: “the equivalence, at the source's own hypotheses. The forward implication is the source's cofinality argument, `isCountablyIndexed_target_of_surjective_flat`, which rests on Stacks 0AIA, on Stacks 0AKN — the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` — and on faithful flatness of a represented base change; the reverse implication is part (2) of Stacks 0AKP, the library's `isCountablyIndexed_of_relative_isAffineHom`”.

> **Stacks 0AKS.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is countably indexed
> if and only if `Y` is.

```lean
theorem isCountablyIndexed_iff_of_surjective_flat {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsurj : IsSurjective B S hS f) (hflat : IsRepresentableFlat B S hS f) :
    IsCountablyIndexed B S hS X ↔ IsCountablyIndexed B S hS Y
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_iff_of_surjective_flat'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L122). The attribute's comment: “the equivalence, at the source's own hypotheses. The forward implication is the source's cofinality argument, `AlgebraicGeometry.FormalSpace.isCountablyIndexed_target_of_surjective_flat`, which rests on Stacks 0AIA, on Stacks 0AKN — the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces` — and on faithful flatness of a represented base change; the reverse implication is clause (1) of Stacks 0AKQ”.

> **Stacks 0AKS.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is countably indexed
> if and only if `Y` is.

```lean
alias isCountablyIndexed_iff_of_surjective_flat'
```

## Tag 0GXR, a lemma

[Tag 0GXR](https://stacks.math.columbia.edu/tag/0GXR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_iff_of_isSurjective_of_isRepresentableFlat`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleChartTypes.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleChartTypes.lean#L114).

> **Stacks 0GXR.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is countably indexed
> and classical if and only if `Y` is.
>
> The countably indexed half is Stacks 0AKS. For the classical half, a presenting ring `A` of `Y`
> with a continuous taut homomorphism `A → C` to a presenting ring of `X` whose maps on quotients
> by open ideals are faithfully flat is
> `AlgebraicGeometry.FormalSpace.exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`,
> and pre-admissibility descends along it by Stacks 0GXN.

```lean
alias isCountablyIndexedAndClassical_iff_of_isSurjective_of_isRepresentableFlat
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAndClassical_iff_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L505). The attribute's comment: “the equivalence, at the source's own hypotheses. Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`; the countably indexed half of the forward implication is `isCountablyIndexed_target_of_surjective_flat`, the presenting ring of the target with its continuous taut homomorphism to that of the source is `exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`, and pre-admissibility descends along it by Stacks 0GXN; the reverse implication is clause (3) of Stacks 0AKP, the library's `isCountablyIndexedAndClassical_of_relative_isAffineHom`”.

> **Stacks 0GXR.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is countably indexed
> and classical if and only if `Y` is.

```lean
theorem isCountablyIndexedAndClassical_iff_of_surjective_flat {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsurj : IsSurjective B S hS f) (hflat : IsRepresentableFlat B S hS f) :
    IsCountablyIndexed B S hS X ∧ IsClassical B S hS X ↔
      IsCountablyIndexed B S hS Y ∧ IsClassical B S hS Y
```

## Tag 0GXS, a lemma

[Tag 0GXS](https://stacks.math.columbia.edu/tag/0GXS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_iff_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L535). The attribute's comment: “the equivalence, at the source's own hypotheses. Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`; the presenting ring of the target with its continuous taut homomorphism to that of the source is `exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`, which takes countable indexing of the source from item (5) of Stacks 0AIK. The forward implication is the library's Stacks 0GXP and the reverse one is clause (4) of Stacks 0AKP, the library's `isWeaklyAdic_of_relative_isAffineHom`”.

> **Stacks 0GXS.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is weakly adic if
> and only if `Y` is.

```lean
theorem isWeaklyAdic_iff_of_surjective_flat {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsurj : IsSurjective B S hS f) (hflat : IsRepresentableFlat B S hS f) :
    IsWeaklyAdic B S hS X ↔ IsWeaklyAdic B S hS Y
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_iff_of_surjective_flat'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L160). The attribute's comment: “the equivalence, at the source's own hypotheses. The presenting ring of the target together with the continuous taut homomorphism to the source's, which is Stacks 0AN0, the implication (1) ⟹ (3) of Stacks 0AN5 and the identification of Stacks 0AMZ, is the library's `AlgebraicGeometry.FormalSpace``.exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`, which takes countable indexing of the source from item (5) of Stacks 0AIK; Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`. The forward implication is the library's Stacks 0GXP and the reverse one is clause (3) of Stacks 0AKQ”.

> **Stacks 0GXS.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is weakly adic if
> and only if `Y` is.

```lean
alias isWeaklyAdic_iff_of_surjective_flat'
```

## Tag 0AKT, a lemma

[Tag 0AKT](https://stacks.math.columbia.edu/tag/0AKT) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAdicStar_iff_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L566). The attribute's comment: “the equivalence, at the source's own hypotheses. The presenting ring of the target with its continuous taut homomorphism to that of the source is `exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`, which takes countable indexing of the source from items (2), (3) and (5) of Stacks 0AIK; Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`. The forward implication is the library's Stacks 0GXQ and the reverse one is clause (5) of Stacks 0AKP, the library's `isAdicStar_of_relative_isAffineHom`”.

> **Stacks 0AKT.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is adic\* if and
> only if `Y` is.

```lean
theorem isAdicStar_iff_of_surjective_flat {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsurj : IsSurjective B S hS f) (hflat : IsRepresentableFlat B S hS f) :
    IsAdicStar B S hS X ↔ IsAdicStar B S hS Y
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_iff_of_surjective_flat'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferRefined.lean#L173). The attribute's comment: “the equivalence, at the source's own hypotheses. The presenting ring of the target together with the continuous taut homomorphism to the source's, which is Stacks 0AN0, the implication (1) ⟹ (3) of Stacks 0AN5 and the identification of Stacks 0AMZ, is the library's `AlgebraicGeometry.FormalSpace``.exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`, which takes countable indexing of the source from items (2), (3) and (5) of Stacks 0AIK; Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`. The forward implication is the library's Stacks 0GXQ and the reverse one is clause (4) of Stacks 0AKQ”.

> **Stacks 0AKT.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective and flat. Then `X` is adic\* if and
> only if `Y` is.

```lean
alias isAdicStar_iff_of_surjective_flat'
```

## Tag 0AKW, a lemma

[Tag 0AKW](https://stacks.math.columbia.edu/tag/0AKW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isNoetherian_iff_of_isSurjective_of_isRepresentableFlat`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleChartTypes.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleChartTypes.lean#L130).

> **Stacks 0AKW.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective, flat and locally of finite type. Then
> `X` is Noetherian if and only if `Y` is.
>
> The reverse implication is clause (5) of Stacks 0AKQ. For the forward one, let `C` be a
> Noetherian adic ring presenting `X`. A presenting ring `A` of `Y` with a continuous taut
> homomorphism `φ : A → C` whose maps on quotients by open ideals are faithfully flat is
> `AlgebraicGeometry.FormalSpace.exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`.
> By Stacks 0GXQ the ring `A` has a finitely generated ideal of definition `J` defining its
> topology; `A ⧸ J` is Noetherian by Stacks 033E, its faithfully flat extension
> `C ⧸ (J C)‾` being a quotient of the Noetherian ring `C`; and `A`, complete for the `J`-adic
> topology, is Noetherian by Stacks 05GH.

```lean
alias isNoetherian_iff_of_isSurjective_of_isRepresentableFlat
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_iff_of_surjective_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L599). The attribute's comment: “the equivalence, at the source's own hypotheses. The presenting ring of the target with its continuous taut homomorphism to that of the source is `exists_isTaut_faithfullyFlat_presentingRing_of_surjective_flat`; its finitely generated ideal of definition is the library's Stacks 0GXQ, the descent of the Noetherian property to the quotient by it is Stacks 033E, `descent_noetherian`, and the passage to the complete ring is Stacks 05GH, `noetherian_of_isAdicComplete_fg`; Stacks 0AKN is the library's `relative_isAffineHom_of_isRepresentableByAlgebraicSpaces`. The reverse implication is clause (6) of Stacks 0AKP, the library's `isNoetherian_of_relative_isAffineHom`”.

> **Stacks 0AKW.** Let `f : X ⟶ Y` be a morphism of affine formal algebraic spaces over `S`
> which is representable by algebraic spaces, surjective, flat and locally of finite type. Then
> `X` is Noetherian if and only if `Y` is.

```lean
theorem isNoetherian_iff_of_surjective_flat {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hY : IsAffineFormalAlgebraicSpace B S hS Y)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hsurj : IsSurjective B S hS f) (hflat : IsRepresentableFlat B S hS f)
    (hft : IsLocallyOfFiniteType B S hS f) :
    IsNoetherian B S hS X ↔ IsNoetherian B S hS Y
```

## Tag 0AKX, a lemma

[Tag 0AKX](https://stacks.math.columbia.edu/tag/0AKX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty_of_mem`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleChartTypes.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineEtaleChartTypes.lean#L172).

> **Stacks 0AKX.** Let `X` be a formal algebraic space over `S` and let `P` be one of the
> properties of affine formal algebraic spaces *countably indexed*, *countably indexed and
> classical*, *weakly adic*, *adic\** and *Noetherian*. The following are equivalent:
>
> 1. if `Y` is an affine formal algebraic space and `Y ⟶ X` is representable by algebraic spaces
>    and étale, then `Y` has property `P`;
> 2. for some covering `{Xᵢ ⟶ X}` as in Definition 0AIM each `Xᵢ` has property `P`.
>
> For (2) ⟹ (1) the atlas is refined against the chart and cut down to a finite subfamily by
> quasi-compactness; its members have `P` by Stacks 0AKQ, their disjoint union has `P`, and `P`
> passes to the chart along the surjective flat morphism from that disjoint union by Stacks 0AKS,
> 0GXR, 0GXS, 0AKT or 0AKW.

```lean
alias hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty_of_mem
```

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty_isCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AtlasChartCountablyIndexed.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AtlasChartCountablyIndexed.lean#L99). The attribute's comment: “the equivalence of conditions (1) and (2) at the property of being countably indexed, with nothing assumed. The refinement of the atlas against a chart is the library's `exists_countablyIndexed_surjective_flat_over_chart` (Stacks 0AJ3 in its chart form, clause (1) of Stacks 0AKQ, the implication (1) ⟹ (2) of Stacks 0AJ9 and the coproduct stability of countable indexing), and the transfer of countable indexing along the surjective flat morphism it produces is Stacks 0AKS. The equivalence is registered at this property rather than at an arbitrary one because the refinement is false at an arbitrary property”.

> **Stacks 0AKX at countable indexing.** Let `X` be a formal algebraic space over `S`. Then
> every affine formal algebraic space representable étale over `X` is countably indexed if and
> only if `X` admits an atlas as in Definition **Stacks 0AIM** all of whose members are countably
> indexed.
>
> The implication (1) ⟹ (2) is the atlas of `X`. For (2) ⟹ (1), a chart `g : Z ⟶ X` receives a
> surjective flat morphism, representable by algebraic spaces, from a countably indexed affine
> formal algebraic space — the coproduct of a finite jointly surjective subfamily of the atlas
> refined against `Z` — and **Stacks 0AKS** transfers countable indexing along it.

```lean
theorem hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty_isCountablyIndexed
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasAffineEtaleChartProperty B S hS X (IsCountablyIndexed B S hS) ↔
      HasAffineEtaleAtlasWithProperty B S hS X (IsCountablyIndexed B S hS)
```

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean, line 786](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransfer.lean#L786). The attribute's comment: “the equivalence of conditions (1) and (2), at the source's own hypotheses and for each of the five properties of its list. For (2) ⟹ (1) the refinement of the atlas against a chart is `exists_surjective_flat_over_chart_of_hasAffineEtaleAtlasWithProperty`: Stacks 0AJ3 for the fibre products, the coverings of Definition 0AIM, quasi-compactness of the chart, Stacks 0AKQ along the étale maps and the finite disjoint union of the members; the property then passes to the chart by Stacks 0AKS, 0GXR, 0GXS, 0AKT or 0AKW”.

> **Stacks 0AKX.** Let `X` be a formal algebraic space over `S` and let `P` be one of the
> properties of affine formal algebraic spaces *countably indexed*, *countably indexed and
> classical*, *weakly adic*, *adic\** and *Noetherian*. The following are equivalent:
>
> 1. if `Y` is an affine formal algebraic space and `Y ⟶ X` is representable by algebraic spaces
>    and étale, then `Y` has property `P`;
> 2. for some covering `{Xᵢ ⟶ X}` as in Definition 0AIM each `Xᵢ` has property `P`.
>
> For (2) ⟹ (1) the atlas is refined against the chart and cut down to a finite subfamily by
> quasi-compactness; its members have `P` by Stacks 0AKQ, their disjoint union has `P`, and `P`
> passes to the chart along the surjective flat morphism from that disjoint union by Stacks 0AKS,
> 0GXR, 0GXS, 0AKT or 0AKW.

```lean
theorem hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) (P : FppfSheaf B S hS → Prop)
    (hP : P = IsCountablyIndexed B S hS ∨
      P = (fun Z ↦ IsCountablyIndexed B S hS Z ∧ IsClassical B S hS Z) ∨
      P = IsWeaklyAdic B S hS ∨ P = IsAdicStar B S hS ∨ P = IsNoetherian B S hS) :
    HasAffineEtaleChartProperty B S hS X P ↔ HasAffineEtaleAtlasWithProperty B S hS X P
```

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_atlas_isCountablyIndexedAndClassical_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean#L224). The attribute's comment: “the equivalence of conditions (1) and (2) for the countably indexed and classical property of Stacks 0AIJ and Stacks 0AID, unconditionally. The three conditions on the property asked for by `hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty` above are, in order, clause (2) of Stacks 0AKQ (`isCountablyIndexedAndClassical_of_isRepresentable'`), the passage to a finite disjoint union (`isCountablyIndexed_sigma'` and `isClassical_sigma`), and Stacks 0GXR (`isCountablyIndexedAndClassical_iff_of_isSurjective_of_isRepresentableFlat`)”.

> Every affine formal algebraic space representable étale over a formal algebraic space `X` is
> countably indexed and classical if and only if `X` admits an atlas as in Definition 0AIM all of
> whose members are.

```lean
theorem hasAffineEtaleChartProperty_iff_atlas_isCountablyIndexedAndClassical_unconditional
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasAffineEtaleChartProperty B S hS X
        (fun Y ↦ IsCountablyIndexed B S hS Y ∧ IsClassical B S hS Y) ↔
      HasAffineEtaleAtlasWithProperty B S hS X
        (fun Y ↦ IsCountablyIndexed B S hS Y ∧ IsClassical B S hS Y)
```

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_atlas_isWeaklyAdic_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean#L247). The attribute's comment: “the equivalence of conditions (1) and (2) for the weakly adic property of Stacks 0AID, unconditionally. The three conditions on the property asked for by `hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty` above are, in order, clause (3) of Stacks 0AKQ (`isWeaklyAdic_of_isRepresentable'`), the passage to a finite disjoint union (`isWeaklyAdic_sigma'`), and Stacks 0GXS (`isWeaklyAdic_iff_of_surjective_flat'`)”.

> Every affine formal algebraic space representable étale over a formal algebraic space `X` is
> weakly adic if and only if `X` admits an atlas as in Definition 0AIM all of whose members are.

```lean
theorem hasAffineEtaleChartProperty_iff_atlas_isWeaklyAdic_unconditional
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasAffineEtaleChartProperty B S hS X (IsWeaklyAdic B S hS) ↔
      HasAffineEtaleAtlasWithProperty B S hS X (IsWeaklyAdic B S hS)
```

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_atlas_isAdicStar_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean#L265). The attribute's comment: “the equivalence of conditions (1) and (2) for the adic* property of Stacks 0AID, unconditionally. The three conditions on the property asked for by `hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty` above are, in order, clause (4) of Stacks 0AKQ (`isAdicStar_of_isRepresentable'`), the passage to a finite disjoint union (`isAdicStar_sigma'`), and Stacks 0AKT (`isAdicStar_iff_of_surjective_flat'`)”.

> Every affine formal algebraic space representable étale over a formal algebraic space `X` is
> adic\* if and only if `X` admits an atlas as in Definition 0AIM all of whose members are.

```lean
theorem hasAffineEtaleChartProperty_iff_atlas_isAdicStar_unconditional
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasAffineEtaleChartProperty B S hS X (IsAdicStar B S hS) ↔
      HasAffineEtaleAtlasWithProperty B S hS X (IsAdicStar B S hS)
```

**`AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_atlas_isNoetherian_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/TypeTransferVariants.lean#L285). The attribute's comment: “the equivalence of conditions (1) and (2) for the Noetherian property of Stacks 0AID, unconditionally. The three conditions on the property asked for by `hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty` above are, in order, clause (5) of Stacks 0AKQ (`isNoetherian_of_isRepresentable'`, which for this property also uses that a representable étale morphism is locally of finite type), the passage to a finite disjoint union (`isNoetherian_sigma'`), and Stacks 0AKW (`isNoetherian_iff_of_isSurjective_of_isRepresentableFlat`)”.

> Every affine formal algebraic space representable étale over a formal algebraic space `X` is
> Noetherian if and only if `X` admits an atlas as in Definition 0AIM all of whose members are.

```lean
theorem hasAffineEtaleChartProperty_iff_atlas_isNoetherian_unconditional
    (X : FppfSheaf B S hS) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasAffineEtaleChartProperty B S hS X (IsNoetherian B S hS) ↔
      HasAffineEtaleAtlasWithProperty B S hS X (IsNoetherian B S hS)
```

## Tag 0AKY, a definition

[Tag 0AKY](https://stacks.math.columbia.edu/tag/0AKY) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsLocallyCountablyIndexed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean#L98). The attribute's comment: “locally countably indexed”.

> **Stacks 0AKY, locally countably indexed.** A formal algebraic space over `S` is *locally
> countably indexed* when it admits an atlas as in Definition 0AIM by countably indexed affine
> formal algebraic spaces.

```lean
abbrev IsLocallyCountablyIndexed (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsLocallyCountablyIndexedAndClassical`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean#L106). The attribute's comment: “locally countably indexed and classical”.

> **Stacks 0AKY, locally countably indexed and classical.** A formal algebraic space over
> `S` is *locally countably indexed and classical* when it admits an atlas as in Definition 0AIM
> by affine formal algebraic spaces which are countably indexed and classical.

```lean
abbrev IsLocallyCountablyIndexedAndClassical (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsLocallyWeaklyAdic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean#L115). The attribute's comment: “locally weakly adic”.

> **Stacks 0AKY, locally weakly adic.** A formal algebraic space over `S` is *locally weakly
> adic* when it admits an atlas as in Definition 0AIM by weakly adic affine formal algebraic
> spaces.

```lean
abbrev IsLocallyWeaklyAdic (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsLocallyAdicStar`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean#L122). The attribute's comment: “locally adic star”.

> **Stacks 0AKY, locally adic\*.** A formal algebraic space over `S` is *locally adic\**
> when it admits an atlas as in Definition 0AIM by adic\* affine formal algebraic spaces.

```lean
abbrev IsLocallyAdicStar (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsLocallyNoetherian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Types.lean#L131). The attribute's comment: “locally Noetherian”.

> **Stacks 0AKY, locally Noetherian.** A formal algebraic space over `S` is *locally
> Noetherian* when it admits an atlas as in Definition 0AIM by Noetherian affine formal
> algebraic spaces, that is by affine formal algebraic spaces whose associated weakly admissible
> topological ring is Noetherian and adic.

```lean
abbrev IsLocallyNoetherian (X : FppfSheaf B S hS) : Prop
```

## Tag 0AQ1, a lemma

[Tag 0AQ1](https://stacks.math.columbia.edu/tag/0AQ1) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionSheaf_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlgebraicSpaceAtlas.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAlgebraicSpaceAtlas.lean#L538). The attribute's comment: “part (2)”.

> **Stacks 0AQ1, part (2).** Let `S` be a scheme, let `X` be a locally Noetherian algebraic
> space over `S` and let `T ⊆ |X|` be a closed subset. The completion `X_{/T}` of `X` along `T` is
> locally Noetherian.
>
> The affine étale charts `Spec A_k ⟶ X` of
> `AlgebraicGeometry.FormalSpace.exists_affine_etale_charts` are étale over the locally Noetherian
> `X`, so each `Spec A_k` is locally Noetherian and each `A_k` is a Noetherian ring; the
> set-theoretic condition is
> `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_completionSheaf`. With these the
> atlas argument of `AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionSheaf`
> applies.

```lean
theorem isLocallyNoetherian_completionSheaf_of_isLocallyNoetherian
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (T : Set (Space.points B S hS X)) (hT : @IsClosed _ (Space.pointTopology B S hS X) T) :
    IsLocallyNoetherian B S hS (Space.completionSheaf B S hS X T)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalAlgebraicSpace.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalAlgebraicSpace.lean#L321). The attribute's comment: “part (1): locally adic star; assumes the affine étale charts of X as hA, str, a, ha, hcov, chartwise quasi-compactness of the complement as hqc, and the 0AIS condition as hset”.

> **Stacks 0AQ1, part (1).** Let `S` be a scheme, let `X` be an algebraic space over `S` and
> let `T ⊆ |X|` be a closed subset such that `X \ T ⟶ X` is quasi-compact. The completion `X_{/T}`
> of `X` along `T` is *locally adic\**: the completions of the affine charts of `X` along the
> inverse images of `T` form an atlas of `X_{/T}`, and each of them is an adic\* affine formal
> algebraic space by the affine case, Stacks 0GBA (1), the complement of the inverse image of `T`
> on a chart being quasi-compact.
>
> The affine étale charts of `X` and the set-theoretic condition of Stacks 0AIS are carried as
> hypotheses, as in `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf`
> (Stacks 0AIZ); quasi-compactness of `X \ T ⟶ X` is carried in the form it is used in, namely
> chartwise quasi-compactness of the complement `hqc`, which is the source's step transferring
> the hypothesis from `X` to the charts. The hypothesis `HasStageAtlas` of Stacks 0AIY is *not*
> needed here: being adic\* already contains being an affine formal algebraic space.

```lean
theorem isLocallyAdicStar_completionSheaf
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    {Ix : Type (u + 1)} {A : Ix → Type u} [∀ i, CommRing (A i)]
    (hA : ∀ i, B.Contains (AlgebraicGeometry.Spec (.of (A i))))
    (str : ∀ i, AlgebraicGeometry.Spec (.of (A i)) ⟶ S)
    (a : ∀ i, yoneda.obj (affineOver B S hS (hA i) (str i)) ⟶ X)
    (ha : ∀ i, ∃ hai : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.sheafifiedULiftMap B S hS (a i)).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ q ↦ Space.IsEtaleULift.{u + 1} B S hS q.hom)
        (Space.sheafifiedULiftMap B S hS (a i)).hom hai)
    (hcov : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
          Sheaf.instHasColimitsOfSize
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i ↦ Space.sheafifiedULiftMap B S hS (a i)))
    (hqc : ∀ i, @IsCompact _
      (Space.pointTopology B S hS (yoneda.obj (affineOver B S hS (hA i) (str i))))
      (Space.pointsMap B S hS _ (a i) ⁻¹' T)ᶜ)
    (hset : SatisfiesSetTheoreticCondition B S hS (Space.completionSheaf B S hS X T)) :
    IsLocallyAdicStar B S hS (Space.completionSheaf B S hS X T)
```

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalAlgebraicSpace.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionFormalAlgebraicSpace.lean#L371). The attribute's comment: “part (2): locally Noetherian; assumes the affine étale charts of X as hA, str, a, ha, hcov, Noetherianness of the chart rings as hNoeth, and the 0AIS condition as hset”.

> **Stacks 0AQ1, part (2).** Let `S` be a scheme, let `X` be a locally Noetherian algebraic
> space over `S` and let `T ⊆ |X|` be a closed subset. The completion `X_{/T}` of `X` along `T` is
> *locally Noetherian*: the completions of the affine charts of `X` along the inverse images of
> `T` form an atlas of `X_{/T}`, and each of them is a Noetherian affine formal algebraic space by
> the affine case, Stacks 0GBA (3), the chart rings being Noetherian.
>
> The affine étale charts of `X` and the set-theoretic condition of Stacks 0AIS are carried as
> hypotheses, as in `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheaf`
> (Stacks 0AIZ); local Noetherianness of `X` is carried in the form it is used in, namely
> Noetherianness of the chart rings `hNoeth`, which is the source's step transferring the
> hypothesis from `X` to the charts. The hypothesis `HasStageAtlas` of Stacks 0AIY is *not* needed
> here: being Noetherian already contains being an affine formal algebraic space.

```lean
theorem isLocallyNoetherian_completionSheaf
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    {Ix : Type (u + 1)} {A : Ix → Type u} [∀ i, CommRing (A i)]
    (hNoeth : ∀ i, IsNoetherianRing (A i))
    (hA : ∀ i, B.Contains (AlgebraicGeometry.Spec (.of (A i))))
    (str : ∀ i, AlgebraicGeometry.Spec (.of (A i)) ⟶ S)
    (a : ∀ i, yoneda.obj (affineOver B S hS (hA i) (str i)) ⟶ X)
    (ha : ∀ i, ∃ hai : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.sheafifiedULiftMap B S hS (a i)).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun _ _ q ↦ Space.IsEtaleULift.{u + 1} B S hS q.hom)
        (Space.sheafifiedULiftMap B S hS (a i)).hom hai)
    (hcov : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
          Sheaf.instHasColimitsOfSize
        Sheaf.IsLocallySurjective
          (Sigma.desc fun i ↦ Space.sheafifiedULiftMap B S hS (a i)))
    (hset : SatisfiesSetTheoreticCondition B S hS (Space.completionSheaf B S hS X T)) :
    IsLocallyNoetherian B S hS (Space.completionSheaf B S hS X T)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSheaf_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionLocallyAdicStar.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionLocallyAdicStar.lean#L130). The attribute's comment: “part (1)”.

> **Stacks 0AQ1, part (1).** Let `S` be a scheme, let `X` be an algebraic space over `S` and
> let `T ⊆ |X|` be a closed subset such that the inclusion `X ∖ T ⟶ X` of the open complement is
> quasi-compact. Then the completion `X_{/T}` of `X` along `T` is locally adic*.
>
> The affine étale charts `Spec A_k ⟶ X` are those of
> `AlgebraicGeometry.FormalSpace.exists_affine_etale_charts`; on each, the complement of the
> inverse image of `T` is quasi-compact
> (`AlgebraicGeometry.Space.isCompact_compl_preimage_pointsMap_of_isQuasiCompact_ι`), and the
> set-theoretic condition of Stacks 0AIS is
> `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_completionSheaf`. With these the
> atlas argument of `AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSheaf` applies.

```lean
theorem isLocallyAdicStar_completionSheaf_of_isQuasiCompact
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X)) (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    (hqc : Space.IsQuasiCompact B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ).ι) :
    IsLocallyAdicStar B S hS (Space.completionSheaf B S hS X T)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSheaf_and_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionLocallyAdicStar.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionLocallyAdicStar.lean#L156).

> **Stacks 0AQ1.** Let `S` be a scheme, let `X` be an algebraic space over `S`, let `T ⊆ |X|`
> be a closed subset and let `X_{/T}` be the completion of `X` along `T`.
>
> 1. If `X ∖ T ⟶ X` is quasi-compact, then `X_{/T}` is locally adic*.
> 2. If `X` is locally Noetherian, then `X_{/T}` is locally Noetherian.
>
> The two parts are
> `AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionSheaf_of_isQuasiCompact` and
> `AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionSheaf_of_isLocallyNoetherian`.

```lean
theorem isLocallyAdicStar_completionSheaf_and_isLocallyNoetherian
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X)) (hT : @IsClosed _ (Space.pointTopology B S hS X) T) :
    (Space.IsQuasiCompact B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ).ι →
        IsLocallyAdicStar B S hS (Space.completionSheaf B S hS X T)) ∧
      (Space.IsLocallyNoetherian B S hS X →
        IsLocallyNoetherian B S hS (Space.completionSheaf B S hS X T))
```

## Tag 0CKX, a remark

[Tag 0CKX](https://stacks.math.columbia.edu/tag/0CKX) in the Stacks Project.

**`RationalPowerSeries.mem_radical_polynomialTIdeal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L138). The attribute's comment: “the radical of (t) in the monoid algebra”.

> **Stacks 0CKX.** The radical of `(t)` in `k[t^(ℚ≥0)]` is the ideal of polynomials with
> vanishing constant coefficient: a positive exponent becomes at least one after enough
> multiplications.

```lean
theorem mem_radical_polynomialTIdeal_iff (k : Type*) [Field k] (p : rationalPolynomial k) :
    p ∈ (polynomialTIdeal k).radical ↔ p.coeff 0 = 0
```

**`RationalPowerSeries.isMaximal_radical_polynomialTIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L177). The attribute's comment: “the radical of (t) is the maximal ideal”.

> **Stacks 0CKX.** The radical of `(t)` is a maximal ideal of `k[t^(ℚ≥0)]`, being the
> kernel of the constant-coefficient map onto the field `k`.

```lean
theorem isMaximal_radical_polynomialTIdeal (k : Type*) [Field k] :
    ((polynomialTIdeal k).radical).IsMaximal
```

**`RationalPowerSeries.radicalQuotientEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L184). The attribute's comment: “the residue field at the radical of (t)”.

> **Stacks 0CKX.** The residue field of `k[t^(ℚ≥0)]` at the radical of `(t)` is `k`.

```lean
def radicalQuotientEquiv (k : Type*) [Field k] :
    rationalPolynomial k ⧸ (polynomialTIdeal k).radical ≃+* k
```

**`RationalPowerSeries.radical_polynomialTIdeal_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L192). The attribute's comment: “J ^ 2 = J for J the radical of (t)”.

> **Stacks 0CKX.** The radical of `(t)` is idempotent: a monomial of positive exponent is
> the square of the monomial of half that exponent.

```lean
theorem radical_polynomialTIdeal_sq (k : Type*) [Field k] :
    (polynomialTIdeal k).radical ^ 2 = (polynomialTIdeal k).radical
```

**`RationalPowerSeries.radical_polynomialTIdeal_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L223). The attribute's comment: “J ^ n = J for J the radical of (t)”.

> **Stacks 0CKX.** Every positive power of the radical of `(t)` equals it, so the tower
> defining its adic completion is constant.

```lean
theorem radical_polynomialTIdeal_pow (k : Type*) [Field k] {n : ℕ} (hn : n ≠ 0) :
    (polynomialTIdeal k).radical ^ n = (polynomialTIdeal k).radical
```

**`RationalPowerSeries.radicalAdicCompletionEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L267). The attribute's comment: “the radical-adic completion of the monoid algebra is k”.

> **Stacks 0CKX.** The completion of `k[t^(ℚ≥0)]` at the radical of `(t)` is `k` itself,
> because that radical is idempotent.

```lean
def radicalAdicCompletionEquiv (k : Type*) [Field k] :
    AdicCompletion (polynomialTIdeal k).radical (rationalPolynomial k) ≃+* k
```

**`RationalPowerSeries.injective_of_rationalPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L282). The attribute's comment: “the monoid algebra sits inside its (t)-adic completion”.

> **Stacks 0CKX.** The monoid algebra is contained in its `(t)`-adic completion: a
> polynomial whose class vanishes modulo every power of `(t)` has all coefficients zero.

```lean
theorem injective_of_rationalPolynomial (k : Type*) [CommRing k] :
    Function.Injective
      (AdicCompletion.of (polynomialTIdeal k) (rationalPolynomial k))
```

**`RationalPowerSeries.not_injective_compareAlgHom_radical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L314). The attribute's comment: “the comparison map is not injective”.

> **Stacks 0CKX.** The comparison map from the `(t)`-adic completion of `k[t^(ℚ≥0)]` to the
> completion at the radical of `(t)` is not injective: it kills the nonzero element `t`.

```lean
theorem not_injective_compareAlgHom_radical (k : Type*) [Field k] :
    ¬ Function.Injective
      (AdicCompletion.compareAlgHom k (polynomialTIdeal_pow_one_le_radical k))
```

**`RationalPowerSeries.not_bijective_compareAlgHom_radical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L324). The attribute's comment: “the comparison map is not a ring isomorphism”.

> **Stacks 0CKX.** The natural map from the `I`-adic completion to the `√I`-adic completion
> of a ring can fail to be an isomorphism: for `I = (t)` in `k[t^(ℚ≥0)]` it is not bijective.

```lean
theorem not_bijective_compareAlgHom_radical (k : Type*) [Field k] :
    ¬ Function.Bijective
      (AdicCompletion.compareAlgHom k (polynomialTIdeal_pow_one_le_radical k))
```

**`RationalPowerSeries.isEmpty_ringEquiv_adicCompletion_radical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/RadicalCompletion.lean#L333). The attribute's comment: “the two completions are not isomorphic”.

> **Stacks 0CKX.** The two completions are not isomorphic by any ring map at all: the
> completion at the radical is the field `k`, while `t` is a nonzero non-unit of the `(t)`-adic
> completion.

```lean
theorem isEmpty_ringEquiv_adicCompletion_radical (k : Type*) [Field k] :
    IsEmpty (rationalPowerSeries k ≃+*
      AdicCompletion (polynomialTIdeal k).radical (rationalPolynomial k))
```

## Tag 0GBB, a lemma

[Tag 0GBB](https://stacks.math.columbia.edu/tag/0GBB) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyCountablyIndexed_pullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesRefined.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesRefined.lean#L133). The attribute's comment: “clause (1), locally countably indexed; the affine case (0AN3 with 0GB4) and the 0AIM covering condition for the chart cover are named hypotheses”.

> **Stacks 0GBB, clause (1).** If `X` and `Z` are locally countably indexed, then so is
> `X ×_Y Z`. The hypotheses `hPaff` and `hcover` are the inputs of the source which the
> library does not carry; the implication (2) ⟹ (1) of Stacks 0AKX, which the other four clauses
> carry as `h0AKX`, is a theorem at countable indexing and is discharged here, as is
> separatedness of the chart.

```lean
theorem isLocallyCountablyIndexed_pullback' {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z)
    (hPaff : AffineChartFibreProductStable B S hS (IsCountablyIndexed B S hS))
    (hcover : HasChartPullbackCover B S hS f g) :
    IsLocallyCountablyIndexed B S hS (pullback f g)
```

**`AlgebraicGeometry.FormalSpace.isLocallyCountablyIndexed_pullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean#L286). The attribute's comment: “clause (1), locally countably indexed, in full under the source's hypotheses. The affine case (0AN3 with 0GB4) is `affineChartFibreProductStable_isCountablyIndexed`; the 0AIS set-theoretic condition for X ×\_Y Z is `satisfiesSetTheoreticCondition_pullback_of_isFormalAlgebraicSpace'`, from 0AIP; the 0AIM covering condition for the chart cover is `isLocallySurjective_sigmaDesc_chartPullbackMap`; Stacks 0AKX (2) implies (1) is `AlgebraicGeometry.FormalSpace.hasAffineEtaleChartProperty_iff_hasAffineEtaleAtlasWithProperty_isCountablyIndexed`; and the étale case of Stacks 0AJ3 is `isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`”.

> **Stacks 0GBB, clause (1).** If `X` and `Z` are locally countably indexed, then so is
> `X ×_Y Z`. The hypotheses are exactly the source's.

```lean
theorem isLocallyCountablyIndexed_pullback_unconditional {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Z ⟶ Y)
    (hX : IsLocallyCountablyIndexed B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyCountablyIndexed B S hS Z) :
    IsLocallyCountablyIndexed B S hS (pullback f g)
```

**`AlgebraicGeometry.FormalSpace.isLocallyCountablyIndexedAndClassical_pullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean#L311). The attribute's comment: “clause (2), locally countably indexed and classical, in full under the source's hypotheses. The affine case (0AN3 with 0GB4) is `affineChartFibreProductStable_isCountablyIndexedAndClassical`; the 0AIS set-theoretic condition for X ×\_Y Z is `satisfiesSetTheoreticCondition_pullback_of_isFormalAlgebraicSpace'`, from 0AIP; the 0AIM covering condition for the chart cover is `isLocallySurjective_sigmaDesc_chartPullbackMap`; Stacks 0AKX (2) implies (1) is `hasAffineEtaleChartProperty_iff_atlas_isCountablyIndexedAndClassical_unconditional`; and the étale case of Stacks 0AJ3 is `isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`”.

> **Stacks 0GBB, clause (2).** If `X` and `Z` are locally countably indexed and classical, then
> so is `X ×_Y Z`. The hypotheses are exactly the source's.

```lean
theorem isLocallyCountablyIndexedAndClassical_pullback_unconditional {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Z ⟶ Y) (hX : IsLocallyCountablyIndexedAndClassical B S hS X)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyCountablyIndexedAndClassical B S hS Z) :
    IsLocallyCountablyIndexedAndClassical B S hS (pullback f g)
```

**`AlgebraicGeometry.FormalSpace.isLocallyWeaklyAdic_pullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean#L335). The attribute's comment: “clause (3), locally weakly adic, in full under the source's hypotheses. The affine case (0AN3 with 0GXJ) is `affineChartFibreProductStable_isWeaklyAdic`; the 0AIS set-theoretic condition for X ×\_Y Z is `satisfiesSetTheoreticCondition_pullback_of_isFormalAlgebraicSpace'`, from 0AIP; the 0AIM covering condition for the chart cover is `isLocallySurjective_sigmaDesc_chartPullbackMap`; Stacks 0AKX (2) implies (1) is `hasAffineEtaleChartProperty_iff_atlas_isWeaklyAdic_unconditional`; and the étale case of Stacks 0AJ3 is `isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`”.

> **Stacks 0GBB, clause (3).** If `X` and `Z` are locally weakly adic, then so is `X ×_Y Z`. The
> hypotheses are exactly the source's.

```lean
theorem isLocallyWeaklyAdic_pullback_unconditional {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Z ⟶ Y)
    (hX : IsLocallyWeaklyAdic B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyWeaklyAdic B S hS Z) :
    IsLocallyWeaklyAdic B S hS (pullback f g)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_pullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean#L357). The attribute's comment: “clause (4), locally adic*, in full under the source's hypotheses. The affine case (0AN3 with 0GB4) is `affineChartFibreProductStable_isAdicStar`; the 0AIS set-theoretic condition for X ×\_Y Z is `satisfiesSetTheoreticCondition_pullback_of_isFormalAlgebraicSpace'`, from 0AIP; the 0AIM covering condition for the chart cover is `isLocallySurjective_sigmaDesc_chartPullbackMap`; Stacks 0AKX (2) implies (1) is `hasAffineEtaleChartProperty_iff_atlas_isAdicStar_unconditional`; and the étale case of Stacks 0AJ3 is `isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`”.

> **Stacks 0GBB, clause (4).** If `X` and `Z` are locally adic\*, then so is `X ×_Y Z`. The
> hypotheses are exactly the source's.

```lean
theorem isLocallyAdicStar_pullback_unconditional {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyAdicStar B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyAdicStar B S hS Z) :
    IsLocallyAdicStar B S hS (pullback f g)
```

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_pullback_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FibreProductTypesSupplement.lean#L410). The attribute's comment: “clause (5), locally Noetherian, in full under the source's hypotheses. The affine case (0AN3 with 0GB4) is `affineChartFibreProductStable_isNoetherian`, the affine case RELATIVE TO THE CHART MAP: the map-blind form is unsatisfiable at IsNoetherian -- it quantifies over all affine U, V, W with no condition on the maps, which is false for Spec K over Spec k with K/k of infinite transcendence degree, the presenting ring of the fibre product being the non-Noetherian K tensor K -- so a registration on it would have been vacuous. The docstring gives that witness. The source's finite type condition on the reductions, hfin, is carried to the chart maps by `hasLocallyOfFiniteTypeReduction_chart` and from there to `algebraMap C A` by the affine dictionary `chartPropertyIsFiniteTypeOnReductions`. The 0AIS set-theoretic condition for X ×\_Y Z is `satisfiesSetTheoreticCondition_pullback_of_isFormalAlgebraicSpace'`, from 0AIP; the 0AIM covering condition for the chart cover is `isLocallySurjective_sigmaDesc_chartPullbackMap`; Stacks 0AKX (2) implies (1) is `hasAffineEtaleChartProperty_iff_atlas_isNoetherian_unconditional`; and the étale case of Stacks 0AJ3 is `isFormalAlgebraicSpace_pullback_of_isRepresentableEtale`”.

> **Stacks 0GBB, clause (5).** If `X` and `Z` are locally Noetherian and `X_red ⟶ Y_red` is
> locally of finite type, then `X ×_Y Z` is locally Noetherian.
>
> `hfin` is the source's own hypothesis on the reduction morphism, and the hypotheses are exactly
> the source's.
>
> The affine case is relative to the chart map,
> `AlgebraicGeometry.FormalSpace.AffineChartFibreProductStableRel`: the map-blind
> `AlgebraicGeometry.FormalSpace.AffineChartFibreProductStable`, which the other four clauses
> prove, is *unsatisfiable* at `P := IsNoetherian`: it asserts that every fibre product of
> Noetherian affine formal algebraic spaces over an affine formal algebraic space is Noetherian,
> which is false in every big fppf site over a nonempty base. Take a point of `S` with residue field
> `k` and `K = k(x₁, x₂, …)`; then `Spec k` and `Spec K` are affine objects of the site, hence affine
> formal algebraic spaces by
> `AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_sheafifiedYoneda'`, and `Spec K` is
> Noetherian — its presenting ring `K` is discrete, hence Noetherian, complete and adic with ideal of
> definition `(0)`. The sheafified Yoneda embedding preserves fibre products on this subcanonical
> site, so `Spec K ×_{Spec k} Spec K = Spec (K ⊗_k K)`, whose presenting ring is `K ⊗_k K`; that
> ring is not Noetherian, and by
> `AlgebraicGeometry.FormalSpace.exists_continuous_ringEquiv_of_isPresentingRing` the presenting
> ring is unique up to isomorphism of topological rings, so no Noetherian one presents it. A
> registration of this clause on the map-blind affine case would be vacuously true.
>
> The passage from the chart map to the morphism into the shrunk base of the affine case transports
> nothing along the monomorphism of the shrink: reduction is not invariant along an arbitrary
> monomorphism, `AlgebraicGeometry.FormalSpace.isReduction_completionSheaf` being a
> counterexample.

```lean
theorem isLocallyNoetherian_pullback_unconditional {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Z ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hfin : HasLocallyOfFiniteTypeReduction B S hS f) :
    IsLocallyNoetherian B S hS (pullback f g)
```

## Tag 0GHM, a lemma

[Tag 0GHM](https://stacks.math.columbia.edu/tag/0GHM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_finiteOrderThickening_presentation_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianColimitPresentation.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/LocallyNoetherianColimitPresentation.lean#L317).

> **Stacks 0GHM.** Let `X` be a locally Noetherian formal algebraic space over `S`. Then
> `X = colim X_n` for a system `X_0 ⟶ X_1 ⟶ X_2 ⟶ ⋯` of finite-order thickenings of locally
> Noetherian algebraic spaces over `S`, where `X_0 = X_red` and `X_n` is the `n`th infinitesimal
> neighbourhood of `X_0` in `X_m` for all `m ≥ n`.
>
> The stages are indexed from zero, so the stage `n` is the source's `X_{n+1}`. In detail: every
> `X_n` is an algebraic space whose étale atlases are locally Noetherian; every transition morphism
> `X_n ⟶ X_m` is representable and an `m`th-order thickening on every represented base change; on
> every represented base change along a section of `X_m`, the ideal sheaf of `X_n` is the
> `(n + 1)`st power of the ideal sheaf of `X_0`; and `X` is the colimit of the `X_n`, its colimit
> leg at `0` exhibiting `X_0` as the reduction of `X`.

```lean
theorem exists_finiteOrderThickening_presentation_of_isLocallyNoetherian
    (X : FppfSheaf B S hS) (hX : IsLocallyNoetherian B S hS X) :
    ∃ E : ℕ ⥤ FppfSheaf B S hS,
      (∀ n, Space.IsAlgebraicSpaceULift.{u + 1} B S hS (E.obj n).obj) ∧
      (∀ n, Space.HasEtaleLocalPropertyULift.{u + 1} B S hS (E.obj n).obj
        (fun T : Scheme.{u} ↦ AlgebraicGeometry.IsLocallyNoetherian T)) ∧
      (∀ ⦃n m : ℕ⦄ (f : n ⟶ m), Space.HasSchemePropertyULift.{u + 1} B S hS
        (fun _ _ k ↦ Stacks.Thickenings.IsNthOrderThickening m k) (E.map f).hom) ∧
      (∀ (n m : ℕ) (hnm : n ≤ m) {a b c : BigFppfOver B S hS}
        (g : uliftYoneda.{u + 1}.obj a ⟶ (E.obj m).obj)
        {fst₀ : uliftYoneda.{u + 1}.obj b ⟶ (E.obj 0).obj} {snd₀ : b ⟶ a}
        (_ : IsPullback fst₀ (uliftYoneda.{u + 1}.map snd₀)
          (E.map (homOfLE (Nat.zero_le m))).hom g)
        {fstₙ : uliftYoneda.{u + 1}.obj c ⟶ (E.obj n).obj} {sndₙ : c ⟶ a}
        (_ : IsPullback fstₙ (uliftYoneda.{u + 1}.map sndₙ) (E.map (homOfLE hnm)).hom g),
        ((BigFppfOver.toScheme B S hS).map snd₀).ker ^ (n + 1) =
          ((BigFppfOver.toScheme B S hS).map sndₙ).ker) ∧
      ∃ e : X ≅ colimit E, IsReduction B S hS X (E.obj 0) (colimit.ι E 0 ≫ e.inv)
```

**`AlgebraicGeometry.FormalSpace.exists_finiteOrderThickening_presentation_formalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianColimitPresentation.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianColimitPresentation.lean#L174). The attribute's comment: “Noetherian affine formal algebraic space”.

> **Stacks 0GHM**, for a Noetherian affine formal algebraic space. Let `A` be a Noetherian
> topological ring whose topology is adic. Then the formal spectrum of `A` is the colimit of a
> sequence `X_0 → X_1 → X_2 → ⋯` of affine schemes over `S` whose transition morphisms are
> finite-order thickenings, whose terms are all locally Noetherian, whose first term `X_0` is
> reduced, and in which `X_n` is the `n`th infinitesimal neighbourhood of `X_0` inside `X_m` for
> every `m ≥ n` — the last clause in the form of the equality
> `(X_0 ⟶ X_m).ker ^ (n + 1) = (X_n ⟶ X_m).ker` of ideal sheaves on `X_m`.

```lean
theorem exists_finiteOrderThickening_presentation_formalSpectrum
    [IsTopologicalRing A] [IsLinearTopology A A] [IsNoetherianRing A]
    {I : Ideal A} (hI : _root_.IsAdic I) (D : QuotientSystem B S hS A) :
    ∃ E : ℕ ⥤ BigAffineFppf B S hS,
      IsReduced ((BigAffineFppf.toScheme B S hS).obj (E.obj 0)) ∧
      (∀ n, IsLocallyNoetherian ((BigAffineFppf.toScheme B S hS).obj (E.obj n))) ∧
      (∀ ⦃n m : ℕ⦄ (f : n ⟶ m), Stacks.Thickenings.IsFiniteOrderThickening
        ((BigAffineFppf.toScheme B S hS).map (E.map f))) ∧
      (∀ (n m : ℕ) (hnm : n ≤ m),
        ((BigAffineFppf.toScheme B S hS).map (E.map (homOfLE (Nat.zero_le m)))).ker ^ (n + 1) =
          ((BigAffineFppf.toScheme B S hS).map (E.map (homOfLE hnm))).ker) ∧
      Nonempty (formalSpectrum D ≅ colimit (E ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.20, Tag 0AKR](https://stacks.math.columbia.edu/tag/0AKR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
