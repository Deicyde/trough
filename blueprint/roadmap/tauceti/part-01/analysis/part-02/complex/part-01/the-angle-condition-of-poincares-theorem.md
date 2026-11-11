---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum
statement: formalized
proof: formalized
---

# The angle condition of Poincaré's theorem

If every angle of `P` is `π / m` for a natural
number `m`, then at each finite vertex of the double the order of the cycle transformation times
the cycle angle sum is `2π`.

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum
  {P : TauCeti.UpperHalfPlane.ConvexPolygon 3} {h₀ : P.interiorAngle 0 < Real.pi / 2}
  {h₁ : P.interiorAngle 1 < Real.pi / 2} (hP : ∀ (i : Fin 3), ∃ m, P.interiorAngle i = Real.pi / ↑m)
  (j : Fin 4) (z : UpperHalfPlane) (hz : (P.doubleTriangle h₀ h₁).vertex j = Sum.inl z) :
  ↑(orderOf ((P.doubleTriangleSidePairing h₀ h₁).cycleMap j)) *
      (P.doubleTriangleSidePairing h₀ h₁).cycleAngleSum j =
    2 * Real.pi
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Möbius difference formula](../../../../algebra/part-02/other-results/the-mobius-difference-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.html#TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum).

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.html#TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum)
- [Source of `TauCeti.UpperHalfPlane.ConvexPolygon.orderOf_doubleTriangleSidePairing_cycleMap_mul_cycleAngleSum` in TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/UpperHalfPlane/Polygon/SidePairing/DoubleTriangle.lean#L269)
