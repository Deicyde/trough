---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Polynomial.normalizedGcdMonoid
mathlib_file: Mathlib/RingTheory/Polynomial/Content.lean
---

# $A[X]$ has gcd and lcm if $A$ does

Mathlib states this as `Polynomial.normalizedGcdMonoid`.

```lean
Polynomial.normalizedGcdMonoid.{u_1} {R : Type u_1} [CommRing R] [NormalizedGCDMonoid R] :
  NormalizedGCDMonoid (Polynomial R)
```

## Depends on

- [Greatest common divisor](../divisibility-in-integral-domains/greatest-common-divisor.md)
- [Least common multiple](../divisibility-in-integral-domains/least-common-multiple.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `Polynomial.normalizedGcdMonoid`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Content.html#Polynomial.normalizedGcdMonoid)
- [Source of `Polynomial.normalizedGcdMonoid` in Mathlib/RingTheory/Polynomial/Content.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/Content.lean#L457)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L102)
