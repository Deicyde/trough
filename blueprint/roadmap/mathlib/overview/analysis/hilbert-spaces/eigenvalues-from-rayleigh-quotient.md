# Eigenvalues from Rayleigh quotient

For a self-adjoint operator `T`, a local extremum of the Rayleigh quotient of `T` on a sphere
centred at the origin is an eigenvector of `T`.

```lean
IsSelfAdjoint.hasEigenvector_of_isLocalExtrOn.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] {T : E →L[𝕜] E}
  (hT : IsSelfAdjoint T) {x₀ : E} (hx₀ : x₀ ≠ 0)
  (hextr : IsLocalExtrOn T.reApplyInnerSelf (Metric.sphere 0 ‖x₀‖) x₀) :
  Module.End.HasEigenvector (↑T) (↑(T.rayleighQuotient x₀)) x₀
```

## Depends on

- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Eigenvector](../../linear-algebra/structure-theory-of-endomorphisms/eigenvector.md)
- [Inner product space, over $R$ or $C$](inner-product-space-over-r-or-c.md)
- [Self-adjoint operator](self-adjoint-operator.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Dual of a normed space](../normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Hellinger–Toeplitz theorem](../../../thousand-plus/analysis/46-functional-analysis/hellinger-toeplitz-theorem.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `IsSelfAdjoint.hasEigenvector_of_isLocalExtrOn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Rayleigh.html#IsSelfAdjoint.hasEigenvector_of_isLocalExtrOn)
- [Source of `IsSelfAdjoint.hasEigenvector_of_isLocalExtrOn` in Mathlib/Analysis/InnerProductSpace/Rayleigh.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Rayleigh.lean#L264)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L302)
