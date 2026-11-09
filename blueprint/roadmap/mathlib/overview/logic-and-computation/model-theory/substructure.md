# Substructure

A substructure of a structure `M` is a set closed under application of function symbols.

```lean
FirstOrder.Language.Substructure.{u, v, w} (L : FirstOrder.Language) (M : Type w) [L.Structure M] :
  Type w
```

## Depends on

- [First-order structure](first-order-structure.md)

## Sources

- [Mathlib documentation: `FirstOrder.Language.Substructure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Substructures.html#FirstOrder.Language.Substructure)
- [Source of `FirstOrder.Language.Substructure` in Mathlib/ModelTheory/Substructures.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/ModelTheory/Substructures.lean#L96)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L639)
