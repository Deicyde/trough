---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff
statement: formalized
proof: formalized
---

# The cross-difference criterion for scalar multiples

For `B ≠ 0`, the coordinate pairs of
`[m] Q` and `[n] Q` have vanishing cross difference exactly when `[m - n] Q = 0` or
`[m + n] Q = 0`.

```lean
TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff.{u_1} {K : Type u_1} [Field K] {A B : K}
  [DecidableEq K] (hB : B ≠ 0) {Q : (TauCeti.Montgomery.model A B).toAffine.Point} {m n : ℤ} :
  (TauCeti.Montgomery.coordinates A B (m • Q)).cross (TauCeti.Montgomery.coordinates A B (n • Q)) =
      0 ↔
    (m - n) • Q = 0 ∨ (m + n) • Q = 0
```

## Depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)
- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff)
- [Source of `TauCeti.Montgomery.cross_coordinates_zsmul_eq_zero_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean#L262)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ECM/STATUS.md)
