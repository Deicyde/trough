---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.finite_zeroDimensionalSpecializations, AlgebraicGeometry.Space.exists_genericResidueFieldTranscendenceDegreeAt_eq, AlgebraicGeometry.Space.localRingDimension_add_residueFieldTranscendenceDegree_le, AlgebraicGeometry.Space.dimension_le_add_iSup_residueFieldTranscendenceDegree
statement: formalized
proof: formalized
---

# 67.35 The dimension formula

Section 67.35 of the Stacks Project, [Tag 0BAW](https://stacks.math.columbia.edu/tag/0BAW). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BAX, a lemma

[Tag 0BAX](https://stacks.math.columbia.edu/tag/0BAX) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_zeroDimensionalSpecializations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L463). The attribute's comment: “finiteness of the family entering the maximum”. References: EGA IV (13.2.6), “more general”.

> **Stacks 0BAX, finiteness of the family entering the maximum.** Under the hypotheses of the
> dimension formula only finitely many codimension-zero points of the source specialize to a
> given point.
>
> The source is locally Noetherian by Stacks 04ZK, hence has locally finite irreducible
> components by Stacks 0GMB, so every quasi-compact algebraic space étale over it has finitely
> many codimension-zero points by Stacks 0BB1. An affine étale chart through the point is such a
> space, its image on points is open by Stacks 03BX and therefore contains every point
> specializing to the given one, and codimension zero is étale-invariant by Stacks 0A4H.

```lean
theorem finite_zeroDimensionalSpecializations (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hf : IsLocallyOfFiniteType B S hS f) (x : points B S hS X) :
    {ξ : points B S hS X | x ∈ closure {ξ} ∧ localRingDimension B S hS ξ = 0}.Finite
```

**`AlgebraicGeometry.Space.exists_genericResidueFieldTranscendenceDegreeAt_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 520](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L520). The attribute's comment: “attainment of the maximum”.

> **Stacks 0BAX, attainment of the maximum.** Under the hypotheses of the dimension formula
> the supremum defining the correction term is attained, so it is a maximum.
>
> The family is finite by `AlgebraicGeometry.Space.finite_zeroDimensionalSpecializations`, and it
> is nonempty because the generic point of an irreducible component of an étale chart through the
> chosen point maps to a codimension-zero point specializing to it (Stacks 0BAQ).

```lean
theorem exists_genericResidueFieldTranscendenceDegreeAt_eq (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hf : IsLocallyOfFiniteType B S hS f) (x : points B S hS X) :
    ∃ ξ : {ξ : points B S hS X // x ∈ closure {ξ} ∧ localRingDimension B S hS ξ = 0},
      genericResidueFieldTranscendenceDegreeAt B S hS f x =
        residueFieldTranscendenceDegreeAt B S hS f ξ.1
```

**`AlgebraicGeometry.Space.localRingDimension_add_residueFieldTranscendenceDegree_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L594). The attribute's comment: “dimension inequality”. References: EGA IV (5.6.5), “more general”.

> **Stacks 0BAX, the dimension inequality.** For a morphism of algebraic spaces over `S`
> locally of finite type with locally Noetherian target, the dimension of the local ring at a
> point plus the residue-field transcendence degree there is at most the dimension of the local
> ring at the image point plus the largest residue-field transcendence degree at a
> codimension-zero point specializing to the given one.
>
> Everything is read on one pointed étale chart of Stacks 04NC: the two local dimensions are the
> Krull dimensions of the two chart stalks by Stacks 0BAM, the two residue-field degrees are
> those of the morphism of charts by Stacks 04NK, and the inequality between them is the
> dimension formula for schemes, Stacks 0BAE. The chart's own maximum is bounded by the one in
> the statement because each generic point of the chart through the chart point maps to a
> codimension-zero point of the source specializing to the given one, by Stacks 0BAQ and
> Stacks 0A4H.

```lean
theorem localRingDimension_add_residueFieldTranscendenceDegree_le (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hf : IsLocallyOfFiniteType B S hS f) (x : points B S hS X) :
    (localRingDimension B S hS x : WithBot ℕ∞) +
        (residueFieldTranscendenceDegreeAt B S hS f x : WithBot ℕ∞) ≤
      (localRingDimension B S hS (pointsMap B S hS X f x) : WithBot ℕ∞) +
        (genericResidueFieldTranscendenceDegreeAt B S hS f x : WithBot ℕ∞)
```

## Tag 0BAY, a lemma

[Tag 0BAY](https://stacks.math.columbia.edu/tag/0BAY) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_le_add_iSup_residueFieldTranscendenceDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean, line 677](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ConstructibleSets.lean#L677).

> **Stacks 0BAY.** For a morphism of algebraic spaces over `S` locally of finite type with
> locally Noetherian target, the dimension of the source is at most the dimension of the target
> plus the supremum of the residue-field transcendence degrees at the codimension-zero points of
> the source.
>
> Both dimensions are suprema of local-ring dimensions by Stacks 0BAN, and at each point the
> pointwise inequality is Stacks 0BAX, whose correction term is attained at a codimension-zero
> point and so is bounded by the supremum over all of them.

```lean
theorem dimension_le_add_iSup_residueFieldTranscendenceDegree (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hNoeth : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hf : IsLocallyOfFiniteType B S hS f) :
    dimension B S hS X hX ≤ dimension B S hS Y hY +
      ((⨆ ξ : {ξ : points B S hS X // localRingDimension B S hS ξ = 0},
        residueFieldTranscendenceDegreeAt B S hS f ξ.1 : ℕ∞) : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.35, Tag 0BAW](https://stacks.math.columbia.edu/tag/0BAW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
