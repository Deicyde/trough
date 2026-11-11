---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_exists_etale_genericPoint, AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_all_etale_genericPoints, AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_genericPoint_of_isRepresentable, AlgebraicGeometry.Space.codimensionZeroPoints_dense
statement: formalized
proof: formalized
---

# 66.11 Generic points

Section 66.11 of the Stacks Project, [Tag 0BAP](https://stacks.math.columbia.edu/tag/0BAP). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BAQ, a lemma

[Tag 0BAQ](https://stacks.math.columbia.edu/tag/0BAQ) in the Stacks Project.

**`AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_exists_etale_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean#L79). The attribute's comment: “condition (2)”.

> **Stacks 0BAQ, conditions (1) and (2).** A point of an algebraic space has a local ring of
> dimension zero exactly when some étale scheme chart has, above it, a generic point of an
> irreducible component.

```lean
theorem localRingDimension_eq_zero_iff_exists_etale_genericPoint
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    localRingDimension B S hS x = 0 ↔
      ∃ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F)
        (u : (BigFppfOver.toScheme B S hS).obj U),
        IsEtale B S hS a ∧ ChartPoint B S hS U a u x ∧
          u ∈ genericPoints ((BigFppfOver.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_all_etale_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean#L95). The attribute's comment: “condition (3)”.

> **Stacks 0BAQ, conditions (1) and (3).** A point of an algebraic space has a local ring of
> dimension zero exactly when every point above it in every étale scheme chart is the generic
> point of an irreducible component.

```lean
theorem localRingDimension_eq_zero_iff_all_etale_genericPoints
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    localRingDimension B S hS x = 0 ↔
      ∀ (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F)
        (u : (BigFppfOver.toScheme B S hS).obj U),
        IsEtale B S hS a → ChartPoint B S hS U a u x →
          u ∈ genericPoints ((BigFppfOver.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_genericPoint_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean#L139). The attribute's comment: “representable case”. References: EGA I (2.4.3).

> **Stacks 0BAQ, the representable case.** For a representable algebraic space, a point has a
> local ring of dimension zero exactly when it is the generic point of an irreducible component
> of the space of points.

```lean
theorem localRingDimension_eq_zero_iff_genericPoint_of_isRepresentable
    (hF : IsAlgebraicSpace B S hS F) (hrep : F.IsRepresentable) (x : points B S hS F) :
    localRingDimension B S hS x = 0 ↔ x ∈ genericPoints (points B S hS F)
```

## Tag 0BAR, a lemma

[Tag 0BAR](https://stacks.math.columbia.edu/tag/0BAR) in the Stacks Project.

**`AlgebraicGeometry.Space.codimensionZeroPoints_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroPoints.lean#L148).

> **Stacks 0BAR.** The points of codimension zero of an algebraic space are dense in its
> space of points.

```lean
theorem codimensionZeroPoints_dense (hF : IsAlgebraicSpace B S hS F) :
    Dense {x : points B S hS F | localRingDimension B S hS x = 0}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.11, Tag 0BAP](https://stacks.math.columbia.edu/tag/0BAP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
