---
declaration: theorem
origin: cited
lean: TauCeti.differentiableOn_integral_mul_cexp_neg_mul
statement: formalized
proof: formalized
---

# Holomorphy of the Laplace transform

If `f` is bounded on `[0, ∞)`, its Laplace transform
`z ↦ ∫ t in Ici 0, f t * exp (-z t)` is complex differentiable on the half-plane `0 < re z`.

```lean
TauCeti.differentiableOn_integral_mul_cexp_neg_mul {f : ℝ → ℂ} {M : ℝ}
  (hbound : ∀ t ∈ Set.Ici 0, ‖f t‖ ≤ M) :
  DifferentiableOn ℂ (fun z => ∫ (t : ℝ) in Set.Ici 0, f t * Complex.exp (-z * ↑t)) {z | 0 < z.re}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Truncated Laplace transforms are entire](truncated-laplace-transforms-are-entire.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.differentiableOn_integral_mul_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.differentiableOn_integral_mul_cexp_neg_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.differentiableOn_integral_mul_cexp_neg_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.differentiableOn_integral_mul_cexp_neg_mul)
- [Source of `TauCeti.differentiableOn_integral_mul_cexp_neg_mul` in TauCeti/Analysis/Complex/LaplaceTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/LaplaceTransform.lean#L190)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
