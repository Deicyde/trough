---
declaration: theorem
origin: cited
lean: TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt
statement: formalized
proof: formalized
---

# The connected sum of oriented manifolds is well defined

Let `M` and `N` be connected,
Hausdorff, σ-compact smooth manifolds without boundary modelled on a nontrivial finite-dimensional
real inner product space `E`, with orientations `oM` and `oN`. Let `e₁ : E → M` and `e₂ : E → N`
be coordinate balls inducing opposite orientations of `E` at `0`: `e₁` preserves orientation from
an orientation `o` of `E` to `oM`, and `e₂` reverses it from `o` to `oN`. Let `e₁'` and `e₂'` be
another such pair, for a possibly different orientation `o'` of `E`. All balls are open embeddings
and smooth local diffeomorphisms. Then the connected sum along `e₁` and `e₂` is diffeomorphic to
the connected sum along `e₁'` and `e₂'`.

```lean
TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt.{u_1, u_2, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  {M : Type u_2} [TopologicalSpace M] [T2Space M] [PreconnectedSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M] {N : Type u_3} [TopologicalSpace N] [T2Space N]
  [PreconnectedSpace N] [ChartedSpace E N] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) N]
  {ι : Type u_4} [Fintype ι] [Nontrivial E] {e₁ e₁' : E → M} {e₂ e₂' : E → N}
  (h₁ : Topology.IsOpenEmbedding e₁) (h₂ : Topology.IsOpenEmbedding e₂)
  (h₁' : Topology.IsOpenEmbedding e₁') (h₂' : Topology.IsOpenEmbedding e₂')
  (d₁ : IsLocalDiffeomorph (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) e₁)
  (d₂ : IsLocalDiffeomorph (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) e₂)
  (d₁' : IsLocalDiffeomorph (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) e₁')
  (d₂' : IsLocalDiffeomorph (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (↑⊤) e₂')
  (o o' : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) E ι)
  (oM : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) M ι)
  (oN : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) N ι)
  (hf₁ : o.IsOrientationPreservingAt oM e₁ 0) (hf₂ : o.IsOrientationReversingAt oN e₂ 0)
  (hf₁' : o'.IsOrientationPreservingAt oM e₁' 0) (hf₂' : o'.IsOrientationReversingAt oN e₂' 0) :
  Nonempty
    (Diffeomorph (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ E) (TauCeti.ConnectedSum e₁ e₂)
      (TauCeti.ConnectedSum e₁' e₂') ↑⊤)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The ambient disc theorem in a manifold](../../geometry/part-02/manifold/part-01/the-ambient-disc-theorem-in-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ConnectedSum/Independence.html#TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt).

## Sources

- [Tau Ceti documentation: `TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ConnectedSum/Independence.html#TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt)
- [Source of `TauCeti.ConnectedSum.nonempty_diffeomorph_of_isOrientationReversingAt` in TauCeti/Geometry/Manifold/ConnectedSum/Independence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/ConnectedSum/Independence.lean#L108)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricTopology/STATUS.md)
