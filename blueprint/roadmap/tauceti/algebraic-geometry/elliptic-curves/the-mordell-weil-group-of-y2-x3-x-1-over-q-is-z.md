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

- [Brill's theorem, parity form](../../number-theory/part-02/number-field/brills-theorem-parity-form.md)
- [The Mordell–Weil rank bound from the 2-Selmer group](../elliptic-curve/part-01/the-mordell-weil-rank-bound-from-the-2-selmer-gr.md)
- [The Mordell–Weil theorem](the-mordell-weil-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/part-01/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.html#TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne).

## Sources

- [Tau Ceti documentation: `TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.html#TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne)
- [Source of `TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.lean#L181)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
