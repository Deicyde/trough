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
- [Source of `TauCeti.Montgomery.orbitRelQuotientEquivRangeProjectiveX` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Coordinates.lean#L305)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ECM/STATUS.md)
