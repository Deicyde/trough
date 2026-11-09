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
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Giry monad](../../analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Fubini's theorem](../../analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Topology on a normed vector space](../../analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Probability/Independence/Integration.html#ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral)
- [Source of `ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral` in Mathlib/Probability/Independence/Integration.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Probability/Independence/Integration.lean#L405)
- [Mathlib overview: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L404)
