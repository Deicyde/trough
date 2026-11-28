---
catalog: module
lean: Cslib.Query.IsSort.lowerBound_infinite
statement: formalized
proof: formalized
---

# Comparison Sorting Lower Bound

`Cslib.Algorithms.Lean.Query.Sort.LowerBound`, in [Cslib/Algorithms/Lean/Query/Sort/LowerBound.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/LowerBound.lean), by Kim Morrison, Shreyas Srinivas, Eric Wieser.

> `IsSort.lowerBound_infinite`: any correct comparison sort on an infinite type
> has query complexity at least `⌈log₂(n!)⌉` for every input size `n`.
>
> The proof constructs `n!` distinct total orders on `α` (one per permutation of `n`
> embedded elements), shows they produce distinct sorted outputs, and applies
> `FreeM.exists_countQueries_ge_clog` with `LEQuery.cardResponse_le_two` witnessing that
> all responses come from `Bool` (cardinality 2).

> ## PrefixPermOrder: constructing n! distinct total orders

> ## Main theorem

`Cslib.Query.IsSort.lowerBound_infinite` (theorem, [line 116](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/LowerBound.lean#L116))

> Any correct comparison sort on an infinite type has query complexity at least `⌈log₂(n!)⌉`
> for every input size `n`.

```lean
theorem IsSort.lowerBound_infinite [Infinite α]
    {sort : List α → FreeM (LEQuery α) (List α)}
    (hs : IsSort sort) :
    LowerBound sort List.length (fun n => Nat.clog 2 (Nat.factorial n))
```

## Depends on

- [Upper and Lower Bounds for Query Complexity](../bounds.md)
- [IsSort: Specification for Comparison Sorts](issort.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/LowerBound.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Algorithms/Lean/Query/Sort/LowerBound.lean)
- [Declaration ledger](../../../../../../sources/cslib/Cslib.Algorithms.Lean.Query.Sort.LowerBound.json)
