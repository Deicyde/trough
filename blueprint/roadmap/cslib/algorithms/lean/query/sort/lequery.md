---
catalog: module
lean: Cslib.Query.LEQuery, Cslib.Query.LEQuery.ask, Cslib.Query.LEQuery.eval_ask, Cslib.Query.LEQuery.oracleOf, Cslib.Query.LEQuery.oracleOf_le, Cslib.Query.LEQuery.cardResponse_eq_two, Cslib.Query.LEQuery.cardResponse_le_two
statement: formalized
proof: formalized
---

# LEQuery: Comparison Queries for Sorting

`Cslib.Algorithms.Lean.Query.Sort.LEQuery`, in [Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean), by Sebastian Graf, Kim Morrison, Shreyas Srinivas.

> `LEQuery α` is the query type for comparison-based sorting algorithms.
> A query `LEQuery.le a b` asks whether `a ≤ b` and returns a `Bool`.

`Cslib.Query.LEQuery` (inductive type, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L23))

> Comparison query: asks whether `a ≤ b`, returning a `Bool`.

```lean
inductive LEQuery (α : Type) : Type → Type where
  | le (a b : α) : LEQuery α Bool
```

`Cslib.Query.LEQuery.ask` (abbreviation, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L27))

> Lift `LEQuery.le a b` into a `FreeM` that returns the comparison result.

```lean
abbrev LEQuery.ask (a b : α) : FreeM (LEQuery α) Bool
```

`Cslib.Query.LEQuery.eval_ask` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L30))

```lean
theorem LEQuery.eval_ask (oracle : {ι : Type} → LEQuery α ι → ι) (a b : α) :
    (LEQuery.ask a b).eval oracle = oracle (.le a b)
```

`Cslib.Query.LEQuery.oracleOf` (definition, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L34))

> Build an oracle for `LEQuery α` from a binary predicate `α → α → Bool`.

```lean
def LEQuery.oracleOf (f : α → α → Bool) : {ι : Type} → LEQuery α ι → ι
```

`Cslib.Query.LEQuery.oracleOf_le` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L37))

```lean
theorem LEQuery.oracleOf_le (f : α → α → Bool) (a b : α) :
    LEQuery.oracleOf f (.le a b) = f a b
```

`Cslib.Query.LEQuery.cardResponse_eq_two` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L41))

> Every `LEQuery α ι` has response type `ι = Bool`, of cardinality two.

```lean
theorem LEQuery.cardResponse_eq_two : ∀ {ι : Type}, LEQuery α ι → #ι = 2
```

`Cslib.Query.LEQuery.cardResponse_le_two` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean#L44))

```lean
theorem LEQuery.cardResponse_le_two {ι : Type} (op : LEQuery α ι) : #ι ≤ 2
```

## Depends on

- [FreeM: query/cost interpreters and lower-bound lemma](../freem.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Sort/LEQuery.lean)
