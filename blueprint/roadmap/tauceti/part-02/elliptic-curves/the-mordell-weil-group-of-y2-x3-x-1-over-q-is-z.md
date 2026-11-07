---
declaration: theorem
origin: cited
lean: TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne
statement: formalized
proof: formalized
---

# The Mordell–Weil group of `y² = x³ - x + 1` over `ℚ` is `ℤ`

It is finitely generated,
torsion-free and of rank one.

```lean
TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne :
  Nonempty ((TauCeti.WorkedExamples.curveX3SubXAddOne.baseChange ℚ).toAffine.Point ≃+ ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mordell–Weil theorem](the-mordell-weil-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.html#TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne).

## Sources

- [Tau Ceti documentation: `TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.html#TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne)
- [Source of `TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.lean#L181)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
