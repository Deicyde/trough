---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: char_dvd_card_solutions
mathlib_file: Mathlib/FieldTheory/ChevalleyWarning.lean
---

# Chevalley-Warning theorem (Number theory)

The **Chevalley–Warning theorem**, unary version.
Let `f` be a multivariate polynomial in finitely many variables (`X s`, `s : σ`)
over a finite field of characteristic `p`.
Assume that the total degree of `f` is less than the cardinality of `σ`.
Then the number of solutions of `f` is divisible by `p`.
See `char_dvd_card_solutions_of_sum_lt` for a version that takes a family of polynomials `f i`.

```lean
char_dvd_card_solutions.{u_1, u_2} {K : Type u_1} {σ : Type u_2} [Fintype K] [Field K] [Fintype σ]
  [DecidableEq σ] [DecidableEq K] (p : ℕ) [CharP K p] {f : MvPolynomial σ K}
  (h : f.totalDegree < Fintype.card σ) : p ∣ Fintype.card { x // (MvPolynomial.eval x) f = 0 }
```

## Depends on

- [Characteristic p](../field-theory/characteristic-p.md)
- [Field](../field-theory/field.md)
- [Polynomial in several indeterminates](../polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Rational number](../numbers/rational-number.md)
- [Ring morphism](../rings/ring-morphism.md)

## Proof depends on

- [Chevalley–Warning theorem (1000+ theorems)](../../../thousand-plus/algebra/12-field-theory-and-polynomials/chevalley-warning-theorem.md)

## Sources

- [Mathlib documentation: `char_dvd_card_solutions`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/ChevalleyWarning.html#char_dvd_card_solutions)
- [Source of `char_dvd_card_solutions` in Mathlib/FieldTheory/ChevalleyWarning.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/ChevalleyWarning.lean#L173)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L149)
