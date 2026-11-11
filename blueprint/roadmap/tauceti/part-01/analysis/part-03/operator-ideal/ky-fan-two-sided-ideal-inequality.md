---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.kyFanGauge_comp_comp_le
statement: formalized
proof: formalized
---

# Ky Fan two-sided ideal inequality

`Kₖ(A T B) ≤ ‖A‖ Kₖ(T) ‖B‖`.

```lean
ContinuousLinearMap.kyFanGauge_comp_comp_le.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} {G : Type u_4} {H : Type u_5} [NontriviallyNormedField 𝕜]
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [SeminormedAddCommGroup F] [NormedSpace 𝕜 F]
  [SeminormedAddCommGroup G] [NormedSpace 𝕜 G] [SeminormedAddCommGroup H] [NormedSpace 𝕜 H]
  (A : G →L[𝕜] H) (T : F →L[𝕜] G) (B : E →L[𝕜] F) (k : ℕ) :
  (A ∘SL T ∘SL B).kyFanGauge k ≤ ‖A‖₊ * T.kyFanGauge k * ‖B‖₊
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.kyFanGauge_comp_comp_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.html#ContinuousLinearMap.kyFanGauge_comp_comp_le).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.kyFanGauge_comp_comp_le`](https://taucetiproject.org/docs/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.html#ContinuousLinearMap.kyFanGauge_comp_comp_le)
- [Source of `ContinuousLinearMap.kyFanGauge_comp_comp_le` in TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/OperatorIdeal/ApproximationNumber/Basic.lean#L341)
