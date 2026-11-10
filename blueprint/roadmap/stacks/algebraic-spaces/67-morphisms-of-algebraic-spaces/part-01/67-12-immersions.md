---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isClosedImmersion_tfae, AlgebraicGeometry.Space.isImmersion_tfae_of_isAlgebraicSpace, AlgebraicGeometry.Space.isOpenImmersion_tfae_of_isAlgebraicSpace, AlgebraicGeometry.Space.isLocallyOfFiniteType_of_comp, AlgebraicGeometry.Space.relativelyRepresentable_of_comp, AlgebraicGeometry.Space.isSeparated_of_comp, AlgebraicGeometry.Space.mono_of_comp, AlgebraicGeometry.Space.isImmersion_of_comp_of_isLocallySeparated
statement: formalized
proof: formalized
---

# 67.12 Immersions

Section 67.12 of the Stacks Project, [Tag 03HB](https://stacks.math.columbia.edu/tag/03HB). 6 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03M4, a lemma

[Tag 03M4](https://stacks.math.columbia.edu/tag/03M4) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ClosedImmersionLocalCriterion.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/ClosedImmersionLocalCriterion.lean#L78). The attribute's comment: “closed immersions”. References: EGA I (4.2.4), “(b)”.

> **Stacks 03M4 for closed immersions**, unconditionally.
>
> A morphism of algebraic spaces over `S` is a closed immersion exactly when every one of its base
> changes to a representable presheaf is, exactly when every one of its base changes to an affine
> object of the site is, exactly when its base change along one surjective étale scheme chart of
> the target is, and exactly when its base changes along the members of some Zariski covering of
> the target are.
>
> This is `AlgebraicGeometry.Space.presheaf_tfae` at the closed immersions, whose descent
> hypothesis — Stacks 03I2 for the closed immersions of schemes — is
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`.

```lean
theorem isClosedImmersion_tfae
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    List.TFAE [
      IsClosedImmersion B S hS f,
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
        IsClosedImmersion B S hS (pullback.snd f g)),
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsClosedImmersion B S hS (pullback.snd f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ G),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsClosedImmersion B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor G),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsClosedImmersion B S hS (pullback.snd f (U i).ι))
    ]
```

**`AlgebraicGeometry.Space.isImmersion_tfae_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/ImmersionEtaleDescent.lean#L303). The attribute's comment: “immersions”. References: EGA I (4.2.4), “(a) immersion case”.

> A morphism of algebraic spaces over `S` is an immersion exactly when every one of its base
> changes to a representable presheaf is, exactly when every one of its base changes to an affine
> object of the site is, exactly when its base change along one surjective étale scheme chart of
> the target is, and exactly when its base changes along the members of some Zariski covering of
> the target are.
>
> This is `AlgebraicGeometry.Space.isImmersion_tfae` with its hypothesis `hdesc` supplied by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isImmersion`.

```lean
theorem isImmersion_tfae_of_isAlgebraicSpace
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    List.TFAE [
      IsImmersion B S hS f,
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
        IsImmersion B S hS (pullback.snd f g)),
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsImmersion B S hS (pullback.snd f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ G),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsImmersion B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor G),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsImmersion B S hS (pullback.snd f (U i).ι))
    ]
```

**`AlgebraicGeometry.Space.isOpenImmersion_tfae_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/OpenImmersionEtaleDescent.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/OpenImmersionEtaleDescent.lean#L510). The attribute's comment: “open immersions”.

> **Stacks 03M4 for open immersions**, unconditionally.
>
> A morphism of algebraic spaces over `S` is an open immersion exactly when every one of its base
> changes to a representable presheaf is, exactly when every one of its base changes to an affine
> object of the site is, exactly when its base change along one surjective étale scheme chart of
> the target is, and exactly when its base changes along the members of some Zariski covering of
> the target are.
>
> This is `AlgebraicGeometry.Space.isOpenImmersion_tfae` with its hypothesis `hdesc` — Stacks 03I2
> for open immersions — supplied by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isOpenImmersion`.

```lean
theorem isOpenImmersion_tfae_of_isAlgebraicSpace
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) :
    List.TFAE [
      IsOpenImmersion B S hS f,
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
        IsOpenImmersion B S hS (pullback.snd f g)),
      (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ G),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsOpenImmersion B S hS (pullback.snd f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ G),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsOpenImmersion B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor G),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsOpenImmersion B S hS (pullback.snd f (U i).ι))
    ]
```

## Tag 0AGC, a lemma

[Tag 0AGC](https://stacks.math.columbia.edu/tag/0AGC) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L206). The attribute's comment: “part (1): locally of finite type”. References: EGA I (6.6.6), “(v)”; EGA IV (1.3.4), “(v)”.

> **Stacks 0462.** If a composite of morphisms of algebraic spaces over `S` is locally of
> finite type, then so is its first factor.
>
> This is also the locally-of-finite-type clause of part (1) of **Stacks 0AGC**, whose other
> clauses are in
> `StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean`.

```lean
theorem isLocallyOfFiniteType_of_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g)) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.Space.relativelyRepresentable_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L270). The attribute's comment: “part (1): representable”.

> **Stacks 0AGC, part (1): representability.** If a composite of morphisms of presheaves on
> the big fppf site of `S` is representable and the intermediate presheaf has representable
> diagonal — in particular, if it is an algebraic space over `S` — then the first factor is
> representable.

```lean
theorem relativelyRepresentable_of_comp (hY : yoneda.relativelyRepresentable (diag Y))
    (g : Z ⟶ Y) (f : Y ⟶ X) (hgf : yoneda.relativelyRepresentable (g ≫ f)) :
    yoneda.relativelyRepresentable g
```

**`AlgebraicGeometry.Space.isSeparated_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L292). The attribute's comment: “part (1): separated”. References: EGA I (5.5.1), “(v)”.

> **Stacks 0AGC, part (1): separatedness.** If a composite of morphisms of algebraic spaces
> over `S` is separated, so is its first factor.
>
> This is also the separated part of **Stacks 03KR**, whose locally separated and
> quasi-separated parts are `AlgebraicGeometry.Space.isLocallySeparated_of_comp` and
> `AlgebraicGeometry.Space.isQuasiSeparated_of_comp`.

```lean
theorem isSeparated_of_comp (g : Z ⟶ Y) (f : Y ⟶ X)
    (hgf : IsSeparated B S hS (g ≫ f)) :
    IsSeparated B S hS g
```

**`AlgebraicGeometry.Space.mono_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L316). The attribute's comment: “part (1): monomorphism”.

> **Stacks 0AGC, part (1): monomorphisms.** If a composite of morphisms of algebraic spaces
> over `S` is a monomorphism, so is its first factor.
>
> Monomorphy of a morphism of algebraic spaces over `S` is monomorphy of the underlying morphism
> of presheaves on the big fppf site of `S`, by `AlgebraicGeometry.Space.mono_hom_iff_mono` of
> `StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Monomorphisms.lean`, so this clause is the
> cancellation of monomorphisms `CategoryTheory.mono_of_mono` read in that presheaf category.
> Nothing is required of `Y`.

```lean
theorem mono_of_comp (g : Z ⟶ Y) (f : Y ⟶ X) (hgf : Mono (g ≫ f)) : Mono g
```

**`AlgebraicGeometry.Space.isImmersion_of_comp_of_isLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L346). The attribute's comment: “part (2): immersion”.

> **Stacks 0AGC, part (2).** If a composite of morphisms of algebraic spaces over `S` is an
> immersion and its second factor is locally separated, then its first factor is an
> immersion.

```lean
theorem isImmersion_of_comp_of_isLocallySeparated (g : Z ⟶ Y) (f : Y ⟶ X)
    (hgf : IsImmersion B S hS (g ≫ f)) (hf : IsLocallySeparated B S hS f) :
    IsImmersion B S hS g
```

**`AlgebraicGeometry.Space.isClosedImmersion_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L357). The attribute's comment: “part (3): closed immersion”. References: EGA I (5.4.4).

> **Stacks 0AGC, part (3).** If a composite of morphisms of algebraic spaces over `S` is a
> closed immersion and its second factor is separated, then its first factor is a closed
> immersion.

```lean
theorem isClosedImmersion_of_comp_of_isSeparated (g : Z ⟶ Y) (f : Y ⟶ X)
    (hgf : IsClosedImmersion B S hS (g ≫ f)) (hf : IsSeparated B S hS f) :
    IsClosedImmersion B S hS g
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L417). The attribute's comment: “part (1): locally quasi-finite”.

> **Stacks 03XN.** If a composite of morphisms of algebraic spaces over `S` is locally
> quasi-finite, then so is its first factor.
>
> Local quasi-finiteness of morphisms of schemes is étale local on the source and target
> (Stacks 04R3) and is inherited by the first factor of a composite that has it, local finite
> type by Stacks 01T8 and the fibre condition by `AlgebraicGeometry.LocallyQuasiFinite.of_comp`,
> so this is an instance of the cancellation form of Stacks 03MJ.
>
> This is also the locally-quasi-finite clause of part (1) of **Stacks 0AGC**, whose other
> clauses are in `StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean`.

```lean
theorem isLocallyQuasiFinite_of_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hfg : IsLocallyQuasiFinite B S hS (f ≫ g)) :
    IsLocallyQuasiFinite B S hS f
```

## Tag 04CD, a lemma

[Tag 04CD](https://stacks.math.columbia.edu/tag/04CD) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_iff_isClosed_range_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionPoints.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionPoints.lean#L167). The attribute's comment: “closed immersion criterion”.

> **Stacks 04CD.** An immersion of algebraic spaces over `S` is a closed immersion exactly
> when the image of its point set is a closed subset of the point space of the target.

```lean
theorem isClosedImmersion_iff_isClosed_range_pointsMap (hX : IsAlgebraicSpace B S hS X)
    (i : Z ⟶ X) (hi : IsImmersion B S hS i) :
    IsClosedImmersion B S hS i ↔ IsClosed (Set.range (pointsMap B S hS Z i))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isEmbedding_pointsMap_of_isImmersion`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean#L219), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean#L241) (StacksFrontier).
- [`AlgebraicGeometry.Space.isLocallyClosed_range_pointsMap_of_isImmersion`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean#L228), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionPointEmbedding.lean#L242) (StacksFrontier).

## Tag 04CE, a remark

[Tag 04CE](https://stacks.math.columbia.edu/tag/04CE) in the Stacks Project.

**`AlgebraicGeometry.Space.range_pointsMap_ι_boundarySubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 680](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L680). The attribute's comment: “the points of the boundary subspace”.

> **Stacks 04CE.** The point set of the boundary subspace of an immersion is the boundary
> of the image of that immersion.

```lean
theorem range_pointsMap_ι_boundarySubspace (hX : IsAlgebraicSpace B S hS X) (i : Z ⟶ X)
    (hi : IsImmersion B S hS i) :
    Set.range (pointsMap B S hS (boundarySubspace B S hS hX i hi).toFunctor
        (boundarySubspace B S hS hX i hi).ι) =
      closure (Set.range (pointsMap B S hS Z i)) \ Set.range (pointsMap B S hS Z i)
```

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isReduced_boundarySubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 690](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L690). The attribute's comment: “the boundary subspace is reduced”.

> **Stacks 04CE.** The boundary subspace of an immersion is reduced, in the étale-local
> sense of Stacks 03E6.

```lean
theorem hasEtaleLocalProperty_isReduced_boundarySubspace (hX : IsAlgebraicSpace B S hS X)
    (i : Z ⟶ X) (hi : IsImmersion B S hS i) :
    HasEtaleLocalProperty B S hS (boundarySubspace B S hS hX i hi).toFunctor
      (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.range_pointsMap_ι_boundaryComplement_eq_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L699). The attribute's comment: “the open subspace is the complement of the boundary subspace”.

> **Stacks 04CE.** The open subspace through which an immersion is to be factored is the
> complement of its boundary subspace: the two have complementary point sets.

```lean
theorem range_pointsMap_ι_boundaryComplement_eq_compl (hX : IsAlgebraicSpace B S hS X)
    (i : Z ⟶ X) (hi : IsImmersion B S hS i) :
    Set.range (pointsMap B S hS
        (boundaryComplement B S hS X (Set.range (pointsMap B S hS Z i))).toFunctor
        (boundaryComplement B S hS X (Set.range (pointsMap B S hS Z i))).ι) =
      (Set.range (pointsMap B S hS (boundarySubspace B S hS hX i hi).toFunctor
        (boundarySubspace B S hS hX i hi).ι))ᶜ
```

**`AlgebraicGeometry.Space.isClosed_range_pointsMap_of_comp_ι_boundaryComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L742). The attribute's comment: “the image is closed away from the boundary”.

> **Stacks 04CE.** The image of an immersion is closed in the complement of its boundary:
> any factorisation of the immersion through that open subspace has closed image on points.

```lean
theorem isClosed_range_pointsMap_of_comp_ι_boundaryComplement (i : Z ⟶ X)
    (g : Z ⟶ (boundaryComplement B S hS X (Set.range (pointsMap B S hS Z i))).toFunctor)
    (hg : g ≫ (boundaryComplement B S hS X (Set.range (pointsMap B S hS Z i))).ι = i) :
    IsClosed (Set.range (pointsMap B S hS Z g))
```

**`AlgebraicGeometry.Space.exists_isClosedImmersion_comp_ι_boundaryComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 753](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L753). The attribute's comment: “an immersion is a closed immersion followed by an open immersion”.

> **Stacks 04CE.** Every immersion of algebraic spaces over `S` factors as a closed
> immersion into the complement of its boundary, followed by the open immersion of that open
> subspace into the target.

```lean
theorem exists_isClosedImmersion_comp_ι_boundaryComplement
    (hX : IsAlgebraicSpace B S hS X) (hZ : IsAlgebraicSpace B S hS Z) (i : Z ⟶ X)
    (hi : IsImmersion B S hS i) :
    ∃ g : Z ⟶ (boundaryComplement B S hS X (Set.range (pointsMap B S hS Z i))).toFunctor,
      IsClosedImmersion B S hS g ∧
        g ≫ (boundaryComplement B S hS X (Set.range (pointsMap B S hS Z i))).ι = i
```

## Tag 06EC, a remark

[Tag 06EC](https://stacks.math.columbia.edu/tag/06EC) in the Stacks Project.

**`AlgebraicGeometry.Space.boundaryComplement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L394). The attribute's comment: “the open subspace U with |U| = |X| ∖ ∂T”.

> **Stacks 06EC, the open subspace.** The open subspace of `X` obtained by removing the
> boundary `closure T \ T` of a set `T` of points of `X`: its point set is Mathlib's
> `coborder T`.
>
> This is `AlgebraicGeometry.Space.openSubspaceOfPoints` at `coborder T`; the definition needs
> no hypothesis on `T`, local closedness entering only through
> `AlgebraicGeometry.Space.isOpenSubspace_boundaryComplement`.

```lean
noncomputable def boundaryComplement (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (T : Set (points B S hS X)) : Subfunctor X
```

**`AlgebraicGeometry.Space.range_pointsMap_ι_boundaryComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L402). The attribute's comment: “the point set of U is the complement of the boundary of T”.

> **The point set of the complement of the boundary of `T` is `coborder T`**, that is, the
> complement of `closure T \ T`. This is the defining property `|U| = |X| ∖ ∂T` of the open
> subspace `U` of Stacks 06EC.

```lean
theorem range_pointsMap_ι_boundaryComplement (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (T : Set (points B S hS X)) :
    Set.range (pointsMap B S hS (boundaryComplement B S hS X T).toFunctor
      (boundaryComplement B S hS X T).ι) = coborder T
```

**`AlgebraicGeometry.Space.isOpenSubspace_boundaryComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L412). The attribute's comment: “U is an open subspace of X”.

> **The complement of the boundary of a locally closed set of points of an algebraic space is
> an open subspace of it.** This is the open subspace `U` of Stacks 06EC, whose existence the
> source takes from Stacks 03BZ.

```lean
theorem isOpenSubspace_boundaryComplement (hX : IsAlgebraicSpace B S hS X)
    {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    IsOpenSubspace B S hS (boundaryComplement B S hS X T)
```

**`AlgebraicGeometry.Space.reducedInducedSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L560). The attribute's comment: “the reduced induced subspace Z on a locally closed set of points”.

> **Stacks 06EC, the reduced induced subspace `Z`.** The *reduced induced subspace structure*
> on a locally closed set `T` of points of an algebraic space `X` over `S`: the reduced induced
> closed subspace of Stacks 03IQ on `T`, formed inside the open subspace
> `AlgebraicGeometry.Space.boundaryComplement` complementary to the boundary of `T`, where `T`
> is closed.

```lean
noncomputable def reducedInducedSubspace (hX : IsAlgebraicSpace B S hS X)
    {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    Subfunctor (boundaryComplement B S hS X T).toFunctor
```

**`AlgebraicGeometry.Space.isClosedSubspace_reducedInducedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L573). The attribute's comment: “Z is a closed subspace of U, so Z ⟶ U is a closed immersion”.

> **Stacks 06EC.** The reduced induced subspace on `T` is a closed subspace of the open
> subspace complementary to the boundary of `T`, so `Z ⟶ U` is a closed immersion.

```lean
theorem isClosedSubspace_reducedInducedSubspace (hX : IsAlgebraicSpace B S hS X)
    {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    IsClosedSubspace B S hS (reducedInducedSubspace B S hS hX hT)
```

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isReduced_reducedInducedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L581). The attribute's comment: “Z is a reduced algebraic space”.

> **Stacks 06EC.** The reduced induced subspace on `T` is reduced, in the étale-local sense
> of Stacks 03E6.

```lean
theorem hasEtaleLocalProperty_isReduced_reducedInducedSubspace
    (hX : IsAlgebraicSpace B S hS X) {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    HasEtaleLocalProperty B S hS (reducedInducedSubspace B S hS hX hT).toFunctor
      (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.range_pointsMap_comp_ι_reducedInducedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L600). The attribute's comment: “|Z| = T as subsets of |X|”.

> **Stacks 06EC.** The point set of the reduced induced subspace on `T` is `T` itself, as a
> subset of the points of `X`.

```lean
theorem range_pointsMap_comp_ι_reducedInducedSubspace (hX : IsAlgebraicSpace B S hS X)
    {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    Set.range (pointsMap B S hS (reducedInducedSubspace B S hS hX hT).toFunctor
      ((reducedInducedSubspace B S hS hX hT).ι ≫ (boundaryComplement B S hS X T).ι)) = T
```

**`AlgebraicGeometry.Space.isImmersion_comp_ι_reducedInducedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L612). The attribute's comment: “Z ⟶ U ⟶ X is an immersion”.

> **Stacks 06EC.** The composite `Z ⟶ U ⟶ X` of the reduced induced subspace on `T` with the
> open subspace complementary to the boundary of `T` is an immersion: a closed immersion
> followed by an open immersion, by Stacks 02YV.

```lean
theorem isImmersion_comp_ι_reducedInducedSubspace (hX : IsAlgebraicSpace B S hS X)
    {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    IsImmersion B S hS ((reducedInducedSubspace B S hS hX hT).ι ≫
      (boundaryComplement B S hS X T).ι)
```

**`AlgebraicGeometry.Space.eq_reducedInducedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L625). The attribute's comment: “uniqueness of the reduced induced subspace”.

> **Stacks 06EC, uniqueness.** A reduced closed subspace of the open subspace complementary
> to the boundary of `T` whose point set in `|X|` is `T` is the reduced induced subspace on
> `T`.

```lean
theorem eq_reducedInducedSubspace (hX : IsAlgebraicSpace B S hS X)
    {T : Set (points B S hS X)} (hT : IsLocallyClosed T)
    (W : Subfunctor (boundaryComplement B S hS X T).toFunctor)
    (hWc : IsClosedSubspace B S hS W)
    (hWT : Set.range (pointsMap B S hS W.toFunctor
      (W.ι ≫ (boundaryComplement B S hS X T).ι)) = T)
    (hWr : HasEtaleLocalProperty B S hS W.toFunctor (fun Y : Scheme.{u} => IsReduced Y)) :
    W = reducedInducedSubspace B S hS hX hT
```

**`AlgebraicGeometry.Space.existsUnique_reducedInducedSubspace_of_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean, line 646](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean#L646). The attribute's comment: “existence and uniqueness of the reduced induced subspace”.

> **Stacks 06EC.** A locally closed set `T` of points of an algebraic space `X` over `S`
> carries a unique reduced closed subspace structure inside the open subspace complementary to
> its boundary, and that subspace is an immersion into `X` with point set `T`. This is the
> *reduced induced subspace structure* on `T`, and it is
> `AlgebraicGeometry.Space.reducedInducedSubspace`.

```lean
theorem existsUnique_reducedInducedSubspace_of_isLocallyClosed
    (hX : IsAlgebraicSpace B S hS X) {T : Set (points B S hS X)} (hT : IsLocallyClosed T) :
    ∃! W : Subfunctor (boundaryComplement B S hS X T).toFunctor,
      IsClosedSubspace B S hS W ∧
        HasEtaleLocalProperty B S hS W.toFunctor (fun Y : Scheme.{u} => IsReduced Y) ∧
          Set.range (pointsMap B S hS W.toFunctor
            (W.ι ≫ (boundaryComplement B S hS X T).ι)) = T ∧
            IsImmersion B S hS (W.ι ≫ (boundaryComplement B S hS X T).ι)
```

## Tag 081U, a lemma

[Tag 081U](https://stacks.math.columbia.edu/tag/081U) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenImmersion_isClosedImmersion_comp_eq_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImmersionFactorization.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactImmersionFactorization.lean#L457).

> **Stacks 081U.** An immersion of algebraic spaces over `S` which is quasi-compact factors as
> an open immersion followed by a closed immersion.
>
> The intermediate algebraic space is the scheme-theoretic image of the morphism: it is a closed
> subspace of the target by Stacks 082X, and the morphism onto it is an open immersion by the
> quasi-compact case of Stacks 088G.

```lean
theorem exists_isOpenImmersion_isClosedImmersion_comp_eq_of_isQuasiCompact
    (hX : IsAlgebraicSpace B S hS X) (f : Z ⟶ X) (hf : IsImmersion B S hS f)
    (hq : IsQuasiCompact B S hS f) :
    ∃ (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (j : Z ⟶ W) (i : W ⟶ X),
      IsAlgebraicSpace B S hS W ∧ IsOpenImmersion B S hS j ∧
        IsClosedImmersion B S hS i ∧ j ≫ i = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.12, Tag 03HB](https://stacks.math.columbia.edu/tag/03HB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
