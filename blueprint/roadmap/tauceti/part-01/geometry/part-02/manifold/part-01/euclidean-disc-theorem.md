---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos, TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_pos
statement: formalized
proof: formalized
---

# Euclidean disc theorem

Smooth self-embeddings with a common centre and the
same derivative orientation there are smoothly isotopic relative to that centre.
The determinant condition permits either common orientation and includes dimension zero.

```lean
TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E E)
  (hcentre : f 0 = g 0) (hdet : 0 < (fderiv ℝ (⇑f) 0).det * (fderiv ℝ (⇑g) 0).det) :
  ∃ G, ∀ (t : ↑unitInterval), G (t, 0) = f 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos).

## Other forms

**Euclidean disc theorem.** Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_pos).

```lean
TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_pos.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {F : Type u_2}
  [NormedAddCommGroup F] [NormedSpace ℝ F]
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) (↑⊤) E F)
  (hcentre : f 0 = g 0) (Lf Lg : E ≃L[ℝ] F) (hLf : HasFDerivAt (⇑f) (↑Lf) 0)
  (hLg : HasFDerivAt (⇑g) (↑Lg) 0) (hrelative : 0 < (↑(Lf.trans Lg.symm)).det) :
  ∃ G, ∀ (t : ↑unitInterval), G (t, 0) = f 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos)
- [Source of `TauCeti.SmoothEmbedding.exists_smoothIsotopy_of_det_mul_pos` in TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.lean#L128)
