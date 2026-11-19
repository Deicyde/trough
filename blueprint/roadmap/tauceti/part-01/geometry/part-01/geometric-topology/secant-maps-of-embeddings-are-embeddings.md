---
declaration: theorem
origin: cited
lean: TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision
statement: formalized
proof: formalized
---

# Secant maps of embeddings are embeddings

Let `f` be an injective `Cⁿ` star immersion,
`1 ≤ n`, of a complex on a finite vertex type into a normed space. For all sufficiently large
`k`, the secant map of `f` on the `k`-th edgewise subdivision, the map which agrees with `f` at
the points `edgewisePoint u` and is linear on every simplex of the subdivision, is a closed
embedding.

```lean
TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision.{u_1, u_2}
  {ι : Type u_1} {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E]
  {K : AbstractSimplicialComplex ι} {n : WithTop ℕ∞} {f : K.Realization → E} [LinearOrder ι]
  [Finite ι] (h : TauCeti.IsStarImmersion n f) (hn : 1 ≤ n) (hf : Function.Injective f) :
  ∀ᶠ (k : ℕ) in Filter.atTop,
    Topology.IsClosedEmbedding
      ((K.edgewiseSubdivision k).secantMap (f ∘ K.edgewiseSubdivisionRealizationMap k))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothTriangulation/StarImmersion.html#TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision).

## Sources

- [Tau Ceti documentation: `TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothTriangulation/StarImmersion.html#TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision)
- [Source of `TauCeti.IsStarImmersion.eventually_isClosedEmbedding_secantMap_edgewiseSubdivision` in TauCeti/Geometry/Manifold/SmoothTriangulation/StarImmersion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothTriangulation/StarImmersion.lean#L561)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricTopology/STATUS.md)
