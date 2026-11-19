---
declaration: theorem
origin: cited
lean: TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq
statement: formalized
proof: formalized
---

# Converse half of Bochner's theorem

The Fourier-convention transform of a measure is
continuous and positive definite.

```lean
TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq.{u_2} {V : Type u_2}
  [SeminormedAddCommGroup V] [InnerProductSpace ℝ V] [MeasurableSpace V] [OpensMeasurableSpace V]
  {F : V → ℂ} (μ : MeasureTheory.Measure V)
  (hrep : ∀ (v : V), F v = ∫ (q : V), TauCeti.fourierAtom v q ∂μ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq)
- [Source of `TauCeti.continuous_and_isPositiveDefiniteSub_of_integral_fourierAtom_eq` in TauCeti/Analysis/Bochner/BochnerTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Bochner/BochnerTheorem.lean#L222)
