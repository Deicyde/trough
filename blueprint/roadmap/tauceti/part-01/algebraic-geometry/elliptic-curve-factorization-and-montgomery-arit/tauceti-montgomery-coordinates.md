---
declaration: def
origin: cited
lean: TauCeti.Montgomery.coordinates
statement: formalized
---

# TauCeti.Montgomery.coordinates

The **coordinate pair** of a native point of the monic Montgomery model `model A B`: `(1, 0)`
at infinity and `(x', B)` at the affine point `(x', y')`, which stands for the Montgomery
coordinate `x = x' / B`. It is Mathlib's `xRep` with its second entry scaled by `B`.

```lean
TauCeti.Montgomery.coordinates.{u_1} {R : Type u_1} [CommRing R] (A B : R)
  (P : (TauCeti.Montgomery.model A B).toAffine.Point) : TauCeti.Montgomery.Pair R
```

## Depends on

- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.coordinates`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.coordinates).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.coordinates`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.coordinates)
- [Source of `TauCeti.Montgomery.coordinates` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean#L94)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
