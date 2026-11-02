---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasStrictFDerivAt.to_localInverse
mathlib_file: Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.lean
---

# Inverse function theorem

If `f` has an invertible derivative `f'` at `a` in the sense of strict differentiability `(hf)`,
then the inverse function `hf.localInverse f` has derivative `f'.symm` at `f a`.

```lean
HasStrictFDerivAt.to_localInverse.{u_1, u_2, u_3} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {f : E → F} {f' : E ≃L[𝕜] F} {a : E} [CompleteSpace E]
  (hf : HasStrictFDerivAt f (↑f') a) :
  HasStrictFDerivAt (HasStrictFDerivAt.localInverse f f' a hf) (↑f'.symm) (f a)
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Normed vector space over a normed field](../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../topology/general-topology/part-01/cluster-point.md)
- [Euclidean affine space](../../geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Hausdorff space](../../topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Lipschitz continuity](../../topology/metric-spaces/lipschitz-continuity.md)
- [Metric structure](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)
- [Open map](../../topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `HasStrictFDerivAt.to_localInverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.html#HasStrictFDerivAt.to_localInverse)
- [Source of `HasStrictFDerivAt.to_localInverse` in Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/InverseFunctionTheorem/FDeriv.lean#L185)
- [Mathlib overview: Analysis › Differentiability](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L316)
- [1000+ theorems list: Q931001](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1108)
- [1000+ theorems project: Q931001](https://1000-plus.github.io/?length=-1#Q931001)
- [Wikipedia: Inverse function theorem](https://en.wikipedia.org/wiki/Inverse_function_theorem)
- [Wikidata: Q931001](https://www.wikidata.org/wiki/Q931001)
