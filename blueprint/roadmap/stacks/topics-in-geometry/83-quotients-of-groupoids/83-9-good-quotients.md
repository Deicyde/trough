---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsGoodQuotient
statement: formalized
proof: formalized
---

# 83.9 Good quotients

Section 83.9 of the Stacks Project, [Tag 04AB](https://stacks.math.columbia.edu/tag/04AB). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 04AC, a definition

[Tag 04AC](https://stacks.math.columbia.edu/tag/04AC) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGoodQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean, line 277](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean#L277).

> **Stacks 04AC.** A morphism `φ : U ⟶ X` of algebraic spaces over `B` is a *good quotient*
> of a pre-relation `j` when it is `R`-invariant, affine and surjective, condition (3) of
> **Stacks 04A4** holds for it universally, and the functions on `X` are the `R`-invariant
> functions on `U`.

```lean
abbrev IsGoodQuotient {B : AlgebraicSpaces site S hS} {R U X : Over B} (j : PreRelation R U)
    (φ : U ⟶ X) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.9, Tag 04AB](https://stacks.math.columbia.edu/tag/04AB)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
