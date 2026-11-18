---
catalog: module
lean: Cslib.Algorithms.Lean.TimeM.ret_mergeM, Cslib.Algorithms.Lean.TimeM.ret_mergeSortM, Cslib.Algorithms.Lean.TimeM.merge, Cslib.Algorithms.Lean.TimeM.mergeSort, Cslib.Algorithms.Lean.TimeM.ret_merge, Cslib.Algorithms.Lean.TimeM.IsSorted, Cslib.Algorithms.Lean.TimeM.MinOfList, Cslib.Algorithms.Lean.TimeM.mem_either_merge, Cslib.Algorithms.Lean.TimeM.min_all_merge, Cslib.Algorithms.Lean.TimeM.sorted_merge, Cslib.Algorithms.Lean.TimeM.mergeSort_sorted, Cslib.Algorithms.Lean.TimeM.merge_perm, Cslib.Algorithms.Lean.TimeM.mergeSort_perm, Cslib.Algorithms.Lean.TimeM.mergeSort_correct, Cslib.Algorithms.Lean.TimeM.timeMergeSortRec, Cslib.Algorithms.Lean.TimeM.clog2_half_le, Cslib.Algorithms.Lean.TimeM.clog2_floor_half_le, Cslib.Algorithms.Lean.TimeM.T, Cslib.Algorithms.Lean.TimeM.timeMergeSortRec_le, Cslib.Algorithms.Lean.TimeM.merge_ret_length_eq_sum, Cslib.Algorithms.Lean.TimeM.mergeSort_same_length, Cslib.Algorithms.Lean.TimeM.merge_time, Cslib.Algorithms.Lean.TimeM.mergeSort_time_le, Cslib.Algorithms.Lean.TimeM.mergeSort_time
statement: formalized
proof: formalized
---

# MergeSort on a list

`Cslib.Algorithms.Lean.MergeSort.MergeSort`, in [Cslib/Algorithms/Lean/MergeSort/MergeSort.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean), by Sorrachai Yingchareonthawornhcai.

> In this file we introduce `merge` and `mergeSort` algorithms that returns a time monad
> over the list `TimeM ℕ (List α)`. The time complexity of `mergeSort` is the number of comparisons.
>
> --
> ## Main results
>
> - `mergeSort_correct`: `mergeSort` permutes the list into a sorted one.
> - `mergeSort_time`:  The number of comparisons of `mergeSort` is at most `n*⌈log₂ n⌉`.

`Cslib.Algorithms.Lean.TimeM.ret_mergeM` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L41))

> `TimeM.ret` passes through `List.mergeM` into the comparator.

```lean
theorem ret_mergeM {T} [AddMonoid T] (xs ys : List α) (le : α → α → TimeM T Bool) :
    ⟪List.mergeM xs ys le⟫ = List.merge xs ys (fun x y => ⟪le x y⟫)
```

`Cslib.Algorithms.Lean.TimeM.ret_mergeSortM` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L48))

> `TimeM.ret` passes through `List.mergeSortM` into the comparator.

```lean
theorem ret_mergeSortM {T} [AddMonoid T] (xs : List α) (le : α → α → TimeM T Bool) :
    ⟪List.mergeSortM xs le⟫ = List.mergeSort xs (fun x y => ⟪le x y⟫)
```

`Cslib.Algorithms.Lean.TimeM.merge` (abbreviation, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L56))

> Merges two lists into a single list, counting comparisons as time cost.
> Returns a `TimeM ℕ (List α)` where the time represents the number of comparisons performed.

```lean
abbrev merge (xs ys : List α) : TimeM ℕ (List α)
```

`Cslib.Algorithms.Lean.TimeM.mergeSort` (abbreviation, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L61))

> Sorts a list using the merge sort algorithm, counting comparisons as time cost.
> Returns a `TimeM ℕ (List α)` where the time represents the total number of comparisons.

```lean
abbrev mergeSort (xs : List α) : TimeM ℕ (List α)
```

`Cslib.Algorithms.Lean.TimeM.ret_merge` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L69))

> Our merge computes the one already in mathlib.

```lean
theorem ret_merge (xs ys : List α) : ⟪merge xs ys⟫ = xs.merge ys
```

`Cslib.Algorithms.Lean.TimeM.IsSorted` (abbreviation, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L73))

> A list is sorted if it satisfies the `Pairwise (· ≤ ·)` predicate.

```lean
abbrev IsSorted (l : List α) : Prop
```

`Cslib.Algorithms.Lean.TimeM.MinOfList` (abbreviation, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L76))

> `x` is a minimum element of list `l` if `x ≤ b` for all `b ∈ l`.

```lean
abbrev MinOfList (x : α) (l : List α) : Prop
```

`Cslib.Algorithms.Lean.TimeM.mem_either_merge` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L79))

```lean
theorem mem_either_merge (xs ys : List α) (z : α) (hz : z ∈ ⟪merge xs ys⟫) : z ∈ xs ∨ z ∈ ys
```

`Cslib.Algorithms.Lean.TimeM.min_all_merge` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L82))

```lean
theorem min_all_merge (x : α) (xs ys : List α) (hxs : MinOfList x xs) (hys : MinOfList x ys) :
    MinOfList x ⟪merge xs ys⟫
```

`Cslib.Algorithms.Lean.TimeM.sorted_merge` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L86))

```lean
theorem sorted_merge {l1 l2 : List α} (hxs : IsSorted l1) (hys : IsSorted l2) :
    IsSorted ⟪merge l1 l2⟫
```

`Cslib.Algorithms.Lean.TimeM.mergeSort_sorted` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L90))

```lean
theorem mergeSort_sorted (xs : List α) : IsSorted ⟪mergeSort xs⟫
```

`Cslib.Algorithms.Lean.TimeM.merge_perm` (lemma, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L93))

```lean
lemma merge_perm (l₁ l₂ : List α) : ⟪merge l₁ l₂⟫ ~ l₁ ++ l₂
```

`Cslib.Algorithms.Lean.TimeM.mergeSort_perm` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L96))

```lean
theorem mergeSort_perm (xs : List α) : ⟪mergeSort xs⟫ ~ xs
```

`Cslib.Algorithms.Lean.TimeM.mergeSort_correct` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L100))

> MergeSort is functionally correct.

```lean
theorem mergeSort_correct (xs : List α) : IsSorted ⟪mergeSort xs⟫ ∧ ⟪mergeSort xs⟫ ~ xs
```

`Cslib.Algorithms.Lean.TimeM.timeMergeSortRec` (definition, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L112))

> Recurrence relation for the time complexity of merge sort.
> For a list of length `n`, this counts the total number of comparisons:
> - Base cases: 0 comparisons for lists of length 0 or 1
> - Recursive case: split the list, sort both halves,
>   then merge (which takes at most `n` comparisons)

```lean
def timeMergeSortRec : ℕ → ℕ
```

`Cslib.Algorithms.Lean.TimeM.clog2_half_le` (lemma, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L121))

> Key Lemma: ⌈log2 ⌈n/2⌉⌉ ≤ ⌈log2 n⌉ - 1 for n > 1

```lean
lemma clog2_half_le (n : ℕ) (h : 1 < n) : clog 2 ((n + 1) / 2) ≤ clog 2 n - 1
```

`Cslib.Algorithms.Lean.TimeM.clog2_floor_half_le` (lemma, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L126))

> Same logic for the floor half: ⌈log2 ⌊n/2⌋⌉ ≤ ⌈log2 n⌉ - 1

```lean
lemma clog2_floor_half_le (n : ℕ) (h : 1 < n) : clog 2 (n / 2) ≤ clog 2 n - 1
```

`Cslib.Algorithms.Lean.TimeM.T` (abbreviation, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L149))

> Upper bound function for merge sort time complexity: `T(n) = n * ⌈log₂ n⌉`

```lean
abbrev T (n : ℕ) : ℕ
```

`Cslib.Algorithms.Lean.TimeM.timeMergeSortRec_le` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L152))

> Solve the recurrence

```lean
theorem timeMergeSortRec_le (n : ℕ) : timeMergeSortRec n ≤ T n
```

`Cslib.Algorithms.Lean.TimeM.merge_ret_length_eq_sum` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L161))

```lean
theorem merge_ret_length_eq_sum (xs ys : List α) :
    ⟪merge xs ys⟫.length = xs.length + ys.length
```

`Cslib.Algorithms.Lean.TimeM.mergeSort_same_length` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L165))

```lean
theorem mergeSort_same_length (xs : List α) :
    ⟪mergeSort xs⟫.length = xs.length
```

`Cslib.Algorithms.Lean.TimeM.merge_time` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L169))

```lean
theorem merge_time (xs ys : List α) : (merge xs ys).time ≤ xs.length + ys.length
```

`Cslib.Algorithms.Lean.TimeM.mergeSort_time_le` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L173))

```lean
theorem mergeSort_time_le (xs : List α) :
    (mergeSort xs).time ≤ timeMergeSortRec xs.length
```

`Cslib.Algorithms.Lean.TimeM.mergeSort_time` (theorem, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean#L187))

> Time complexity of mergeSort

```lean
theorem mergeSort_time (xs : List α) :
    let n := xs.length
    (mergeSort xs).time ≤ n * clog 2 n
```

## Depends on

- [A Monadic version of the builtin `List.mergeSort`](../sort/merge.md)
- [TimeM: Time Complexity Monad](../timem.md)

## Sources

- [Cslib/Algorithms/Lean/MergeSort/MergeSort.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/MergeSort/MergeSort.lean)
