---
declaration: theorem
origin: cited
lean: TauCeti.bochner
statement: formalized
proof: formalized
---

# Bochner's theorem

A function `F` on a finite-dimensional real inner-product space is
continuous and positive definite if and only if it is the Fourier-convention transform
`v ↦ ∫ q, fourierAtom v q ∂μ` of a unique finite Borel measure `μ`. Bochner (1932); Rudin,
*Fourier Analysis on Groups*, Theorem 1.4.3.

```lean
TauCeti.bochner.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ↔
    ∃! μ, MeasureTheory.IsFiniteMeasure μ ∧ ∀ (v : V), F v = ∫ (q : V), TauCeti.fourierAtom v q ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.bochner`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner).

## Sources

- [Tau Ceti documentation: `TauCeti.bochner`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochner)
- [Source of `TauCeti.bochner` in TauCeti/Analysis/Bochner/BochnerTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/BochnerTheorem.lean#L238)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OneParameterSemigroups/STATUS.md)
