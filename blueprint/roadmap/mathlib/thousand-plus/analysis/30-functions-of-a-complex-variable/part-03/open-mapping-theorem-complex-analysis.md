---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AnalyticOnNhd.is_constant_or_isOpen
mathlib_file: Mathlib/Analysis/Complex/OpenMapping.lean
---

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

- [Analytic function](../../../../overview/analysis/differentiability/analytic-function.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Inner product space, over $R$ or $C$](../../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)

## Proof depends on

- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../../overview/topology/general-topology/part-01/closure.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Differentiable function between normed vector spaces](../../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Extreme value theorem](../../../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Order topology](../../../../overview/topology/topological-algebra/order-topology.md)
- [Principle of analytic continuation](../../../../overview/analysis/complex-analysis/principle-of-analytic-continuation.md)
- [Topological module](../../../../overview/topology/topological-algebra/topological-module.md)
- [Topology of a metric space](../../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `AnalyticOnNhd.is_constant_or_isOpen`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/OpenMapping.html#AnalyticOnNhd.is_constant_or_isOpen)
- [Source of `AnalyticOnNhd.is_constant_or_isOpen` in Mathlib/Analysis/Complex/OpenMapping.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Complex/OpenMapping.lean#L162)
- [1000+ theorems list: Q967972](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1158)
- [1000+ theorems project: Q967972](https://1000-plus.github.io/all.html?length=-1#Q967972)
- [Wikipedia: Open mapping theorem (complex analysis)](https://en.wikipedia.org/wiki/Open_mapping_theorem_%28complex_analysis%29)
- [Wikidata: Q967972](https://www.wikidata.org/wiki/Q967972)
