---
declaration: theorem
origin: cited
lean: QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff
statement: formalized
proof: formalized
---

# Dedekind's criterion for a quadratic order

Let `r` be a root of `X² - b X - a` modulo
`p`, so that `b - r` is the second root. Then `p` factors as `(p) = (p, ω - r) (p, ω - (b - r))`
in `ℤ[ω]` if and only if `p` does not divide both the derivative `2r - b` and the quotient
`(r² - b r - a)/p`, that is, unless `p ∣ 2r - b` and `p² ∣ r² - b r - a`.

```lean
QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff {a b : ℤ} {p : ℕ} {r : ℤ}
  [Fact (Nat.Prime p)] (hr : ↑p ∣ r ^ 2 - b * r - a) :
  Ideal.span {↑p, QuadraticAlgebra.omega - ↑r} *
        Ideal.span {↑p, QuadraticAlgebra.omega - ↑(b - r)} =
      Ideal.span {↑p} ↔
    ¬(↑p ∣ 2 * r - b ∧ ↑p ^ 2 ∣ r ^ 2 - b * r - a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticOrder/PrimeIdeal.html#QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff).

## Sources

- [Tau Ceti documentation: `QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticOrder/PrimeIdeal.html#QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff)
- [Source of `QuadraticAlgebra.span_natCast_omega_sub_mul_span_natCast_omega_sub_eq_iff` in TauCeti/NumberTheory/QuadraticOrder/PrimeIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticOrder/PrimeIdeal.lean#L282)
