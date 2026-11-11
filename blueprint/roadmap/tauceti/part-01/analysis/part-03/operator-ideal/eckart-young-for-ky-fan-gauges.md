---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.kyFanGauge_eq_kyFanSum, ContinuousLinearMap.singularValue_eq_linearMap_singularValues
statement: formalized
proof: formalized
---

# Eckart–Young for Ky Fan gauges

Between finite-dimensional inner product spaces, the Ky Fan
gauge `Kₖ(T)` of a bounded linear map is the Ky Fan `k`-sum `σ₀(T) + ⋯ + σₖ₋₁(T)` of its singular
values.

```lean
ContinuousLinearMap.kyFanGauge_eq_kyFanSum.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 E] [FiniteDimensional 𝕜 F] (T : E →L[𝕜] F) (k : ℕ) :
  ↑(T.kyFanGauge k) = (↑T).kyFanSum k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Courant–Fischer, lower direction](../inner-product-space/part-01/courant-fischer-lower-direction.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.kyFanGauge_eq_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.kyFanGauge_eq_kyFanSum).

## Other forms

**Eckart–Young.** Formalized in Tau Ceti as [`ContinuousLinearMap.singularValue_eq_linearMap_singularValues`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#ContinuousLinearMap.singularValue_eq_linearMap_singularValues).

```lean
ContinuousLinearMap.singularValue_eq_linearMap_singularValues.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  (T : E →L[𝕜] F) (n : ℕ) : ↑(T.singularValue n) = (↑T).singularValues n
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.kyFanGauge_eq_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.kyFanGauge_eq_kyFanSum)
- [Source of `ContinuousLinearMap.kyFanGauge_eq_kyFanSum` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.lean#L63)
