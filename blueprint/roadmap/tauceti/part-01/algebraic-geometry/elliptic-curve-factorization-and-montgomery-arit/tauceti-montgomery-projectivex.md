---
declaration: def
origin: cited
lean: TauCeti.Montgomery.projectiveX
statement: formalized
---

# TauCeti.Montgomery.projectiveX

The **projective `x`-coordinate** of a native point of `model A B` over a field, for
`B ≠ 0`: the point of the projective line `ℙ K (Fin 2 → K)` defined by its coordinate pair. It is
`(1 : 0)` at infinity and `(x' : B)` at the affine point `(x', y')`.

```lean
TauCeti.Montgomery.projectiveX.{u_1} {K : Type u_1} [Field K] {B : K} (A : K) (hB : B ≠ 0)
  (P : (TauCeti.Montgomery.model A B).toAffine.Point) : Projectivization K (Fin 2 → K)
```

## Depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)
- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.projectiveX`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.projectiveX).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.projectiveX`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.projectiveX)
- [Source of `TauCeti.Montgomery.projectiveX` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean#L214)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ECM/STATUS.md)
