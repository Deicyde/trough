---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasCompactSupport.contDiff_convolution_left
mathlib_file: Mathlib/Analysis/Calculus/ContDiff/Convolution.lean
---

# Regularization by convolution

Mathlib states this as `HasCompactSupport.contDiff_convolution_left`.

```lean
HasCompactSupport.contDiff_convolution_left.{u𝕜, uG, uE, uE', uF} {𝕜 : Type u𝕜} {G : Type uG}
  {E : Type uE} {E' : Type uE'} {F : Type uF} [NormedAddCommGroup E] [NormedAddCommGroup E']
  [NormedAddCommGroup F] {f : G → E} {g : G → E'} [RCLike 𝕜] [NormedSpace 𝕜 E] [NormedSpace 𝕜 E']
  [NormedSpace ℝ F] [NormedSpace 𝕜 F] [MeasurableSpace G] [NormedAddCommGroup G] [BorelSpace G]
  [NormedSpace 𝕜 G] {μ : MeasureTheory.Measure G} (L : E →L[𝕜] E' →L[𝕜] F) [μ.IsAddLeftInvariant]
  [μ.IsNegInvariant] {n : ℕ∞} (hcf : HasCompactSupport f) (hf : ContDiff 𝕜 (↑n) f)
  (hg : MeasureTheory.LocallyIntegrable g μ) : ContDiff 𝕜 (↑n) (MeasureTheory.convolution f g L μ)
```

## Depends on

- [$C^k$ function](../../differentiability/c-k-function.md)
- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Borel sigma-algebra](../part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Convolution (Measures and integral calculus)](convolution.md)
- [Measurable function](../part-01/measurable-function.md)

## Proof depends on

- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Derivative of a composition of functions (Analysis)](../../differentiability/derivative-of-a-composition-of-functions.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Hausdorff space](../../../topology/general-topology/part-01/hausdorff-space.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Homeomorphisms](../../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Inner product space, over $R$ or $C$](../../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `HasCompactSupport.contDiff_convolution_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Convolution.html#HasCompactSupport.contDiff_convolution_left)
- [Source of `HasCompactSupport.contDiff_convolution_left` in Mathlib/Analysis/Calculus/ContDiff/Convolution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/ContDiff/Convolution.lean#L428)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L361)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L530)
