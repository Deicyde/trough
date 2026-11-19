---
declaration: def
origin: cited
lean: TauCeti.manifoldDiffeology
statement: formalized
---

# TauCeti.manifoldDiffeology

The standard diffeology of a finite-dimensional boundaryless real smooth manifold.
Its plots are smooth manifold maps, and its D-topology is the given topology.

```lean
TauCeti.manifoldDiffeology.{u_1, u_2} (E : Type u_1) [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] (M : Type u_2) [tM : TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M] : DiffeologicalSpace M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.manifoldDiffeology`](https://taucetiproject.org/docs/TauCeti/Geometry/Diffeology/Manifold.html#TauCeti.manifoldDiffeology).

## Sources

- [Tau Ceti documentation: `TauCeti.manifoldDiffeology`](https://taucetiproject.org/docs/TauCeti/Geometry/Diffeology/Manifold.html#TauCeti.manifoldDiffeology)
- [Source of `TauCeti.manifoldDiffeology` in TauCeti/Geometry/Diffeology/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Diffeology/Manifold.lean#L45)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
