---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.norm_sum_inner_le_kyFanGauge, ContinuousLinearMap.IsPositive.exists_orthonormal_kyFanGauge_le_sum_re_inner_add, ContinuousLinearMap.IsPositive.kyFanGauge_le_iff
statement: formalized
proof: formalized
---

# Ky Fan's maximum principle

For a bounded linear map `T` between inner product spaces and
orthonormal families `(uᵢ)` in `F` and `(vᵢ)` in `E` with `k` members,
`‖∑ᵢ ⟪uᵢ, T vᵢ⟫‖ ≤ a₀(T) + ⋯ + aₖ₋₁(T)`.

```lean
ContinuousLinearMap.norm_sum_inner_le_kyFanGauge.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] {ι : Type u_4} [Fintype ι] (T : E →L[𝕜] F) {u : ι → F} {v : ι → E}
  (hu : Orthonormal 𝕜 u) (hv : Orthonormal 𝕜 v) :
  ‖∑ i, inner 𝕜 (u i) (T (v i))‖ ≤ ↑(T.kyFanGauge (Fintype.card ι))
```

## Depends on

- [ContinuousLinearMap.singularValue](../../part-01/operator-theory/continuouslinearmap-singularvalue.md)

## Proof depends on

- [Eckart–Young for Ky Fan gauges](eckart-young-for-ky-fan-gauges.md)
- [Ky Fan's maximum principle, attainment](../inner-product-space/part-02/ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.norm_sum_inner_le_kyFanGauge`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.norm_sum_inner_le_kyFanGauge).

## Other forms

**Ky Fan's maximum principle for positive operators, approximate attainment.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsPositive.exists_orthonormal_kyFanGauge_le_sum_re_inner_add`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Positive.html#ContinuousLinearMap.IsPositive.exists_orthonormal_kyFanGauge_le_sum_re_inner_add).

```lean
ContinuousLinearMap.IsPositive.exists_orthonormal_kyFanGauge_le_sum_re_inner_add.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [CompleteSpace E] {T : E →L[𝕜] E} (hT : T.IsPositive) (k : ℕ) {ε : ℝ} (hε : 0 < ε) :
  ∃ m v, m ≤ k ∧ Orthonormal 𝕜 v ∧ ↑(T.kyFanGauge k) ≤ ∑ i, RCLike.re (inner 𝕜 (v i) (T (v i))) + ε
```

**Ky Fan's maximum principle for positive operators.** Formalized in Tau Ceti as [`ContinuousLinearMap.IsPositive.kyFanGauge_le_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Positive.html#ContinuousLinearMap.IsPositive.kyFanGauge_le_iff).

```lean
ContinuousLinearMap.IsPositive.kyFanGauge_le_iff.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E] {T : E →L[𝕜] E}
  (hT : T.IsPositive) {k : ℕ} {c : ℝ} :
  ↑(T.kyFanGauge k) ≤ c ↔
    ∀ m ≤ k, ∀ (v : Fin m → E), Orthonormal 𝕜 v → ∑ i, RCLike.re (inner 𝕜 (v i) (T (v i))) ≤ c
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.norm_sum_inner_le_kyFanGauge`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.norm_sum_inner_le_kyFanGauge)
- [Source of `ContinuousLinearMap.norm_sum_inner_le_kyFanGauge` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.lean#L83)
