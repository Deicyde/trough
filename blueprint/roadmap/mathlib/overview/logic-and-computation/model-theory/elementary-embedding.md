---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: FirstOrder.Language.ElementaryEmbedding
mathlib_file: Mathlib/ModelTheory/ElementaryMaps.lean
---

# Elementary embedding

An elementary embedding of first-order structures is an embedding that commutes with the
realizations of formulas.

```lean
FirstOrder.Language.ElementaryEmbedding.{u_1, u_2, u_5, u_6} (L : FirstOrder.Language)
  (M : Type u_1) (N : Type u_2) [L.Structure M] [L.Structure N] : Type (max u_1 u_2)
```

## Depends on

- [First-order formula](first-order-formula.md)
- [First-order structure](first-order-structure.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.ElementaryEmbedding`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/ElementaryMaps.html#FirstOrder.Language.ElementaryEmbedding)
- [Source of `FirstOrder.Language.ElementaryEmbedding` in Mathlib/ModelTheory/ElementaryMaps.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/ModelTheory/ElementaryMaps.lean#L42)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L641)
