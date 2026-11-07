---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat
statement: formalized
---

# The anti-equivalence between regular proper curves and algebraic function fields

over a
field `k`: the function-field functor `X ↦ k(X)` is an equivalence
`RegularProperCurveCat k ≌ (FunctionFieldCat k)ᵒᵖ` with inverse the model functor
`F ↦ twoChartModel F`.

```lean
TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat.{u} (k : Type u) [Field k] :
  TauCeti.AlgebraicGeometry.RegularProperCurveCat k ≌ (TauCeti.FunctionFieldCat k)ᵒᵖ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Ring.IsJapanese](../../part-06/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.html#TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.html#TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat)
- [Source of `TauCeti.AlgebraicGeometry.RegularProperCurveCat.equivFunctionFieldCat` in TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.lean#L292)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
