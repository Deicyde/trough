---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat
statement: formalized
---

# The anti-equivalence between regular projective curves and algebraic function fields over a field `k`

the functor sending a regular projective curve `X` to its function field `k(X)` and a
dominant `k`-morphism to the pullback of rational functions along it is an equivalence
`RegularProjectiveCurveCat k ≌ (FunctionFieldCat k)ᵒᵖ`. Its inverse sends a function field to its
two-chart model, the normalization of the projective line in it.

```lean
TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat.{u} (k : Type u)
  [Field k] : TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat k ≌ (TauCeti.FunctionFieldCat k)ᵒᵖ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A regular proper curve is projective](a-regular-proper-curve-is-projective.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.html#TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.html#TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat)
- [Source of `TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat` in TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.lean#L392)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
