---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ContinuousLinearMap.isOpenMap
mathlib_file: Mathlib/Analysis/Normed/Operator/Banach.lean
---

# Banach open mapping theorem

The Banach open mapping theorem: a surjective bounded linear map between Banach spaces is
open.

```lean
ContinuousLinearMap.isOpenMap.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {𝕜' : Type u_2}
  [NontriviallyNormedField 𝕜] [NontriviallyNormedField 𝕜'] {σ : 𝕜 →+* 𝕜'} {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_4} [NormedAddCommGroup F] [NormedSpace 𝕜' F]
  (f : E →SL[σ] F) {σ' : 𝕜' →+* 𝕜} [RingHomInvPair σ σ'] [RingHomIsometric σ] [RingHomIsometric σ']
  [CompleteSpace F] [CompleteSpace E] (surj : Function.Surjective ⇑f) : IsOpenMap ⇑f
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Normed vector space over a normed field](normed-vector-space-over-a-normed-field.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](absolutely-convergent-series-in-banach-spaces.md)
- [Baire theorem](../../topology/metric-spaces/baire-theorem.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Euclidean affine space](../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../topology/topological-algebra/order-topology.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `ContinuousLinearMap.isOpenMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Operator/Banach.html#ContinuousLinearMap.isOpenMap)
- [Source of `ContinuousLinearMap.isOpenMap` in Mathlib/Analysis/Normed/Operator/Banach.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Operator/Banach.lean#L227)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L286)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L425)
- [1000+ theorems list: Q944297](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1131)
- [1000+ theorems project: Q944297](https://1000-plus.github.io/all.html?length=-1#Q944297)
- [Wikipedia: Open mapping theorem (functional analysis)](https://en.wikipedia.org/wiki/Open_mapping_theorem_%28functional_analysis%29)
- [Wikidata: Q944297](https://www.wikidata.org/wiki/Q944297)
