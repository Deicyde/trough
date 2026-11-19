---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm, ContinuousLinearMap.summingENorm_one_le_ofReal_eight_mul_norm, ContinuousLinearMap.summingENorm_two_le_ofReal_eight_mul_norm, ContinuousLinearMap.summingENorm_two_le_ofReal_sixteen_mul_norm
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

- [Grothendieck's inequality (`LinearMap.abs_sum_apply_apply_le_eight_mul`)](../../../part-01/banach-space-theory/part-01/grothendiecks-inequality-linearmap-abs-sum-apply.md)
- [Grothendieck's inequality (`LinearMap.norm_sum_apply_apply_le_sixteen_mul`)](../../../part-01/banach-space-theory/part-01/grothendiecks-inequality-linearmap-norm-sum-appl.md)
- [Grothendieck's inequality over an `RCLike` field, with constant `κ_𝕜 = 16`](../../../part-01/banach-space-theory/part-01/grothendiecks-inequality-over-an-rclike-field-wi.md)
- [Grothendieck's inequality over the reals, with constant `κ_ℝ = 8`](../../../part-01/banach-space-theory/part-01/grothendiecks-inequality-over-the-reals-with-con.md)
- [Hölder's inequality for disjoint pieces](../../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)

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

**Grothendieck's theorem for `C(K, ℝ) → L¹(μ, ℝ)`.** Formalized in Tau Ceti as [`ContinuousLinearMap.summingENorm_two_le_ofReal_eight_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.html#ContinuousLinearMap.summingENorm_two_le_ofReal_eight_mul_norm).

```lean
ContinuousLinearMap.summingENorm_two_le_ofReal_eight_mul_norm.{u_1, u_2} {K : Type u_1}
  {α : Type u_2} [TopologicalSpace K] {m : MeasurableSpace α} {μ : MeasureTheory.Measure α}
  [CompactSpace K] (T : C(K, ℝ) →L[ℝ] ↥(MeasureTheory.Lp ℝ 1 μ)) :
  ContinuousLinearMap.summingENorm 2 T ≤ ENNReal.ofReal (8 * ‖T‖)
```

**Grothendieck's theorem for `C(K) → L¹(μ)`.** Formalized in Tau Ceti as [`ContinuousLinearMap.summingENorm_two_le_ofReal_sixteen_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.html#ContinuousLinearMap.summingENorm_two_le_ofReal_sixteen_mul_norm).

```lean
ContinuousLinearMap.summingENorm_two_le_ofReal_sixteen_mul_norm.{u_1, u_2, u_3} {K : Type u_1}
  {α : Type u_2} {𝕜 : Type u_3} [TopologicalSpace K] [RCLike 𝕜] {m : MeasurableSpace α}
  {μ : MeasureTheory.Measure α} [CompactSpace K] (T : C(K, 𝕜) →L[𝕜] ↥(MeasureTheory.Lp 𝕜 1 μ)) :
  ContinuousLinearMap.summingENorm 2 T ≤ ENNReal.ofReal (16 * ‖T‖)
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.html#ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm)
- [Source of `ContinuousLinearMap.summingENorm_one_le_ofReal_sixteen_mul_norm` in TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Grothendieck.lean#L231)
