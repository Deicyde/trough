---
declaration: theorem
origin: cited
lean: PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id
statement: formalized
proof: formalized
---

# Realization of compactly supported laws

A finite measure `μ` on `ℝ` concentrated on a
compact set `K` is the law of the coordinate function `x ↦ x` in the commutative C⋆-algebra
`C(K, ℂ)`, with respect to integration against `μ` on `K`. This functional is a state when `μ` is
a probability measure (`ContinuousMap.integralPositiveLinearMap_one`).

```lean
PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id {K : Set ℝ} [CompactSpace ↑K]
  {μ : MeasureTheory.Measure ℝ} [MeasureTheory.IsFiniteMeasure μ] (hμ : μ Kᶜ = 0) :
  (ContinuousMap.integralPositiveLinearMap (MeasureTheory.Measure.comap Subtype.val μ)).law
      (ContinuousMap.realToRCLike ℂ (ContinuousMap.restrict K (ContinuousMap.id ℝ))) =
    μ
```

## Depends on

- [PositiveLinearMap.law](positivelinearmap-law.md)

## Lean

Formalized in Tau Ceti as [`PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id).

## Sources

- [Tau Ceti documentation: `PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id)
- [Source of `PositiveLinearMap.law_integralPositiveLinearMap_comap_restrict_id` in TauCeti/Probability/FreeProbability/Law/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/FreeProbability/Law/Basic.lean#L314)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeProbability/STATUS.md)
