---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Hindman.FS_partition_regular
mathlib_file: Mathlib/Combinatorics/Hindman.lean
---

# Hindman's theorem

The strong form of **Hindman's theorem**: in any finite
cover of an FS-set, one the parts contains an FS-set.

```lean
Hindman.FS_partition_regular.{u_1} {M : Type u_1} [AddSemigroup M] (a : Stream' M) (s : Set (Set M))
  (sfin : s.Finite) (scov : ∀ (m : M), Hindman.FS a m → m ∈ ⋃₀ s) :
  ∃ c ∈ s, ∃ b, ∀ (m : M), Hindman.FS b m → m ∈ c
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Set](../../data-structures/sets/set.md)
- [Stream](../../data-structures/list-like-structures/stream.md)

## Proof depends on

- [Closed map](../../topology/general-topology/part-01/closed-map.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous function](../../topology/general-topology/part-01/continuous-function.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Limit point](../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)

## Sources

- [Mathlib documentation: `Hindman.FS_partition_regular`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Hindman.html#Hindman.FS_partition_regular)
- [Source of `Hindman.FS_partition_regular` in Mathlib/Combinatorics/Hindman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Hindman.lean#L192)
- [Mathlib overview: Combinatorics › Ramsey theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L536)
