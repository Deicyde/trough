---
declaration: theorem
origin: cited
lean: TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one
statement: formalized
proof: formalized
---

# Substitution `x = exp t`

For `0 < u` and `0 < v`, the integral of `x ^ (-z - 1)` over
`[u, v]` is the truncated Laplace transform `∫ t in log u..log v, exp (-z t)` of the constant
function `1`.

```lean
TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one {u v : ℝ} (hu : 0 < u) (hv : 0 < v) (z : ℂ) :
  ∫ (x : ℝ) in u..v, ↑x ^ (-z - 1) = ∫ (t : ℝ) in Real.log u..Real.log v, Complex.exp (-z * ↑t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one).

## Sources

- [Tau Ceti documentation: `TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/LaplaceTransform.html#TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one)
- [Source of `TauCeti.intervalIntegral_ofReal_cpow_neg_sub_one` in TauCeti/Analysis/Complex/LaplaceTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/LaplaceTransform.lean#L115)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
