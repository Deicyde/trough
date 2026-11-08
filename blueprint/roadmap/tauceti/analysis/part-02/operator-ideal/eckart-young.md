---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.singularValue_eq_linearMap_singularValues, ContinuousLinearMap.kyFanGauge_eq_kyFanSum
statement: formalized
proof: formalized
---

# Eckart–Young

Between finite-dimensional inner product spaces, the approximation numbers
of a bounded linear map are its singular values: `aₙ(T) = σₙ(T)` for every `n`, both sides
vanishing from the dimension of the source on.

```lean
ContinuousLinearMap.singularValue_eq_linearMap_singularValues.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  (T : E →L[𝕜] F) (n : ℕ) : ↑(T.singularValue n) = (↑T).singularValues n
```

## Depends on

- [ContinuousLinearMap.singularValue](../../part-01/operator-theory/continuouslinearmap-singularvalue.md)

## Proof depends on

- [Courant–Fischer, lower direction](../inner-product-space/part-01/courant-fischer-lower-direction.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.singularValue_eq_linearMap_singularValues`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#ContinuousLinearMap.singularValue_eq_linearMap_singularValues).

## Other forms

**Eckart–Young for Ky Fan gauges.** Formalized in Tau Ceti as [`ContinuousLinearMap.kyFanGauge_eq_kyFanSum`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/KyFan.html#ContinuousLinearMap.kyFanGauge_eq_kyFanSum).

```lean
ContinuousLinearMap.kyFanGauge_eq_kyFanSum.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F]
  [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 E] [FiniteDimensional 𝕜 F] (T : E →L[𝕜] F) (k : ℕ) :
  ↑(T.kyFanGauge k) = (↑T).kyFanSum k
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.singularValue_eq_linearMap_singularValues`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.html#ContinuousLinearMap.singularValue_eq_linearMap_singularValues)
- [Source of `ContinuousLinearMap.singularValue_eq_linearMap_singularValues` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/EckartYoung.lean#L62)
