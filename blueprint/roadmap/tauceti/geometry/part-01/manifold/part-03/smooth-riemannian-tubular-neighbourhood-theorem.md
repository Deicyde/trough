---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset
statement: formalized
proof: formalized
---

# Smooth Riemannian tubular neighbourhood theorem

The entire intrinsic normal bundle
of a smooth embedding is diffeomorphic to an open neighbourhood inside any prescribed open
neighbourhood of its image. The zero section is sent to the original embedding. Neither
compactness nor closedness of the embedded image nor completeness of the ambient metric
is required.

```lean
TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset.{u_1, u_2, u_3, u_4, u_5,
    u_6, u_7}
  {E : Type u_1} {V : Type u_2} {P : Type u_3} {H : Type u_4} {G : Type u_5} {M : Type u_6}
  {N : Type u_7} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup P]
  [NormedSpace ℝ P] [FiniteDimensional ℝ P] [TopologicalSpace H] [TopologicalSpace G]
  {I : ModelWithCorners ℝ E H} {J : ModelWithCorners ℝ V G} [TopologicalSpace M] [ChartedSpace H M]
  [TopologicalSpace N] [ChartedSpace G N] [IsManifold J (↑⊤) N] [I.Boundaryless] [J.Boundaryless]
  [T2Space N] [Bundle.RiemannianBundle fun y => TangentSpace J y]
  [IsContMDiffRiemannianBundle J (↑⊤) V fun y => TangentSpace J y] [IsManifold I (↑⊤) M]
  [SecondCountableTopology N] (f : TauCeti.SmoothEmbedding I J (↑⊤) M N)
  (hdim : Module.finrank ℝ P = Module.finrank ℝ V - Module.finrank ℝ E) {O : Set N} (hO : IsOpen O)
  (hfO : Set.range ⇑f ⊆ O) :
  have hn := TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset._proof_1;
  ∃ W, ↑W ⊆ O ∧ ∃ Φ, ∀ (x : M), ↑(Φ (Bundle.zeroSection P (fun x => f.NormalSpace x hn) x)) = f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../part-02/the-koszul-formula.md)
- [TauCeti.CotangentBundle](../../symplectic-geometry-and-hamiltonian-mechanics/tauceti-cotangentbundle.md)
- [TauCeti.Manifold.riemannianExp](../../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Coordinates.html#TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Coordinates.html#TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset)
- [Source of `TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_riemannian_subset` in TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Coordinates.lean#L141)
