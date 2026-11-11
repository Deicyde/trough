---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isReasonableSpace, AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isDecentSpace, AlgebraicGeometry.Space.mem_range_pointsMap_schematicLocus_iff_exists_isAffine_isOpenImmersion, AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_finite_etale_cover
statement: formalized
proof: formalized
---

# 68.10 Schematic locus

Section 68.10 of the Stacks Project, [Tag 06NN](https://stacks.math.columbia.edu/tag/06NN). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03JI, a proposition

[Tag 03JI](https://stacks.math.columbia.edu/tag/03JI) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isReasonableSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableDenseSchematicLocus.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableDenseSchematicLocus.lean#L206).

> **Stacks 03JI.** The schematic locus of a reasonable algebraic space is dense: a reasonable
> algebraic space `X` over a scheme `S` has a representable open subspace whose point set is dense
> in `|X|`.
>
> Reasonableness is condition (2) of Stacks 03JT, so Stacks 03JT in the form
> `AlgebraicGeometry.Space.exists_boundedEtaleCover_of_isReasonableSpace` gives a jointly
> surjective family of étale charts `φ i` by affine schemes with universally bounded fibres. No
> member of the family is surjective, so the corollary does not apply to `X` directly. Replacing
> `X` by the open subspace `X i` swept out by `φ i` — Stacks 06NF — makes the induced chart
> `ψ i : h_{U i} ⟶ X i` surjective, and the bound passes from `φ i` to `ψ i` because `(X i).ι` is
> a monomorphism. The corollary then gives in each `X i` a representable open subspace `L i` with
> dense point set.
>
> Stacks 03JH, in the form
> `AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isAlgebraicSpace`,
> reduces the conclusion to finding a nonempty representable open subspace inside every nonempty
> open subspace `G` of `X`. The point sets of the `X i` cover `|X|`, so some `|X i|` meets `|G|`;
> the preimage of `|G|` in `|X i|` is then a nonempty open set, which by density meets `|L i|`. So
> `|G| ∩ |L i|` is nonempty, and the open subspace of `X` it cuts out is contained in `G` and
> contained in `L i`, hence representable by
> `AlgebraicGeometry.Space.isRepresentable_of_le_of_isRepresentable`.

```lean
theorem exists_denseRange_isRepresentable_isOpenSubspace_of_isReasonableSpace
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hreasonable : IsReasonableSpace B S hS X) :
    ∃ G : Subfunctor X, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      DenseRange (pointsMap B S hS G.toFunctor G.ι)
```

## Tag 086U, a theorem

[Tag 086U](https://stacks.math.columbia.edu/tag/086U) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusDecent.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusDecent.lean#L322).

> **Stacks 086U (David Rydh).** A decent algebraic space over a scheme has a dense open
> subspace which is a scheme: its schematic locus of Stacks 03JH is a representable open subspace
> whose set of points is dense.
>
> The reduction to the local statement
> `AlgebraicGeometry.Space.exists_isRepresentable_isOpenSubspace_nonempty_of_isDecentSpace` is
> `AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isAlgebraicSpace`,
> which is Stacks 03JH together with the reduction of
> `StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocus.lean`.

```lean
theorem exists_denseRange_isRepresentable_isOpenSubspace_of_isDecentSpace
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) :
    ∃ G : Subfunctor X, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      DenseRange (pointsMap B S hS G.toFunctor G.ι)
```

## Tag 0BA1, a lemma

[Tag 0BA1](https://stacks.math.columbia.edu/tag/0BA1) in the Stacks Project.

**`AlgebraicGeometry.Space.mem_range_pointsMap_schematicLocus_iff_exists_isAffine_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeSchematicLocus.lean, line 804](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeSchematicLocus.lean#L804).

> **Stacks 0BA1.** Let `X ⟶ Y` be a surjective finite locally free morphism of algebraic
> spaces over a scheme `S`, and let `y` be a point of `Y`. Then the following are equivalent:
>
> 1. `y` lies in the schematic locus of `Y` — the point set of
>    `AlgebraicGeometry.Space.schematicLocus`, the largest open subspace of `Y` which is a
>    scheme (Tag 03JH); and
> 2. there is an affine open subspace of `X`, presented as an open immersion `i : h_U ⟶ X`
>    from an affine object `U` of the site, whose point set contains the whole fibre of `y`.
>
> Finite local freeness of `f` is taken in the representable sense: `f` is representable and
> every represented base change of it is a finite locally free morphism of schemes.  That is
> condition (1) of Tag 03ZW, which the source's Definition 03ZV — condition (2) of that tag —
> is equivalent to.  Surjectivity is likewise taken after representable base change, which is
> condition (1) of Tag 02YN.
>
> The two implications are
> `AlgebraicGeometry.Space.exists_isAffine_isOpenImmersion_of_mem_schematicLocus` and
> `AlgebraicGeometry.Space.mem_range_pointsMap_schematicLocus_of_exists_isAffine`; see their
> docstrings for the two arguments.

```lean
theorem mem_range_pointsMap_schematicLocus_iff_exists_isAffine_isOpenImmersion
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hsurj : (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom)
    (hflf : (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom)
    (y : points B S hS Y.obj) :
    y ∈ Set.range (pointsMap B S hS (schematicLocus B S hS Y.obj).toFunctor
        (schematicLocus B S hS Y.obj).ι) ↔
      ∃ (U : BigFppfOver B S hS) (i : yoneda.obj U ⟶ X.obj),
        IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧ IsOpenImmersion B S hS i ∧
        ∀ x : points B S hS X.obj, pointsMap B S hS X.obj f.hom x = y →
          x ∈ Set.range (pointsMap B S hS (yoneda.obj U) i)
```

## Tag 06NG, a lemma

[Tag 06NG](https://stacks.math.columbia.edu/tag/06NG) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_finite_etale_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteEtaleAtlasSchematicLocus.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FiniteEtaleAtlasSchematicLocus.lean#L106).

> **Stacks 06NG.** An algebraic space over `S` admitting a finite étale surjective morphism
> from a scheme over `S` has a representable open subspace whose point set is dense: such a
> space is reasonable, so Stacks 03JI applies.

```lean
theorem exists_denseRange_isRepresentable_isOpenSubspace_of_finite_etale_cover
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    {U : BigFppfOver B S hS} (f : yoneda.obj U ⟶ X)
    (hfin : IsFinite B S hS f) (_hetale : IsEtale B S hS f)
    (hsurj : IsSurjective B S hS f) :
    ∃ G : Subfunctor X, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      DenseRange (pointsMap B S hS G.toFunctor G.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.10, Tag 06NN](https://stacks.math.columbia.edu/tag/06NN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
