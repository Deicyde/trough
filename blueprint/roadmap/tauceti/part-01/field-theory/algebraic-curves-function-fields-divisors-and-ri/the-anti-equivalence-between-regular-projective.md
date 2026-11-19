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

- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem](../function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.html#TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.html#TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat)
- [Source of `TauCeti.AlgebraicGeometry.RegularProjectiveCurveCat.equivFunctionFieldCat` in TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/AntiEquivalence.lean#L386)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
