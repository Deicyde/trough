---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.cubic_eq_zero_iff
mathlib_file: Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.lean
---

# The Solution of a Cubic

**The Solution of Cubic**.
The roots of a cubic polynomial whose discriminant is nonzero.

```lean
Theorems100.cubic_eq_zero_iff.{u_1} {K : Type u_1} [Field K] (a b c d : K) {ω p q r s t : K}
  [Invertible 2] [Invertible 3] (ha : a ≠ 0) (hω : IsPrimitiveRoot ω 3)
  (hp : p = (3 * a * c - b ^ 2) / (9 * a ^ 2)) (hp_nonzero : p ≠ 0)
  (hq : q = (9 * a * b * c - 2 * b ^ 3 - 27 * a ^ 2 * d) / (54 * a ^ 3))
  (hr : r ^ 2 = q ^ 2 + p ^ 3) (hs3 : s ^ 3 = q + r) (ht : t * s = p) (x : K) :
  a * x ^ 3 + b * x ^ 2 + c * x + d = 0 ↔
    x = s - t - b / (3 * a) ∨
      x = s * ω - t * ω ^ 2 - b / (3 * a) ∨ x = s * ω ^ 2 - t * ω - b / (3 * a)
```

## Depends on

- [Field](../../overview/general-algebra/field-theory/field.md)
- [Invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Rational number](../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Cyclotomic polynomials in $\Q\[X\]$](../../undergraduate/ring-theory/polynomial-rings/cyclotomic-polynomials-in-q-x.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Local ring](../../overview/general-algebra/rings/local-ring.md)

## Sources

- [Mathlib documentation: `Theorems100.cubic_eq_zero_iff`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.html#Theorems100.cubic_eq_zero_iff)
- [Source of `Theorems100.cubic_eq_zero_iff` in Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.lean#L108)
- [Freek Wiedijk's 100 theorems, no. 37](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L195)
- [1000+ theorems list: Q203565](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L200)
- [1000+ theorems project: Q203565](https://1000-plus.github.io/all.html?length=-1#Q203565)
- [Wikipedia: Cubic equation](https://en.wikipedia.org/wiki/Cubic_equation)
- [Wikidata: Q203565](https://www.wikidata.org/wiki/Q203565)
