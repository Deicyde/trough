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
- [Differentiable function between normed vector spaces](../../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Lebesgue measure](lebesgue-measure.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Topological module](../../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Affine space](../../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Approximation by step functions](../../../../undergraduate/measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Fatou's lemma](fatous-lemma.md)
- [Giry monad](giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Monotone convergence theorem](monotone-convergence-theorem.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../hilbert-spaces/orthogonal-projection.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Quotient space](../../../linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../../hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](stieltjes-measure.md)

## Sources

- [Mathlib documentation: `intervalIntegral.integral_hasFDerivAt_of_tendsto_ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.html#intervalIntegral.integral_hasFDerivAt_of_tendsto_ae)
- [Source of `intervalIntegral.integral_hasFDerivAt_of_tendsto_ae` in Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/FundThmCalculus.lean#L676)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L355)
