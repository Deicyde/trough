---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: FirstOrder.Language.Substructure
mathlib_file: Mathlib/ModelTheory/Substructures.lean
---

# Substructure

A substructure of a structure `M` is a set closed under application of function symbols.

```lean
FirstOrder.Language.Substructure.{u, v, w} (L : FirstOrder.Language) (M : Type w) [L.Structure M] :
  Type w
```

## Depends on

- [First-order structure](first-order-structure.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Substructure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Substructures.html#FirstOrder.Language.Substructure)
- [Source of `FirstOrder.Language.Substructure` in Mathlib/ModelTheory/Substructures.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/ModelTheory/Substructures.lean#L96)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L639)
