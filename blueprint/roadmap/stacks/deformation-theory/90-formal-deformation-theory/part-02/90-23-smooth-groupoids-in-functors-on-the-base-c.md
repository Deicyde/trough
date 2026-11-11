---
declaration: section
origin: cited
lean: Deformation.GroupoidInFunctors.IsSmooth, Deformation.smooth_groupoid_quotient_not_smooth, isSmooth_iff_source, source_isSmooth_iff_quotient, Deformation.isSmooth_iff_source, Deformation.source_isSmooth_iff_target, Deformation.source_isSmooth_iff_quotient
statement: formalized
proof: formalized
---

# 90.23 Smooth groupoids in functors on the base category

Section 90.23 of the Stacks Project, [Tag 06KH](https://stacks.math.columbia.edu/tag/06KH). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06KI, a definition

[Tag 06KI](https://stacks.math.columbia.edu/tag/06KI) in the Stacks Project.

**`Deformation.GroupoidInFunctors.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Smooth.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Groupoid/Smooth.lean#L55).

> A groupoid in functors is smooth when both its source and target morphisms are smooth.

```lean
public abbrev GroupoidInFunctors.IsSmooth (G : GroupoidInFunctors
  (ArtinianLocalAlgCat.{u, v, w} Λ k)) : Prop
```

## Tag 06KJ, a remark

[Tag 06KJ](https://stacks.math.columbia.edu/tag/06KJ) in the Stacks Project.

**`Deformation.smooth_groupoid_quotient_not_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/SmoothWarning.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/SmoothWarning.lean#L247). The attribute's comment: “smooth groupoid with nonsmooth quotient category”.

> A smooth groupoid in functors can have a quotient category that is not smooth
> over the base.

```lean
public theorem smooth_groupoid_quotient_not_smooth :
    ∃ G : GroupoidInFunctors (ArtinianLocalAlgCat.{0, 0, 0} ℚ ℚ),
      GroupoidInFunctors.IsSmooth G ∧
        ¬ IsSmooth (quotientProjectionBasedFunctor G)
```

Declarations registered for the tag:

- [`isSmooth_iff_source`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isSmooth_iff_source#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/GroupoidQuotient/SmoothWarning.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/SmoothWarning.lean#L292) (StacksFrontier): “smooth groupoid iff smooth source”.
- [`source_isSmooth_iff_quotient`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=source_isSmooth_iff_quotient#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/GroupoidQuotient/SmoothWarning.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/GroupoidQuotient/SmoothWarning.lean#L293) (StacksFrontier): “smooth source iff smooth quotient morphism”.

## Tag 06KL, a lemma

[Tag 06KL](https://stacks.math.columbia.edu/tag/06KL) in the Stacks Project.

**`Deformation.isSmooth_iff_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Smooth.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Groupoid/Smooth.lean#L411). The attribute's comment: “smooth groupoid iff smooth source”.

> A groupoid in functors is smooth exactly when its source morphism is smooth.

```lean
public theorem isSmooth_iff_source
    (G : GroupoidInFunctors (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
      GroupoidInFunctors.IsSmooth G ↔
      Deformation.IsSmooth (elementsBasedFunctor G.source)
```

**`Deformation.source_isSmooth_iff_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Smooth.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Groupoid/Smooth.lean#L419). The attribute's comment: “smooth source iff smooth target”.

> Smoothness of the source and target morphisms of a groupoid in functors are equivalent.

```lean
public theorem source_isSmooth_iff_target
    (G : GroupoidInFunctors (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    Deformation.IsSmooth (elementsBasedFunctor G.source) ↔
      Deformation.IsSmooth (elementsBasedFunctor G.target)
```

**`Deformation.source_isSmooth_iff_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Smooth.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Groupoid/Smooth.lean#L427). The attribute's comment: “smooth source iff smooth quotient morphism”.

> The source morphism is smooth exactly when the quotient morphism is smooth.

```lean
public theorem source_isSmooth_iff_quotient
    (G : GroupoidInFunctors (ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    Deformation.IsSmooth (elementsBasedFunctor G.source) ↔
      Deformation.IsSmooth (quotientBasedFunctor G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.23, Tag 06KH](https://stacks.math.columbia.edu/tag/06KH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
