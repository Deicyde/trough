---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContDiffBump.convolution_tendsto_right
mathlib_file: Mathlib/Analysis/Calculus/BumpFunction/Convolution.lean
---

# Approximation by convolution

`(φ i ⋆ g i) (k i)` tends to `z₀` as `i` tends to some filter `l` if
* `φ` is a sequence of normed bump functions
  such that `(φ i).rOut` tends to `0` as `i` tends to `l`;
* `g i` is `μ`-a.e. strongly measurable as `i` tends to `l`;
* `g i x` tends to `z₀` as `(i, x)` tends to `l ×ˢ 𝓝 x₀`;
* `k i` tends to `x₀`.

```lean
ContDiffBump.convolution_tendsto_right.{uG, uE', u_1} {G : Type uG} {E' : Type uE'}
  [NormedAddCommGroup E'] [MeasurableSpace G] {μ : MeasureTheory.Measure G} [NormedSpace ℝ E']
  [NormedAddCommGroup G] [NormedSpace ℝ G] [CompleteSpace E'] [BorelSpace G] [FiniteDimensional ℝ G]
  [μ.IsAddHaarMeasure] {ι : Type u_1} {φ : ι → ContDiffBump 0} {g : ι → G → E'} {k : ι → G} {x₀ : G}
  {z₀ : E'} {l : Filter ι} (hφ : Filter.Tendsto (fun i => (φ i).rOut) l (nhds 0))
  (hig : ∀ᶠ (i : ι) in l, MeasureTheory.AEStronglyMeasurable (g i) μ)
  (hcg : Filter.Tendsto (Function.uncurry g) (l ×ˢ nhds x₀) (nhds z₀))
  (hk : Filter.Tendsto k l (nhds x₀)) :
  Filter.Tendsto
    (fun i =>
      MeasureTheory.convolution ((φ i).normed μ) (g i) (ContinuousLinearMap.lsmul ℝ ℝ) μ (k i))
    l (nhds z₀)
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Ball](../../../topology/metric-spaces/ball.md)
- [Borel sigma-algebra](../part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Convolution (Measures and integral calculus)](convolution.md)
- [Finite-dimensionality](../../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Measurable function](../part-01/measurable-function.md)
- [Radius of convergence](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)

## Proof depends on

- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)

## Sources

- [Mathlib documentation: `ContDiffBump.convolution_tendsto_right`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/BumpFunction/Convolution.html#ContDiffBump.convolution_tendsto_right)
- [Source of `ContDiffBump.convolution_tendsto_right` in Mathlib/Analysis/Calculus/BumpFunction/Convolution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/BumpFunction/Convolution.lean#L77)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L360)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L529)
