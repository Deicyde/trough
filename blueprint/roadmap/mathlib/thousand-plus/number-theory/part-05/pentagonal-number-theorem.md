---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: PowerSeries.WithPiTopology.hasProd_one_sub_X_pow, hasProd_eulerFunction
mathlib_file: Mathlib/Combinatorics/Enumerative/Pentagonal/PowerSeries.lean
---

# Pentagonal number theorem

Mathlib records this with 2 declarations.

`PowerSeries.WithPiTopology.hasProd_one_sub_X_pow`: **Pentagonal number theorem** for power series, expressed as an infinite product. See also
`PowerSeries.WithPiTopology.hasSum_pentagonalSeries` that expresses `pentagonalSeries` as an
infinite sum.

```lean
PowerSeries.WithPiTopology.hasProd_one_sub_X_pow.{u_1} (R : Type u_1) [CommRing R]
  [TopologicalSpace R] :
  HasProd (fun n => 1 - PowerSeries.X ^ (n + 1)) (PowerSeries.pentagonalSeries R)
```

`hasProd_eulerFunction`: **Pentagonal number theorem** for Euler function, expressed as an infinite product.
See `hasSum_eulerFunction_pentagonal` that expresses `eulerFunction` as an infinite sum.

```lean
hasProd_eulerFunction.{u_1} {R : Type u_1} [NormedCommRing R] [NormOneClass R] [CompleteSpace R]
  {x : R} (hx : ‖x‖ < 1) : HasProd (fun n => 1 - x ^ (n + 1)) (eulerFunction x)
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Induced topology](../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)
- [Power series](../../../overview/general-algebra/polynomials-and-power-series/power-series.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `PowerSeries.WithPiTopology.hasProd_one_sub_X_pow`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/Pentagonal/PowerSeries.html#PowerSeries.WithPiTopology.hasProd_one_sub_X_pow)
- [Source of `PowerSeries.WithPiTopology.hasProd_one_sub_X_pow` in Mathlib/Combinatorics/Enumerative/Pentagonal/PowerSeries.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/Pentagonal/PowerSeries.lean#L180)
- [Mathlib documentation: `hasProd_eulerFunction`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/Pentagonal/EulerFunction.html#hasProd_eulerFunction)
- [Source of `hasProd_eulerFunction` in Mathlib/Combinatorics/Enumerative/Pentagonal/EulerFunction.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/Pentagonal/EulerFunction.lean#L149)
- [1000+ theorems list: Q282649](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L329)
- [1000+ theorems project: Q282649](https://1000-plus.github.io/?length=-1#Q282649)
- [Wikipedia: Pentagonal number theorem](https://en.wikipedia.org/wiki/Pentagonal_number_theorem)
- [Wikidata: Q282649](https://www.wikidata.org/wiki/Q282649)
