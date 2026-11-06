---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: DistribLattice.prime_ideal_of_disjoint_filter_ideal
mathlib_file: Mathlib/Order/PrimeSeparator.lean
---

# Boolean prime ideal theorem

Mathlib states this as `DistribLattice.prime_ideal_of_disjoint_filter_ideal`.

```lean
DistribLattice.prime_ideal_of_disjoint_filter_ideal.{u_1} {α : Type u_1} [DistribLattice α]
  {F : Order.PFilter α} {I : Order.Ideal α} (hFI : Disjoint ↑F ↑I) :
  ∃ J, J.IsPrime ∧ I ≤ J ∧ Disjoint ↑F ↑J
```

This is the prime ideal separation theorem for (bounded) distributive lattices, of which the Boolean prime ideal theorem is a special case.

## Depends on

- [Set](../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `DistribLattice.prime_ideal_of_disjoint_filter_ideal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/PrimeSeparator.html#DistribLattice.prime_ideal_of_disjoint_filter_ideal)
- [Source of `DistribLattice.prime_ideal_of_disjoint_filter_ideal` in Mathlib/Order/PrimeSeparator.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Order/PrimeSeparator.lean#L46)
- [1000+ theorems list: Q872088](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1025)
- [1000+ theorems project: Q872088](https://1000-plus.github.io/all.html?length=-1#Q872088)
- [Wikipedia: Boolean prime ideal theorem](https://en.wikipedia.org/wiki/Boolean_prime_ideal_theorem)
- [Wikidata: Q872088](https://www.wikidata.org/wiki/Q872088)
