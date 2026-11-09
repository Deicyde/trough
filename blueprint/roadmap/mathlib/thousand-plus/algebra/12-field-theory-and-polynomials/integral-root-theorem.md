# Integral root theorem

**Integral root theorem**:
if `r : f.codomain` is a root of a monic polynomial over the ufd `A`,
then `r` is an integer

```lean
isInteger_of_is_root_of_monic.{u_1, u_2} {A : Type u_1} {K : Type u_2} [CommRing A] [IsDomain A]
  [UniqueFactorizationMonoid A] [Field K] [Algebra A K] [IsFractionRing A K] {p : Polynomial A}
  (hp : p.Monic) {r : K} (hr : (Polynomial.aeval r) p = 0) : IsLocalization.IsInteger A r
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field of fractions of an integral domain](../../../overview/general-algebra/field-theory/field-of-fractions-of-an-integral-domain.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)
- [Unique factorisation domain](../../../overview/general-algebra/divisibility-in-integral-domains/unique-factorisation-domain.md)

## Proof depends on

- [Rational root theorem](rational-root-theorem.md)

## Sources

- [Mathlib documentation: `isInteger_of_is_root_of_monic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/RationalRoot.html#isInteger_of_is_root_of_monic)
- [Source of `isInteger_of_is_root_of_monic` in Mathlib/RingTheory/Polynomial/RationalRoot.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Polynomial/RationalRoot.lean#L111)
- [1000+ theorems list: Q180345X](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L98)
- [1000+ theorems project: Q180345X](https://1000-plus.github.io/all.html?length=-1#Q180345)
- [Wikipedia: Integral root theorem](https://en.wikipedia.org/wiki/Integral_root_theorem)
- [Wikidata: Q180345](https://www.wikidata.org/wiki/Q180345)
