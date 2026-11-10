---
declaration: def
origin: cited
lean: TauCeti.ProjValMeasure.integral
statement: formalized
---

# TauCeti.ProjValMeasure.integral

The **integral** of a bounded Borel symbol against a projection-valued measure `P`,
`P.integral f = ∫ f dP`, as a unital star algebra homomorphism. It is characterised by
`integral_ofSimpleFunc` on simple symbols and its continuity (`continuous_integral`); see
`eq_integral_of_continuous`.

```lean
TauCeti.ProjValMeasure.integral.{u_1, u_2} {X : Type u_1} {H : Type u_2} [MeasurableSpace X]
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
  (P : TauCeti.ProjValMeasure X H) : TauCeti.BoundedBorelFunction X →⋆ₐ[ℂ] H →L[ℂ] H
```

## Depends on

- [TauCeti.ProjValMeasure](tauceti-projvalmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ProjValMeasure.integral`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Integral.html#TauCeti.ProjValMeasure.integral).

## Sources

- [Tau Ceti documentation: `TauCeti.ProjValMeasure.integral`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Integral.html#TauCeti.ProjValMeasure.integral)
- [Source of `TauCeti.ProjValMeasure.integral` in TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/ProjValMeasure/Integral.lean#L216)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
