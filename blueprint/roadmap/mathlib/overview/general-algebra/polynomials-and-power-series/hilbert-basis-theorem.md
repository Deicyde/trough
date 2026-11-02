---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Polynomial.isNoetherianRing
mathlib_file: Mathlib/RingTheory/Polynomial/Basic.lean
---

# Hilbert basis theorem

**Hilbert basis theorem**: a polynomial ring over a Noetherian ring is a Noetherian ring.

```lean
Polynomial.isNoetherianRing.{u} {R : Type u} [CommRing R] [inst : IsNoetherianRing R] :
  IsNoetherianRing (Polynomial R)
```

## Depends on

- [Noetherian ring](../rings/noetherian-ring.md)
- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Ring](../rings/ring.md)

## Proof depends on

- [Characteristic zero](../field-theory/characteristic-zero.md)
- [Ideal of a commutative ring](../ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Polynomial.isNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Basic.html#Polynomial.isNoetherianRing)
- [Source of `Polynomial.isNoetherianRing` in Mathlib/RingTheory/Polynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/Basic.lean#L756)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L101)
- [1000+ theorems list: Q656645](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L695)
- [1000+ theorems project: Q656645](https://1000-plus.github.io/?length=-1#Q656645)
- [Wikipedia: Hilbert's basis theorem](https://en.wikipedia.org/wiki/Hilbert's_basis_theorem)
- [Wikidata: Q656645](https://www.wikidata.org/wiki/Q656645)
