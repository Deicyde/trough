---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.forall_etale_iff_forall_affine_etale, AlgebraicGeometry.Space.forall_etale_iff_exists_surjective_etale, AlgebraicGeometry.Space.IsEtaleLocallyConstructible
statement: formalized
proof: formalized
---

# 66.8 Constructible sets

Section 66.8 of the Stacks Project, [Tag 0ECS](https://stacks.math.columbia.edu/tag/0ECS). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ECT, a lemma

[Tag 0ECT](https://stacks.math.columbia.edu/tag/0ECT) in the Stacks Project.

**`AlgebraicGeometry.Space.forall_etale_iff_forall_affine_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePoints.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePoints.lean#L103). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0ECT, conditions (1) and (2).** Étale-local constructibility can be tested on
> affine étale charts, where it becomes constructibility.

```lean
theorem forall_etale_iff_forall_affine_etale :
    IsEtaleLocallyConstructible B S hS X E ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (f : yoneda.obj U ⟶ X), IsEtale B S hS f →
          IsConstructible (pointsMap B S hS (yoneda.obj U) f ⁻¹' E)
```

**`AlgebraicGeometry.Space.forall_etale_iff_exists_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePoints.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePoints.lean#L139). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 0ECT, conditions (1) and (3).** Étale-local constructibility holds as soon as it
> holds on a single surjective étale chart.

```lean
theorem forall_etale_iff_exists_surjective_etale (hX : IsAlgebraicSpace B S hS X) :
    IsEtaleLocallyConstructible B S hS X E ↔
      ∃ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ X),
        IsSurjective B S hS f ∧ IsEtale B S hS f ∧
          IsLocallyConstructible (pointsMap B S hS (yoneda.obj U) f ⁻¹' E)
```

## Tag 0ECU, a definition

[Tag 0ECU](https://stacks.math.columbia.edu/tag/0ECU) in the Stacks Project.

**`AlgebraicGeometry.Space.IsEtaleLocallyConstructible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePoints.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ConstructiblePoints.lean#L96).

> **Stacks 0ECU.** A subset of the points of a presheaf on the big fppf site of `S` is
> *étale locally constructible* when its inverse image on every étale chart from a scheme is a
> locally constructible subset of that chart.

```lean
abbrev IsEtaleLocallyConstructible : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.8, Tag 0ECS](https://stacks.math.columbia.edu/tag/0ECS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
