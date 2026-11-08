---
declaration: theorem
origin: cited
lean: TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq
statement: formalized
proof: formalized
---

# Existence half of Bochner's theorem

A continuous positive-definite function `F` on a
finite-dimensional real inner-product space is the Fourier-convention transform
`v ↦ ∫ q, fourierAtom v q ∂μ` of a finite Borel measure `μ`. Rudin, *Fourier Analysis on Groups*,
Theorem 1.4.3.

```lean
TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ)
  (hcont : Continuous F) (hpd : TauCeti.IsPositiveDefiniteSub F) :
  ∃ μ, MeasureTheory.IsFiniteMeasure μ ∧ ∀ (v : V), F v = ∫ (q : V), TauCeti.fourierAtom v q ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lévy's continuity theorem, including existence](../../../../measure-theory/measure/levys-continuity-theorem-including-existence.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq)
- [Source of `TauCeti.exists_isFiniteMeasure_integral_fourierAtom_eq` in TauCeti/Analysis/Bochner/BochnerTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/BochnerTheorem.lean#L193)
