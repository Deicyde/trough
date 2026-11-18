# Descartes Rule of Signs

**Descartes' Rule of Signs**: the number of positive roots is at most the number of sign
variations.

```lean
Polynomial.roots_countP_pos_le_signVariations.{u_1} {R : Type u_1} [CommRing R] [LinearOrder R]
  [IsStrictOrderedRing R] (P : Polynomial R) :
  Multiset.countP (fun x => 0 < x) P.roots ≤ P.signVariations
```

## Depends on

- [Roots of a polynomial](../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)

## Proof depends on

- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Polynomial.roots_countP_pos_le_signVariations`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/RuleOfSigns.html#Polynomial.roots_countP_pos_le_signVariations)
- [Source of `Polynomial.roots_countP_pos_le_signVariations` in Mathlib/Algebra/Polynomial/RuleOfSigns.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Algebra/Polynomial/RuleOfSigns.lean#L343)
- [Freek Wiedijk's 100 theorems, no. 100](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L517)
- [Outside Mathlib: github](https://github.com/Timeroot/lean-descartes-signs/)
