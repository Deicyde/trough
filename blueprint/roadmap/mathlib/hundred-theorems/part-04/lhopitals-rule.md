---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: deriv.lhopital_zero_nhds
mathlib_file: Mathlib/Analysis/Calculus/LHopital.lean
---

# L’Hopital’s Rule

**L'Hôpital's rule** for approaching a real, `deriv` version

```lean
deriv.lhopital_zero_nhds {a : ℝ} {l : Filter ℝ} {f g : ℝ → ℝ}
  (hdf : ∀ᶠ (x : ℝ) in nhds a, DifferentiableAt ℝ f x) (hg' : ∀ᶠ (x : ℝ) in nhds a, deriv g x ≠ 0)
  (hfa : Filter.Tendsto f (nhds a) (nhds 0)) (hga : Filter.Tendsto g (nhds a) (nhds 0))
  (hdiv : Filter.Tendsto (fun x => deriv f x / deriv g x) (nhds a) l) :
  Filter.Tendsto (fun x => f x / g x) (nhdsWithin a {a}ᶜ) l
```

## Depends on

- [Differentiable function between normed vector spaces](../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Differentials (linear tangent functions)](../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Field $\R$ of real numbers](../../undergraduate/ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Metric structure](../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)

## Proof depends on

- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Associative algebra over a commutative ring](../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Closure](../../overview/topology/general-topology/part-01/closure.md)
- [Completeness of R](../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Convex subsets](../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Dual of a normed space](../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Extreme value theorem](../../overview/topology/topological-algebra/extreme-value-theorem.md)
- [Hausdorff space](../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Lipschitz continuity](../../overview/topology/metric-spaces/lipschitz-continuity.md)
- [Norm of a continuous linear map](../../overview/analysis/normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Open map](../../overview/topology/general-topology/part-01/open-map.md)
- [Product of vector spaces](../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Squeeze theorem](../../thousand-plus/analysis/26-real-functions/part-03/squeeze-theorem.md)
- [The Triangle Inequality](../part-05/the-triangle-inequality.md)
- [Topological ring](../../overview/topology/topological-algebra/topological-ring.md)
- [Topology of a metric space](../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)
- [Topology on a normed vector space](../../overview/analysis/normed-vector-spaces-banach-spaces/topology-on-a-normed-vector-space.md)
- [Uniformly continuous function](../../overview/topology/uniform-notions/uniformly-continuous-function.md)

## Sources

- [Mathlib documentation: `deriv.lhopital_zero_nhds`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/LHopital.html#deriv.lhopital_zero_nhds)
- [Source of `deriv.lhopital_zero_nhds` in Mathlib/Analysis/Calculus/LHopital.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/LHopital.lean#L429)
- [Freek Wiedijk's 100 theorems, no. 64](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L323)
