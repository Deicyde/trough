---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.hasChartLocalRingDimension_iff_allChartsLocalRingDimension, AlgebraicGeometry.Space.hasChartLocalRingDimension_iff_ringKrullDim_stalk, AlgebraicGeometry.Space.localRingDimension, AlgebraicGeometry.Space.localRingDimension_eq_iff_hasChartLocalRingDimension, AlgebraicGeometry.Space.dimension_eq_iSup_localRingDimension, AlgebraicGeometry.Space.iSup_dimensionAtPoint_eq_iSup_localRingDimension
statement: formalized
proof: formalized
---

# 66.10 Dimension of local rings

Section 66.10 of the Stacks Project, [Tag 04N7](https://stacks.math.columbia.edu/tag/04N7). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BAM, a lemma

[Tag 0BAM](https://stacks.math.columbia.edu/tag/0BAM) in the Stacks Project.

**`AlgebraicGeometry.Space.hasChartLocalRingDimension_iff_allChartsLocalRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean#L165). The attribute's comment: “equivalence of étale-chart conditions”.

> **Stacks 0BAM.** The Krull dimension of the local ring measured on an étale scheme chart
> of an algebraic space is independent of the chart and of the point above `x`: one chart
> realizes the value `d` exactly when every chart does.

```lean
theorem hasChartLocalRingDimension_iff_allChartsLocalRingDimension
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) (d : ℕ∞) :
    HasChartLocalRingDimension B S hS x d ↔ AllChartsLocalRingDimension B S hS x d
```

**`AlgebraicGeometry.Space.hasChartLocalRingDimension_iff_ringKrullDim_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean#L183). The attribute's comment: “representable case”.

> **Stacks 0BAM, the representable case.** For a represented algebraic space the chart
> condition at a point is the Krull dimension of the local ring of the representing scheme at
> the corresponding scheme point.

```lean
theorem hasChartLocalRingDimension_iff_ringKrullDim_stalk (U : BigFppfOver B S hS)
    (u : (BigFppfOver.toScheme B S hS).obj U) (x : points B S hS (yoneda.obj U))
    (hx : ChartPoint B S hS U (𝟙 (yoneda.obj U)) u x) (d : ℕ∞) :
    HasChartLocalRingDimension B S hS x d ↔
      ringKrullDim (((BigFppfOver.toScheme B S hS).obj U).presheaf.stalk u) =
        (d : WithBot ℕ∞)
```

## Tag 04NA, a definition

[Tag 04NA](https://stacks.math.columbia.edu/tag/04NA) in the Stacks Project.

**`AlgebraicGeometry.Space.localRingDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean#L229). The attribute's comment: “dimension”.

> **Stacks 04NA.** The Krull dimension of the local ring of an algebraic space at a point,
> measured on an étale scheme chart at a point above it.
>
> By `AlgebraicGeometry.Space.localRingDimension_eq_iff_hasChartLocalRingDimension` exactly one
> value is realized by such a chart, and it is this infimum.

```lean
noncomputable def localRingDimension (x : points B S hS F) : ℕ∞
```

**`AlgebraicGeometry.Space.localRingDimension_eq_iff_hasChartLocalRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocalRingDimension.lean#L235). The attribute's comment: “characterization by étale charts”.

> **Stacks 04NA.** The dimension of the local ring of an algebraic space at a point is the
> value measured on any étale scheme chart at a point above it.

```lean
theorem localRingDimension_eq_iff_hasChartLocalRingDimension (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) (d : ℕ∞) :
    localRingDimension B S hS x = d ↔ HasChartLocalRingDimension B S hS x d
```

## Tag 0BAN, a lemma

[Tag 0BAN](https://stacks.math.columbia.edu/tag/0BAN) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_eq_iSup_localRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionLocalRings.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionLocalRings.lean#L55). The attribute's comment: “the dimension of the space is the supremum over its local rings”.

> **Stacks 0BAN, quantities (1) and (2).** The dimension of an algebraic space is the
> supremum of the Krull dimensions of its local rings.

```lean
theorem dimension_eq_iSup_localRingDimension (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    dimension B S hS F hF =
      ⨆ x : points B S hS F, (localRingDimension B S hS x : WithBot ℕ∞)
```

**`AlgebraicGeometry.Space.iSup_dimensionAtPoint_eq_iSup_localRingDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionLocalRings.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionLocalRings.lean#L97). The attribute's comment: “the supremum over the points of the dimension at the point”.

> **Stacks 0BAN, quantities (3) and (2).** The supremum, over the points `x` of an algebraic
> space, of its dimension `dim_x(X)` at `x` is the supremum of the Krull dimensions of its local
> rings. By Definition 04N6 the left-hand side is the dimension of the algebraic space, so
> together with `AlgebraicGeometry.Space.dimension_eq_iSup_localRingDimension` this is the
> equality of all three quantities of the source.

```lean
theorem iSup_dimensionAtPoint_eq_iSup_localRingDimension (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    (⨆ x : points B S hS F, dimensionAtPoint B S hS F hF x) =
      ⨆ x : points B S hS F, (localRingDimension B S hS x : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.10, Tag 04N7](https://stacks.math.columbia.edu/tag/04N7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
