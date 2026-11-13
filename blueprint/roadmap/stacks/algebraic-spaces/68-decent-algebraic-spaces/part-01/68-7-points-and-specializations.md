---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.eq_of_specializes_of_pointsMap_eq, AlgebraicGeometry.Space.eq_of_specializes_of_chartPoint_of_isLocallyNoetherian, AlgebraicGeometry.Space.exists_specializes_pointsMap_eq_of_isEtale, AlgebraicGeometry.Space.exists_specializes_pointsMap_eq_of_isFlat
statement: formalized
proof: formalized
---

# 68.7 Points and specializations

Section 68.7 of the Stacks Project, [Tag 03K1](https://stacks.math.columbia.edu/tag/03K1). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03IM, a lemma

[Tag 03IM](https://stacks.math.columbia.edu/tag/03IM) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_specializes_of_pointsMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean#L256).

> **Stacks 03IM.** Let `X` be an algebraic space over `S` and let `x` be a point of `X`
> above which every étale chart of `X` by an affine scheme has a finite fibre, which is
> condition (2) of Stacks 03JS for the pair `(X, x)`. If two points `u` and `u'` of an étale
> scheme chart of `X` both lie above `x` and `u` is a specialization of `u'`, then `u = u'`.

```lean
theorem eq_of_specializes_of_pointsMap_eq {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (x : points B S hS X)
    (hfinite : ∀ V : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj V) →
      ∀ ψ : yoneda.obj V ⟶ X, (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf ψ →
      (pointsMap B S hS (yoneda.obj V) ψ ⁻¹' {x}).Finite)
    (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
    (hφ : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf φ)
    (u u' : points B S hS (yoneda.obj U))
    (hu : pointsMap B S hS (yoneda.obj U) φ u = x)
    (hu' : pointsMap B S hS (yoneda.obj U) φ u' = x)
    (hs : u' ⤳ u) : u = u'
```

## Tag 0H1Q, a lemma

[Tag 0H1Q](https://stacks.math.columbia.edu/tag/0H1Q) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_specializes_of_chartPoint_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/GenericPointsAndDimension.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/GenericPointsAndDimension.lean#L125).

> Let `X` be an algebraic space over `S` and let `a : h_U ⟶ X` be an étale scheme chart of `X`
> whose scheme is locally Noetherian. Two points `u`, `u'` of `U` lying above the same point `x` of
> `|X|` with `u' ⤳ u` are then equal.

```lean
theorem eq_of_specializes_of_chartPoint_of_isLocallyNoetherian
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X)
    (ha : (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf a)
    [IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj U)]
    (u u' : (BigFppfOver.toScheme B S hS).obj U) (x : points B S hS X)
    (hu : ChartPoint B S hS U a u x) (hu' : ChartPoint B S hS U a u' x)
    (hs : u' ⤳ u) : u = u'
```

## Tag 03K2, a lemma

[Tag 03K2](https://stacks.math.columbia.edu/tag/03K2) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_specializes_pointsMap_eq_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean, line 517](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean#L517).

> **Stacks 03K2.** Let `X` be an algebraic space over `S`, let `x' ⤳ x` be a
> specialization of points of `X` and assume that every étale chart of `X` by an affine scheme
> has a finite fibre above `x'`, which is condition (2) of Stacks 03JS for the pair `(X, x')`.
> Then for every étale chart `φ : h_U ⟶ X` of `X` by a scheme and every point `u` of the chart
> above `x` there is a point `u'` of the chart above `x'` with `u' ⤳ u`.

```lean
theorem exists_specializes_pointsMap_eq_of_isEtale
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    {x x' : points B S hS X} (hs : x' ⤳ x)
    (hfinite : ∀ V : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj V) →
      ∀ ψ : yoneda.obj V ⟶ X, (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf ψ →
      (pointsMap B S hS (yoneda.obj V) ψ ⁻¹' {x'}).Finite)
    (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
    (hφ : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf φ)
    (u : points B S hS (yoneda.obj U)) (hu : pointsMap B S hS (yoneda.obj U) φ u = x) :
    ∃ u' : points B S hS (yoneda.obj U), u' ⤳ u ∧
      pointsMap B S hS (yoneda.obj U) φ u' = x'
```

## Tag 0B7W, a lemma

[Tag 0B7W](https://stacks.math.columbia.edu/tag/0B7W) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_specializes_pointsMap_eq_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean#L552).

> **Stacks 0B7W.** Let `f : Y ⟶ X` be a flat morphism of algebraic spaces over `S`, let
> `x' ⤳ x` be a specialization of points of `X` and assume that every étale chart of `X` by an
> affine scheme has a finite fibre above `x'`, which is condition (2) of Stacks 03JS for the
> pair `(X, x')`. Then every point `y` of `Y` above `x` is the specialization of a point of `Y`
> above `x'`.

```lean
theorem exists_specializes_pointsMap_eq_of_isFlat
    {Y X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hY : IsAlgebraicSpace B S hS Y) (hX : IsAlgebraicSpace B S hS X)
    (f : Y ⟶ X) (hf : IsFlat B S hS f)
    {x x' : points B S hS X} (hs : x' ⤳ x)
    (hfinite : ∀ V : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj V) →
      ∀ ψ : yoneda.obj V ⟶ X, (MorphismProperty.inverseImage
        (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf ψ →
      (pointsMap B S hS (yoneda.obj V) ψ ⁻¹' {x'}).Finite)
    (y : points B S hS Y) (hy : pointsMap B S hS Y f y = x) :
    ∃ y' : points B S hS Y, y' ⤳ y ∧ pointsMap B S hS Y f y' = x'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.7, Tag 03K1](https://stacks.math.columbia.edu/tag/03K1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
