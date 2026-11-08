---
declaration: theorem
origin: cited
lean: PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant
statement: formalized
proof: formalized
---

# The Coleman majorant bounds the coefficients

If `B` is restricted at the radius `r`, every
weighted coefficient `‖bₘ‖ rᵐ` of positive degree is at most `β_B(r)`.

```lean
PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant.{u_1} {R : Type u_1} [NormedRing R]
  {B : PowerSeries R} {r : ℝ} (hB : PowerSeries.IsRestricted r B) (m : ℕ) :
  ‖(PowerSeries.coeff (m + 1)) B‖ * r ^ (m + 1) ≤ B.colemanMajorant r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Majorant.html#PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant).

## Sources

- [Tau Ceti documentation: `PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Entire/Majorant.html#PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant)
- [Source of `PowerSeries.norm_coeff_succ_mul_pow_le_colemanMajorant` in TauCeti/RingTheory/PowerSeries/Entire/Majorant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Entire/Majorant.lean#L248)
