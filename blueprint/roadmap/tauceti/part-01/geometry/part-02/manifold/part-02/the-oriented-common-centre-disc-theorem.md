---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt
statement: formalized
proof: formalized
---

# The oriented common-centre disc theorem

Two smooth embeddings that preserve the chosen
orientations at the origin and have the same centre are smoothly isotopic relative to that centre.
No orientation condition away from the origin is required.

```lean
TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  {ι : Type u_3} [Fintype ι]
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E M)
  (hcentre : f 0 = g 0) (o : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) E ι)
  (oM : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) M ι)
  (hf : o.IsOrientationPreservingAt oM (⇑f) 0) (hg : o.IsOrientationPreservingAt oM (⇑g) 0) :
  ∃ G, ∀ (t : ↑unitInterval), G (t, 0) = f 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The disc theorem in a manifold](../part-01/the-disc-theorem-in-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt)
- [Source of `TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_isOrientationPreservingAt` in TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.lean#L94)
