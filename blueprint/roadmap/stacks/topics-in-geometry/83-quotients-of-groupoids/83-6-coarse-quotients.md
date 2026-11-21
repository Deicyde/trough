---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsCoarseQuotient, AlgebraicGeometry.Space.IsCoarseQuotientInSchemes
statement: formalized
proof: formalized
---

# 83.6 Coarse quotients

Section 83.6 of the Stacks Project, [Tag 04A1](https://stacks.math.columbia.edu/tag/04A1). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 04A2, a definition

[Tag 04A2](https://stacks.math.columbia.edu/tag/04A2) in the Stacks Project.

**`AlgebraicGeometry.Space.IsCoarseQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoarseQuotient.lean, line 150](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoarseQuotient.lean#L150). The attribute's comment: “algebraic spaces”.

> **Stacks 04A2.** A morphism `φ : U ⟶ X` of algebraic spaces over `B` is a *coarse
> quotient* of a pre-relation `j` when it is a categorical quotient of `j` and an orbit space
> for it.

```lean
noncomputable abbrev IsCoarseQuotient {R U X : Over B} (j : PreRelation R U) (φ : U ⟶ X) :
    Prop
```

**`AlgebraicGeometry.Space.IsCoarseQuotientInSchemes`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoarseQuotient.lean, line 252](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CoarseQuotient.lean#L252). The attribute's comment: “schemes”.

> **Stacks 04A2.** A morphism `φ : U ⟶ X` of schemes over the base scheme `S`, with `R`,
> `U` and `X` contained in the big fppf site, is a *coarse quotient in schemes* of a
> pre-relation `j` of schemes over `S` when it is a categorical quotient in schemes of `j`
> and an orbit space for it.

```lean
noncomputable abbrev IsCoarseQuotientInSchemes {R U X : Over S} (hR : site.Contains R.left)
    (hU : site.Contains U.left) (hX : site.Contains X.left)
    (j : Stacks.Groupoids.PreRelation R U) (φ : U ⟶ X) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.6, Tag 04A1](https://stacks.math.columbia.edu/tag/04A1)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
