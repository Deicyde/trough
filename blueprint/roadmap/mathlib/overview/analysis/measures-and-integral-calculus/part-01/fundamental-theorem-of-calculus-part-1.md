---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: intervalIntegral.integral_hasFDerivAt_of_tendsto_ae
mathlib_file: Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean
---

# Fundamental theorem of calculus, part 1

**Fundamental theorem of calculus-1**: if `f : ℝ → E` is integrable on `a..b` and `f x` has
finite limits `ca` and `cb` almost surely as `x` tends to `a` and `b`, respectively, then
`(u, v) ↦ ∫ x in u..v, f x` has derivative `(u, v) ↦ v • cb - u • ca` at `(a, b)`.

```lean
intervalIntegral.integral_hasFDerivAt_of_tendsto_ae.{u_3} {E : Type u_3} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] {f : ℝ → E} {ca cb : E} {a b : ℝ}
  (hf : IntervalIntegrable f MeasureTheory.volume a b)
  (hmeas_a : StronglyMeasurableAtFilter f (nhds a) MeasureTheory.volume)
  (hmeas_b : StronglyMeasurableAtFilter f (nhds b) MeasureTheory.volume)
  (ha : Filter.Tendsto f (nhds a ⊓ MeasureTheory.ae MeasureTheory.volume) (nhds ca))
  (hb : Filter.Tendsto f (nhds b ⊓ MeasureTheory.ae MeasureTheory.volume) (nhds cb)) :
  HasFDerivAt (fun p => ∫ (x : ℝ) in p.1..p.2, f x)
    ((ContinuousLinearMap.snd ℝ ℝ ℝ).smulRight cb - (ContinuousLinearMap.fst ℝ ℝ ℝ).smulRight ca)
    (a, b)
```

## Depends on

- [Bochner integral](bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Differentiable function between normed vector spaces](../../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Lebesgue measure (Measures and integral calculus)](lebesgue-measure.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_hasFDerivAt_of_tendsto_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#intervalIntegral.integral_hasFDerivAt_of_tendsto_ae)
- [Source of `intervalIntegral.integral_hasFDerivAt_of_tendsto_ae` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L676)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L355)
