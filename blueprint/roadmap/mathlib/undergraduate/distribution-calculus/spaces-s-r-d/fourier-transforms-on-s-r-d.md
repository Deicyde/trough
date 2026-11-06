# Fourier transforms on $\mathcal{S}(\R^d)$

The Fourier transform on a real inner product space, as a continuous linear map on the
Schwartz space.

This definition is only to define the Fourier transform, use `FourierTransform.fourierCLM` instead.

```lean
SchwartzMap.fourierTransformCLM.{u_1, u_2, u_3} (𝕜 : Type u_1) [RCLike 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [NormedSpace 𝕜 E] [SMulCommClass ℂ 𝕜 E] {V : Type u_3}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] : SchwartzMap V E →L[𝕜] SchwartzMap V E
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lebesgue measure (Measure theory)](../../measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)

## Sources

- [Mathlib documentation: `SchwartzMap.fourierTransformCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.html#SchwartzMap.fourierTransformCLM)
- [Source of `SchwartzMap.fourierTransformCLM` in Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean#L48)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L611)
