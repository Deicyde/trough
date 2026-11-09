# The Solution of the General Quartic Equation

**The Solution of Quartic**.
The roots of a quartic polynomial when `q` is nonzero. See [Zwillinger](https://leanprover-community.github.io/mathlib4_docs/references.html#ref_zwillinger2003).
Here, `u` needs to satisfy the cubic resolvent. An explicit expression of `u` is possible using
the cubic formula, but would be too long.

```lean
Theorems100.quartic_eq_zero_iff.{u_1} {K : Type u_1} [Field K] (a b c d e : K) {p q r s u v w : K}
  [Invertible 2] (ha : a ≠ 0) (hp : p = (8 * a * c - 3 * b ^ 2) / (8 * a ^ 2))
  (hq : q = (b ^ 3 - 4 * a * b * c + 8 * a ^ 2 * d) / (8 * a ^ 3)) (hq_nonzero : q ≠ 0)
  (hr : r = (16 * a * b ^ 2 * c + 256 * a ^ 3 * e - 3 * b ^ 4 - 64 * a ^ 2 * b * d) / (256 * a ^ 4))
  (hu : u ^ 3 - p * u ^ 2 - 4 * r * u + 4 * p * r - q ^ 2 = 0) (hs : s ^ 2 = u - p)
  (hv : v ^ 2 = 4 * s ^ 2 - 8 * (u - q / s)) (hw : w ^ 2 = 4 * s ^ 2 - 8 * (u + q / s)) (x : K) :
  a * x ^ 4 + b * x ^ 3 + c * x ^ 2 + d * x + e = 0 ↔
    x = (-2 * s - v) / 4 - b / (4 * a) ∨
      x = (-2 * s + v) / 4 - b / (4 * a) ∨
        x = (2 * s - w) / 4 - b / (4 * a) ∨ x = (2 * s + w) / 4 - b / (4 * a)
```

## Depends on

- [Field](../../overview/general-algebra/field-theory/field.md)
- [Invertible elements](../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Rational number](../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [List](../../overview/data-structures/list-like-structures/list.md)
- [Local ring](../../overview/general-algebra/rings/local-ring.md)

## Sources

- [Mathlib documentation: `Theorems100.quartic_eq_zero_iff`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.html#Theorems100.quartic_eq_zero_iff)
- [Source of `Theorems100.quartic_eq_zero_iff` in Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Archive/Wiedijk100Theorems/SolutionOfCubicQuartic.lean#L194)
- [Freek Wiedijk's 100 theorems, no. 46](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L243)
- [1000+ theorems list: Q476776](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L489)
- [1000+ theorems project: Q476776](https://1000-plus.github.io/all.html?length=-1#Q476776)
- [Wikipedia: Quartic equation](https://en.wikipedia.org/wiki/Quartic_equation)
- [Wikidata: Q476776](https://www.wikidata.org/wiki/Q476776)
