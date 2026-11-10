---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.numberOfGeometricBranches, AlgebraicGeometry.Stack.numberOfGeometricBranches_eq_nat_iff, AlgebraicGeometry.Stack.numberOfGeometricBranches_eq_top_iff, AlgebraicGeometry.Stack.IsGeometricallyUnibranchAt
statement: formalized
proof: formalized
---

# 100.13 Local irreducibility

Section 100.13 of the Stacks Project, [Tag 0DQG](https://stacks.math.columbia.edu/tag/0DQG). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DQH, a definition

[Tag 0DQH](https://stacks.math.columbia.edu/tag/0DQH) in the Stacks Project.

**`AlgebraicGeometry.Stack.numberOfGeometricBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean#L116). The attribute's comment: “part (1)”.

> **Stacks 0DQH, part (1).** The number of geometric branches of an algebraic stack at a
> point: the natural number for which the equivalent conditions of Tag 04YI hold for the germ
> property of having that many geometric branches, and `⊤` otherwise.

```lean
def numberOfGeometricBranches : ℕ∞
```

**`AlgebraicGeometry.Stack.numberOfGeometricBranches_eq_nat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean#L142). The attribute's comment: “part (1), finite value”.

> **Stacks 0DQH, part (1).** A finite value of the number of geometric branches of an
> algebraic stack at a point is exactly the value for which the equivalent conditions of Tag 04YI
> hold.

```lean
theorem numberOfGeometricBranches_eq_nat_iff (n : ℕ) :
    numberOfGeometricBranches.{u, w} B S hS 𝒳 x = (n : ℕ∞) ↔
      GermPropertyAtSomeSchemeChart B S hS 𝒳 x
        (GermOfScheme.GeometricBranchCountEq (n : ℕ∞))
```

**`AlgebraicGeometry.Stack.numberOfGeometricBranches_eq_top_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean#L160). The attribute's comment: “part (1), infinite value”.

> **Stacks 0DQH, part (1).** The number of geometric branches of an algebraic stack at a point
> is infinite exactly when the equivalent conditions of Tag 04YI hold for no natural number.

```lean
theorem numberOfGeometricBranches_eq_top_iff :
    numberOfGeometricBranches.{u, w} B S hS 𝒳 x = ⊤ ↔
      ∀ n : ℕ, ¬ GermPropertyAtSomeSchemeChart B S hS 𝒳 x
        (GermOfScheme.GeometricBranchCountEq (n : ℕ∞))
```

**`AlgebraicGeometry.Stack.IsGeometricallyUnibranchAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LocalIrreducibility.lean#L172). The attribute's comment: “part (2)”.

> **Stacks 0DQH, part (2).** An algebraic stack is geometrically unibranch at a point when its
> number of geometric branches there is `1`.

```lean
abbrev IsGeometricallyUnibranchAt : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.13, Tag 0DQG](https://stacks.math.columbia.edu/tag/0DQG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
