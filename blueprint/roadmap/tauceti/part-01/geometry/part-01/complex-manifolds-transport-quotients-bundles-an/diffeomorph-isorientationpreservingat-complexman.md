---
declaration: theorem
origin: cited
lean: Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation
statement: formalized
proof: formalized
---

# Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation

Biholomorphisms preserve canonical orientations: at every point `x`, the derivative of a
`C^n` biholomorphism `Φ : M → N`, for `n ≠ 0`, carries the canonical orientation of `M` at `x` to
that of `N` at `Φ x`.

```lean
Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℂ E) 1 M] {N : Type u_3}
  [TopologicalSpace N] [ChartedSpace E N] [IsManifold (modelWithCornersSelf ℂ E) 1 N]
  (n : WithTop ℕ∞) [NeZero n] [IsManifold (modelWithCornersSelf ℂ E) n M]
  [IsManifold (modelWithCornersSelf ℂ E) n N]
  (Φ : Diffeomorph (modelWithCornersSelf ℂ E) (modelWithCornersSelf ℂ E) M N n) (x : M) :
  (TauCeti.complexManifoldOrientation E M).IsOrientationPreservingAt
    (TauCeti.complexManifoldOrientation E N) (⇑Φ) x
```

## Depends on

- [TauCeti.complexManifoldOrientation](tauceti-complexmanifoldorientation.md)

## Proof depends on

- [ModelWithCorners.restrictScalars](modelwithcorners-restrictscalars.md)
- [TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero](tauceti-orientationpreservingon-iff-det-fderiv-n.md)

## Lean

Formalized in Tau Ceti as [`Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Orientation.html#Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation).

## Sources

- [Tau Ceti documentation: `Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Orientation.html#Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation)
- [Source of `Diffeomorph.isOrientationPreservingAt_complexManifoldOrientation` in TauCeti/Geometry/Manifold/Complex/Orientation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Complex/Orientation.lean#L437)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexManifolds/STATUS.md)
