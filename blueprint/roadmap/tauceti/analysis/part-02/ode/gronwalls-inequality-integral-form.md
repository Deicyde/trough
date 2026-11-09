---
declaration: theorem
origin: cited
lean: TauCeti.le_mul_exp_of_le_add_mul_integral, TauCeti.mul_exp_integral_le_of_mul_le_deriv
statement: formalized
proof: formalized
---

# Grönwall's inequality, integral form

If `φ` is continuous on `[a, b]`, `0 ≤ K` and
`φ t ≤ c + K ∫ₐᵗ φ` for every `t ∈ [a, b]`, then `φ t ≤ c exp (K (t - a))` on `[a, b]`.

```lean
TauCeti.le_mul_exp_of_le_add_mul_integral {φ : ℝ → ℝ} {a b c K : ℝ}
  (hφ : ContinuousOn φ (Set.Icc a b)) (hK : 0 ≤ K)
  (h : ∀ t ∈ Set.Icc a b, φ t ≤ c + K * ∫ (s : ℝ) in a..t, φ s) (t : ℝ) :
  t ∈ Set.Icc a b → φ t ≤ c * Real.exp (K * (t - a))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.le_mul_exp_of_le_add_mul_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Gronwall.html#TauCeti.le_mul_exp_of_le_add_mul_integral).

## Other forms

**Grönwall's inequality for monotone functions, almost-everywhere form.** Formalized in Tau Ceti as [`TauCeti.mul_exp_integral_le_of_mul_le_deriv`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Gronwall.html#TauCeti.mul_exp_integral_le_of_mul_le_deriv).

```lean
TauCeti.mul_exp_integral_le_of_mul_le_deriv {g k : ℝ → ℝ} {s t : ℝ} (hst : s ≤ t)
  (hg : MonotoneOn g (Set.Icc s t)) (hgs : 0 ≤ g s)
  (hk : IntervalIntegrable k MeasureTheory.volume s t)
  (h : ∀ᵐ (σ : ℝ), σ ∈ Set.Ioo s t → k σ * g σ ≤ deriv g σ) :
  g s * Real.exp (∫ (σ : ℝ) in s..t, k σ) ≤ g t
```

## Sources

- [Tau Ceti documentation: `TauCeti.le_mul_exp_of_le_add_mul_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Gronwall.html#TauCeti.le_mul_exp_of_le_add_mul_integral)
- [Source of `TauCeti.le_mul_exp_of_le_add_mul_integral` in TauCeti/Analysis/ODE/Gronwall.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/ODE/Gronwall.lean#L65)
