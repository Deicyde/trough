---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: niven
mathlib_file: Mathlib/NumberTheory/Niven.lean
---

# Niven's theorem

**Niven's theorem**: The only rational values of `cos` that occur at rational multiples of π
are `{-1, -1/2, 0, 1/2, 1}`.

```lean
niven {θ : ℝ} (hθ : ∃ r, θ = ↑r * Real.pi) (hcos : ∃ q, Real.cos θ = ↑q) :
  Real.cos θ ∈ {-1, -1 / 2, 0, 1 / 2, 1}
```

## Depends on

- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)

## Proof depends on

- [Cantor’s Theorem](../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Cayley-Hamilton theorem](../../../overview/linear-algebra/endomorphism-polynomials/cayley-hamilton-theorem.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Integral root theorem](../../algebra/12-field-theory-and-polynomials/integral-root-theorem.md)
- [Kernel of a linear map](../../../undergraduate/linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Lipschitz continuity](../../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Localization](../../../overview/general-algebra/rings/localization.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Noetherian ring](../../../overview/general-algebra/rings/noetherian-ring.md)
- [Norm of a continuous linear map](../../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Schroeder-Bernstein Theorem](../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)
- [Squeeze theorem](../../analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Subring](../../../overview/general-algebra/rings/subring.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Trigonometric functions](../../../overview/analysis/special-functions/trigonometric-functions.md)
- [Uniformly continuous function](../../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `niven`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Niven.html#niven)
- [Source of `niven` in Mathlib/NumberTheory/Niven.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Niven.lean#L105)
- [1000+ theorems list: Q4116459](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2668)
- [1000+ theorems project: Q4116459](https://1000-plus.github.io/?length=-1#Q4116459)
- [Wikipedia: Niven's theorem](https://en.wikipedia.org/wiki/Niven's_theorem)
- [Wikidata: Q4116459](https://www.wikidata.org/wiki/Q4116459)
