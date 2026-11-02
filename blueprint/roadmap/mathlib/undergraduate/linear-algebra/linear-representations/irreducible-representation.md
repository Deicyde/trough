---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Representation.IsIrreducible
mathlib_file: Mathlib/RepresentationTheory/Irreducible.lean
---

# Irreducible representation

A representation `ρ` is irreducible if it is non-trivial and has no proper non-trivial
subrepresentations.

```lean
Representation.IsIrreducible.{u_1, u_2, u_3} {G : Type u_1} {k : Type u_2} {V : Type u_3} [Monoid G]
  [Field k] [AddCommGroup V] [_root_.Module k V] (ρ : Representation k G V) : Prop
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Representation](../../../overview/general-algebra/representation-theory/representation.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Representation.IsIrreducible`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Irreducible.html#Representation.IsIrreducible)
- [Source of `Representation.IsIrreducible` in Mathlib/RepresentationTheory/Irreducible.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RepresentationTheory/Irreducible.lean#L27)
- [Mathlib undergraduate list: Linear algebra › Linear representations](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L69)
