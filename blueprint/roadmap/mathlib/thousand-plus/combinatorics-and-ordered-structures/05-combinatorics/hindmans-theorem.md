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

- [Stream](../../../overview/data-structures/list-like-structures/stream.md)

## Proof depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)

## Sources

- [Mathlib documentation: `Hindman.FP_partition_regular`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Hindman.html#Hindman.FP_partition_regular)
- [Source of `Hindman.FP_partition_regular` in Mathlib/Combinatorics/Hindman.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Hindman.lean#L190)
- [1000+ theorems list: Q1566341](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1767)
- [1000+ theorems project: Q1566341](https://1000-plus.github.io/all.html?length=-1#Q1566341)
- [Wikipedia: Hindman's theorem](https://en.wikipedia.org/wiki/Hindman's_theorem)
- [Wikidata: Q1566341](https://www.wikidata.org/wiki/Q1566341)
