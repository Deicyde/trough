---
declaration: theorem
origin: cited
lean: ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted
statement: formalized
proof: formalized
---

# ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted

Under the constant-drift exponential change of measure, the usual augmented natural
σ-algebra of `W_t + κ t` is the usual augmented natural σ-algebra of `W_t` under the
original measure. The change of measure is constructed here, not assumed equivalent.

```lean
ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted.{u_1}
  {Ω : Type u_1} {m : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω} {W : NNReal → Ω → ℝ}
  (hW : ProbabilityTheory.IsPreBrownianReal W P)
  (hmeas : ∀ (t : NNReal), MeasureTheory.StronglyMeasurable (W t)) (κ : ℝ) (T t : NNReal) :
  ↑((MeasureTheory.Filtration.natural (fun u ω => W u ω + κ * ↑u) ⋯).nullAugment
            (P.tilted fun ω => -κ * W T ω)).rightCont
      t =
    ↑((MeasureTheory.Filtration.natural W hmeas).nullAugment P).rightCont t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/NaturalFiltration.html#ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/NaturalFiltration.html#ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted)
- [Source of `ProbabilityTheory.IsPreBrownianReal.rightCont_nullAugment_natural_add_drift_tilted` in TauCeti/Probability/BrownianMotion/NaturalFiltration.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/BrownianMotion/NaturalFiltration.lean#L44)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
