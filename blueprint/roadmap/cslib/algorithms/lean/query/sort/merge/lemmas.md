---
catalog: module
lean: Cslib.Query.eval_merge, Cslib.Query.eval_mergeSort, Cslib.Query.mergeSort_perm, Cslib.Query.mergeSort_sorted, Cslib.Query.countQueries_merge_nil_left, Cslib.Query.countQueries_merge_nil_right, Cslib.Query.countQueries_merge_cons_cons, Cslib.Query.countQueries_mergeSort_nil, Cslib.Query.countQueries_mergeSort_singleton, Cslib.Query.countQueries_mergeSort_cons_cons, Cslib.Query.merge_countQueries_le, Cslib.Query.mergeSort_countQueries_le, Cslib.Query.mergeSort_upperBound, Cslib.Query.mergeSort_isSort
statement: formalized
proof: formalized
---

# Merge Sort: Correctness and Upper Bound

`Cslib.Algorithms.Lean.Query.Sort.Merge.Lemmas`, in [Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean), by Kim Morrison, Shreyas Srinivas, Eric Wieser, Sorrachai Yingchareonthawornchai.

> Proofs that `mergeSort` is a correct comparison sort and uses at most `n * ⌈log₂ n⌉` queries.
>
> `eval_mergeSort` identifies the query program with `List.mergeSort`: evaluating against any
> oracle produces the same list as `List.mergeSort` with the comparator induced by the oracle.
> Correctness properties (permutation, sortedness) transfer directly from the `List.mergeSort`
> API. The query bound is proved by equational reasoning on `FreeM.countQueries`, which has no
> `List` counterpart.

> ## Evaluation

`Cslib.Query.eval_merge` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L39))

> Evaluating the query-based merge agrees with `List.merge` using the relation supplied
> by the oracle.

```lean
theorem eval_merge (oracle : {ι : Type} → LEQuery α ι → ι) (xs ys : List α) :
    (merge xs ys).eval oracle = xs.merge ys (fun a b => oracle (.le a b))
```

`Cslib.Query.eval_mergeSort` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L49))

> Evaluating query-based merge sort agrees with `List.mergeSort` using the relation
> supplied by the oracle.
>
> This is the essential correctness statement: it identifies the query program as *the*
> merge sort operation, so correctness properties (permutation, sortedness, stability)
> transfer directly from the `List.mergeSort` API rather than being restated here.

```lean
theorem eval_mergeSort (oracle : {ι : Type} → LEQuery α ι → ι) (xs : List α) :
    (mergeSort xs).eval oracle = xs.mergeSort (fun a b => oracle (.le a b))
```

> ## Correctness, transferred from the `List.mergeSort` API

`Cslib.Query.mergeSort_perm` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L55))

```lean
theorem mergeSort_perm (oracle : {ι : Type} → LEQuery α ι → ι) (xs : List α) :
    (mergeSort xs).eval oracle ~ xs
```

`Cslib.Query.mergeSort_sorted` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L60))

```lean
theorem mergeSort_sorted
    (r : α → α → Prop) [DecidableRel r] [Std.Total r] [IsTrans α r]
    (oracle : {ι : Type} → LEQuery α ι → ι)
    (horacle : ∀ a b, oracle (.le a b) = decide (r a b))
    (xs : List α) :
    ((mergeSort xs).eval oracle).Pairwise r
```

> ## Query count simp lemmas

`Cslib.Query.countQueries_merge_nil_left` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L77))

```lean
theorem countQueries_merge_nil_left (oracle : {ι : Type} → LEQuery α ι → ι) (ys : List α) :
    (merge ([] : List α) ys).countQueries oracle = 0
```

`Cslib.Query.countQueries_merge_nil_right` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L81))

```lean
theorem countQueries_merge_nil_right (oracle : {ι : Type} → LEQuery α ι → ι) (xs : List α) :
    (merge xs ([] : List α)).countQueries oracle = 0
```

`Cslib.Query.countQueries_merge_cons_cons` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L85))

```lean
theorem countQueries_merge_cons_cons (oracle : {ι : Type} → LEQuery α ι → ι)
    (x : α) (xs' : List α) (y : α) (ys' : List α) :
    (merge (x :: xs') (y :: ys')).countQueries oracle =
      1 + if oracle (.le x y)
      then (merge xs' (y :: ys')).countQueries oracle
      else (merge (x :: xs') ys').countQueries oracle
```

`Cslib.Query.countQueries_mergeSort_nil` (theorem, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L93))

```lean
theorem countQueries_mergeSort_nil (oracle : {ι : Type} → LEQuery α ι → ι) :
    (mergeSort (α := α) []).countQueries oracle = 0
```

`Cslib.Query.countQueries_mergeSort_singleton` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L97))

```lean
theorem countQueries_mergeSort_singleton (oracle : {ι : Type} → LEQuery α ι → ι) (x : α) :
    (mergeSort [x]).countQueries oracle = 0
```

`Cslib.Query.countQueries_mergeSort_cons_cons` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L102))

```lean
theorem countQueries_mergeSort_cons_cons (oracle : {ι : Type} → LEQuery α ι → ι)
    (x y : α) (zs : List α) :
    (mergeSort (x :: y :: zs)).countQueries oracle =
      (mergeSort (x :: y :: zs).split.1).countQueries oracle +
      ((mergeSort (x :: y :: zs).split.2).countQueries oracle +
       (merge ((x :: y :: zs).split.1.mergeSort fun a b => oracle (.le a b))
              ((x :: y :: zs).split.2.mergeSort fun a b => oracle (.le a b))).countQueries
         oracle)
```

> ## Query count proofs

`Cslib.Query.merge_countQueries_le` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L115))

```lean
theorem merge_countQueries_le (oracle : {ι : Type} → LEQuery α ι → ι)
    (xs ys : List α) :
    (merge xs ys).countQueries oracle ≤ xs.length + ys.length
```

`Cslib.Query.mergeSort_countQueries_le` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L145))

```lean
theorem mergeSort_countQueries_le (oracle : {ι : Type} → LEQuery α ι → ι)
    (xs : List α) :
    (mergeSort xs).countQueries oracle ≤ xs.length * Nat.clog 2 xs.length
```

> ## UpperBound and IsSort instances

`Cslib.Query.mergeSort_upperBound` (theorem, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L167))

```lean
theorem mergeSort_upperBound :
    UpperBound (mergeSort (α := α)) List.length (fun n => n * Nat.clog 2 n)
```

`Cslib.Query.mergeSort_isSort` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean#L173))

```lean
theorem mergeSort_isSort : IsSort (mergeSort (α := α))
```

## Depends on

- [Upper and Lower Bounds for Query Complexity](../../bounds.md)
- [IsSort: Specification for Comparison Sorts](../issort.md)
- [Merge Sort as a Query Program](defs.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Lemmas.lean)
