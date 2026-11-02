---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: SchwartzMap.tsum_eq_tsum_fourier
mathlib_file: Mathlib/Analysis/Fourier/PoissonSummation.lean
---

# Poisson’s formula

**Poisson's summation formula** for Schwartz functions.

```lean
SchwartzMap.tsum_eq_tsum_fourier (f : SchwartzMap ℝ ℂ) (x : ℝ) :
  ∑' (n : ℤ), f (x + ↑n) = ∑' (n : ℤ), (FourierTransform.fourier f) ↑n * (fourier n) ↑x
```

## Depends on

- [Fourier transforms on $\mathcal{S}(\R^d)$](../spaces-s-r-d/fourier-transforms-on-s-r-d.md)

## Proof depends on

- [Fourier Series](../../../hundred-theorems/part-04/fourier-series.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Sources

- [Mathlib documentation: `SchwartzMap.tsum_eq_tsum_fourier`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/PoissonSummation.html#SchwartzMap.tsum_eq_tsum_fourier)
- [Source of `SchwartzMap.tsum_eq_tsum_fourier` in Mathlib/Analysis/Fourier/PoissonSummation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/PoissonSummation.lean#L214)
- [Mathlib undergraduate list: Distribution calculus › Applications](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L626)
