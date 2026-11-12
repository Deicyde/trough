---
catalog: module
lean: Cslib.Query.eval_orderedInsert, Cslib.Query.eval_insertionSort, Cslib.Query.orderedInsert_countQueries_le, Cslib.Query.insertionSort_countQueries_le, Cslib.Query.insertionSort_countQueries_le_sq, Cslib.Query.insertionSort_upperBound, Cslib.Query.insertionSort_isSort
statement: formalized
proof: formalized
---

# Insertion Sort: Correctness and Upper Bound

`Cslib.Algorithms.Lean.Query.Sort.Insertion.Lemmas`, in [Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean), by Kim Morrison, Shreyas Srinivas, Eric Wieser.

> Proofs that `insertionSort` is a correct comparison sort and uses at most `n * (n - 1) / 2`
> queries (with `n²` as a corollary). All proofs are by plain equational reasoning on
> `FreeM.eval` and `FreeM.countQueries`.

> ## Evaluation

`Cslib.Query.eval_orderedInsert` (theorem, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L32))

> Evaluating query-based insertion agrees with `List.orderedInsert` using the relation
> supplied by the oracle.

```lean
theorem eval_orderedInsert (oracle : {ι : Type} → LEQuery α ι → ι)
(x : α) (xs : List α) :
(orderedInsert x xs).eval oracle =
xs.orderedInsert (fun x y => oracle (.le x y)) x
```

`Cslib.Query.eval_insertionSort` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L44))

> Evaluating query-based insertion sort agrees with `List.insertionSort` using the relation
> supplied by the oracle.
>
> This is the essential correctness statement: it identifies the query program as *the*
> insertion sort operation, so correctness properties (permutation, sortedness) transfer
> directly from the `List.insertionSort` API rather than being restated here.

```lean
theorem eval_insertionSort (oracle : {ι : Type} → LEQuery α ι → ι) (xs : List α) :
(insertionSort xs).eval oracle =
xs.insertionSort (fun x y => oracle (.le x y))
```

> ## Query count proofs

`Cslib.Query.orderedInsert_countQueries_le` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L51))

```lean
theorem orderedInsert_countQueries_le (oracle : {ι : Type} → LEQuery α ι → ι)
    (x : α) (xs : List α) :
    (orderedInsert x xs).countQueries oracle ≤ xs.length
```

`Cslib.Query.insertionSort_countQueries_le` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L65))

> Insertion sort makes at most `n * (n - 1) / 2` queries: inserting into the sorted
> prefix of length `k` costs at most `k` queries. This bound is attained by the all-`false`
> oracle.

```lean
theorem insertionSort_countQueries_le (oracle : {ι : Type} → LEQuery α ι → ι)
    (xs : List α) :
    (insertionSort xs).countQueries oracle ≤ xs.length * (xs.length - 1) / 2
```

`Cslib.Query.insertionSort_countQueries_le_sq` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L86))

```lean
theorem insertionSort_countQueries_le_sq (oracle : {ι : Type} → LEQuery α ι → ι)
    (xs : List α) :
    (insertionSort xs).countQueries oracle ≤ xs.length ^ 2
```

> ## UpperBound and IsSort instances

`Cslib.Query.insertionSort_upperBound` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L97))

```lean
theorem insertionSort_upperBound :
    UpperBound (insertionSort (α := α)) List.length (· ^ 2)
```

`Cslib.Query.insertionSort_isSort` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean#L102))

```lean
theorem insertionSort_isSort : IsSort (insertionSort (α := α))
```

## Depends on

- [Upper and Lower Bounds for Query Complexity](../../bounds.md)
- [Insertion Sort as a Query Program](defs.md)
- [IsSort: Specification for Comparison Sorts](../issort.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Insertion/Lemmas.lean)
