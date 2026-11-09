# Fourier transform on $\mathrm{L}^2(\R^d)$

The Fourier transform on `L2` as a linear isometry equivalence.

```lean
MeasureTheory.Lp.fourierTransformₗᵢ.{u_1, u_2} (E : Type u_1) (F : Type u_2) [NormedAddCommGroup E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F]
  [CompleteSpace F] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] :
  ↥(MeasureTheory.Lp F 2 MeasureTheory.volume) ≃ₗᵢ[ℂ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)
```

## Depends on

- [$L^p$ space](../../../overview/analysis/measures-and-integral-calculus/part-01/l-p-space.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Extension by continuity](../../../overview/topology/general-topology/part-01/extension-by-continuity.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Kernel of a linear map](../../linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Lebesgue measure (Measure theory)](../measure-theory/lebesgue-measure.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)
- [Vector-valued integrable function (Bochner integral)](../../../overview/analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Lp.fourierTransformₗᵢ`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/LpSpace.html#MeasureTheory.Lp.fourierTransform%E2%82%97%E1%B5%A2)
- [Source of `MeasureTheory.Lp.fourierTransformₗᵢ` in Mathlib/Analysis/Fourier/LpSpace.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Fourier/LpSpace.lean#L48)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L539)
