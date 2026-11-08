---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.kyFanGauge_add_le, TauCeti.HasMinMaxLowerBound.kyFanGauge_add_le
statement: formalized
proof: formalized
---

# Ky Fan triangle inequality

For bounded linear maps from a complete inner product space to
an inner product space, the Ky Fan gauges are subadditive: `Kₖ(S + T) ≤ Kₖ(S) + Kₖ(T)`.

```lean
ContinuousLinearMap.kyFanGauge_add_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [CompleteSpace E] (S T : E →L[𝕜] F) (k : ℕ) :
  (S + T).kyFanGauge k ≤ S.kyFanGauge k + T.kyFanGauge k
```

## Depends on

- [ContinuousLinearMap.singularValue](../../part-01/operator-theory/continuouslinearmap-singularvalue.md)

## Proof depends on

- [Eckart–Young for Ky Fan gauges](eckart-young-for-ky-fan-gauges.md)
- [Ky Fan's maximum principle, attainment](../inner-product-space/part-02/ky-fans-maximum-principle-attainment.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.kyFanGauge_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.kyFanGauge_add_le).

## Other forms

**Ky Fan triangle inequality from the converse min–max localization.** Formalized in Tau Ceti as [`TauCeti.HasMinMaxLowerBound.kyFanGauge_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#TauCeti.HasMinMaxLowerBound.kyFanGauge_add_le).

```lean
TauCeti.HasMinMaxLowerBound.kyFanGauge_add_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] (h : TauCeti.HasMinMaxLowerBound 𝕜 E F) (S T : E →L[𝕜] F) (k : ℕ) :
  (S + T).kyFanGauge k ≤ S.kyFanGauge k + T.kyFanGauge k
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.kyFanGauge_add_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.kyFanGauge_add_le)
- [Source of `ContinuousLinearMap.kyFanGauge_add_le` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.lean#L149)
