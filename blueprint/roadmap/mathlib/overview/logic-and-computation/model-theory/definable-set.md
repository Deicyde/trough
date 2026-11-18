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
- [Source of `Set.Definable` in Mathlib/ModelTheory/Definability.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/ModelTheory/Definability.lean#L51)
- [Mathlib overview: Logic and computation › Model theory](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L640)
