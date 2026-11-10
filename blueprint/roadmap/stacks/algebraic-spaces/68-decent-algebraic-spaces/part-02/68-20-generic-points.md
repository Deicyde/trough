---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.mem_genericPoints_tfae, AlgebraicGeometry.Space.codimension_eq_localRingDimension, AlgebraicGeometry.Space.isReasonableSpace_of_finite_irreducibleComponents_of_mono, AlgebraicGeometry.Space.IsDecentWithFinitelyManyComponents.hasMonomorphicCodimensionZeroPoints, AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasFiniteEtaleIrreducibleComponents, AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasFiniteCodimensionZeroPoints, AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasMonomorphicCodimensionZeroPoints, AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasFiniteEtaleComponentsAndCodimensionZeroPoints
statement: formalized
proof: formalized
---

# 68.20 Generic points

Section 68.20 of the Stacks Project, [Tag 0BB7](https://stacks.math.columbia.edu/tag/0BB7). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ABV, a lemma

[Tag 0ABV](https://stacks.math.columbia.edu/tag/0ABV) in the Stacks Project.

**`AlgebraicGeometry.Space.mem_genericPoints_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/CodimensionZeroCriterion.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/CodimensionZeroCriterion.lean#L165).

> **Stacks 0ABV.** For a point `x` of a decent algebraic space `X` over `S` the following
> are equivalent: `x` is a generic point of an irreducible component of `|X|`; for every étale
> morphism of algebraic spaces onto `X`, every point above `x` is a generic point of an
> irreducible component of the source; for some étale morphism onto `X` some point above `x`
> is; and the local ring of `X` at `x` has dimension zero, which is to say that `x` is a point
> of codimension `0` on `X`.

```lean
theorem mem_genericPoints_tfae (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (x : points B S hS X) :
    List.TFAE
      [ x ∈ genericPoints (points B S hS X),
        ∀ (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS Y → ∀ f : Y ⟶ X,
          IsEtale B S hS f → ∀ y : points B S hS Y, pointsMap B S hS Y f y = x →
            y ∈ genericPoints (points B S hS Y),
        ∃ (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Y) (f : Y ⟶ X)
          (y : points B S hS Y), IsEtale B S hS f ∧ pointsMap B S hS Y f y = x ∧
            y ∈ genericPoints (points B S hS Y),
        localRingDimension B S hS x = 0 ]
```

## Tag 0ED1, a lemma

[Tag 0ED1](https://stacks.math.columbia.edu/tag/0ED1) in the Stacks Project.

**`AlgebraicGeometry.Space.codimension_eq_localRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/CodimensionLocalRing.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/CodimensionLocalRing.lean#L85).

> For an irreducible closed subset `T` of the point space of a decent algebraic space over `S`,
> with generic point `ξ`, the codimension of `T` is the dimension of the local ring of the space
> at `ξ`.

```lean
theorem codimension_eq_localRingDimension (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) (T : IrreducibleCloseds (points B S hS X))
    (ξ : points B S hS X) (hξ : IsGenericPoint ξ (T : Set (points B S hS X))) :
    codimension T = localRingDimension B S hS ξ
```

## Tag 0BB8, a lemma

[Tag 0BB8](https://stacks.math.columbia.edu/tag/0BB8) in the Stacks Project.

**`AlgebraicGeometry.Space.isReasonableSpace_of_finite_irreducibleComponents_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReasonableFromGenericPoints.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ReasonableFromGenericPoints.lean#L358).

> **Stacks 0BB8.** An algebraic space over a scheme `S` is reasonable as soon as every
> quasi-compact scheme étale over it has finitely many irreducible components and every one of
> its points of codimension zero is represented by a monomorphism from the spectrum of a
> field.

```lean
theorem isReasonableSpace_of_finite_irreducibleComponents_of_mono
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hfinite : ∀ U : BigFppfOver B S hS,
      CompactSpace ((BigFppfOver.toScheme B S hS).obj U) →
      ∀ f : yoneda.obj U ⟶ X,
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@_root_.AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) f →
        (irreducibleComponents ((BigFppfOver.toScheme B S hS).obj U)).Finite)
    (hgeneric : ∀ x : points B S hS X, localRingDimension B S hS x = 0 →
      ∃ p : FieldValuedPoint B S hS X,
        p.class B S hS X = x ∧ Mono (yonedaEquiv.symm p.value)) :
    IsReasonableSpace B S hS X
```

## Tag 0BB9, a lemma

[Tag 0BB9](https://stacks.math.columbia.edu/tag/0BB9) in the Stacks Project.

**`AlgebraicGeometry.Space.IsDecentWithFinitelyManyComponents.hasMonomorphicCodimensionZeroPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L388). The attribute's comment: “condition (1) implies the third clause of condition (2)”.

> **Stacks 0BB9, condition (1) implies the third clause of condition (2).** A decent
> algebraic space has a monomorphic field-valued representative at every point, in particular at
> every point of codimension `0`.

```lean
theorem IsDecentWithFinitelyManyComponents.hasMonomorphicCodimensionZeroPoints
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (h : IsDecentWithFinitelyManyComponents B S hS X) :
    HasMonomorphicCodimensionZeroPoints B S hS X
```

**`AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasFiniteEtaleIrreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L510). The attribute's comment: “condition (3) implies the first clause of condition (2)”.

> **Stacks 0BB9, condition (3) implies the first clause of condition (2).** If an algebraic
> space over `S` has a dense open subspace which is a scheme with finitely many irreducible
> components whose generic points are represented by quasi-compact morphisms, then every
> quasi-compact scheme étale over it has finitely many irreducible components.
>
> Let `a : U ⟶ X` be étale with `U` compact, and let `V ⊂ U` be the preimage of the point set of
> the open subspace: it is open, and dense because an étale morphism is open on points. A
> generic point of an irreducible component of `U` lying in `V` has codimension `0` on `X` by
> condition (2) of Stacks 0BAQ, so its image is the image of a generic point of the open
> subspace; there are finitely many of those, and the fibre of `|U| → |X|` above each is finite
> because the morphism representing it is quasi-compact. So `V` meets only finitely many generic
> points, which bounds the irreducible components of `U`.

```lean
theorem HasQuasiCompactGenericDenseOpenScheme.hasFiniteEtaleIrreducibleComponents
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : HasQuasiCompactGenericDenseOpenScheme B S hS X) :
    HasFiniteEtaleIrreducibleComponents B S hS X
```

**`AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasFiniteCodimensionZeroPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L612). The attribute's comment: “condition (3) implies the second clause of condition (2)”.

> **Stacks 0BB9, condition (3) implies the second clause of condition (2).** Only finitely
> many points have codimension `0`: each of them lies over the dense open subspace, and is the
> image of a generic point of one of its finitely many irreducible components.

```lean
theorem HasQuasiCompactGenericDenseOpenScheme.hasFiniteCodimensionZeroPoints
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : HasQuasiCompactGenericDenseOpenScheme B S hS X) :
    HasFiniteCodimensionZeroPoints B S hS X
```

**`AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasMonomorphicCodimensionZeroPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L632). The attribute's comment: “condition (3) implies the third clause of condition (2)”.

> **Stacks 0BB9, condition (3) implies the third clause of condition (2).** A point of
> codimension `0` lies over the dense open subspace, which is a scheme, so the residue field at
> the corresponding point of that scheme presents it by a monomorphism.

```lean
theorem HasQuasiCompactGenericDenseOpenScheme.hasMonomorphicCodimensionZeroPoints
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : HasQuasiCompactGenericDenseOpenScheme B S hS X) :
    HasMonomorphicCodimensionZeroPoints B S hS X
```

**`AlgebraicGeometry.Space.HasQuasiCompactGenericDenseOpenScheme.hasFiniteEtaleComponentsAndCodimensionZeroPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L645). The attribute's comment: “condition (3) implies condition (2)”.

> **Stacks 0BB9, condition (3) implies condition (2).** The three clauses together.

```lean
theorem HasQuasiCompactGenericDenseOpenScheme.hasFiniteEtaleComponentsAndCodimensionZeroPoints
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : HasQuasiCompactGenericDenseOpenScheme B S hS X) :
    HasFiniteEtaleComponentsAndCodimensionZeroPoints B S hS X
```

**`AlgebraicGeometry.Space.IsDecentWithFinitelyManyComponents.hasQuasiCompactGenericDenseOpenScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L720). The attribute's comment: “condition (1) implies condition (3)”.

> **Stacks 0BB9, condition (1) implies condition (3).** A decent algebraic space over `S`
> whose space of points has finitely many irreducible components has a dense open subspace which
> is a scheme, with finitely many irreducible components, each of whose generic points is
> represented by a quasi-compact morphism from the spectrum of a field.
>
> The dense open subscheme is Stacks 086U, in the form
> `AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_of_isDecentSpace`.
> Its components are finite in number because the inclusion is an open embedding on points and
> an open embedding pulls components back onto components
> (`AlgebraicGeometry.finite_irreducibleComponents_of_isOpenEmbedding`), which is the
> source's "taking closures sends irreducible components of `|X'|` to irreducible components of
> `|X|`". The quasi-compactness of the generic-point morphisms is decency itself, with the
> monomorphism condition of Stacks 03JV (4) dropped to Stacks 03JV (5).

```lean
theorem IsDecentWithFinitelyManyComponents.hasQuasiCompactGenericDenseOpenScheme
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : IsDecentWithFinitelyManyComponents B S hS X) :
    HasQuasiCompactGenericDenseOpenScheme B S hS X
```

**`AlgebraicGeometry.Space.HasFiniteEtaleComponentsAndCodimensionZeroPoints.isReasonableSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 740](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L740). The attribute's comment: “condition (2) implies the conclusion that the space is reasonable”.

> **Condition (2) of Stacks 0BB9 makes the algebraic space reasonable.** This is Stacks 0BB8,
> `AlgebraicGeometry.Space.isReasonableSpace_of_finite_irreducibleComponents_of_mono`, whose two
> hypotheses are the first and third clauses of condition (2).

```lean
theorem HasFiniteEtaleComponentsAndCodimensionZeroPoints.isReasonableSpace
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : HasFiniteEtaleComponentsAndCodimensionZeroPoints B S hS X) :
    IsReasonableSpace B S hS X
```

**`AlgebraicGeometry.Space.HasFiniteEtaleComponentsAndCodimensionZeroPoints.isDecentWithFinitelyManyComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 755](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L755). The attribute's comment: “condition (2) implies condition (1)”.

> **Stacks 0BB9, condition (2) implies condition (1).** Decency comes from Stacks 0BB8: the
> first and third clauses of condition (2) make the space reasonable, and a reasonable algebraic
> space is decent. Finiteness of the irreducible components of `|X|` comes from the second
> clause together with Stacks 0BAR: the points of codimension `0` are dense, there are finitely
> many of them, and so the finitely many irreducible closed sets they generate cover a dense
> subset of `|X|`, which bounds the components.

```lean
theorem HasFiniteEtaleComponentsAndCodimensionZeroPoints.isDecentWithFinitelyManyComponents
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : HasFiniteEtaleComponentsAndCodimensionZeroPoints B S hS X) :
    IsDecentWithFinitelyManyComponents B S hS X
```

**`AlgebraicGeometry.Space.isDecentWithFinitelyManyComponents_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 777](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L777).

> **Stacks 0BB9.** For an algebraic space `X` over a scheme `S` the three conditions are
> equivalent: `X` is decent with finitely many irreducible components; every quasi-compact scheme
> étale over `X` has finitely many irreducible components, there are finitely many points of
> codimension `0` and each is represented by a monomorphism from the spectrum of a field; and
> there is a dense open subspace which is a scheme with finitely many irreducible components
> whose generic points are represented by quasi-compact morphisms.

```lean
theorem isDecentWithFinitelyManyComponents_tfae
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) :
    [IsDecentWithFinitelyManyComponents B S hS X,
      HasFiniteEtaleComponentsAndCodimensionZeroPoints B S hS X,
      HasQuasiCompactGenericDenseOpenScheme B S hS X].TFAE
```

**`AlgebraicGeometry.Space.IsDecentWithFinitelyManyComponents.isReasonableSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 791](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L791). The attribute's comment: “the conclusion that the space is reasonable”.

> **Stacks 0BB9, the concluding assertion that the space is reasonable.** An algebraic space
> over `S` which is decent and has finitely many irreducible components is reasonable.

```lean
theorem IsDecentWithFinitelyManyComponents.isReasonableSpace
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (h : IsDecentWithFinitelyManyComponents B S hS X) :
    IsReasonableSpace B S hS X
```

**`AlgebraicGeometry.Space.image_genericPoints_eq_genericPoints_of_denseRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean, line 808](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GenericPointsFiniteComponents.lean#L808). The attribute's comment: “the conclusion identifying the generic points of the dense open subscheme”.

> **Stacks 0BB9, the concluding assertion about generic points.** If the space of points of
> an algebraic space over `S` has finitely many irreducible components and `X' ⊂ X` is an open
> subspace whose point set is dense, then the generic points of the irreducible components of
> `|X'|` map exactly onto the generic points of the irreducible components of `|X|`.
>
> The inclusion is an open embedding on points, and an open embedding matches up the generic
> points of its source with those of its target lying in its range; the range is all of them
> because a dense open subset of a space with finitely many irreducible components contains every
> generic point.

```lean
theorem image_genericPoints_eq_genericPoints_of_denseRange
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {G : Subfunctor X} (hG : IsOpenSubspace B S hS G)
    (hdense : DenseRange (pointsMap B S hS G.toFunctor G.ι))
    (hfin : (irreducibleComponents (points B S hS X)).Finite) :
    pointsMap B S hS G.toFunctor G.ι '' genericPoints (points B S hS G.toFunctor) =
      genericPoints (points B S hS X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.20, Tag 0BB7](https://stacks.math.columbia.edu/tag/0BB7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
