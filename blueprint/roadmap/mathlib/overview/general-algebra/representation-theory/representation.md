---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Representation
mathlib_file: Mathlib/RepresentationTheory/Basic.lean
---

# Representation

A representation of `G` on the `k`-module `V` is a homomorphism `G →* (V →ₗ[k] V)`.

```lean
Representation.{u_1, u_2, u_3} (k : Type u_1) (G : Type u_2) (V : Type u_3) [Semiring k] [Monoid G]
  [AddCommMonoid V] [_root_.Module k V] : Type (max u_2 u_3)
```

## Depends on

- [Linear map](../../linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `Representation`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Basic.html#Representation)
- [Source of `Representation` in Mathlib/RepresentationTheory/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/Basic.lean#L46)
- [Mathlib overview: General algebra › Representation theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L162)
