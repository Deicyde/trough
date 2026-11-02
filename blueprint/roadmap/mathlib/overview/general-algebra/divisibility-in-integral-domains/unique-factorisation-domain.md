---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: UniqueFactorizationMonoid
mathlib_file: Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean
---

# Unique factorisation domain

Unique factorization monoids are defined as cancellative `CommMonoidWithZero`s with well-founded
strict divisibility relations, but this is equivalent to more familiar definitions:

Each element (except zero) is uniquely represented as a multiset of irreducible factors.
Uniqueness is only up to associated elements.

Each element (except zero) is non-uniquely represented as a multiset
of prime factors.

To define a UFD using the definition in terms of multisets
of irreducible factors, use the definition `of_existsUnique_irreducible_factors`

To define a UFD using the definition in terms of multisets
of prime factors, use the definition `of_exists_prime_factors`

```lean
UniqueFactorizationMonoid.{u_2} (α : Type u_2) [CommMonoidWithZero α] : Prop
```

## Depends on

- [Irreducible element](irreducible-element.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Sources

- [Mathlib documentation: `UniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid)
- [Source of `UniqueFactorizationMonoid` in Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean#L113)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L86)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L144)
