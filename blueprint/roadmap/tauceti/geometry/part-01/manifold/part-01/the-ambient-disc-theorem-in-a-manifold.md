---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos, TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt
statement: formalized
proof: formalized
---

# The ambient disc theorem in a manifold

Let `f` and `g` be smooth embeddings of `E` into a
Hausdorff, σ-compact boundaryless manifold modelled on `E`, with the same centre `f 0 = g 0` and
derivatives at `0` of the same orientation, compared in the chart at the centre. On every compact
subset `A` of `E`, `g` is `f` followed by the final diffeomorphism of a smooth diffeotopy of `M`
fixing every point outside a compact set.

```lean
TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M] [T2Space M]
  [SigmaCompactSpace M]
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E M)
  (hcentre : f 0 = g 0)
  (hdet :
    0 < (fderiv ℝ (↑(chartAt E (f 0)) ∘ ⇑f) 0).det * (fderiv ℝ (↑(chartAt E (f 0)) ∘ ⇑g) 0).det)
  {A : Set E} (hA : IsCompact A) :
  ∃ Φ K,
    IsCompact K ∧
      (∀ (t : ↑unitInterval), ∀ y ∉ K, (fun p => (Φ.toDiffeomorph p).2) (t, y) = y) ∧
        Set.EqOn (⇑Φ.final ∘ ⇑f) (⇑g) A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The disc theorem in a manifold](the-disc-theorem-in-a-manifold.md)
- [The inverse function theorem, with a `C^n` inverse on the whole target](../../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-with-a-c-n-inverse.md)
- [The relative ambient disc theorem](../part-02/the-relative-ambient-disc-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.html#TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos).

## Other forms

**The ambient disc theorem for oriented embeddings (Palais).** Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/Orientation.html#TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt).

```lean
TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_isOrientationPreservingAt.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  {ι : Type u_3} [Fintype ι] [T2Space M] [PreconnectedSpace M]
  (f g : TauCeti.SmoothEmbedding (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) E M)
  (o : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) E ι)
  (oM : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) M ι)
  (hf : o.IsOrientationPreservingAt oM (⇑f) 0) (hg : o.IsOrientationPreservingAt oM (⇑g) 0)
  {A : Set E} (hA : IsCompact A) :
  ∃ Φ K,
    IsCompact K ∧
      (∀ (t : ↑unitInterval), ∀ y ∉ K, (fun p => (Φ.toDiffeomorph p).2) (t, y) = y) ∧
        Set.EqOn (⇑Φ.final ∘ ⇑f) (⇑g) A
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.html#TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos)
- [Source of `TauCeti.SmoothEmbedding.exists_diffeotopy_eqOn_of_det_chartAt_mul_pos` in TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/SmoothIsotopy/DiscTheorem.lean#L158)
