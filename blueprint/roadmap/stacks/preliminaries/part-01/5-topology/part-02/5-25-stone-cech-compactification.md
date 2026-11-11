---
declaration: section
origin: cited
lean: mk_le_mk_set_set_of_denseRange, exists_compactification_and_isOpenEmbedding_stoneCechUnit
statement: formalized
proof: formalized
---

# 5.25 Stone-Čech compactification

Section 5.25 of the Stacks Project, [Tag 0908](https://stacks.math.columbia.edu/tag/0908). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0909, a lemma

[Tag 0909](https://stacks.math.columbia.edu/tag/0909) in the Stacks Project.

**`mk_le_mk_set_set_of_denseRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compactification/CardinalityBound.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Compactification/CardinalityBound.lean#L106).

> **Stacks 0909.** If `f : X → Y` is a continuous map of topological spaces with dense image
> and `Y` is Hausdorff, then `#Y ≤ #P(P(X))`.

```lean
theorem mk_le_mk_set_set_of_denseRange
    {X Y : Type u} [TopologicalSpace X] [TopologicalSpace Y] [T2Space Y]
    (f : X → Y) (hf : Continuous f) (hd : DenseRange f) :
    Cardinal.mk Y ≤ Cardinal.mk (Set (Set X))
```

## Tag 090A, a lemma

[Tag 090A](https://stacks.math.columbia.edu/tag/090A) in the Stacks Project.

**`exists_compactification_and_isOpenEmbedding_stoneCechUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compactification/OnePoint.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Compactification/OnePoint.lean#L220).

> **Stacks 090A.**  For a Hausdorff, locally quasi-compact space `X`:
> (1) there exists a compact Hausdorff space `X*` and an open embedding
>     `f : X → X*` whose range has singleton complement, and
> (2) the canonical map `X → StoneCech X` is also an open embedding.

```lean
theorem exists_compactification_and_isOpenEmbedding_stoneCechUnit [WeaklyLocallyCompactSpace X]
  [T2Space X] :
    (∃ (Xstar : Type u) (_ : TopologicalSpace Xstar)
      (_ : CompactSpace Xstar) (_ : T2Space Xstar)
      (f : X → Xstar) (p : Xstar),
        IsOpenEmbedding f ∧ (range f)ᶜ = {p}) ∧
    IsOpenEmbedding (stoneCechUnit : X → StoneCech X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.25, Tag 0908](https://stacks.math.columbia.edu/tag/0908)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
