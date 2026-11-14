---
catalog: module
lean: Cslib.Query.UpperBound, Cslib.Query.LowerBound, Cslib.Query.UpperBound.of_pointwise, Cslib.Query.LowerBound.le_upperBound
statement: formalized
proof: formalized
---

# Upper and Lower Bounds for Query Complexity

`Cslib.Algorithms.Lean.Query.Bounds`, in [Cslib/Algorithms/Lean/Query/Bounds.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Bounds.lean), by Sebastian Graf, Kim Morrison, Shreyas Srinivas.

> Definitions of upper and lower bounds on the number of queries a program makes,
> quantified over oracles.

`Cslib.Query.UpperBound` (definition, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Bounds.lean#L26))

> Upper bound: for all oracles, inputs of size ≤ n make at most `bound n` queries.

```lean
def UpperBound (prog : α → FreeM Q β)
    (size : α → Nat) (bound : Nat → Nat) : Prop
```

`Cslib.Query.LowerBound` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Bounds.lean#L33))

> Lower bound: for every size n, there exists an input of size at most n and an oracle
> making the program perform ≥ `bound n` queries.

```lean
def LowerBound (prog : α → FreeM Q β)
    (size : α → Nat) (bound : Nat → Nat) : Prop
```

`Cslib.Query.UpperBound.of_pointwise` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Bounds.lean#L40))

> To prove an `UpperBound` with a monotone bound function, it suffices to bound the
> query count of each input by `bound` at its own size.

```lean
theorem UpperBound.of_pointwise {prog : α → FreeM Q β} {size : α → Nat} {bound : Nat → Nat}
    (hmono : Monotone bound)
    (h : ∀ (oracle : {ι : Type u} → Q ι → ι) (x : α),
      (prog x).countQueries oracle ≤ bound (size x)) :
    UpperBound prog size bound
```

`Cslib.Query.LowerBound.le_upperBound` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Bounds.lean#L49))

> A lower bound for a program never exceeds an upper bound for the same program and
> size function.

```lean
theorem LowerBound.le_upperBound {prog : α → FreeM Q β} {size : α → Nat} {l u : Nat → Nat}
    (hl : LowerBound prog size l) (hu : UpperBound prog size u) (n : Nat) : l n ≤ u n
```

## Depends on

- [FreeM: query/cost interpreters and lower-bound lemma](freem.md)

## Sources

- [Cslib/Algorithms/Lean/Query/Bounds.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/Bounds.lean)
