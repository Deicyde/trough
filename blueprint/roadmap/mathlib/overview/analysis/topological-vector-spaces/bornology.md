---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Bornology
mathlib_file: Mathlib/Topology/Bornology/Basic.lean
---

# Bornology

A **bornology** on a type `α` is a filter of cobounded sets which contains the cofinite filter.
Such spaces are equivalently specified by their bounded sets, see `Bornology.ofBounded`
and `Bornology.ext_iff_isBounded`

```lean
Bornology.{u_4} (α : Type u_4) : Type u_4
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Filter](../../topology/general-topology/part-01/filter.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Bornology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Bornology/Basic.html#Bornology)
- [Source of `Bornology` in Mathlib/Topology/Bornology/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Bornology/Basic.lean#L48)
- [Mathlib overview: Analysis › Topological vector spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L275)
