# Poisson’s formula

**Poisson's summation formula** for Schwartz functions.

```lean
SchwartzMap.tsum_eq_tsum_fourier (f : SchwartzMap ℝ ℂ) (x : ℝ) :
  ∑' (n : ℤ), f (x + ↑n) = ∑' (n : ℤ), (FourierTransform.fourier f) ↑n * (fourier n) ↑x
```

## Depends on

- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Fourier Series](../../../hundred-theorems/part-03/fourier-series.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Sources

- [Mathlib documentation: `SchwartzMap.tsum_eq_tsum_fourier`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/PoissonSummation.html#SchwartzMap.tsum_eq_tsum_fourier)
- [Source of `SchwartzMap.tsum_eq_tsum_fourier` in Mathlib/Analysis/Fourier/PoissonSummation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/PoissonSummation.lean#L214)
- [Mathlib undergraduate list: Distribution calculus › Applications](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L626)
