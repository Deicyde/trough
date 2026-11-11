---
declaration: section
origin: cited
lean: IsProfiniteStacks, isProfinite_iff, Profinite.hasLimits, TopologicalSpace.IsOpenCover.exists_finite_nonempty_disjoint_clopen_cover, isProfiniteSpacePropForm_connectedComponents
statement: formalized
proof: formalized
---

# 5.22 Profinite spaces

Section 5.22 of the Stacks Project, [Tag 08ZW](https://stacks.math.columbia.edu/tag/08ZW). 5 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08ZX, a definition

[Tag 08ZX](https://stacks.math.columbia.edu/tag/08ZX) in the Stacks Project.

**`IsProfiniteStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Profinite/Defs.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Profinite/Defs.lean#L36).

> **Stacks 08ZX** (definition of profinite). A topological space `X` is profinite if it is
> homeomorphic to (the underlying space of) the limit of some diagram of finite discrete topological
> spaces.

```lean
def IsProfiniteStacks (X : Type u) [TopologicalSpace X] : Prop
```

## Tag 08ZY, a lemma

[Tag 08ZY](https://stacks.math.columbia.edu/tag/08ZY) in the Stacks Project.

**`isProfinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Profinite/Characterization.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Profinite/Characterization.lean#L107).

> **Stacks 08ZY.** For a topological space `X` the following are equivalent: (1) `X` is a
> profinite space; (2) `X` is Hausdorff, quasi-compact and totally disconnected.

```lean
theorem isProfinite_iff (X : Type u) [TopologicalSpace X] :
    IsProfinite X ↔
      (T2Space X ∧ CompactSpace X ∧ TotallyDisconnectedSpace X)
```

## Tag 0ET8, a lemma

[Tag 0ET8](https://stacks.math.columbia.edu/tag/0ET8) in the Stacks Project.

Declarations registered for the tag:

- [`Profinite.hasLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Profinite.hasLimits#doc) registered with `add_to_stacks` in [StacksCore/Topology/Profinite/Limits.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Profinite/Limits.lean#L21) (StacksCore): “every small diagram of profinite spaces has a limit in `Profinite`, i.e. its limit is again a profinite space”.

## Tag 08ZZ, a lemma

[Tag 08ZZ](https://stacks.math.columbia.edu/tag/08ZZ) in the Stacks Project.

Declarations registered for the tag:

- [`TopologicalSpace.IsOpenCover.exists_finite_nonempty_disjoint_clopen_cover`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.IsOpenCover.exists_finite_nonempty_disjoint_clopen_cover#doc) registered with `add_to_stacks` in [StacksCore/Topology/Profinite/ClopenRefinement.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Profinite/ClopenRefinement.lean#L21) (StacksCore).

## Tag 0900, a lemma

[Tag 0900](https://stacks.math.columbia.edu/tag/0900) in the Stacks Project.

**`isProfiniteSpacePropForm_connectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/ComponentSpaceCompact.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Connected/ComponentSpaceCompact.lean#L60).

> **Stacks 0900.** Let `X` be a quasi-compact topological space such that every connected
> component of `X` equals the intersection of the clopen subsets of `X` containing it. Then
> `ConnectedComponents X`, with the quotient topology, is a profinite space: compact, Hausdorff and
> totally disconnected.

```lean
theorem isProfiniteSpacePropForm_connectedComponents
    (X : Type*) [TopologicalSpace X] [CompactSpace X]
    (h_clopen_inter : ∀ x : X,
      connectedComponent x = ⋂₀ {U : Set X | IsClopen U ∧ connectedComponent x ⊆ U}) :
    IsProfiniteSpacePropForm (ConnectedComponents X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.22, Tag 08ZW](https://stacks.math.columbia.edu/tag/08ZW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
