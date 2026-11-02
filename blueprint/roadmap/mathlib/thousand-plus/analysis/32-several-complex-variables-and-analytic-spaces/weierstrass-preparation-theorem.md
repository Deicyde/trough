---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: PowerSeries.exists_isWeierstrassFactorization
mathlib_file: Mathlib/RingTheory/PowerSeries/WeierstrassPreparation.lean
---

# Weierstrass preparation theorem

**Weierstrass preparation theorem** ([washington_cyclotomic], Theorem 7.3):
let `g` be a power series over a complete local ring,
such that its image in the residue field is not zero. Then there exists a distinguished
polynomial `f` and a power series `h` which is a unit, such that `g = f * h`.

```lean
PowerSeries.exists_isWeierstrassFactorization.{u_1} {A : Type u_1} [CommRing A] [IsLocalRing A]
  [IsAdicComplete (IsLocalRing.maximalIdeal A) A] {g : PowerSeries A}
  (hg : (PowerSeries.map (IsLocalRing.residue A)) g ≠ 0) : ∃ f h, g.IsWeierstrassFactorization f h
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Power series](../../../overview/general-algebra/polynomials-and-power-series/power-series.md)
- [Quotient ring](../../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Proof depends on

- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `PowerSeries.exists_isWeierstrassFactorization`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/WeierstrassPreparation.html#PowerSeries.exists_isWeierstrassFactorization)
- [Source of `PowerSeries.exists_isWeierstrassFactorization` in Mathlib/RingTheory/PowerSeries/WeierstrassPreparation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/PowerSeries/WeierstrassPreparation.lean#L810)
- [1000+ theorems list: Q3527219](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2553)
- [1000+ theorems project: Q3527219](https://1000-plus.github.io/all.html?length=-1#Q3527219)
- [Wikipedia: Weierstrass preparation theorem](https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem)
- [Wikidata: Q3527219](https://www.wikidata.org/wiki/Q3527219)
