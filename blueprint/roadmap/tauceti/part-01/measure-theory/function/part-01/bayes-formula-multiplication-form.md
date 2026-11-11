---
declaration: theorem
origin: cited
lean: MeasureTheory.condExp_toReal_smul_condExp_withDensity, MeasureTheory.condExp_withDensity, MeasureTheory.condExp_withDensity_eq_div
statement: formalized
proof: formalized
---

# Bayes' formula, multiplication form

The conditional density times the
new-measure conditional expectation is the old-measure conditional expectation of
the weighted variable. The observable need not be integrable under the old measure.

```lean
MeasureTheory.condExp_toReal_smul_condExp_withDensity.{u_1, u_2} {Ω : Type u_1} {E : Type u_2}
  {m mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] {w : Ω → ENNReal} {f : Ω → E} (hm : m ≤ mΩ)
  [MeasureTheory.SigmaFinite (μ.trim hm)] (hw : AEMeasurable w μ)
  [MeasureTheory.IsFiniteMeasure (μ.withDensity w)]
  (hf : MeasureTheory.Integrable f (μ.withDensity w)) :
  (fun x => μ[fun y => (w y).toReal | m] x • (μ.withDensity w)[f | m] x) =ᵐ[μ]
    μ[fun x => (w x).toReal • f x | m]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.condExp_toReal_smul_condExp_withDensity`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation/WithDensity.html#MeasureTheory.condExp_toReal_smul_condExp_withDensity).

## Other forms

**Bayes' formula for a Banach-valued integrable observable.** Formalized in Tau Ceti as [`MeasureTheory.condExp_withDensity`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation/WithDensity.html#MeasureTheory.condExp_withDensity).

```lean
MeasureTheory.condExp_withDensity.{u_1, u_2} {Ω : Type u_1} {E : Type u_2}
  {m mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] {w : Ω → ENNReal} {f : Ω → E} (hm : m ≤ mΩ)
  [MeasureTheory.SigmaFinite (μ.trim hm)] (hw : AEMeasurable w μ)
  [MeasureTheory.IsFiniteMeasure (μ.withDensity w)]
  (hf : MeasureTheory.Integrable f (μ.withDensity w)) :
  (μ.withDensity w)[f | m] =ᵐ[μ.withDensity w] fun x =>
    (μ[fun y => (w y).toReal | m] x)⁻¹ • μ[fun y => (w y).toReal • f y | m] x
```

**Bayes' formula for a real integrable observable, in quotient notation.** Formalized in Tau Ceti as [`MeasureTheory.condExp_withDensity_eq_div`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation/WithDensity.html#MeasureTheory.condExp_withDensity_eq_div).

```lean
MeasureTheory.condExp_withDensity_eq_div.{u_1} {Ω : Type u_1} {m mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} {w : Ω → ENNReal} {f : Ω → ℝ} (hm : m ≤ mΩ)
  [MeasureTheory.SigmaFinite (μ.trim hm)] (hw : AEMeasurable w μ)
  [MeasureTheory.IsFiniteMeasure (μ.withDensity w)]
  (hf : MeasureTheory.Integrable f (μ.withDensity w)) :
  (μ.withDensity w)[f | m] =ᵐ[μ.withDensity w] fun x =>
    μ[fun y => (w y).toReal * f y | m] x / μ[fun y => (w y).toReal | m] x
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.condExp_toReal_smul_condExp_withDensity`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation/WithDensity.html#MeasureTheory.condExp_toReal_smul_condExp_withDensity)
- [Source of `MeasureTheory.condExp_toReal_smul_condExp_withDensity` in TauCeti/MeasureTheory/Function/ConditionalExpectation/WithDensity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/ConditionalExpectation/WithDensity.lean#L41)
