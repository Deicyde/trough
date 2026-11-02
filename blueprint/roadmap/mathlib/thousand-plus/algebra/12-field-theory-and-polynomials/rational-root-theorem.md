---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: num_dvd_of_is_root, den_dvd_of_is_root
mathlib_file: Mathlib/RingTheory/Polynomial/RationalRoot.lean
---

# Rational root theorem

Mathlib records this with 2 declarations.

`num_dvd_of_is_root`: **Rational root theorem** part 1:
if `r : f.codomain` is a root of a polynomial over the ufd `A`,
then the numerator of `r` divides the constant coefficient

```lean
num_dvd_of_is_root.{u_1, u_2} {A : Type u_1} {K : Type u_2} [CommRing A] [IsDomain A]
  [UniqueFactorizationMonoid A] [Field K] [Algebra A K] [IsFractionRing A K] {p : Polynomial A}
  {r : K} (hr : (Polynomial.aeval r) p = 0) : IsFractionRing.num A r ∣ p.coeff 0
```

`den_dvd_of_is_root`: Rational root theorem part 2:
if `r : f.codomain` is a root of a polynomial over the ufd `A`,
then the denominator of `r` divides the leading coefficient

```lean
den_dvd_of_is_root.{u_1, u_2} {A : Type u_1} {K : Type u_2} [CommRing A] [IsDomain A]
  [UniqueFactorizationMonoid A] [Field K] [Algebra A K] [IsFractionRing A K] {p : Polynomial A}
  {r : K} (hr : (Polynomial.aeval r) p = 0) : ↑(IsFractionRing.den A r) ∣ p.leadingCoeff
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Field of fractions of an integral domain](../../../overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)

## Proof depends on

- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)

## Sources

- [Mathlib documentation: `num_dvd_of_is_root`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/RationalRoot.html#num_dvd_of_is_root)
- [Source of `num_dvd_of_is_root` in Mathlib/RingTheory/Polynomial/RationalRoot.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/RationalRoot.lean#L65)
- [Mathlib documentation: `den_dvd_of_is_root`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/RationalRoot.html#den_dvd_of_is_root)
- [Source of `den_dvd_of_is_root` in Mathlib/RingTheory/Polynomial/RationalRoot.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Polynomial/RationalRoot.lean#L85)
- [1000+ theorems list: Q180345](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L102)
- [1000+ theorems project: Q180345](https://1000-plus.github.io/?length=-1#Q180345)
- [Wikipedia: Rational root theorem](https://en.wikipedia.org/wiki/Rational_root_theorem)
- [Wikidata: Q180345](https://www.wikidata.org/wiki/Q180345)
