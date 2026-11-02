---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Stirling.tendsto_stirlingSeq_sqrt_pi
mathlib_file: Mathlib/Analysis/SpecialFunctions/Stirling.lean
---

# Stirling’s Formula

**Stirling's Formula**

```lean
Stirling.tendsto_stirlingSeq_sqrt_pi :
  Filter.Tendsto Stirling.stirlingSeq Filter.atTop (nhds √Real.pi)
```

## Depends on

- [Bornology](../../overview/analysis/topological-vector-spaces/bornology.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Exponential](../../overview/analysis/special-functions/exponential.md)
- [Uniform space](../../overview/topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Infinite sum](../../overview/topology/topological-algebra/infinite-sum.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Order topology](../../overview/topology/topological-algebra/order-topology.md)
- [Power functions](../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Topological module](../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Stirling.tendsto_stirlingSeq_sqrt_pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Stirling.html#Stirling.tendsto_stirlingSeq_sqrt_pi)
- [Source of `Stirling.tendsto_stirlingSeq_sqrt_pi` in Mathlib/Analysis/SpecialFunctions/Stirling.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/Stirling.lean#L210)
- [Freek Wiedijk's 100 theorems, no. 90](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L463)
- [1000+ theorems list: Q470877](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L471)
- [1000+ theorems project: Q470877](https://1000-plus.github.io/?length=-1#Q470877)
- [Wikipedia: Stirling's theorem](https://en.wikipedia.org/wiki/Stirling's_theorem)
- [Wikidata: Q470877](https://www.wikidata.org/wiki/Q470877)
