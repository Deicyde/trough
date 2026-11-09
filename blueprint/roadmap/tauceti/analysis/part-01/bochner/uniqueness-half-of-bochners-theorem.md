---
declaration: theorem
origin: cited
lean: TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq
statement: formalized
proof: formalized
---

# Uniqueness half of Bochner's theorem

Two finite Borel measures with the same
Fourier-convention transform coincide; this is Mathlib's characteristic-function uniqueness
theorem, transported through the `-2π` rescaling. Stated on any complete second-countable real
inner-product space; no finite-dimensionality is needed.

```lean
TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq.{u_3} {W : Type u_3} [NormedAddCommGroup W]
  [InnerProductSpace ℝ W] [MeasurableSpace W] [BorelSpace W] [SecondCountableTopology W]
  [CompleteSpace W] {μ ν : MeasureTheory.Measure W} [MeasureTheory.IsFiniteMeasure μ]
  [MeasureTheory.IsFiniteMeasure ν]
  (h : ∀ (v : W), ∫ (q : W), TauCeti.fourierAtom v q ∂μ = ∫ (q : W), TauCeti.fourierAtom v q ∂ν) :
  μ = ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Fourier/Convention.html#TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Fourier/Convention.html#TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq)
- [Source of `TauCeti.Measure.ext_of_forall_integral_fourierAtom_eq` in TauCeti/Analysis/Bochner/Fourier/Convention.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/Fourier/Convention.lean#L187)
