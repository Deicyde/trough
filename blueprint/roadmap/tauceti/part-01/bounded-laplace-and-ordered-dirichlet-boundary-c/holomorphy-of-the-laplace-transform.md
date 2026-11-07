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
  (hf : MeasureTheory.AEStronglyMeasurable f (MeasureTheory.volume.restrict (Set.Ici 0)))
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
- [Source of `TauCeti.differentiableOn_integral_mul_cexp_neg_mul` in TauCeti/Analysis/Complex/LaplaceTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/LaplaceTransform.lean#L166)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
