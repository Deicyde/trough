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

- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Dimension theorem for vector spaces](../../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Euclidean affine space](../../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Extreme value theorem](../../../topology/topological-algebra/extreme-value-theorem.md)
- [Finite-dimensional normed spaces over complete normed fields are complete](../../normed-vector-spaces-banach-spaces/finite-dimensional-normed-spaces-over-complete-n.md)
- [Gaussian elimination](../../../../undergraduate/linear-algebra/matrices/gaussian-elimination.md)
- [Giry monad](../part-01/giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Invertibility](../../../linear-algebra/matrices/invertibility.md)
- [Lebesgue measure](../part-01/lebesgue-measure.md)
- [Lebesgue's density theorem](../../../../thousand-plus/geometry-and-topology/54-general-topology/part-01/lebesgues-density-theorem.md)
- [Maximal ideal](../../../general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../hilbert-spaces/orthogonal-projection.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of finitely many measures](product-of-finitely-many-measures.md)
- [Quotient ring](../../../general-algebra/ideals-and-quotients/quotient-ring.md)
- [Self-adjoint operator](../../hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../part-01/stieltjes-measure.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/Jacobian.html#MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul)
- [Source of `MeasureTheory.integral_image_eq_integral_abs_det_fderiv_smul` in Mathlib/MeasureTheory/Function/Jacobian.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Function/Jacobian.lean#L1211)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L362)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L525)
