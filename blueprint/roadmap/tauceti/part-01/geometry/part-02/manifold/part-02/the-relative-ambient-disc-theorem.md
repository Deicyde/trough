---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset
statement: formalized
proof: formalized
---

# The relative ambient disc theorem

Let `f` and `g` be smooth embeddings of `E` into a
Hausdorff boundaryless manifold `M` modelled on `E`, preserving the orientations `o` of `E` and
`oM` of `M` at the origin, with images in a preconnected open set `U`. On every compact subset `A`
of `E`, `g` is `f` followed by the final diffeomorphism of a smooth diffeotopy of `M` fixing every
point outside a compact subset of `U`. Points outside `U`, for instance protected discs and
collars, are not moved.

```lean
TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset.{u_1,
    u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  {ι : Type u_3} [Fintype ι] [T2Space M] {U : Set M} (hU : IsOpen U) (hUc : IsPreconnected U)
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E M)
  (hfU : Set.range ⇑f ⊆ U) (hgU : Set.range ⇑g ⊆ U)
  (o : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) E ι)
  (oM : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) M ι)
  (hf : o.IsOrientationPreservingAt oM (⇑f) 0) (hg : o.IsOrientationPreservingAt oM (⇑g) 0)
  {A : Set E} (hA : IsCompact A) :
  ∃ Φ K,
    IsCompact K ∧
      K ⊆ U ∧
        (∀ (t : ↑unitInterval), ∀ y ∉ K, (fun p => (Φ.toDiffeomorph p).2) (t, y) = y) ∧
          Set.EqOn (⇑Φ.final ∘ ⇑f) (⇑g) A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](the-inverse-function-theorem-for-manifolds.md)

## Informally uses

- [The ambient disc theorem in a manifold](../part-01/the-ambient-disc-theorem-in-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.html#TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.html#TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset)
- [Source of `TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt_of_range_subset` in TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.lean#L165)
