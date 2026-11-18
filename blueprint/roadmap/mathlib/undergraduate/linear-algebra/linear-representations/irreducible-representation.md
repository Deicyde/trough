# Irreducible representation

A representation `ρ` is irreducible if it is non-trivial and has no proper non-trivial
subrepresentations.

```lean
Representation.IsIrreducible.{u_1, u_2, u_3} {G : Type u_1} {k : Type u_2} {V : Type u_3} [Monoid G]
  [Field k] [AddCommGroup V] [_root_.Module k V] (ρ : Representation k G V) : Prop
```

## Depends on

- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Representation](../../../overview/general-algebra/representation-theory/representation.md)

## Sources

- [Mathlib documentation: `Representation.IsIrreducible`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RepresentationTheory/Irreducible.html#Representation.IsIrreducible)
- [Source of `Representation.IsIrreducible` in Mathlib/RepresentationTheory/Irreducible.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/RepresentationTheory/Irreducible.lean#L26)
- [Mathlib undergraduate list: Linear algebra › Linear representations](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L69)
