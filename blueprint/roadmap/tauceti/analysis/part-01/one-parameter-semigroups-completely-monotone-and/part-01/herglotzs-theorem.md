---
declaration: theorem
origin: cited
lean: TauCeti.exists_isFiniteMeasure_integral_zpow_eq, TauCeti.isPositiveDefiniteSub_iff_exists_isFiniteMeasure_integral_zpow_eq
statement: formalized
proof: formalized
---

# Herglotz's theorem

A positive-definite function `φ` on `ℤ` is the moment sequence
`φ n = ∫ zⁿ dμ(z)` of a finite positive measure `μ` on the unit circle.

```lean
TauCeti.exists_isFiniteMeasure_integral_zpow_eq (φ : ℤ → ℂ) (hφ : TauCeti.IsPositiveDefiniteSub φ) :
  ∃ μ, MeasureTheory.IsFiniteMeasure μ ∧ ∀ (n : ℤ), φ n = ∫ (z : Circle), ↑z ^ n ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Prokhorov's theorem for finite measures](../../../../measure-theory/measure/prokhorovs-theorem-for-finite-measures.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isFiniteMeasure_integral_zpow_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Herglotz.html#TauCeti.exists_isFiniteMeasure_integral_zpow_eq).

## Other forms

**Herglotz's theorem, as a characterization.** Formalized in Tau Ceti as [`TauCeti.isPositiveDefiniteSub_iff_exists_isFiniteMeasure_integral_zpow_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Herglotz.html#TauCeti.isPositiveDefiniteSub_iff_exists_isFiniteMeasure_integral_zpow_eq).

```lean
TauCeti.isPositiveDefiniteSub_iff_exists_isFiniteMeasure_integral_zpow_eq (φ : ℤ → ℂ) :
  TauCeti.IsPositiveDefiniteSub φ ↔
    ∃ μ, MeasureTheory.IsFiniteMeasure μ ∧ ∀ (n : ℤ), φ n = ∫ (z : Circle), ↑z ^ n ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isFiniteMeasure_integral_zpow_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Herglotz.html#TauCeti.exists_isFiniteMeasure_integral_zpow_eq)
- [Source of `TauCeti.exists_isFiniteMeasure_integral_zpow_eq` in TauCeti/Analysis/Bochner/Herglotz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/Herglotz.lean#L197)
