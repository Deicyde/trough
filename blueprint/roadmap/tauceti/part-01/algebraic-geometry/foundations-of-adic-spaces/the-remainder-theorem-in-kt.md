---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom
statement: formalized
proof: formalized
---

# The remainder theorem in `K⟨T⟩`

For `a` in the closed unit disc (power-bounded, that is
`‖a‖ ≤ 1`), `T - a` divides `f - f(a)` for every restricted power series `f` in one variable over
a complete nonarchimedean field. This is the analogue of Mathlib's
`Polynomial.X_sub_C_dvd_sub_C_eval`.

```lean
TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom.{u_1} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [NonarchimedeanRing K] [CompleteSpace K] (a : Fin 1 → K)
  (ha : ∀ (i : Fin 1), TauCeti.Huber.IsPowerBounded (a i))
  (f : ↥(TauCeti.Huber.weightedRestrictedSubring (fun x => {1}) ⋯)) :
  TauCeti.Huber.weightedX (fun x => {1}) ⋯ 0 - (TauCeti.Huber.weightedC (fun x => {1}) ⋯) (a 0) ∣
    f - (TauCeti.Huber.weightedC (fun x => {1}) ⋯) ((TauCeti.ValuationSpectrum.evalAtHom a ha) f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.html#TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.html#TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom)
- [Source of `TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.lean#L74)
