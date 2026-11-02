---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Hindman.FP_partition_regular
mathlib_file: Mathlib/Combinatorics/Hindman.lean
---

# Hindman's theorem (1000+ theorems)

The strong form of **Hindman's theorem**: in any finite cover of an FP-set, one the parts
contains an FP-set.

```lean
Hindman.FP_partition_regular.{u_1} {M : Type u_1} [Semigroup M] (a : Stream' M) (s : Set (Set M))
  (sfin : s.Finite) (scov : ∀ (m : M), Hindman.FP a m → m ∈ ⋃₀ s) :
  ∃ c ∈ s, ∃ b, ∀ (m : M), Hindman.FP b m → m ∈ c
```

## Depends on

- [Array](../../../../overview/data-structures/list-like-structures/array.md)
- [Set](../../../../overview/data-structures/sets/set.md)
- [Stream](../../../../overview/data-structures/list-like-structures/stream.md)

## Proof depends on

- [Closed map](../../../../overview/topology/general-topology/part-01/closed-map.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous function](../../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Finite set](../../../../overview/data-structures/sets/finite-set.md)
- [Hausdorff space](../../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Integer](../../../../overview/general-algebra/numbers/integer.md)
- [Limit of a map with respect to filters](../../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)

## Sources

- [Mathlib documentation: `Hindman.FP_partition_regular`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Hindman.html#Hindman.FP_partition_regular)
- [Source of `Hindman.FP_partition_regular` in Mathlib/Combinatorics/Hindman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Hindman.lean#L190)
- [1000+ theorems list: Q1566341](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1767)
- [1000+ theorems project: Q1566341](https://1000-plus.github.io/?length=-1#Q1566341)
- [Wikipedia: Hindman's theorem](https://en.wikipedia.org/wiki/Hindman's_theorem)
- [Wikidata: Q1566341](https://www.wikidata.org/wiki/Q1566341)
