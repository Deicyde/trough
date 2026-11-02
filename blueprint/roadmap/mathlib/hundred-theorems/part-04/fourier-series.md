---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: fourierCoeff, hasSum_fourier_series_L2
mathlib_file: Mathlib/Analysis/Fourier/AddCircle.lean
---

# Fourier Series

Mathlib records this with 2 declarations.

`fourierCoeff`: The `n`-th Fourier coefficient of a function `AddCircle T → E`, for `E` a complete normed
`ℂ`-vector space, defined as the integral over `AddCircle T` of `fourier (-n) t • f t`.

```lean
fourierCoeff.{u_1} {T : ℝ} [hT : Fact (0 < T)] {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] (f : AddCircle T → E) (n : ℤ) : E
```

`hasSum_fourier_series_L2`: The Fourier series of an `L2` function `f` sums to `f`, in the `L²` space of `AddCircle T`.

```lean
hasSum_fourier_series_L2 {T : ℝ} [hT : Fact (0 < T)]
  (f : ↥(MeasureTheory.Lp ℂ 2 AddCircle.haarAddCircle)) :
  HasSum (fun i => fourierCoeff (↑↑f) i • fourierLp 2 i) f
```

## Depends on

- [Bochner integral](../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compact open topology](../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Inner product space, over $R$ or $C$](../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Completeness of $L^2$](../../undergraduate/topology/hilbert-spaces/completeness-of-l-2-2.md)
- [Example, the Hilbert basis of trigonometric polynomials](../../undergraduate/topology/hilbert-spaces/example-the-hilbert-basis-of-trigonometric-polyn.md)
- [Finite-dimensionality](../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Weierstrass trigonometric approximation theorem](../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/weierstrass-trigonometric-approximation-theorem.md)

## Sources

- [Mathlib documentation: `fourierCoeff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#fourierCoeff)
- [Source of `fourierCoeff` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/AddCircle.lean#L295)
- [Mathlib documentation: `hasSum_fourier_series_L2`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#hasSum_fourier_series_L2)
- [Source of `hasSum_fourier_series_L2` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/AddCircle.lean#L431)
- [Freek Wiedijk's 100 theorems, no. 76](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L383)
