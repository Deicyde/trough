---
declaration: theorem
origin: cited
lean: PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast
statement: formalized
proof: formalized
---

# Cauchy–Hadamard for entire series

The `n`-th roots `‖aₙ‖ ^ (1 / n)` of the coefficient
norms of an entire series tend to zero.

```lean
PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast.{u_1} {R : Type u_1} [NormedRing R]
  {F : PowerSeries R} (hF : F.IsEntire) :
  Filter.Tendsto (fun n => ‖(PowerSeries.coeff n) F‖ ^ (↑n)⁻¹) Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Majorant.html#PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast).

## Sources

- [Tau Ceti documentation: `PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Majorant.html#PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast)
- [Source of `PowerSeries.IsEntire.tendsto_norm_coeff_rpow_inv_natCast` in TauCeti/RingTheory/PowerSeries/Entire/Majorant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Entire/Majorant.lean#L90)
