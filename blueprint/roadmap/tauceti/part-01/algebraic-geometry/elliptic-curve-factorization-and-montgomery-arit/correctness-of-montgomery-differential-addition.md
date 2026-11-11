---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.diffAdd_coordinates
statement: formalized
proof: formalized
---

# Correctness of Montgomery differential addition on native points

Over a field with
`2 ≠ 0` and for `B ≠ 0`, differential addition of the coordinate pairs of `P`, `Q` and `P - Q`
has vanishing cross difference with the coordinate pair of `P + Q`, and it is nonzero exactly
when `P - Q` is neither the point at infinity nor the distinguished point of order two `(0, 0)`.
No ellipticity assumption is needed.

```lean
TauCeti.Montgomery.diffAdd_coordinates.{u_1} {K : Type u_1} [Field K] [DecidableEq K] {A B : K}
  (h₂ : 2 ≠ 0) (hB : B ≠ 0) (P Q : (TauCeti.Montgomery.model A B).toAffine.Point) :
  (TauCeti.Montgomery.diffAdd (TauCeti.Montgomery.coordinates A B P)
            (TauCeti.Montgomery.coordinates A B Q)
            (TauCeti.Montgomery.coordinates A B (P - Q))).cross
        (TauCeti.Montgomery.coordinates A B (P + Q)) =
      0 ∧
    (TauCeti.Montgomery.diffAdd (TauCeti.Montgomery.coordinates A B P)
          (TauCeti.Montgomery.coordinates A B Q) (TauCeti.Montgomery.coordinates A B (P - Q)) ≠
        0 ↔
      P - Q ≠ 0 ∧ P - Q ≠ TauCeti.Montgomery.twoTorsionPoint A hB)
```

## Depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)
- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.diffAdd_coordinates`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/DiffAdd.html#TauCeti.Montgomery.diffAdd_coordinates).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.diffAdd_coordinates`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/DiffAdd.html#TauCeti.Montgomery.diffAdd_coordinates)
- [Source of `TauCeti.Montgomery.diffAdd_coordinates` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/DiffAdd.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/DiffAdd.lean#L221)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
