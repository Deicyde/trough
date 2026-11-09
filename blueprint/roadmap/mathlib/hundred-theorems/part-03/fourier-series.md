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
- [Carathéodory's theorem (measure theory)](../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Compact open topology](../../overview/topology/general-topology/part-01/compact-open-topology.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Field $\C$ of complex numbers](../../undergraduate/ring-theory/field-theory/field-c-of-complex-numbers.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Inner product space, over $R$ or $C$](../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Completeness of $L^2$](../../undergraduate/topology/hilbert-spaces/completeness-of-l-2-2.md)
- [Completeness of $l^2$](../../undergraduate/topology/hilbert-spaces/completeness-of-l-2.md)
- [Example, the Hilbert basis of trigonometric polynomials](../../undergraduate/topology/hilbert-spaces/example-the-hilbert-basis-of-trigonometric-polyn.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Probability measure](../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Urysohn's lemma](../../overview/topology/general-topology/part-02/urysohns-lemma.md)
- [Weierstrass trigonometric approximation theorem](../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/weierstrass-trigonometric-approximation-theorem.md)

## Sources

- [Mathlib documentation: `fourierCoeff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#fourierCoeff)
- [Source of `fourierCoeff` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Fourier/AddCircle.lean#L294)
- [Mathlib documentation: `hasSum_fourier_series_L2`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/AddCircle.html#hasSum_fourier_series_L2)
- [Source of `hasSum_fourier_series_L2` in Mathlib/Analysis/Fourier/AddCircle.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Fourier/AddCircle.lean#L430)
- [Freek Wiedijk's 100 theorems, no. 76](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L383)
