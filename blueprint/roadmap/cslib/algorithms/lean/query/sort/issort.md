---
catalog: module
lean: Cslib.Query.IsSort, Cslib.Query.IsSort.eval_eq
statement: formalized
proof: formalized
---

# IsSort: Specification for Comparison Sorts

`Cslib.Algorithms.Lean.Query.Sort.IsSort`, in [Cslib/Algorithms/Lean/Query/Sort/IsSort.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/IsSort.lean), by Kim Morrison, Shreyas Srinivas.

> `IsSort sort` asserts that `sort` is a correct comparison sort when viewed as a `FreeM`
> over `LEQuery α`. Correctness means: for any oracle, the result is a permutation of the
> input; and for any oracle implementing a total order, the result is sorted.

`Cslib.Query.IsSort` (structure, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/IsSort.lean#L26))

> A `FreeM`-based function is a correct comparison sort if it always produces a permutation
> of its input, and produces a sorted list when the oracle implements a total order.

```lean
structure IsSort (sort : List α → FreeM (LEQuery α) (List α)) : Prop where
  /-- The sort produces a permutation of its input, for any oracle. -/
  perm : ∀ (xs : List α) (oracle : {ι : Type} → LEQuery α ι → ι),
    ((sort xs).eval oracle).Perm xs
  /-- The sort produces a sorted list, when the oracle implements a total order. -/
  sorted : ∀ (xs : List α) (oracle : {ι : Type} → LEQuery α ι → ι)
    (r : α → α → Prop) [DecidableRel r] [Std.Total r] [IsTrans α r]
    (_ : ∀ a b, oracle (.le a b) = decide (r a b)),
    ((sort xs).eval oracle).Pairwise r
```

`Cslib.Query.IsSort.eval_eq` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/IsSort.lean#L38))

> `IsSort` determines the output: under an oracle implementing an antisymmetric total
> transitive relation, all correct comparison sorts produce the same list.

```lean
theorem IsSort.eval_eq {sort₁ sort₂ : List α → FreeM (LEQuery α) (List α)}
    (h₁ : IsSort sort₁) (h₂ : IsSort sort₂)
    (r : α → α → Prop) [DecidableRel r] [Std.Total r] [IsTrans α r] [Std.Antisymm r]
    (oracle : {ι : Type} → LEQuery α ι → ι)
    (horacle : ∀ a b, oracle (.le a b) = decide (r a b)) (xs : List α) :
    (sort₁ xs).eval oracle = (sort₂ xs).eval oracle
```

## Depends on

- [LEQuery: Comparison Queries for Sorting](lequery.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/IsSort.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/IsSort.lean)
