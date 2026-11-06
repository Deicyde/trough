# Definable set

A subset of a finite Cartesian product of a structure is definable over a set `A` when
membership in the set is given by a first-order formula with parameters from `A`.

```lean
Set.Definable.{u, v, w, u₁} {M : Type w} (A : Set M) (L : FirstOrder.Language) [L.Structure M]
  {α : Type u₁} (s : Set (α → M)) : Prop
```

## Depends on

- [First-order formula](first-order-formula.md)
- [First-order structure](first-order-structure.md)

## Sources

- [Mathlib documentation: `Set.Definable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/Definability.html#Set.Definable)
- [Source of `Set.Definable` in Mathlib/ModelTheory/Definability.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/ModelTheory/Definability.lean#L52)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L640)
