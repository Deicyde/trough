---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.uniqueBranch_tfae, AlgebraicGeometry.Space.IsGeometricallyUnibranchAt, AlgebraicGeometry.Space.IsGeometricallyUnibranch, AlgebraicGeometry.Space.minimalPrimeCount_iff_componentCount, AlgebraicGeometry.Space.componentCount_iff_branchCount, AlgebraicGeometry.Space.branchCount_iff_geometricBranchCount, AlgebraicGeometry.Space.geometricBranchCount_iff_etaleLocalRingMinimalPrimeCount, AlgebraicGeometry.Space.numberOfGeometricBranches
statement: formalized
proof: formalized
---

# 66.23 Local irreducibility

Section 66.23 of the Stacks Project, [Tag 06DJ](https://stacks.math.columbia.edu/tag/06DJ). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06DK, a lemma

[Tag 06DK](https://stacks.math.columbia.edu/tag/06DK) in the Stacks Project.

**`AlgebraicGeometry.Space.uniqueBranch_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnibranchCriteria.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnibranchCriteria.lean#L480).

> **Stacks 06DK.** For a point `x` of an algebraic space `F` the five branch criteria are
> equivalent: a unique minimal prime in the local rings of the étale charts above `x`, a unique
> irreducible component of those charts through those points, unibranchness and geometric
> unibranchness of those local rings, and a unique minimal prime in the étale local ring at
> every geometric point above `x`.

```lean
theorem uniqueBranch_tfae (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    List.TFAE [HasUniqueMinimalPrimeOnEtaleCharts B S hS F x,
      HasUniqueIrreducibleComponentOnEtaleCharts B S hS F x,
      IsUnibranchOnEtaleCharts B S hS F x,
      IsGeometricallyUnibranchAt B S hS F x,
      HasUniqueMinimalPrimeAtGeometricPoints B S hS F x]
```

## Tag 06DL, a definition

[Tag 06DL](https://stacks.math.columbia.edu/tag/06DL) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGeometricallyUnibranchAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unibranch.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Unibranch.lean#L66). The attribute's comment: “at a point”.

> **Stacks 06DL, at a point.** The presheaf `F` is geometrically unibranch at a point `x` of
> `|F|` when the local ring of every étale chart of `F` at every point above `x` is geometrically
> unibranch.  This is condition (4) of Tag 06DK, which for an algebraic space is equivalent to the
> four other branch criteria there.

```lean
noncomputable def IsGeometricallyUnibranchAt (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.IsGeometricallyUnibranch`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Unibranch.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Unibranch.lean#L78). The attribute's comment: “at every point”.

> **Stacks 06DL, at every point.** The presheaf `F` is geometrically unibranch when it is
> geometrically unibranch at every point of `|F|`.

```lean
noncomputable abbrev IsGeometricallyUnibranch : Prop
```

## Tag 0DQ3, a lemma

[Tag 0DQ3](https://stacks.math.columbia.edu/tag/0DQ3) in the Stacks Project.

**`AlgebraicGeometry.Space.minimalPrimeCount_iff_componentCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean#L261). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0DQ3, conditions (1) and (2).** A point of a presheaf on the big fppf site has
> minimal-prime count `n` on its étale scheme charts exactly when it has irreducible-component
> count `n` on them: the two counts agree at each chart point separately.

```lean
theorem minimalPrimeCount_iff_componentCount (x : points B S hS F) (n : ℕ) :
    HasMinimalPrimeCount B S hS x n ↔ HasComponentCount B S hS x n
```

**`AlgebraicGeometry.Space.componentCount_iff_branchCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean#L382). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0DQ3, conditions (2) and (3).** A point of a presheaf on the big fppf site has
> irreducible-component count `n` on its étale scheme charts exactly when it has branch count `n`
> on them.
>
> No algebraicity hypothesis is needed: both directions only use that an étale neighbourhood of a
> point of a chart above `x` is refined by an open subscheme of a chart above `x`.

```lean
theorem componentCount_iff_branchCount (x : points B S hS F) (n : ℕ) :
    HasComponentCount B S hS x n ↔ HasBranchCount B S hS x n
```

**`AlgebraicGeometry.Space.branchCount_iff_geometricBranchCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean#L400). The attribute's comment: “conditions (3) and (4)”.

> **Stacks 0DQ3, conditions (3) and (4).** A point of an algebraic space has branch count `n`
> on its étale scheme charts exactly when every chart has exactly `n` geometric branches at every
> point above it.

```lean
theorem branchCount_iff_geometricBranchCount (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) (n : ℕ) :
    HasBranchCount B S hS x n ↔ HasGeometricBranchCount B S hS x n
```

**`AlgebraicGeometry.Space.geometricBranchCount_iff_etaleLocalRingMinimalPrimeCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BranchCount.lean#L520). The attribute's comment: “conditions (4) and (5)”.

> **Stacks 0DQ3, conditions (4) and (5).** Every étale scheme chart of an algebraic space has
> exactly `n` geometric branches at every point above `x` exactly when the étale local ring at
> every geometric point above `x` has exactly `n` minimal primes.

```lean
theorem geometricBranchCount_iff_etaleLocalRingMinimalPrimeCount
    (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) (n : ℕ) :
    HasGeometricBranchCount B S hS x n ↔
      HasEtaleLocalRingMinimalPrimeCount B S hS x n
```

## Tag 0DQ4, a definition

[Tag 0DQ4](https://stacks.math.columbia.edu/tag/0DQ4) in the Stacks Project.

**`AlgebraicGeometry.Space.numberOfGeometricBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumberOfGeometricBranches.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumberOfGeometricBranches.lean#L98).

> **Stacks 0DQ4.** The number of geometric branches of an algebraic space at a point: the
> natural number satisfying the equivalent conditions of Tag 0DQ3 if there is one, and `⊤`
> otherwise.

```lean
def numberOfGeometricBranches (x : points B S hS F) : ℕ∞
```

**`AlgebraicGeometry.Space.numberOfGeometricBranches_eq_nat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumberOfGeometricBranches.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumberOfGeometricBranches.lean#L104). The attribute's comment: “finite value”.

> **Stacks 0DQ4.** A finite value of the number of geometric branches of an algebraic space at
> a point is exactly the value appearing in the equivalent conditions of Tag 0DQ3.

```lean
theorem numberOfGeometricBranches_eq_nat_iff (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) (n : ℕ) :
    numberOfGeometricBranches B S hS x = (n : ℕ∞) ↔ HasGeometricBranchCount B S hS x n
```

**`AlgebraicGeometry.Space.numberOfGeometricBranches_eq_top_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumberOfGeometricBranches.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumberOfGeometricBranches.lean#L113). The attribute's comment: “infinite value”.

> **Stacks 0DQ4.** The number of geometric branches of an algebraic space at a point is
> infinite exactly when no natural number satisfies the equivalent conditions of Tag 0DQ3.

```lean
theorem numberOfGeometricBranches_eq_top_iff (x : points B S hS F) :
    numberOfGeometricBranches B S hS x = ⊤ ↔
      ∀ n : ℕ, ¬ HasGeometricBranchCount B S hS x n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.23, Tag 06DJ](https://stacks.math.columbia.edu/tag/06DJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
