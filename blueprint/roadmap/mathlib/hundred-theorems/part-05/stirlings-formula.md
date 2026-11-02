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

- [$C^k$ function](../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Completion of an abelian topological group](../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Derivative of a composition of functions (Analysis)](../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function (Single Variable Real Analysis)](../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentiable functions](../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Differentials (linear tangent functions)](../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Holomorphic functions](../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Integration by parts](../../undergraduate/single-variable-real-analysis/integration/integration-by-parts.md)
- [Matrix exponential](../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Sequential space](../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `Stirling.tendsto_stirlingSeq_sqrt_pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Stirling.html#Stirling.tendsto_stirlingSeq_sqrt_pi)
- [Source of `Stirling.tendsto_stirlingSeq_sqrt_pi` in Mathlib/Analysis/SpecialFunctions/Stirling.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/Stirling.lean#L210)
- [Freek Wiedijk's 100 theorems, no. 90](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L463)
- [1000+ theorems list: Q470877](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L471)
- [1000+ theorems project: Q470877](https://1000-plus.github.io/?length=-1#Q470877)
- [Wikipedia: Stirling's theorem](https://en.wikipedia.org/wiki/Stirling's_theorem)
- [Wikidata: Q470877](https://www.wikidata.org/wiki/Q470877)
