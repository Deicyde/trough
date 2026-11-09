---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball
statement: formalized
proof: formalized
---

# The disc theorem in a ball

Smooth self-embeddings with values in a Euclidean ball, centred
at its centre, with the same derivative orientation there, are smoothly isotopic relative to the
centre through embeddings with values in the ball.

```lean
TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {c : E} {r : ℝ} (hr : 0 < r)
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E E)
  (hf0 : f 0 = c) (hg0 : g 0 = c) (hf : ∀ (x : E), f x ∈ Euclidean.ball c r)
  (hg : ∀ (x : E), g x ∈ Euclidean.ball c r)
  (hdet : 0 < (fderiv ℝ (⇑f) 0).det * (fderiv ℝ (⇑g) 0).det) :
  ∃ L, (∀ (q : ↑unitInterval × E), L q ∈ Euclidean.ball c r) ∧ ∀ (t : ↑unitInterval), L (t, 0) = c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euclidean disc theorem](euclidean-disc-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.html#TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball)
- [Source of `TauCeti.SmoothEmbedding.exists_smoothIsotopy_mapsTo_ball` in TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/SmoothIsotopy/Euclidean.lean#L159)
