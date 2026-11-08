---
declaration: theorem
origin: cited
lean: TauCeti.integral_exp_neg_mul_sin_lt
statement: formalized
proof: formalized
---

# Jordan's integral bound

For `c > 0`, `∫₀^π e^{-c sin θ} dθ < π / c`.

```lean
TauCeti.integral_exp_neg_mul_sin_lt (c : ℝ) (hc : 0 < c) :
  ∫ (θ : ℝ) in 0..Real.pi, Real.exp (-c * Real.sin θ) < Real.pi / c
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_exp_neg_mul_sin_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JordanIntegral.html#TauCeti.integral_exp_neg_mul_sin_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_exp_neg_mul_sin_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/JordanIntegral.html#TauCeti.integral_exp_neg_mul_sin_lt)
- [Source of `TauCeti.integral_exp_neg_mul_sin_lt` in TauCeti/Analysis/SpecialFunctions/JordanIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/JordanIntegral.lean#L65)
