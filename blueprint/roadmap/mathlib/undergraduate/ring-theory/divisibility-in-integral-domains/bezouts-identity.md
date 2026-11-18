# Bézout's identity

**Bézout's lemma**

```lean
exists_gcd_eq_mul_add_mul.{u} {R : Type u} [CommRing R] [IsBezout R] [IsDomain R] [GCDMonoid R]
  (a b : R) : ∃ x y, gcd a b = a * x + b * y
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Principal ideal domain](../../../overview/general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)

## Proof depends on

- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Sum of subspaces](../../linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `exists_gcd_eq_mul_add_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#exists_gcd_eq_mul_add_mul)
- [Source of `exists_gcd_eq_mul_add_mul` in Mathlib/RingTheory/PrincipalIdealDomain.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/RingTheory/PrincipalIdealDomain.lean#L472)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L154)
