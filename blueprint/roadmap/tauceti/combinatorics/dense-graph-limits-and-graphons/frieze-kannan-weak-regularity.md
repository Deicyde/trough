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

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.html#TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.html#TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan)
- [Source of `TauCeti.DenseGraphLimits.weak_regularity_frieze_kannan` in TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/StepGraphon/Regularity.lean#L179)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
