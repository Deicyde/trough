---
catalog: module
lean: Cslib.infinite_pigeonhole_principle, Cslib.infinite_graph_ramsey
statement: formalized
proof: formalized
---

# Ramsey theorem for infinite graphs

`Cslib.Foundations.Combinatorics.InfiniteGraphRamsey`, in [Cslib/Foundations/Combinatorics/InfiniteGraphRamsey.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Combinatorics/InfiniteGraphRamsey.lean), by Ching-Tsun Chou.

> This result really should be in Mathlib, but currently it is not. We do expect
> the Ramsey theorem for infinite hypergraphs to appear in Mathlib eventually and
> this result to be derived as a corollary of the more general result.

`Cslib.infinite_pigeonhole_principle` (theorem, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Combinatorics/InfiniteGraphRamsey.lean#L29))

> An infinite pigeonhole principle.

```lean
theorem infinite_pigeonhole_principle {X Y : Type*} [Finite Y] (f : X → Y) {s : Set X}
    (h_inf : s.Infinite) : ∃ y, ∃ t, t.Infinite ∧ t ⊆ s ∧ ∀ x ∈ t, f x = y
```

`Cslib.infinite_graph_ramsey` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Combinatorics/InfiniteGraphRamsey.lean#L123))

> If the edges of an infinite complete graph is assigned a finite number of colors,
> then there must exist a color `c` and an infinite set `s` of vertices such that the edge
> between any two vertices of `s` is assigned the same color `c`.

```lean
theorem infinite_graph_ramsey :
    ∃ c : Color, ∃ s : Set Vertex, s.Infinite ∧
      ∀ e : Finset Vertex, e.card = 2 → ↑e ⊆ s → color e = c
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Combinatorics/InfiniteGraphRamsey.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Combinatorics/InfiniteGraphRamsey.lean)
