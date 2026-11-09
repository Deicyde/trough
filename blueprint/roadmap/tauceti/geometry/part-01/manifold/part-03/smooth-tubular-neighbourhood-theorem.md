---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset
statement: formalized
proof: formalized
---

# Smooth tubular neighbourhood theorem

The entire intrinsic normal bundle of a
smooth embedding is diffeomorphic to an arbitrarily small open neighbourhood of its image,
with the zero section sent to the embedding. No Riemannian metric is part of the input or
output, and the image need not be closed or compact.

```lean
TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset.{u_1, u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} {V : Type u_2} {P : Type u_3} {H : Type u_4} {G : Type u_5} {M : Type u_6}
  {N : Type u_7} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup P]
  [NormedSpace ℝ P] [FiniteDimensional ℝ P] [TopologicalSpace H] [TopologicalSpace G]
  {I : ModelWithCorners ℝ E H} {J : ModelWithCorners ℝ V G} [I.Boundaryless] [J.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [TopologicalSpace N]
  [ChartedSpace G N] [IsManifold J (↑⊤) N] [T2Space N] [SecondCountableTopology N]
  (f : TauCeti.SmoothEmbedding I J (↑⊤) M N)
  (hdim : Module.finrank ℝ P = Module.finrank ℝ V - Module.finrank ℝ E) {O : Set N} (hO : IsOpen O)
  (hfO : Set.range ⇑f ⊆ O) :
  have hn := TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset._proof_1;
  ∃ W, ↑W ⊆ O ∧ ∃ Φ, ∀ (x : M), ↑(Φ (Bundle.zeroSection P (fun x => f.NormalSpace x hn) x)) = f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Smooth Riemannian tubular neighbourhood theorem](smooth-riemannian-tubular-neighbourhood-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Existence.html#TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Existence.html#TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset)
- [Source of `TauCeti.SmoothEmbedding.exists_diffeomorph_normalBundle_subset` in TauCeti/Geometry/Manifold/TubularNeighborhood/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/TubularNeighborhood/Existence.lean#L49)
