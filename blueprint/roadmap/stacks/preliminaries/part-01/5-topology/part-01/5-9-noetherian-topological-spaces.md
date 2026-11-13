---
declaration: section
origin: cited
lean: noetherianSpace_iff_wellFoundedLT_closeds, isLocallyNoetherianSpace_iff_forall_exists_mem_nhds, TopologicalSpace.NoetherianSpace.range_and_isLocallyNoetherianSpace_range, TopologicalSpace.NoetherianSpace.iUnion, TopologicalSpace.NoetherianSpace.exists_isClosed_singleton, Stacks.LocallyNoetherianNoClosedPoint.isLocallyNoetherianSpace, Stacks.LocallyNoetherianNoClosedPoint.not_isClosed_singleton, TopologicalSpace.IsLocallyNoetherianSpace.locallyConnectedSpace
statement: formalized
proof: formalized
---

# 5.9 Noetherian topological spaces

Section 5.9 of the Stacks Project, [Tag 0050](https://stacks.math.columbia.edu/tag/0050). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0051, a definition

[Tag 0051](https://stacks.math.columbia.edu/tag/0051) in the Stacks Project.

**`noetherianSpace_iff_wellFoundedLT_closeds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/Defs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/Defs.lean#L62). The attribute's comment: “Part (1): a space is Noetherian iff the descending chain condition holds for its closed subsets; part (2) is `isLocallyNoetherianSpace_iff_forall_exists_mem_nhds`.”. References: EGA 0 (2.2.1), “opens max ⇔ closeds min”; SGA 3 V (7.2), “partial”.

> A topological space is Noetherian if and only if its lattice of closed subsets is
> well-founded for the strict order.

```lean
theorem noetherianSpace_iff_wellFoundedLT_closeds
    (X : Type*) [TopologicalSpace X] :
    NoetherianSpace X ↔ WellFoundedLT (Closeds X)
```

**`isLocallyNoetherianSpace_iff_forall_exists_mem_nhds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/Defs.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/Defs.lean#L78). The attribute's comment: “Part (2): the definition of a locally Noetherian space, with Stacks' neighbourhoods (any subset containing an open set containing the point).”.

> A topological space is locally Noetherian, i.e. every point has a Noetherian open
> neighbourhood, if and only if every point has a neighbourhood (a subset containing an open set
> containing the point) which is Noetherian in the induced topology.

```lean
theorem isLocallyNoetherianSpace_iff_forall_exists_mem_nhds
    (X : Type*) [TopologicalSpace X] :
    IsLocallyNoetherianSpace X ↔ ∀ x : X, ∃ N ∈ nhds x, NoetherianSpace N
```

## Tag 04Z8, a lemma

[Tag 04Z8](https://stacks.math.columbia.edu/tag/04Z8) in the Stacks Project.

**`TopologicalSpace.NoetherianSpace.range_and_isLocallyNoetherianSpace_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/Image.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/Image.lean#L74). The attribute's comment: “Both parts: (1) is Mathlib's `TopologicalSpace.NoetherianSpace.range`, (2) is `TopologicalSpace.IsLocallyNoetherianSpace.range_of_isOpenMap`.”.

> **Stacks 04Z8.** Let `f : X → Y` be a continuous map of topological spaces.
> (1) If `X` is Noetherian, then `f(X)` is Noetherian.
> (2) If `X` is locally Noetherian and `f` is open, then `f(X)` is locally Noetherian.
>
> Here `f(X)` is `Set.range f` with the subspace topology.

```lean
theorem NoetherianSpace.range_and_isLocallyNoetherianSpace_range {X Y : Type*}
    [TopologicalSpace X] [TopologicalSpace Y] (f : X → Y) (hf : Continuous f) :
    (NoetherianSpace X → NoetherianSpace (Set.range f)) ∧
      (IsLocallyNoetherianSpace X → IsOpenMap f → IsLocallyNoetherianSpace (Set.range f))
```

## Tag 0053, a lemma

[Tag 0053](https://stacks.math.columbia.edu/tag/0053) in the Stacks Project.

Declarations registered for the tag:

- [`TopologicalSpace.NoetherianSpace.iUnion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.NoetherianSpace.iUnion#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Noetherian/FiniteUnion.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/FiniteUnion.lean#L18) (StacksFrontier). References: EGA 0 (2.2.3), “converse”.

## Tag 02HZ, an example

[Tag 02HZ](https://stacks.math.columbia.edu/tag/02HZ) in the Stacks Project.

**`TopologicalSpace.NoetherianSpace.exists_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/CounterexampleNoClosedPoint.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/CounterexampleNoClosedPoint.lean#L32). References: EGA 0 (2.1.3), “special case”.

> **Stacks 02HZ.** Every nonempty Kolmogorov Noetherian topological space has a closed
> point: it is quasi-compact, so Stacks 005E applies to the closed set `Set.univ`.

```lean
theorem TopologicalSpace.NoetherianSpace.exists_isClosed_singleton
    (X : Type*) [TopologicalSpace X] [Nonempty X] [NoetherianSpace X] [T0Space X] :
    ∃ x : X, IsClosed ({x} : Set X)
```

**`Stacks.LocallyNoetherianNoClosedPoint.isLocallyNoetherianSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/CounterexampleNoClosedPoint.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/CounterexampleNoClosedPoint.lean#L61).

> **Stacks 02HZ.** The space of Stacks 02HZ is locally Noetherian: for each `x`, the open
> neighbourhood `Set.Iic x = {0, …, x}` is finite, hence Noetherian.

```lean
theorem isLocallyNoetherianSpace :
    letI : TopologicalSpace ℕ := iicTopology
    IsLocallyNoetherianSpace ℕ
```

**`Stacks.LocallyNoetherianNoClosedPoint.not_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/CounterexampleNoClosedPoint.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/CounterexampleNoClosedPoint.lean#L73).

> **Stacks 02HZ.** The space of Stacks 02HZ has no closed point: every open set is a lower
> set, so `x + 1 ∈ closure {x}` while `x + 1 ≠ x`.

```lean
theorem not_isClosed_singleton :
    letI : TopologicalSpace ℕ := iicTopology
    ∀ x : ℕ, ¬ IsClosed ({x} : Set ℕ)
```

## Tag 04MF, a lemma

[Tag 04MF](https://stacks.math.columbia.edu/tag/04MF) in the Stacks Project.

**`TopologicalSpace.IsLocallyNoetherianSpace.locallyConnectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/LocallyConnected.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Noetherian/LocallyConnected.lean#L105). References: EGA I (6.1.9); SGA 3 X (7.0), “local connectedness”; SGA 4 VI (2.18), “special case”.

> **Stacks 04MF.** A locally Noetherian topological space is locally connected.

```lean
theorem IsLocallyNoetherianSpace.locallyConnectedSpace
    (α : Type*) [TopologicalSpace α] (hα : IsLocallyNoetherianSpace α) :
    LocallyConnectedSpace α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.9, Tag 0050](https://stacks.math.columbia.edu/tag/0050)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
