---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Submodule.complete_of_finiteDimensional
mathlib_file: Mathlib/Topology/Algebra/Module/FiniteDimension.lean
---

# Finite-dimensional normed spaces over complete normed fields are complete

A finite-dimensional subspace is complete.

```lean
Submodule.complete_of_finiteDimensional.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜] [AddCommGroup E] [UniformSpace E] [T2Space E]
  [IsUniformAddGroup E] [_root_.Module 𝕜 E] [ContinuousSMul 𝕜 E] (s : Submodule 𝕜 E)
  [FiniteDimensional 𝕜 ↥s] : IsComplete ↑s
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)

## Proof depends on

- [Aleph numbers](../../logic-and-computation/set-theory/cardinals/aleph-numbers.md)
- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Equivalence of norms in finite dimension](equivalence-of-norms-in-finite-dimension.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)
- [Fundamental sequences](../../logic-and-computation/set-theory/ordinals/fundamental-sequences.md)
- [Hilbert basis theorem](../../general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Isomorphism with $K^n$](../../linear-algebra/finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Local ring](../../general-algebra/rings/local-ring.md)
- [Polynomial in several indeterminates](../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [Subring](../../general-algebra/rings/subring.md)
- [The Fundamental Theorem of Arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)
- [Well-ordering theorem](../../../thousand-plus/general-topics-history-and-foundations/03-mathematical-logic-and-foundations/part-03/well-ordering-theorem.md)

## Sources

- [Mathlib documentation: `Submodule.complete_of_finiteDimensional`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/FiniteDimension.html#Submodule.complete_of_finiteDimensional)
- [Source of `Submodule.complete_of_finiteDimensional` in Mathlib/Topology/Algebra/Module/FiniteDimension.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Module/FiniteDimension.lean#L519)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L282)
