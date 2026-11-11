---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset
statement: formalized
proof: formalized
---

# Closed normal disc theorem for a closed smooth submanifold

The normal exponential
embeds closed discs and spheres of a positive smooth radius as closed subsets of any prescribed
open neighbourhood of the core. The open discs embed openly. The core may be noncompact,
and the ambient Riemannian metric need not be complete.

```lean
TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset.{u_1, u_2, u_3, u_4, u_5,
    u_6, u_7}
  {E : Type u_1} {V : Type u_2} {P : Type u_3} {H : Type u_4} {G : Type u_5} {M : Type u_6}
  {N : Type u_7} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] [NormedAddCommGroup P]
  [NormedSpace ℝ P] [FiniteDimensional ℝ P] [TopologicalSpace H] [TopologicalSpace G]
  {I : ModelWithCorners ℝ E H} {J : ModelWithCorners ℝ V G} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [TopologicalSpace N] [ChartedSpace G N] [IsManifold J (↑⊤) N]
  [I.Boundaryless] [J.Boundaryless] [T2Space N] [SecondCountableTopology N]
  [Bundle.RiemannianBundle fun y => TangentSpace J y]
  [IsContMDiffRiemannianBundle J (↑⊤) V fun y => TangentSpace J y]
  (f : TauCeti.SmoothEmbedding I J (↑⊤) M N) (hclosed : IsClosed (Set.range ⇑f))
  (hdim : Module.finrank ℝ P = Module.finrank ℝ V - Module.finrank ℝ E) {O : Set N} (hO : IsOpen O)
  (hfO : Set.range ⇑f ⊆ O) {ε : M → ℝ} (hε : Continuous ε) (hεpos : ∀ (x : M), 0 < ε x) :
  have hn := TauCeti.SmoothEmbedding.exists_partialDiffeomorph_normalExp_norm_le_subset._proof_1;
  let ν := fun x => f.NormalSpace x hn;
  ∃ r,
    (∀ (x : M), 0 < r x) ∧
      (∀ (x : M), r x < ε x) ∧
        {p | ‖p.snd‖ ≤ r p.proj} ⊆ f.normalExpDomain hn ∧
          f.normalExp hn '' {p | ‖p.snd‖ ≤ r p.proj} ⊆ O ∧
            Topology.IsOpenEmbedding ({p | ‖p.snd‖ < r p.proj}.domRestrict (f.normalExp hn)) ∧
              Topology.IsClosedEmbedding ({p | ‖p.snd‖ ≤ r p.proj}.domRestrict (f.normalExp hn)) ∧
                Topology.IsClosedEmbedding ({p | ‖p.snd‖ = r p.proj}.domRestrict (f.normalExp hn))
```

## Depends on

- [TauCeti.Manifold.riemannianExp](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Proof depends on

- [The inverse function theorem for manifolds](../part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Noncompact.html#TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Noncompact.html#TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset)
- [Source of `TauCeti.SmoothEmbedding.exists_isClosedEmbedding_normalExp_norm_le_subset` in TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Noncompact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/TubularNeighborhood/Riemannian/Noncompact.lean#L107)
