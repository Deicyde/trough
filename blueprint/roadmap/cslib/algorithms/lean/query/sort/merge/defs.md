---
catalog: module
lean: List.split, List.split_fst_length_eq, List.split_snd_length_eq, List.split_fst_append_split_snd, List.splitInTwo_fst, List.splitInTwo_snd, Cslib.Query.merge, Cslib.Query.mergeSort
statement: formalized
proof: formalized
---

# Merge Sort as a Query Program

`Cslib.Algorithms.Lean.Query.Sort.Merge.Defs`, in [Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean), by Kim Morrison, Shreyas Srinivas, Eric Wieser, Sorrachai Yingchareonthawornchai.

> Merge sort implemented as a `FreeM (LEQuery α)`, making all comparison queries explicit.
> The definitions mirror `List.merge` and `List.mergeSort` exactly: the list is split into
> contiguous halves and the merge prefers the left element on ties. Consequently evaluating
> the query program against any oracle produces literally the same list as `List.mergeSort`
> with the comparator induced by the oracle (`eval_mergeSort` in
> `Cslib.Algorithms.Lean.Query.Sort.Merge.Lemmas`); in particular the sort is stable.
> The recursive calls of `mergeSort` are not structural, since the two halves are not
> syntactic subterms, and are justified separately using their lengths.

`List.split` (definition, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L34))

> Split a list into contiguous halves; if the length is odd, the first half is one element
> longer. This agrees with `List.MergeSort.Internal.splitInTwo`, so that `mergeSort` agrees
> with `List.mergeSort`.

```lean
def split (xs : List α) : List α × List α
```

`List.split_fst_length_eq` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L37))

```lean
theorem split_fst_length_eq (xs : List α) :
    (split xs).1.length = (xs.length + 1) / 2
```

`List.split_snd_length_eq` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L42))

```lean
theorem split_snd_length_eq (xs : List α) :
    (split xs).2.length = xs.length / 2
```

`List.split_fst_append_split_snd` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L47))

```lean
theorem split_fst_append_split_snd (xs : List α) : (split xs).1 ++ (split xs).2 = xs
```

`List.splitInTwo_fst` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L52))

```lean
theorem splitInTwo_fst (xs : {l : List α // l.length = n}) :
    (List.MergeSort.Internal.splitInTwo xs).1 = xs.val.split.1
```

`List.splitInTwo_snd` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L56))

```lean
theorem splitInTwo_snd (xs : {l : List α // l.length = n}) :
    (List.MergeSort.Internal.splitInTwo xs).2 = xs.val.split.2
```

`Cslib.Query.merge` (abbreviation, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L65))

> Merge two sorted lists using comparison queries.

```lean
abbrev merge (xs ys : List α) : FreeM (LEQuery α) (List α)
```

`Cslib.Query.mergeSort` (abbreviation, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean#L69))

> Sort a list using merge sort with comparison queries.

```lean
abbrev mergeSort (xs : List α) : FreeM (LEQuery α) (List α)
```

## Depends on

- [LEQuery: Comparison Queries for Sorting](../lequery.md)
- [A Monadic version of the builtin `List.mergeSort`](../../../sort/merge.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Defs.lean)
