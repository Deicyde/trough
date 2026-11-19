---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.double_coordinates
statement: formalized
proof: formalized
---

# Correctness of Montgomery doubling on native points

For nonzero `D` and `4N = (A + 2)D`,
the output is nonzero and has vanishing cross difference with the coordinate pair of `P + P`. No
ellipticity assumption is needed, nor `B ≠ 0`: for `B = 0` the model is the cusp `y² = x³`. In
characteristic two, the scaled relation and `D ≠ 0` force `A = 0`, so only that degenerate model
is covered.

```lean
TauCeti.Montgomery.double_coordinates.{u_1} {K : Type u_1} [Field K] [DecidableEq K] {A B N D : K}
  (hD : D ≠ 0) (h : 4 * N = (A + 2) * D) (P : (TauCeti.Montgomery.model A B).toAffine.Point) :
  TauCeti.Montgomery.double N D (TauCeti.Montgomery.coordinates A B P) ≠ 0 ∧
    (TauCeti.Montgomery.double N D (TauCeti.Montgomery.coordinates A B P)).cross
        (TauCeti.Montgomery.coordinates A B (P + P)) =
      0
```

## Depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)
- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.double_coordinates`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Double.html#TauCeti.Montgomery.double_coordinates).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.double_coordinates`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Double.html#TauCeti.Montgomery.double_coordinates)
- [Source of `TauCeti.Montgomery.double_coordinates` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Double.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Double.lean#L122)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ECM/STATUS.md)
