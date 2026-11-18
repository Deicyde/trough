---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan
statement: formalized
proof: formalized
---

# Frieze--Kannan weak regularity

Every graphon has a measurable block-average step graphon
within `ε` in cut norm, on a partition with at most `4 ^ ⌈1 / ε²⌉` parts.

```lean
TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  (μ : MeasureTheory.Measure Ω) [MeasureTheory.IsProbabilityMeasure μ]
  (W : TauCeti.DenseGraphLimits.Graphon Ω μ) {ε : ℝ} (hε : 0 < ε) :
  ∃ P,
    ∃ (hP : ∀ p ∈ P.parts, MeasurableSet p),
      P.parts.card ≤ 4 ^ ⌈1 / ε ^ 2⌉₊ ∧
        TauCeti.DenseGraphLimits.cutNorm μ
            (W.toSymmKernel - (TauCeti.DenseGraphLimits.stepGraphonAvg P hP W).toSymmKernel) ≤
          ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.DenseGraphLimits.exists_refinement_energy_add_sq_lt](tauceti-densegraphlimits-exists-refinement-energ.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.html#TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.html#TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan)
- [Source of `TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan` in TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.lean#L157)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/DenseGraphLimits/STATUS.md)
