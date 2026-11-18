# Strongly regular graphs

A graph is strongly regular with parameters `n k ℓ μ` if
* its vertex set has cardinality `n`
* it is regular with degree `k`
* every pair of adjacent vertices has `ℓ` common neighbors
* every pair of nonadjacent vertices has `μ` common neighbors

```lean
SimpleGraph.IsSRGWith.{u} {V : Type u} [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj]
  (n k ℓ μ : ℕ) : Prop
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Simple graph](simple-graph.md)

## Sources

- [Mathlib documentation: `SimpleGraph.IsSRGWith`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/StronglyRegular.html#SimpleGraph.IsSRGWith)
- [Source of `SimpleGraph.IsSRGWith` in Mathlib/Combinatorics/SimpleGraph/StronglyRegular.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/SimpleGraph/StronglyRegular.lean#L45)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L527)
