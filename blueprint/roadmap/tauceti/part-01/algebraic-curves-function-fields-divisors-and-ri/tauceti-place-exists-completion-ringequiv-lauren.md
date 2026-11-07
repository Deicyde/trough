---
declaration: theorem
origin: cited
lean: TauCeti.Place.exists_completion_ringEquiv_laurentSeries
statement: formalized
proof: formalized
---

# TauCeti.Place.exists\_completion\_ringEquiv\_laurentSeries

**At every place the completion is `F_P((T))`**, separable residue field or not: some
isomorphism of the completion with the Laurent-series field over the residue field carries the
valuation of `P` to the `T`-adic valuation. When `F_P` is inseparable over `k` there may be no
`k`-linear such isomorphism (`TauCeti.Place.isEmpty_completion_algEquiv_laurentSeries`).

```lean
TauCeti.Place.exists_completion_ringEquiv_laurentSeries.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] (P : TauCeti.Place k F) :
  ∃ e, ∀ (x : P.Completion), Valued.v (e x) = P.completionPlace.valuation x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.exists_completion_ringEquiv_laurentSeries`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/CoefficientField.html#TauCeti.Place.exists_completion_ringEquiv_laurentSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.exists_completion_ringEquiv_laurentSeries`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/CoefficientField.html#TauCeti.Place.exists_completion_ringEquiv_laurentSeries)
- [Source of `TauCeti.Place.exists_completion_ringEquiv_laurentSeries` in TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/CoefficientField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Expansion/Laurent/CoefficientField.lean#L142)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
