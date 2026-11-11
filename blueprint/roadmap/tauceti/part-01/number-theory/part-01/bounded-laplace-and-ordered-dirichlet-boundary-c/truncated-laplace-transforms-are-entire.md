---
declaration: theorem
origin: cited
lean: TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul
statement: formalized
proof: formalized
---

# Truncated Laplace transforms are entire

The function
`z ↦ ∫ t in a..b, f t * exp (-z t)` is complex differentiable everywhere. If `f` is not
interval integrable on `[a, b]`, it is identically `0`.

```lean
TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul {f : ℝ → ℂ} {a b : ℝ} :
  Differentiable ℂ fun z => ∫ (t : ℝ) in a..b, f t * Complex.exp (-z * ↑t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul)
- [Source of `TauCeti.differentiable_intervalIntegral_mul_cexp_neg_mul` in TauCeti/Analysis/Complex/LaplaceTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/LaplaceTransform.lean#L61)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
