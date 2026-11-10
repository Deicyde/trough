---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsGeometricQuotient
statement: formalized
proof: formalized
---

# 83.10 Geometric quotients

Section 83.10 of the Stacks Project, [Tag 04AD](https://stacks.math.columbia.edu/tag/04AD). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04AE, a definition

[Tag 04AE](https://stacks.math.columbia.edu/tag/04AE) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean#L291).

> **Stacks 04AE.** A morphism `φ : U ⟶ X` of algebraic spaces over `B` is a *geometric
> quotient* of a pre-relation `j` when it is an orbit space for `j`, universally submersive,
> and the functions on `X` are the `R`-invariant functions on `U`.

```lean
abbrev IsGeometricQuotient {B : AlgebraicSpaces site S hS} {R U X : Over B}
    (j : PreRelation R U) (φ : U ⟶ X) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.10, Tag 04AD](https://stacks.math.columbia.edu/tag/04AD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
