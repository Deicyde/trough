---
declaration: theorem
origin: cited
lean: TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul
statement: formalized
proof: formalized
---

# Truncated Laplace transforms are entire

If `f` is interval integrable on `[a, b]`, then
`z ↦ ∫ t in a..b, f t * exp (-z t)` is complex differentiable everywhere.

```lean
TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul {f : ℝ → ℂ} {a b : ℝ}
  (hf : IntervalIntegrable f MeasureTheory.volume a b) :
  Differentiable ℂ fun z => ∫ (t : ℝ) in a..b, f t * Complex.exp (-z * ↑t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul)
- [Source of `TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul` in TauCeti/Analysis/Complex/LaplaceTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/LaplaceTransform.lean#L44)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
