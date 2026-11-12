---
catalog: module
lean: Cslib.Query.mergeSort_lowerBound, Cslib.Query.clog_factorial_le_mul_clog
statement: formalized
proof: formalized
---

# Merge Sort: Combined Bounds

`Cslib.Algorithms.Lean.Query.Sort.Merge.Bounds`, in [Cslib/Algorithms/Lean/Query/Sort/Merge/Bounds.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Bounds.lean), by Kim Morrison.

> Instantiating the general comparison-sorting lower bound at `mergeSort`, and comparing it
> with the `n * ⌈log₂ n⌉` upper bound. Since `LowerBound.le_upperBound` makes the two
> bounds meet, the purely arithmetic fact `⌈log₂ n!⌉ ≤ n * ⌈log₂ n⌉` falls out of the
> framework with no further work.

`Cslib.Query.mergeSort_lowerBound` (theorem, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Bounds.lean#L28))

> Merge sort has worst-case query complexity at least `⌈log₂(n!)⌉`.

```lean
theorem mergeSort_lowerBound [Infinite α] :
    LowerBound (mergeSort (α := α)) List.length (fun n => Nat.clog 2 (Nat.factorial n))
```

`Cslib.Query.clog_factorial_le_mul_clog` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Bounds.lean#L34))

> Sanity check that the bounds compose: comparing merge sort's upper and lower bounds
> yields this arithmetic fact with no further work.

```lean
theorem clog_factorial_le_mul_clog (n : ℕ) :
    Nat.clog 2 (Nat.factorial n) ≤ n * Nat.clog 2 n
```

## Depends on

- [Upper and Lower Bounds for Query Complexity](../../bounds.md)
- [Merge Sort as a Query Program](defs.md)

## Proof depends on

- [Comparison Sorting Lower Bound](../lowerbound.md)
- [Merge Sort: Correctness and Upper Bound](lemmas.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/Merge/Bounds.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/Merge/Bounds.lean)
