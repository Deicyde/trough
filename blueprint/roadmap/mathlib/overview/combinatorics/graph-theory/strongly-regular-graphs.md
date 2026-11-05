---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: SimpleGraph.IsSRGWith
mathlib_file: Mathlib/Combinatorics/SimpleGraph/StronglyRegular.lean
---

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
- [Source of `SimpleGraph.IsSRGWith` in Mathlib/Combinatorics/SimpleGraph/StronglyRegular.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SimpleGraph/StronglyRegular.lean#L45)
- [Mathlib overview: Combinatorics › Graph theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L527)
