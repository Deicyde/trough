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

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Convex subsets](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Differentiable function between normed vector spaces](../../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Induced topology](../../../../overview/topology/general-topology/part-01/induced-topology.md)
- [Metric structure](../../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Normed vector space over a normed field](../../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)

## Sources

- [Mathlib documentation: `AkraBazziRecurrence.isBigO_asympBound`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/AkraBazzi/AkraBazzi.html#AkraBazziRecurrence.isBigO_asympBound)
- [Source of `AkraBazziRecurrence.isBigO_asympBound` in Mathlib/Computability/AkraBazzi/AkraBazzi.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/AkraBazzi/AkraBazzi.lean#L653)
- [1000+ theorems list: Q420714](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L438)
- [1000+ theorems project: Q420714](https://1000-plus.github.io/?length=-1#Q420714)
- [Wikipedia: Akra–Bazzi theorem](https://en.wikipedia.org/wiki/Akra%E2%80%93Bazzi_theorem)
- [Wikidata: Q420714](https://www.wikidata.org/wiki/Q420714)
