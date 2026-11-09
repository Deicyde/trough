# Change of variables formula

Change of variable formula for differentiable functions: if a function `f` is
injective and differentiable on a measurable set `s`, then the Bochner integral of a function
`g : E → F` on `f '' s` coincides with the integral of `|(f' x).det| • g ∘ f` on `s`.

```lean
MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {s : Set E} {f : E → E} {f' : E → E →L[ℝ] E}
  [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure]
  (hs : MeasurableSet s) (hf' : ∀ x ∈ s, HasFDerivWithinAt f (f' x) s x) (hf : Set.InjOn f s)
  (g : E → F) : ∫ (x : E) in f '' s, g x ∂μ = ∫ (x : E) in s, |(f' x).det| • g (f x) ∂μ
```

## Depends on

- [Bochner integral](../part-01/bochner-integral.md)
- [Borel sigma-algebra](../part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Determinant of endomorphisms](../../../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Measurable function](../part-01/measurable-function.md)

## Proof depends on

- [Besicovitch covering theorem](../../../../thousand-plus/analysis/26-real-functions/part-01/besicovitch-covering-theorem.md)
- [Euclidean affine space](../../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Euclidean domain](../../../general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Invertibility](../../../linear-algebra/matrices/invertibility.md)
- [Lebesgue's density theorem](../../../../thousand-plus/geometry-and-topology/54-general-topology/lebesgues-density-theorem.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Uniformly continuous function](../../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Jacobian.html#MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul)
- [Source of `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul` in Mathlib/MeasureTheory/Function/Jacobian.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/MeasureTheory/Function/Jacobian.lean#L1211)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L362)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L525)
