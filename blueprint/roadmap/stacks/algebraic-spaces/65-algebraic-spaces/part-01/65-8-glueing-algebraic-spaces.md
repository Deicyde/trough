---
declaration: section
origin: cited
lean: AlgebraicGeometry.coproductInl_isOpenImmersion, AlgebraicGeometry.coproductInl_isClosedImmersion, AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan_ulift, AlgebraicGeometry.Space.exists_clopen_scheme_coproduct, AlgebraicGeometry.Sheaf.isEmpty_toScheme_of_eq_of_ne_ulift, AlgebraicGeometry.Space.isAlgebraicSpace_of_coproduct, AlgebraicGeometry.isAlgebraicSpace_coproduct, AlgebraicGeometry.Space.isAlgebraicSpaceULift_coproduct
statement: formalized
proof: formalized
---

# 65.8 Glueing algebraic spaces

Section 65.8 of the Stacks Project, [Tag 02WN](https://stacks.math.columbia.edu/tag/02WN). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F15, a lemma

[Tag 0F15](https://stacks.math.columbia.edu/tag/0F15) in the Stacks Project.

**`AlgebraicGeometry.coproductInl_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductInclusion.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductInclusion.lean#L449). The attribute's comment: “open immersion”.

> **Stacks 0F15.** The first inclusion into a binary coproduct of sheaves on the big fppf
> site of `S` is representable by open immersions. By symmetry the same holds for the second
> inclusion.

```lean
theorem coproductInl_isOpenImmersion (hc : IsColimit (BinaryCofan.mk iF iG)) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@IsOpenImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) iF.hom
```

**`AlgebraicGeometry.coproductInl_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductInclusion.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductInclusion.lean#L467). The attribute's comment: “closed immersion”.

> **Stacks 0F15.** The first inclusion into a binary coproduct of sheaves on the big fppf
> site of `S` is representable by closed immersions. By symmetry the same holds for the second
> inclusion.

```lean
theorem coproductInl_isClosedImmersion (hc : IsColimit (BinaryCofan.mk iF iG)) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) iF.hom
```

**`AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan_ulift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproductDecomposition.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproductDecomposition.lean#L86). The attribute's comment: “in an arbitrary value universe”.

> **Stacks 02WO and Stacks 0F15 for sheaves with values in a universe `max w u` independent of
> the universe `u` of the schemes.** A section `x` of a coproduct `P = ∐ᵢ Fᵢ` of pointwise
> `u`-small sheaves over an object `W` of the big fppf site of `S`, the index type being
> `u`-small, decomposes `W` into a family of pairwise disjoint open subobjects `W' i`, covering
> `W`, such that `x` restricted to `W' i` comes from `Fᵢ`; and each `W' i` is universal with that
> property.
>
> This is `AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan` with the value
> universe of the sheaves decoupled from the universe of the morphisms of the site. The
> decomposition machinery is not rebuilt: the sheaves are universe lifts of sheaves of `Type u`,
> the coproduct cocone descends to those by
> `AlgebraicGeometry.Space.exists_shrink_isColimit_cofan_of_small`, and the conclusion, which speaks
> of objects of the site and of sections, transports back along the lift.

```lean
theorem Sheaf.exists_clopen_decomposition_of_isColimit_cofan_ulift {I : Type v} [Small.{u} I]
    {F : I → Sheaf (BigFppfOver.topology B S hS) (Type (max w u))}
    (hF : ∀ i, FunctorToTypes.Small.{u} (F i).obj)
    {P : Sheaf (BigFppfOver.topology B S hS) (Type (max w u))} (ι : ∀ i, F i ⟶ P)
    (hP : IsColimit (Cofan.mk P ι)) (W : BigFppfOver B S hS) (x : P.obj.obj (op W)) :
    ∃ (W' : I → BigFppfOver B S hS) (p : ∀ i, W' i ⟶ W),
      (∀ i, IsOpenImmersion ((BigFppfOver.toScheme B S hS).map (p i))) ∧
      (∀ i, ∃ z : (F i).obj.obj (op (W' i)),
        (ι i).hom.app (op (W' i)) z = P.obj.map (p i).op x) ∧
      (∀ i i', i ≠ i' → ∀ (y : (BigFppfOver.toScheme B S hS).obj (W' i))
        (y' : (BigFppfOver.toScheme B S hS).obj (W' i')),
        (BigFppfOver.toScheme B S hS).map (p i) y ≠
          (BigFppfOver.toScheme B S hS).map (p i') y') ∧
      (∀ w : (BigFppfOver.toScheme B S hS).obj W,
        ∃ i, w ∈ Set.range ((BigFppfOver.toScheme B S hS).map (p i))) ∧
      (∀ (i : I) (T : BigFppfOver B S hS) (t : T ⟶ W),
        (∃ z : (F i).obj.obj (op T), (ι i).hom.app (op T) z = P.obj.map t.op x) →
        ∃ t' : T ⟶ W' i, t' ≫ p i = t)
```

## Tag 02WO, a lemma

[Tag 02WO](https://stacks.math.columbia.edu/tag/02WO) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_clopen_scheme_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Glueing/RepresentableCoproduct.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Glueing/RepresentableCoproduct.lean#L53).

> A sheaf coproduct represented by a scheme comes from an open-and-closed
> coproduct decomposition of that scheme.

```lean
theorem exists_clopen_scheme_coproduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (I : Type v)
    (Fᵢ : I → Sheaf (BigFppfOver.topology B S hS) (Type u))
    (F : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, Fᵢ i ⟶ F)
    (hcoprod : IsColimit (Cofan.mk F ι))
    (U : BigFppfOver B S hS)
    (e : F.obj ≅ yoneda.obj U) :
    ∃ (Uᵢ : I → BigFppfOver B S hS)
      (j : ∀ i, Uᵢ i ⟶ U)
      (eᵢ : ∀ i, (Fᵢ i).obj ≅ yoneda.obj (Uᵢ i)),
      (∀ i, AlgebraicGeometry.IsOpenImmersion
        ((BigFppfOver.toScheme B S hS).map (j i))) ∧
      (∀ i, AlgebraicGeometry.IsClosedImmersion
        ((BigFppfOver.toScheme B S hS).map (j i))) ∧
      (∀ i, (eᵢ i).hom ≫ yoneda.map (j i) = (ι i).hom ≫ e.hom) ∧
      Nonempty (IsColimit (Cofan.mk ((BigFppfOver.toScheme B S hS).obj U)
        (fun i => (BigFppfOver.toScheme B S hS).map (j i))))
```

**`AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan_ulift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproductDecomposition.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproductDecomposition.lean#L86). The attribute's comment: “in an arbitrary value universe, for pointwise `u`-small sheaves and a `u`-small index type; the smallness hypotheses are absent from `AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan`, which is the same statement in the value universe of the site”.

> **Stacks 02WO and Stacks 0F15 for sheaves with values in a universe `max w u` independent of
> the universe `u` of the schemes.** A section `x` of a coproduct `P = ∐ᵢ Fᵢ` of pointwise
> `u`-small sheaves over an object `W` of the big fppf site of `S`, the index type being
> `u`-small, decomposes `W` into a family of pairwise disjoint open subobjects `W' i`, covering
> `W`, such that `x` restricted to `W' i` comes from `Fᵢ`; and each `W' i` is universal with that
> property.
>
> This is `AlgebraicGeometry.Sheaf.exists_clopen_decomposition_of_isColimit_cofan` with the value
> universe of the sheaves decoupled from the universe of the morphisms of the site. The
> decomposition machinery is not rebuilt: the sheaves are universe lifts of sheaves of `Type u`,
> the coproduct cocone descends to those by
> `AlgebraicGeometry.Space.exists_shrink_isColimit_cofan_of_small`, and the conclusion, which speaks
> of objects of the site and of sections, transports back along the lift.

```lean
theorem Sheaf.exists_clopen_decomposition_of_isColimit_cofan_ulift {I : Type v} [Small.{u} I]
    {F : I → Sheaf (BigFppfOver.topology B S hS) (Type (max w u))}
    (hF : ∀ i, FunctorToTypes.Small.{u} (F i).obj)
    {P : Sheaf (BigFppfOver.topology B S hS) (Type (max w u))} (ι : ∀ i, F i ⟶ P)
    (hP : IsColimit (Cofan.mk P ι)) (W : BigFppfOver B S hS) (x : P.obj.obj (op W)) :
    ∃ (W' : I → BigFppfOver B S hS) (p : ∀ i, W' i ⟶ W),
      (∀ i, IsOpenImmersion ((BigFppfOver.toScheme B S hS).map (p i))) ∧
      (∀ i, ∃ z : (F i).obj.obj (op (W' i)),
        (ι i).hom.app (op (W' i)) z = P.obj.map (p i).op x) ∧
      (∀ i i', i ≠ i' → ∀ (y : (BigFppfOver.toScheme B S hS).obj (W' i))
        (y' : (BigFppfOver.toScheme B S hS).obj (W' i')),
        (BigFppfOver.toScheme B S hS).map (p i) y ≠
          (BigFppfOver.toScheme B S hS).map (p i') y') ∧
      (∀ w : (BigFppfOver.toScheme B S hS).obj W,
        ∃ i, w ∈ Set.range ((BigFppfOver.toScheme B S hS).map (p i))) ∧
      (∀ (i : I) (T : BigFppfOver B S hS) (t : T ⟶ W),
        (∃ z : (F i).obj.obj (op T), (ι i).hom.app (op T) z = P.obj.map t.op x) →
        ∃ t' : T ⟶ W' i, t' ≫ p i = t)
```

**`AlgebraicGeometry.Sheaf.isEmpty_toScheme_of_eq_of_ne_ulift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproductDecomposition.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproductDecomposition.lean#L197). The attribute's comment: “disjointness of the legs, in an arbitrary value universe”.

> **Distinct legs of a coproduct cocone of pointwise `u`-small sheaves on the big fppf site of
> `S` have disjoint images**, for a value universe independent of the universe of the objects of
> the site: an object of the site carrying sections of two different members of the family with the
> same image in the coproduct has no points.
>
> This is `AlgebraicGeometry.Sheaf.isEmpty_toScheme_of_eq_of_ne` with the value universe of the
> sheaves decoupled from the universe of the morphisms of the site, and is the disjointness half
> of Stacks 02WO there.

```lean
theorem Sheaf.isEmpty_toScheme_of_eq_of_ne_ulift {I : Type v} [Small.{u} I]
    {F : I → Sheaf (BigFppfOver.topology B S hS) (Type (max w u))}
    (hF : ∀ i, FunctorToTypes.Small.{u} (F i).obj)
    {P : Sheaf (BigFppfOver.topology B S hS) (Type (max w u))} (ι : ∀ i, F i ⟶ P)
    (hP : IsColimit (Cofan.mk P ι)) {i j : I} (hij : i ≠ j) {W : BigFppfOver B S hS}
    (x : (F i).obj.obj (op W)) (y : (F j).obj.obj (op W))
    (h : (ι i).hom.app (op W) x = (ι j).hom.app (op W) y) :
    IsEmpty ((BigFppfOver.toScheme B S hS).obj W)
```

## Tag 02WP, a lemma

[Tag 02WP](https://stacks.math.columbia.edu/tag/02WP) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductSummand.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductSummand.lean#L233).

> **Stacks 02WP.** Every summand of a sheaf coproduct that is an algebraic space is an
> algebraic space.

```lean
theorem isAlgebraicSpace_of_coproduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (I : Type v)
    (Fᵢ : I → Sheaf (BigFppfOver.topology B S hS) (Type u))
    (F : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, Fᵢ i ⟶ F)
    (hcoprod : IsColimit (Cofan.mk F ι))
    (hF : IsAlgebraicSpace B S hS F.obj)
    (i : I) : IsAlgebraicSpace B S hS (Fᵢ i).obj
```

## Tag 02WQ, a lemma

[Tag 02WQ](https://stacks.math.columbia.edu/tag/02WQ) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoproductAlgebraic.lean, line 808](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoproductAlgebraic.lean#L808).

> **Stacks 02WQ.** A coproduct of algebraic spaces over `S` is an algebraic space over `S`,
> provided the chosen surjective étale scheme atlases of the members have a coproduct inside the
> big fppf site over `S`.
>
> The sheaf condition is part of the data. The diagonal is representable by
> `AlgebraicGeometry.relativelyRepresentable_diag_of_isColimit_cofan`, and the coproduct `V` of
> the atlases, with the morphism to the coproduct sheaf glued by
> `AlgebraicGeometry.exists_hom_yoneda_of_isColimit_cofan`, is a surjective étale atlas by
> `AlgebraicGeometry.presheaf_inverseImage_of_isColimit_cofan`.

```lean
theorem isAlgebraicSpace_coproduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type v}
    (F : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : ∀ i, IsAlgebraicSpace B S hS (F i))
    (G : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, (⟨F i, (hF i).isSheaf⟩ :
      Sheaf (BigFppfOver.topology B S hS) (Type u)) ⟶ G)
    (hG : IsColimit (Cofan.mk G ι))
    (U : I → BigFppfOver B S hS)
    (f : ∀ i, yoneda.obj (U i) ⟶ F i)
    (hsurj : ∀ i, (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (f i))
    (hetale : ∀ i, (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (f i))
    (V : BigFppfOver B S hS)
    (j : ∀ i, U i ⟶ V)
    (hV : IsColimit (Cofan.mk V j)) :
    IsAlgebraicSpace B S hS G.obj
```

**`AlgebraicGeometry.Space.isAlgebraicSpaceULift_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproduct.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedCoproduct.lean#L306). The attribute's comment: “in an arbitrary value universe, for a `u`-small index type; the index is unrestricted in `AlgebraicGeometry.isAlgebraicSpace_coproduct`, which is the same statement in the value universe of the site”.

> **Stacks 02WQ** for presheaves with values in a universe `max w u` independent of the
> universe `u` of the schemes. A coproduct of algebraic spaces over `S`, indexed by a `u`-small
> type and with values in `Type (max w u)`, is an algebraic space over `S`, provided the chosen
> surjective étale scheme atlases of the members have a coproduct inside the big fppf site
> over `S`.
>
> The presheaves involved are pointwise `u`-small, so they are universe lifts of presheaves of
> `Type u` and the algebraic-space condition transports along the lift; the universal property of
> the coproduct transports along it too, by fullness, so no coproduct of sheaves of `Type u` is
> formed.

```lean
theorem isAlgebraicSpaceULift_coproduct {I : Type v} [Small.{u} I]
    {Fᵢ : I → Sheaf (BigFppfOver.topology B S hS) (Type (max w u))}
    (hFᵢ : ∀ i, IsAlgebraicSpaceULift.{w} B S hS (Fᵢ i).obj)
    {G : Sheaf (BigFppfOver.topology B S hS) (Type (max w u))} (ι : ∀ i, Fᵢ i ⟶ G)
    (hG : IsColimit (Cofan.mk G ι))
    (U : I → BigFppfOver B S hS)
    (a : ∀ i, (uliftYoneda.{w}).obj (U i) ⟶ (Fᵢ i).obj)
    (hsurj : ∀ i, (surjectiveOnSite B S hS).relative (uliftYoneda.{w}) (a i))
    (hetale : ∀ i, (etaleOnSite B S hS).relative (uliftYoneda.{w}) (a i))
    {V : BigFppfOver B S hS} {j : ∀ i, U i ⟶ V} (hV : IsColimit (Cofan.mk V j)) :
    IsAlgebraicSpaceULift.{w} B S hS G.obj
```

## Tag 02WR, a lemma

[Tag 02WR](https://stacks.math.columbia.edu/tag/02WR) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_open_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenCoverAlgebraic.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenCoverAlgebraic.lean#L308).

> **Stacks 02WR.** An fppf sheaf with a jointly surjective family of representable open
> algebraic-space subfunctors is an algebraic space, when the coproduct of the family is itself
> an algebraic space.

```lean
theorem isAlgebraicSpace_of_open_cover
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (I : Type v)
    (Fᵢ : I → Sheaf (BigFppfOver.topology B S hS) (Type u))
    (hFᵢ : ∀ i, IsAlgebraicSpace B S hS (Fᵢ i).obj)
    (G : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (ι : ∀ i, Fᵢ i ⟶ G)
    (hcoprod : IsColimit (Cofan.mk G ι))
    (g : G.obj ⟶ F)
    (hopen : ∀ i, (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@IsOpenImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) ((ι i).hom ≫ g))
    (hsurj : Presheaf.IsLocallySurjective
      (BigFppfOver.topology B S hS) g)
    (hG : IsAlgebraicSpace B S hS G.obj) :
    IsAlgebraicSpace B S hS F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.8, Tag 02WN](https://stacks.math.columbia.edu/tag/02WN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
