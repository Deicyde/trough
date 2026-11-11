---
declaration: def
origin: cited
lean: TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX
statement: formalized
---

# The quotient of the native point group by negation is the image of the projective `x`-coordinate

`projectiveX` induces a bijection from the orbit quotient of the sign action of
`ℤˣ` onto its range.

```lean
TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX.{u_1} {K : Type u_1} [Field K] {A B : K}
  [DecidableEq K] (hB : B ≠ 0) :
  MulAction.orbitRel.Quotient ℤˣ (TauCeti.Montgomery.model A B).toAffine.Point ≃
    ↑(Set.range (TauCeti.Montgomery.projectiveX A hB))
```

## Depends on

- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)
- [TauCeti.Montgomery.projectiveX](tauceti-montgomery-projectivex.md)

## Proof depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.html#TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX)
- [Source of `TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean#L288)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
