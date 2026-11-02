---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral
mathlib_file: Mathlib/Probability/Independence/Integration.lean
---

# Mean of product of independent random variables

Mathlib states this as `ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral`.

```lean
ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral.{u_1, u_2} {Ω : Type u_1} {𝕜 : Type u_2}
  [RCLike 𝕜] {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} {X Y : Ω → 𝕜}
  (hXY : ProbabilityTheory.IndepFun X Y μ) (hX : MeasureTheory.AEStronglyMeasurable X μ)
  (hY : MeasureTheory.AEStronglyMeasurable Y μ) :
  ∫ (x : Ω), (X * Y) x ∂μ = (∫ (x : Ω), X x ∂μ) * ∫ (x : Ω), Y x ∂μ
```

## Depends on

- [Bochner integral](../../analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Giry monad](../../analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Borel sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/Integration.html#ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral)
- [Source of `ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral` in Mathlib/Probability/Independence/Integration.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Probability/Independence/Integration.lean#L411)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L404)
