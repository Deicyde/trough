---
declaration: theorem
origin: cited
lean: TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero
statement: formalized
proof: formalized
---

# TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero

A holomorphic map on an open subset of a finite-dimensional complex vector space preserves the
real orientation exactly where its complex derivative has nonzero determinant: its real Jacobian
determinant is the squared modulus of the complex one.

```lean
TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] {f : E → E} {s : Set E} (hs : IsOpen s)
  (hf : DifferentiableOn ℂ f s) :
  TauCeti.OrientationPreservingOn (modelWithCornersSelf ℝ E) f s ↔
    ∀ x ∈ s, LinearMap.det ↑(fderiv ℂ f x) ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Orientation.html#TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Orientation.html#TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero)
- [Source of `TauCeti.orientationPreservingOn_iff_det_fderiv_ne_zero` in TauCeti/Geometry/Manifold/Complex/Orientation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/Orientation.lean#L174)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexManifolds/STATUS.md)
