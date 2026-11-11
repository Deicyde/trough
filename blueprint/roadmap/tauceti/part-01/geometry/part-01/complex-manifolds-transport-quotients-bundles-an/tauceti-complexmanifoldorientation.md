---
declaration: def
origin: cited
lean: TauCeti.complexManifoldOrientation
statement: formalized
---

# TauCeti.complexManifoldOrientation

The canonical orientation of a complex manifold `M` modelled on `𝓘(ℂ, E)`, as a manifold
orientation of its underlying real manifold. Every holomorphic chart carries it to the canonical
real orientation `TauCeti.complexOrientation E` of the model
(`TauCeti.map_orientationAt_complexManifoldOrientation`).

```lean
TauCeti.complexManifoldOrientation.{u_1, u_2} (E : Type u_1) [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] (M : Type u_2) [TopologicalSpace M] [ChartedSpace E M]
  [IsManifold (modelWithCornersSelf ℂ E) 1 M] :
  TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) M (Fin (2 * Module.finrank ℂ E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ModelWithCorners.restrictScalars](modelwithcorners-restrictscalars.md)
- [TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero](tauceti-orientationpreservingon-iff-det-fderiv-n.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.complexManifoldOrientation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Orientation.html#TauCeti.complexManifoldOrientation).

## Sources

- [Tau Ceti documentation: `TauCeti.complexManifoldOrientation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Orientation.html#TauCeti.complexManifoldOrientation)
- [Source of `TauCeti.complexManifoldOrientation` in TauCeti/Geometry/Manifold/Complex/Orientation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/Orientation.lean#L261)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
