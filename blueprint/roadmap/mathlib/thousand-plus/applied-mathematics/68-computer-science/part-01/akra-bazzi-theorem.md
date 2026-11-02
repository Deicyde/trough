---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AkraBazziRecurrence.isBigO_asympBound
mathlib_file: Mathlib/Computability/AkraBazzi/AkraBazzi.lean
---

# Akra–Bazzi theorem

The **Akra-Bazzi theorem**: `T ∈ O(n^p (1 + ∑_u^n g(u) / u^{p+1}))`

```lean
AkraBazziRecurrence.isBigO_asympBound.{u_1} {α : Type u_1} [Fintype α] {T : ℕ → ℝ} {g : ℝ → ℝ}
  {a b : α → ℝ} {r : α → ℕ → ℕ} [Nonempty α] (R : AkraBazziRecurrence T g a b r) :
  T =O[Filter.atTop] AkraBazziRecurrence.asympBound g a b
```

## Depends on

- [Filter](../../../../overview/topology/general-topology/part-01/filter.md)
- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)

## Proof depends on

- [$C^k$ function](../../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Characteristic p](../../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../../overview/topology/general-topology/part-01/closed-map.md)
- [Completion of an abelian topological group](../../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Connected components](../../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)
- [Connectedness](../../../../overview/topology/general-topology/part-01/connectedness.md)
- [Continuity of monotone functions](../../../../undergraduate/single-variable-real-analysis/real-valued-functions-defined-on-a-subset-of-r/continuity-of-monotone-functions.md)
- [Convex function](../../../../overview/analysis/convexity/convex-function.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions (Analysis)](../../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function (Single Variable Real Analysis)](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Dual of a normed space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Euclidean affine space](../../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Existence of bases](../../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Intermediate value theorem](../../../../overview/topology/topological-algebra/intermediate-value-theorem.md)
- [Kernel of a linear map](../../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Limit point](../../../../undergraduate/single-variable-real-analysis/sequences-of-real-numbers/limit-point.md)
- [Matrix exponential](../../../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Path connectedness](../../../../undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Sequential space](../../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [Sum of subspaces](../../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Number of Subsets of a Set](../../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)
- [Topology on a normed vector space](../../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `AkraBazziRecurrence.isBigO_asympBound`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/AkraBazzi/AkraBazzi.html#AkraBazziRecurrence.isBigO_asympBound)
- [Source of `AkraBazziRecurrence.isBigO_asympBound` in Mathlib/Computability/AkraBazzi/AkraBazzi.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/AkraBazzi/AkraBazzi.lean#L653)
- [1000+ theorems list: Q420714](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L438)
- [1000+ theorems project: Q420714](https://1000-plus.github.io/?length=-1#Q420714)
- [Wikipedia: Akra–Bazzi theorem](https://en.wikipedia.org/wiki/Akra%E2%80%93Bazzi_theorem)
- [Wikidata: Q420714](https://www.wikidata.org/wiki/Q420714)
