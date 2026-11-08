---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure
statement: formalized
proof: formalized
---

# Pietsch domination theorem

For `1 ≤ p < ∞` and `C ≥ 0`, an operator satisfies
`πₚ(T) ≤ C` if and only if there is a regular Borel probability measure `ν` on the weak-star
compact dual unit ball with `‖T x‖ ≤ C (∫ |f x|ᵖ dν(f))^(1/p)` for all `x`.

```lean
ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} [RCLike 𝕜] [SeminormedAddCommGroup E]
  [NormedSpace 𝕜 E] [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] {p : ENNReal} [Fact (1 ≤ p)]
  [MeasurableSpace (WeakDual 𝕜 E)] [BorelSpace (WeakDual 𝕜 E)] (hp : p ≠ ⊤) {T : E →L[𝕜] F} {C : ℝ}
  (hC : 0 ≤ C) :
  ContinuousLinearMap.summingENorm p T ≤ ENNReal.ofReal C ↔
    ∃ ν,
      MeasureTheory.IsProbabilityMeasure ν ∧
        ν.Regular ∧
          ∀ (x : E),
            ‖T x‖ ≤
              C *
                (∫ (f : ↑(⇑WeakDual.toStrongDual ⁻¹' Metric.closedBall 0 1)),
                    ‖↑f x‖ ^ p.toReal ∂ν) ^
                  (1 / p.toReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Pietsch.html#ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Pietsch.html#ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure)
- [Source of `ContinuousLinearMap.summingENorm_le_ofReal_iff_exists_isProbabilityMeasure` in TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Pietsch.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Pietsch.lean#L254)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
