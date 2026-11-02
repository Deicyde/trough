---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul
mathlib_file: Mathlib/MeasureTheory/Function/Jacobian.lean
---

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
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Determinant of endomorphisms](../../../../undergraduate/linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Measurable function](../part-01/measurable-function.md)

## Proof depends on

- [Cardinal](../../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Equivalence of norms in finite dimension](../../normed-vector-spaces-banach-spaces/equivalence-of-norms-in-finite-dimension.md)
- [Euclidean affine space](../../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Euclidean domain](../../../general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Invertibility](../../../linear-algebra/matrices/invertibility.md)
- [Lebesgue's density theorem](../../../../thousand-plus/geometry-and-topology/54-general-topology/part-01/lebesgues-density-theorem.md)
- [Linear independence](../../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Jacobian.html#MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul)
- [Source of `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul` in Mathlib/MeasureTheory/Function/Jacobian.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/Jacobian.lean#L1211)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L362)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L525)
