---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos
statement: formalized
proof: formalized
---

# The disc theorem in a manifold

Two smooth embeddings of `E` into a boundaryless manifold
modelled on `E`, with the same centre `f 0 = g 0` and derivatives at `0` of the same orientation,
are smoothly isotopic relative to that centre. The orientations are compared in the chart at the
centre: the product of the derivative determinants there is positive. This condition does not
depend on the chart, since a change of chart multiplies both determinants by the same nonzero
number. For `M = E` it is the hypothesis of the Euclidean disc theorem
`TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos`.

```lean
TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E M)
  (hcentre : f 0 = g 0)
  (hdet :
    0 < (fderiv ℝ (↑(chartAt E (f 0)) ∘ ⇑f) 0).det * (fderiv ℝ (↑(chartAt E (f 0)) ∘ ⇑g) 0).det) :
  ∃ G, ∀ (t : ↑unitInterval), G (t, 0) = f 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The disc theorem in a ball](the-disc-theorem-in-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos)
- [Source of `TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_chartAt_mul_pos` in TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.lean#L102)
