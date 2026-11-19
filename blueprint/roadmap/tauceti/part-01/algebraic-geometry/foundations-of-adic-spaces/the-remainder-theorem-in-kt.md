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

- [TauCeti.IsNormMulUnit](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.html#TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.html#TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom)
- [Source of `TauCeti.ValuationSpectrum.weightedX_sub_weightedC_dvd_sub_weightedC_evalAtHom` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Spa/Polydisc/ClassicalPoint.lean#L74)
