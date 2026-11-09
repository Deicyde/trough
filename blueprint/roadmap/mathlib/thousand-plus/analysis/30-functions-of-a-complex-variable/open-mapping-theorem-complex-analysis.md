# Open mapping theorem (complex analysis)

The *open mapping theorem* for holomorphic functions, global version: if a function `g : E → ℂ`
is analytic on a connected set `U`, then either it is constant on `U`, or it is open on `U` (in the
sense that it maps any open set contained in `U` to an open set in `ℂ`).

```lean
AnalyticOnNhd.is_constant_or_isOpen.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  {U : Set E} {g : E → ℂ} (hg : AnalyticOnNhd ℂ g U) (hU : IsPreconnected U) :
  (∃ w, ∀ z ∈ U, g z = w) ∨ ∀ s ⊆ U, IsOpen s → IsOpen (g '' s)
```

## Depends on

- [Analytic function](../../../overview/analysis/differentiability/analytic-function.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Analyticity of holomorphic functions](../../../overview/analysis/complex-analysis/analyticity-of-holomorphic-functions.md)
- [Convex subsets](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Extreme value theorem](../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Maximum modulus principle](../../../overview/analysis/complex-analysis/maximum-modulus-principle.md)
- [Principle of analytic continuation](../../../overview/analysis/complex-analysis/principle-of-analytic-continuation.md)

## Sources

- [Mathlib documentation: `AnalyticOnNhd.is_constant_or_isOpen`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/OpenMapping.html#AnalyticOnNhd.is_constant_or_isOpen)
- [Source of `AnalyticOnNhd.is_constant_or_isOpen` in Mathlib/Analysis/Complex/OpenMapping.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Complex/OpenMapping.lean#L162)
- [1000+ theorems list: Q967972](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1158)
- [1000+ theorems project: Q967972](https://1000-plus.github.io/all.html?length=-1#Q967972)
- [Wikipedia: Open mapping theorem (complex analysis)](https://en.wikipedia.org/wiki/Open_mapping_theorem_%28complex_analysis%29)
- [Wikidata: Q967972](https://www.wikidata.org/wiki/Q967972)
