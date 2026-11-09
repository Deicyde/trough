---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap
statement: formalized
proof: formalized
---

# The cusp condition of Poincaré's theorem

The cycle transformations at the ideal vertices
of the double are parabolic.

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap
  {P : TauCeti.UpperHalfPlane.ConvexPolygon 3} {h₀ : P.interiorAngle 0 < Real.pi / 2}
  {h₁ : P.interiorAngle 1 < Real.pi / 2} (j : Fin 4) (ξ : OnePoint ℝ)
  (hξ : (P.doubleTriangle h₀ h₁).vertex j = Sum.inr ξ) :
  ((P.doubleTriangleSidePairing h₀ h₁).cycleMap j).IsParabolic
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.html#TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap).

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.html#TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap)
- [Source of `TauCeti.UpperHalfPlane.ConvexPolygon.isParabolic_doubleTriangleSidePairing_cycleMap` in TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.lean#L286)
