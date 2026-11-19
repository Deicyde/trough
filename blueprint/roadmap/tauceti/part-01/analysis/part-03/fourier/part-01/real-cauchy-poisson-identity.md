---
declaration: theorem
origin: cited
lean: TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div
statement: formalized
proof: formalized
---

# Real Cauchy Poisson identity

For `y > 0`, the sum over integers of
`exp (-2π y |n|)` equals the sum of `y / (π (y² + n²))`.

```lean
TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div {y : ℝ} (hy : 0 < y) :
  ∑' (n : ℤ), Real.exp (-(2 * Real.pi * y * |↑n|)) = ∑' (n : ℤ), y / (Real.pi * (y ^ 2 + ↑n ^ 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Poisson/CauchyLattice.html#TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Poisson/CauchyLattice.html#TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div)
- [Source of `TauCeti.tsum_exp_neg_mul_abs_int_eq_tsum_div` in TauCeti/Analysis/Fourier/Poisson/CauchyLattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Poisson/CauchyLattice.lean#L86)
