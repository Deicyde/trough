---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.dimensionAtPoint, AlgebraicGeometry.Space.exists_etale_chart_at_point, AlgebraicGeometry.Space.dimensionAtPoint_eq_of_etale_chart, AlgebraicGeometry.Space.dimension
statement: formalized
proof: formalized
---

# 66.9 Dimension at a point

Section 66.9 of the Stacks Project, [Tag 04N3](https://stacks.math.columbia.edu/tag/04N3). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04N5, a definition

[Tag 04N5](https://stacks.math.columbia.edu/tag/04N5) in the Stacks Project.

**`AlgebraicGeometry.Space.dimensionAtPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean#L74). The attribute's comment: “dimension at a point”.

> **Stacks 04N5.** The dimension of an algebraic space at one of its points: the infimum of
> the local dimensions of the étale scheme charts at a point above it. By
> `AlgebraicGeometry.Space.dimensionAtPoint_eq_of_etale_chart` every one of those local
> dimensions equals this infimum.

```lean
noncomputable def dimensionAtPoint (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) : WithBot ℕ∞
```

**`AlgebraicGeometry.Space.exists_etale_chart_at_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean#L88). The attribute's comment: “existence of a chart at the point”.

> **Stacks 04N5.** Every point of an algebraic space has an étale scheme chart above it.

```lean
theorem exists_etale_chart_at_point (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) a ∧
      ∃ p : FieldValuedPoint B S hS (yoneda.obj U),
        pointsMap B S hS (yoneda.obj U) a (p.class B S hS (yoneda.obj U)) = x
```

**`AlgebraicGeometry.Space.dimensionAtPoint_eq_of_etale_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean#L106). The attribute's comment: “independence of the étale chart”.

> **Stacks 04N5.** The dimension of an algebraic space at a point equals the local
> dimension of every étale scheme chart at a point above it; this is the property the source
> uses to define the dimension at a point.

```lean
theorem dimensionAtPoint_eq_of_etale_chart (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) (U : BigFppfOver B S hS)
    (a : yoneda.obj U ⟶ F)
    (ha : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) a)
    (p : FieldValuedPoint B S hS (yoneda.obj U))
    (hp : pointsMap B S hS (yoneda.obj U) a (p.class B S hS (yoneda.obj U)) = x) :
    dimensionAtPoint B S hS F hF x =
      topologicalKrullDimAt ((BigFppfOver.toScheme B S hS).obj U)
        (schemePoint B S hS U p)
```

## Tag 04N6, a definition

[Tag 04N6](https://stacks.math.columbia.edu/tag/04N6) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Dimension.lean#L142).

> **Stacks 04N6.** The dimension of an algebraic space: the supremum of its dimensions at
> its points.

```lean
noncomputable abbrev dimension (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) : WithBot ℕ∞
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.9, Tag 04N3](https://stacks.math.columbia.edu/tag/04N3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
