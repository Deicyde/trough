---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.volume_triangle, TauCeti.UpperHalfPlane.CompactConvexPolygon.volume_carrier, TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier
statement: formalized
proof: formalized
---

# The Gauss–Bonnet formula

the invariant area of a hyperbolic triangle is its angular
defect `π - α - β - γ`.

```lean
TauCeti.UpperHalfPlane.volume_triangle {A B C : UpperHalfPlane} (hAB : A ≠ B)
  (hC :
    C ∉
      Set.range
        (TauCeti.UpperHalfPlane.geodesicLine (TauCeti.UpperHalfPlane.geodesicBetween A B))) :
  MeasureTheory.volume (A.triangle B C) =
    ENNReal.ofReal (Real.pi - A.interiorAngle B C - B.interiorAngle C A - C.interiorAngle A B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gauss–Bonnet for the triangles of the fan from `∞`](gauss-bonnet-for-the-triangles-of-the-fan-from.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.volume_triangle`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Triangle.html#TauCeti.UpperHalfPlane.volume_triangle).

## Other forms

**The Gauss–Bonnet formula for compact convex hyperbolic polygons.** Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.CompactConvexPolygon.volume_carrier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/GaussBonnet.html#TauCeti.UpperHalfPlane.CompactConvexPolygon.volume_carrier).

```lean
TauCeti.UpperHalfPlane.CompactConvexPolygon.volume_carrier {n : ℕ} [NeZero n]
  (P : TauCeti.UpperHalfPlane.CompactConvexPolygon n) :
  MeasureTheory.volume P.carrier = ENNReal.ofReal ((↑n - 2) * Real.pi - ∑ i, P.interiorAngle i)
```

**The Gauss–Bonnet formula for convex hyperbolic polygons with ideal vertices.** Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/Convex/GaussBonnet.html#TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier).

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier {n : ℕ} [NeZero n]
  (P : TauCeti.UpperHalfPlane.ConvexPolygon n) :
  MeasureTheory.volume P.carrier = ENNReal.ofReal ((↑n - 2) * Real.pi - ∑ i, P.interiorAngle i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.volume_triangle`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Triangle.html#TauCeti.UpperHalfPlane.volume_triangle)
- [Source of `TauCeti.UpperHalfPlane.volume_triangle` in TauCeti/Analysis/Complex/UpperHalfPlane/Triangle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/UpperHalfPlane/Triangle.lean#L656)
