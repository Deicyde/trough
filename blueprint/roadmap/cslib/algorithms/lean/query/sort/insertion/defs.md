---
catalog: module
lean: Cslib.Query.orderedInsert, Cslib.Query.insertionSort
statement: formalized
proof: formalized
---

# Insertion Sort as a Query Program

`Cslib.Algorithms.Lean.Query.Sort.Insertion.Defs`, in [Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean), by Kim Morrison, Shreyas Srinivas, Eric Wieser.

> Insertion sort implemented as a `FreeM (LEQuery α)`, making all comparison queries explicit.

`Cslib.Query.orderedInsert` (abbreviation, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean#L23))

> Insert `x` into a sorted list using comparison queries.

```lean
abbrev orderedInsert (x : α) (xs : List α) : FreeM (LEQuery α) (List α)
```

`Cslib.Query.insertionSort` (abbreviation, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean#L27))

> Sort a list using insertion sort with comparison queries.

```lean
abbrev insertionSort (xs : List α) : FreeM (LEQuery α) (List α)
```

## Depends on

- [LEQuery: Comparison Queries for Sorting](../lequery.md)
- [A Monadic version of Mathlib's `List.insertionSort`](../../../sort/insertion.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean)
