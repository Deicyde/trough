---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm
statement: formalized
proof: formalized
---

# The `K`-functional of `(L¹, L∞)`

For an a.e. strongly measurable `f`,
`∫₀ᵗ ‖f‖* = inf {‖f₀‖₁ + t ‖f₁‖_∞ | f₀ + f₁ = f}`, the infimum being attained by the radial
retraction of `f` at the level `‖f‖* t`.

```lean
MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm.{u_1, u_2}
  {α : Type u_1} [MeasurableSpace α] (μ : MeasureTheory.Measure α) {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {f : α → E} (hf : MeasureTheory.AEStronglyMeasurable f μ)
  (t : ℝ) :
  ∫⁻ (s : ℝ) in Set.Ioc 0 t, μ.decreasingRearrangement (fun x => ‖f x‖ₑ) s =
    ⨅ f₀,
      ⨅ f₁,
        ⨅ (_ : f₀ + f₁ = f),
          MeasureTheory.eLpNorm f₀ 1 μ + ENNReal.ofReal t * MeasureTheory.eLpNorm f₁ ⊤ μ
```

## Depends on

- [MeasureTheory.Measure.decreasingRearrangement](measuretheory-measure-decreasingrearrangement.md)

## Proof depends on

- [Equimeasurability](equimeasurability.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm)
- [Source of `MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L456)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
