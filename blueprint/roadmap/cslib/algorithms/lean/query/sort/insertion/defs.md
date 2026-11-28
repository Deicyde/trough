---
catalog: module
lean: Cslib.Query.orderedInsert, Cslib.Query.insertionSort
statement: formalized
proof: formalized
---

# Insertion Sort as a Query Program

`Cslib.Algorithms.Lean.Query.Sort.Insertion.Defs`, in [Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean), by Kim Morrison, Shreyas Srinivas, Eric Wieser.

> Insertion sort implemented as a `FreeM (LEQuery α)`, making all comparison queries explicit.

`Cslib.Query.orderedInsert` (abbreviation, [line 23](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean#L23))

> Insert `x` into a sorted list using comparison queries.

```lean
abbrev orderedInsert (x : α) (xs : List α) : FreeM (LEQuery α) (List α)
```

`Cslib.Query.insertionSort` (abbreviation, [line 27](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean#L27))

> Sort a list using insertion sort with comparison queries.

```lean
abbrev insertionSort (xs : List α) : FreeM (LEQuery α) (List α)
```

## Depends on

- [LEQuery: Comparison Queries for Sorting](../lequery.md)
- [A Monadic version of Mathlib's `List.insertionSort`](../../../sort/insertion.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/Insertion/Defs.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Algorithms.Lean.Query.Sort.Insertion.Defs.json)
