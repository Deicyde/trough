---
declaration: def
origin: cited
lean: TauCeti.CompatibleCouple.KMethodSpace.inclusion
statement: formalized
---

# TauCeti.CompatibleCouple.KMethodSpace.inclusion

The continuous inclusion of real interpolation spaces when the secondary exponent
increases. Its underlying map on the sum space is the identity.

```lean
TauCeti.CompatibleCouple.KMethodSpace.inclusion.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {X₀ : Type u_2}
  {X₁ : Type u_3} {V : Type u_4} [NormedField 𝕜] [NormedAddCommGroup X₀] [NormedSpace 𝕜 X₀]
  [NormedAddCommGroup X₁] [NormedSpace 𝕜 X₁] [AddCommGroup V] [_root_.Module 𝕜 V]
  [TopologicalSpace V] [ContinuousAdd V] {C : TauCeti.CompatibleCouple 𝕜 X₀ X₁ V} {θ : ℝ}
  {p q : ENNReal} [T1Space V] [Fact (1 ≤ p)] [Fact (1 ≤ q)] (hpq : p ≤ q) :
  C.KMethodSpace θ p →L[𝕜] C.KMethodSpace θ q
```

## Depends on

- [TauCeti.CompatibleCouple.KMethodSpace](../../analysis/part-02/pseudodifferential-operators-and-elliptic-analys/tauceti-compatiblecouple-kmethodspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CompatibleCouple.KMethodSpace.inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/Exponent.html#TauCeti.CompatibleCouple.KMethodSpace.inclusion).

## Sources

- [Tau Ceti documentation: `TauCeti.CompatibleCouple.KMethodSpace.inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/Exponent.html#TauCeti.CompatibleCouple.KMethodSpace.inclusion)
- [Source of `TauCeti.CompatibleCouple.KMethodSpace.inclusion` in TauCeti/Analysis/Normed/Interpolation/Exponent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Interpolation/Exponent.lean#L120)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
