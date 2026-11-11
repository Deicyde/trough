---
declaration: theorem
origin: cited
lean: TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le
statement: formalized
proof: formalized
---

# TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le

The secondary-exponent inclusion has the couple-independent norm bound
`max 1 c_{θ,p}⁻¹`.

```lean
TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  {X₀ : Type u_2} {X₁ : Type u_3} {V : Type u_4} [NormedField 𝕜] [NormedAddCommGroup X₀]
  [NormedSpace 𝕜 X₀] [NormedAddCommGroup X₁] [NormedSpace 𝕜 X₁] [AddCommGroup V] [_root_.Module 𝕜 V]
  [TopologicalSpace V] [ContinuousAdd V] {C : TauCeti.CompatibleCouple 𝕜 X₀ X₁ V} {θ : ℝ}
  {p q : ENNReal} [T1Space V] [Fact (1 ≤ p)] [Fact (1 ≤ q)] (hpq : p ≤ q) (u : C.KMethodSpace θ p) :
  ‖(TauCeti.CompatibleCouple.KMethodSpace.inclusion hpq) u‖ ≤
    max 1 (TauCeti.CompatibleCouple.kMethodConst θ p).toReal⁻¹ * ‖u‖
```

## Depends on

- [TauCeti.CompatibleCouple.KMethodSpace](../../analysis/part-02/pseudodifferential-operators-and-elliptic-analys/tauceti-compatiblecouple-kmethodspace.md)
- [TauCeti.CompatibleCouple.KMethodSpace.inclusion](tauceti-compatiblecouple-kmethodspace-inclusion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/Exponent.html#TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Interpolation/Exponent.html#TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le)
- [Source of `TauCeti.CompatibleCouple.KMethodSpace.norm_inclusion_le` in TauCeti/Analysis/Normed/Interpolation/Exponent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Interpolation/Exponent.lean#L145)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
