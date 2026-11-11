---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip
statement: formalized
proof: formalized
---

# Gauss–Bonnet for the triangles of the fan from `∞`

If `vertex 0` is `∞`, the part of
the carrier between the verticals through `vertex i` and `vertex (i + 1)`, for an side `i` not
ending at `∞`, has area `π` minus the angles at `vertex i` and `vertex (i + 1)` of the triangle
with vertices `∞`, `vertex i`, `vertex (i + 1)`. That part of the carrier is this triangle by
`exists_carrier_inter_strip_eq`.

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip {n : ℕ} [NeZero n]
  (P : TauCeti.UpperHalfPlane.ConvexPolygon n) (h₀ : P.vertex 0 = Sum.inr OnePoint.infty)
  {i : Fin n} (hi : i ≠ 0) (hi' : i + 1 ≠ 0) :
  MeasureTheory.volume
      (P.carrier ∩
        {z |
          (TauCeti.UpperHalfPlane.toComplex (P.vertex i)).re ≤ z.re ∧
            z.re ≤ (TauCeti.UpperHalfPlane.toComplex (P.vertex (i + 1))).re}) =
    ENNReal.ofReal
      (Real.pi -
          TauCeti.UpperHalfPlane.vertexAngle (P.vertex i) (Sum.inr OnePoint.infty)
            (P.vertex (i + 1)) -
        TauCeti.UpperHalfPlane.vertexAngle (P.vertex (i + 1)) (P.vertex i) (Sum.inr OnePoint.infty))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Möbius difference formula](../../../../algebra/part-02/other-results/the-mobius-difference-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/Convex/NormalForm.html#TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip).

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/Convex/NormalForm.html#TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip)
- [Source of `TauCeti.UpperHalfPlane.ConvexPolygon.volume_carrier_inter_strip` in TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/Convex/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/Convex/NormalForm.lean#L253)
