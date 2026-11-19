---
declaration: theorem
origin: cited
lean: TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded
statement: formalized
proof: formalized
---

# TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded

A bounded open set whose frontier is a Jordan curve is the inside of that curve.

```lean
TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded {U : Set ℂ}
  (hUJ : TauCeti.IsJordanCurve (frontier U)) (hUo : IsOpen U) (hUb : Bornology.IsBounded U) :
  U = TauCeti.filledHull (frontier U) \ frontier U
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jordan curve theorem](the-jordan-curve-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Inside.html#TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded).

## Sources

- [Tau Ceti documentation: `TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PlaneSeparation/Inside.html#TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded)
- [Source of `TauCeti.IsJordanCurve.eq_filledHull_sdiff_of_isOpen_of_isBounded` in TauCeti/Analysis/Complex/PlaneSeparation/Inside.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/PlaneSeparation/Inside.lean#L212)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ConformalMapping/STATUS.md)
