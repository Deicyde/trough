---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.cyclesOfDimension, AlgebraicGeometry.Space.CycleGroup
statement: formalized
proof: formalized
---

# 82.3 Cycles

Section 82.3 of the Stacks Project, [Tag 0EDY](https://stacks.math.columbia.edu/tag/0EDY). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EDZ, a definition

[Tag 0EDZ](https://stacks.math.columbia.edu/tag/0EDZ) in the Stacks Project.

**`AlgebraicGeometry.Space.cyclesOfDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Cycles.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Cycles.lean#L296). The attribute's comment: “parts (1) and (2): cycles and k-cycles”. References: EGA IV (21.6.1), “fixed δ-dimension k”.

> **Stacks 0EDZ, parts (1) and (2).** The subgroup `Z_k(X)` of integer coefficient families
> on the integral closed subspaces of a good algebraic space `X/B` which are *cycles* — the point
> sets of the subspaces with nonzero coefficient form a locally finite collection of subsets of
> `|X|` — and are *of δ-dimension `k`* — every subspace with nonzero coefficient has δ-dimension
> `k`.

```lean
noncomputable def cyclesOfDimension (sX : X ⟶ D.space) (k : ℤ) :
    AddSubgroup (IntegralClosedSubspace D.site D.base D.base_mem X → ℤ)
```

**`AlgebraicGeometry.Space.CycleGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Cycles.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Cycles.lean#L340). The attribute's comment: “part (3): the abelian group of k-cycles”.

> **Stacks 0EDZ, part (3).** The abelian group `Z_k(X)` of `k`-cycles on a good algebraic
> space `X/B`.

```lean
noncomputable abbrev CycleGroup (sX : X ⟶ D.space) (k : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.3, Tag 0EDY](https://stacks.math.columbia.edu/tag/0EDY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
