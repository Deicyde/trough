---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_isClosed_etaleChart, AlgebraicGeometry.Space.IsFiniteTypePoint, AlgebraicGeometry.Space.finiteTypePoints, AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_isAffine_isClosed_etaleChart, AlgebraicGeometry.Space.mapsTo_finiteTypePoints, AlgebraicGeometry.Space.image_finiteTypePoints_eq, AlgebraicGeometry.Space.inter_finiteTypePoints_nonempty, AlgebraicGeometry.Space.closure_inter_finiteTypePoints
statement: formalized
proof: formalized
---

# 67.25 Points of finite type

Section 67.25 of the Stacks Project, [Tag 06EE](https://stacks.math.columbia.edu/tag/06EE). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06EF, a lemma

[Tag 06EF](https://stacks.math.columbia.edu/tag/06EF) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_isClosed_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L397).

> **Stacks 06EF**, and the assertion of **Stacks 06EH** for arbitrary scheme charts. A point
> of an algebraic space over `S` is a finite type point exactly when it is the image of a closed
> point of a scheme étale over the space.

```lean
theorem isFiniteTypePoint_iff_exists_isClosed_etaleChart
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (x : points B S hS X) :
    IsFiniteTypePoint B S hS X x ↔
      ∃ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
        (p : FieldValuedPoint B S hS (yoneda.obj U)),
        IsEtale B S hS φ ∧
          IsClosed ({schemePoint B S hS U p} : Set ((BigFppfOver.toScheme B S hS).obj U)) ∧
          pointsMap B S hS (yoneda.obj U) φ (p.class B S hS (yoneda.obj U)) = x
```

## Tag 06EG, a definition

[Tag 06EG](https://stacks.math.columbia.edu/tag/06EG) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFiniteTypePoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L191). The attribute's comment: “finite type point”.

> **Stacks 06EG.** A point of an algebraic space over `S` is a *finite type point* when some
> field-valued point representing it has a morphism to the space which is locally of finite
> type.

```lean
abbrev IsFiniteTypePoint (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.finiteTypePoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L198). The attribute's comment: “set of finite type points”.

> **Stacks 06EG.** The set `X_{ft-pts}` of finite type points of an algebraic space
> over `S`.

```lean
abbrev finiteTypePoints (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Set (points B S hS X)
```

## Tag 06EH, a lemma

[Tag 06EH](https://stacks.math.columbia.edu/tag/06EH) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_isClosed_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L397). The attribute's comment: “all scheme charts”.

> **Stacks 06EF**, and the assertion of **Stacks 06EH** for arbitrary scheme charts. A point
> of an algebraic space over `S` is a finite type point exactly when it is the image of a closed
> point of a scheme étale over the space.

```lean
theorem isFiniteTypePoint_iff_exists_isClosed_etaleChart
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (x : points B S hS X) :
    IsFiniteTypePoint B S hS X x ↔
      ∃ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
        (p : FieldValuedPoint B S hS (yoneda.obj U)),
        IsEtale B S hS φ ∧
          IsClosed ({schemePoint B S hS U p} : Set ((BigFppfOver.toScheme B S hS).obj U)) ∧
          pointsMap B S hS (yoneda.obj U) φ (p.class B S hS (yoneda.obj U)) = x
```

**`AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_isAffine_isClosed_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L417). The attribute's comment: “affine scheme charts”.

> **Stacks 06EH**, the assertion for affine scheme charts. A point of an algebraic space
> over `S` is a finite type point exactly when it is the image of a closed point of an affine
> scheme étale over the space.

```lean
theorem isFiniteTypePoint_iff_exists_isAffine_isClosed_etaleChart
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (x : points B S hS X) :
    IsFiniteTypePoint B S hS X x ↔
      ∃ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
        (p : FieldValuedPoint B S hS (yoneda.obj U)),
        IsAffine ((BigFppfOver.toScheme B S hS).obj U) ∧ IsEtale B S hS φ ∧
          IsClosed ({schemePoint B S hS U p} : Set ((BigFppfOver.toScheme B S hS).obj U)) ∧
          pointsMap B S hS (yoneda.obj U) φ (p.class B S hS (yoneda.obj U)) = x
```

## Tag 06EI, a lemma

[Tag 06EI](https://stacks.math.columbia.edu/tag/06EI) in the Stacks Project.

**`AlgebraicGeometry.Space.mapsTo_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L284).

> A locally finite type morphism of algebraic spaces over `S` carries finite type points to
> finite type points. This is the algebraic-space counterpart of Stacks 02J3, and is the easy
> inclusion of `AlgebraicGeometry.Space.image_finiteTypePoints_eq`.

```lean
theorem mapsTo_finiteTypePoints {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    Set.MapsTo (pointsMap B S hS X f) (finiteTypePoints B S hS X)
      (finiteTypePoints B S hS Y)
```

## Tag 06EJ, a lemma

[Tag 06EJ](https://stacks.math.columbia.edu/tag/06EJ) in the Stacks Project.

**`AlgebraicGeometry.Space.image_finiteTypePoints_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L495).

> **Stacks 06EJ.** A surjective morphism of algebraic spaces over `S` which is locally of
> finite type maps the finite type points of its source onto the finite type points of its
> target.
>
> One inclusion is `AlgebraicGeometry.Space.mapsTo_finiteTypePoints`. For the other, a
> finite type point of the target is represented by a locally finite type morphism from a field
> spectrum; the fibre product of the source with that field spectrum over the target is a
> nonempty algebraic space locally of finite type over the source, so it has a finite type point
> by Stacks 06EK, whose image in the source is the required point.

```lean
theorem image_finiteTypePoints_eq {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hsurj : IsSurjective B S hS f) :
    pointsMap B S hS X f '' finiteTypePoints B S hS X = finiteTypePoints B S hS Y
```

## Tag 06EK, a lemma

[Tag 06EK](https://stacks.math.columbia.edu/tag/06EK) in the Stacks Project.

**`AlgebraicGeometry.Space.inter_finiteTypePoints_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L444). The attribute's comment: “locally closed subsets”.

> **Stacks 06EK**, locally closed subsets. A nonempty locally closed set of points of an
> algebraic space over `S` contains a finite type point.
>
> The set is pulled back to a surjective étale scheme chart, where it is again nonempty and
> locally closed because the map on points is continuous and surjective and the point topology
> of a represented presheaf is the topology of the representing scheme; Stacks 02J4 produces a
> finite type point there and its image in `|X|` is a finite type point by Stacks 02J3.

```lean
theorem inter_finiteTypePoints_nonempty (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) {T : Set (points B S hS X)}
    (hT : IsLocallyClosed T) (hne : T.Nonempty) :
    (T ∩ finiteTypePoints B S hS X).Nonempty
```

**`AlgebraicGeometry.Space.closure_inter_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PointsOfFiniteType.lean#L473). The attribute's comment: “closed subsets”.

> **Stacks 06EK**, closed subsets. The finite type points lying in a closed set of points of
> an algebraic space over `S` are dense in it.

```lean
theorem closure_inter_finiteTypePoints (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) {T : Set (points B S hS X)} (hT : IsClosed T) :
    closure (T ∩ finiteTypePoints B S hS X) = T
```

## Tag 06EL, a lemma

[Tag 06EL](https://stacks.math.columbia.edu/tag/06EL) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteTypePoint_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypePointTfae.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypePointTfae.lean#L78).

> Let `S` be a scheme, let `X` be an algebraic space over `S` and let `x` be a point of
> `X`. The following are equivalent:
>
> 1. `x` is a finite type point;
> 2. there is an algebraic space `Z` whose space of points is a singleton and a morphism
>    `f : Z ⟶ X` which is locally of finite type with `{x}` the image of `|f|`;
> 3. there is an algebraic space `Z` and a morphism `f : Z ⟶ X` such that `Z` carries a
>    surjective étale morphism from the spectrum of a field, `f` is locally of finite type, `f`
>    is a monomorphism, and `x` is the image under `|f|` of the point of that field spectrum.
>
> Conditions (1) and (2) are equivalent by
> `AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_singleton_space`; condition (1) implies
> condition (3) by
> `AlgebraicGeometry.Space.exists_mono_isLocallyOfFiniteType_etale_fieldPoint_of_isFiniteTypePoint`,
> and condition (3) implies condition (1) by
> `AlgebraicGeometry.Space.isFiniteTypePoint_pointsMap_of_isSurjective_fieldPoint`.

```lean
theorem isFiniteTypePoint_tfae (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X) (x : points B S hS X) :
    [IsFiniteTypePoint B S hS X x,
      ∃ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z) (f : Z ⟶ X),
        Nonempty (points B S hS Z) ∧ Subsingleton (points B S hS Z) ∧
          IsLocallyOfFiniteType B S hS f ∧ Set.range (pointsMap B S hS Z f) = {x},
      ∃ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z) (f : Z ⟶ X)
          (z : FieldValuedPoint B S hS Z),
        IsSurjective B S hS (yonedaEquiv.symm z.value) ∧
          IsEtale B S hS (yonedaEquiv.symm z.value) ∧
          IsLocallyOfFiniteType B S hS f ∧ Mono f ∧
          x = pointsMap B S hS Z f (z.class B S hS Z)].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.25, Tag 06EE](https://stacks.math.columbia.edu/tag/06EE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
