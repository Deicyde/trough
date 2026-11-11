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
- [Source of `MeasureTheory.Measure.lintegral_decreasingRearrangement_enorm_eq_iInf_eLpNorm` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L429)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
