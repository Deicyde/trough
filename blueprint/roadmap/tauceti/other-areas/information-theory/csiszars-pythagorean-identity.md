---
declaration: theorem
origin: cited
lean: TauCeti.klDiv_eq_klDiv_add_klDiv
statement: formalized
proof: formalized
---

# Csiszár's Pythagorean identity

Let `γ ≪ π ≪ R` be finite measures such that `llr π R` is
integrable against both `γ` and `π`, with the same integral. Then
`klDiv γ R = klDiv γ π + klDiv π R`.

```lean
TauCeti.klDiv_eq_klDiv_add_klDiv.{u_1} {α : Type u_1} [MeasurableSpace α]
  {γ π R : MeasureTheory.Measure α} [MeasureTheory.IsFiniteMeasure γ]
  [MeasureTheory.IsFiniteMeasure π] [MeasureTheory.IsFiniteMeasure R]
  (hγπ : γ.AbsolutelyContinuous π) (hπR : π.AbsolutelyContinuous R)
  (hγ : MeasureTheory.Integrable (MeasureTheory.llr π R) γ)
  (hπ : MeasureTheory.Integrable (MeasureTheory.llr π R) π)
  (h : ∫ (x : α), MeasureTheory.llr π R x ∂γ = ∫ (x : α), MeasureTheory.llr π R x ∂π) :
  InformationTheory.klDiv γ R = InformationTheory.klDiv γ π + InformationTheory.klDiv π R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.klDiv_eq_klDiv_add_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/ChangeOfReference.html#TauCeti.klDiv_eq_klDiv_add_klDiv).

## Sources

- [Tau Ceti documentation: `TauCeti.klDiv_eq_klDiv_add_klDiv`](https://taucetiproject.org/docs/TauCeti/InformationTheory/KullbackLeibler/ChangeOfReference.html#TauCeti.klDiv_eq_klDiv_add_klDiv)
- [Source of `TauCeti.klDiv_eq_klDiv_add_klDiv` in TauCeti/InformationTheory/KullbackLeibler/ChangeOfReference.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/InformationTheory/KullbackLeibler/ChangeOfReference.lean#L70)
