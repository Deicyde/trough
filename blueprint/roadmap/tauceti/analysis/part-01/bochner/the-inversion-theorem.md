---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.eq_withDensity_charFunDensity
statement: formalized
proof: formalized
---

# The inversion theorem

A finite measure on `ℝ` with integrable characteristic function
`φ` has the bounded continuous density `x ↦ (2π)⁻¹ * Re ∫ t, exp (-i t x) * φ(t) dt` with respect
to Lebesgue measure.

```lean
MeasureTheory.Measure.eq_withDensity_charFunDensity {μ : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsFiniteMeasure μ]
  (h : MeasureTheory.Integrable (MeasureTheory.charFun μ) MeasureTheory.volume) :
  μ = MeasureTheory.volume.withDensity fun x => ENNReal.ofReal (μ.charFunDensity x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Uniqueness half of Bochner's theorem](uniqueness-half-of-bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.eq_withDensity_charFunDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/CharFun/Inversion.html#MeasureTheory.Measure.eq_withDensity_charFunDensity).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.eq_withDensity_charFunDensity`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/CharFun/Inversion.html#MeasureTheory.Measure.eq_withDensity_charFunDensity)
- [Source of `MeasureTheory.Measure.eq_withDensity_charFunDensity` in TauCeti/Analysis/Bochner/CharFun/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/CharFun/Inversion.lean#L181)
