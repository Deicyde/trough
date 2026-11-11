---
declaration: section
origin: cited
lean: t2_iff_isClosed_diagonal, Continuous.isClosed_graph, Function.LeftInverse.isClosed_range, fibreProduct_isClosed
statement: formalized
proof: formalized
---

# 5.3 Hausdorff spaces

Section 5.3 of the Stacks Project, [Tag 08ZD](https://stacks.math.columbia.edu/tag/08ZD). 4 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08ZE, a lemma

[Tag 08ZE](https://stacks.math.columbia.edu/tag/08ZE) in the Stacks Project.

Declarations registered for the tag:

- [`t2_iff_isClosed_diagonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=t2_iff_isClosed_diagonal#doc) registered with `add_to_stacks` in [StacksCore/Topology/Separation/Diagonal.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Separation/Diagonal.lean#L19) (StacksCore).

## Tag 08ZF, a lemma

[Tag 08ZF](https://stacks.math.columbia.edu/tag/08ZF) in the Stacks Project.

Declarations registered for the tag:

- [`Continuous.isClosed_graph`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Continuous.isClosed_graph#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Separation/Graph.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Separation/Graph.lean#L20) (StacksFrontier).

## Tag 08ZG, a lemma

[Tag 08ZG](https://stacks.math.columbia.edu/tag/08ZG) in the Stacks Project.

Declarations registered for the tag:

- [`Function.LeftInverse.isClosed_range`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Function.LeftInverse.isClosed_range#doc) registered with `add_to_stacks` in [StacksCore/Topology/Separation/Section.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Separation/Section.lean#L22) (StacksCore): “a retract of a Hausdorff space is closed”.

## Tag 08ZH, a lemma

[Tag 08ZH](https://stacks.math.columbia.edu/tag/08ZH) in the Stacks Project.

**`fibreProduct_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Separation/FibreProduct.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Separation/FibreProduct.lean#L28).

> **Stacks 08ZH.** Let `f : X → Z` and `g : Y → Z` be continuous maps of topological spaces.
> If `Z` is Hausdorff, then the fibre product `X ×_Z Y` is a closed subset of `X × Y`, being the
> equaliser of `f ∘ Prod.fst` and `g ∘ Prod.snd`.

```lean
theorem fibreProduct_isClosed
    {X Y Z : Type*} [TopologicalSpace X] [TopologicalSpace Y] [TopologicalSpace Z]
    [T2Space Z] {f : X → Z} {g : Y → Z} (hf : Continuous f) (hg : Continuous g) :
    IsClosed (fibreProduct f g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.3, Tag 08ZD](https://stacks.math.columbia.edu/tag/08ZD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
