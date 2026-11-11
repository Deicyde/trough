---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm, ContinuousLinearMap.summingENorm_one_le_ofReal_eight_mul_norm
statement: formalized
proof: formalized
---

# Grothendieck's theorem

Every bounded operator `T` from `L¹(μ)` into an inner product space
over an `RCLike` field is absolutely `1`-summing, with `π₁(T) ≤ 16 ‖T‖`. Over `ℝ`,
`ContinuousLinearMap.summingENorm_one_le_ofReal_eight_mul_norm` gives the constant `8`.

```lean
ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm.{u_1, u_2, u_3} {α : Type u_1}
  {𝕜 : Type u_2} {H : Type u_3} [RCLike 𝕜] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] (T : ↥(MeasureTheory.Lp 𝕜 1 μ) →L[𝕜] H) :
  ContinuousLinearMap.summingENorm 1 T ≤ ENNReal.ofReal (16 * ‖T‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's inequality over an `RCLike` field, with constant `κ_𝕜 = 16`](../../../part-01/banach-space-theory/part-01/grothendiecks-inequality-over-an-rclike-field-wi.md)
- [Grothendieck's inequality over the reals, with constant `κ_ℝ = 8`](../../../part-01/banach-space-theory/part-01/grothendiecks-inequality-over-the-reals-with-con.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.html#ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm).

## Other forms

**Grothendieck's theorem over `ℝ`.** Formalized in Tau Ceti as [`ContinuousLinearMap.summingENorm_one_le_ofReal_eight_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.html#ContinuousLinearMap.summingENorm_one_le_ofReal_eight_mul_norm).

```lean
ContinuousLinearMap.summingENorm_one_le_ofReal_eight_mul_norm.{u_1, u_4} {α : Type u_1}
  {m : MeasurableSpace α} {μ : MeasureTheory.Measure α} {H : Type u_4} [NormedAddCommGroup H]
  [InnerProductSpace ℝ H] (T : ↥(MeasureTheory.Lp ℝ 1 μ) →L[ℝ] H) :
  ContinuousLinearMap.summingENorm 1 T ≤ ENNReal.ofReal (8 * ‖T‖)
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.html#ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm)
- [Source of `ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm` in TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.lean#L208)
