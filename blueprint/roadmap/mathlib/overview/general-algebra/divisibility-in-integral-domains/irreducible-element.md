---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Irreducible
mathlib_file: Mathlib/Algebra/Group/Irreducible/Defs.lean
---

# Irreducible element

`Irreducible p` states that `p` is non-unit and only factors into units.

We explicitly avoid stating that `p` is non-zero, this would require a semiring. Assuming only a
monoid allows us to reuse irreducible for associated elements.

[Wikidata Q2989575](https://www.wikidata.org/wiki/Q2989575)

```lean
Irreducible.{u_1} {M : Type u_1} [Monoid M] (p : M) : Prop
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Irreducible`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Irreducible/Defs.html#Irreducible)
- [Source of `Irreducible` in Mathlib/Algebra/Group/Irreducible/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Irreducible/Defs.lean#L40)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L84)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L104)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L141)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L159)
