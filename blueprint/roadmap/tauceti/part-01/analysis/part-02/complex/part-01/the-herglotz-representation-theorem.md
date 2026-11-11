---
declaration: theorem
origin: cited
lean: TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add, TauCeti.differentiableOn_and_re_nonneg_iff_exists_eq_herglotzTransform_add
statement: formalized
proof: formalized
---

# The Herglotz representation theorem

A function holomorphic on the unit disc with
nonnegative real part is the Herglotz transform `∫ (z + w) / (z - w) dμ(z)` of a finite positive
measure `μ` on the unit circle, plus the imaginary constant `(F 0).im * I`.

```lean
TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add {F : ℂ → ℂ}
  (hF : DifferentiableOn ℂ F (Metric.ball 0 1)) (hre : ∀ w ∈ Metric.ball 0 1, 0 ≤ (F w).re) :
  ∃ μ,
    MeasureTheory.IsFiniteMeasure μ ∧
      ∀ w ∈ Metric.ball 0 1, F w = μ.herglotzTransform w + ↑(F 0).im * Complex.I
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Herglotz formula on a disc](the-herglotz-formula-on-a-disc.md)
- [Prokhorov's theorem for finite measures](../../../../measure-theory/measure/prokhorovs-theorem-for-finite-measures.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Herglotz.html#TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add).

## Other forms

**The Herglotz representation theorem, as a characterization.** Formalized in Tau Ceti as [`TauCeti.differentiableOn_and_re_nonneg_iff_exists_eq_herglotzTransform_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Herglotz.html#TauCeti.differentiableOn_and_re_nonneg_iff_exists_eq_herglotzTransform_add).

```lean
TauCeti.differentiableOn_and_re_nonneg_iff_exists_eq_herglotzTransform_add {F : ℂ → ℂ} :
  (DifferentiableOn ℂ F (Metric.ball 0 1) ∧ ∀ w ∈ Metric.ball 0 1, 0 ≤ (F w).re) ↔
    ∃ μ b,
      MeasureTheory.IsFiniteMeasure μ ∧
        ∀ w ∈ Metric.ball 0 1, F w = μ.herglotzTransform w + ↑b * Complex.I
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Herglotz.html#TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add)
- [Source of `TauCeti.exists_isFiniteMeasure_eq_herglotzTransform_add` in TauCeti/Analysis/Complex/Herglotz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Herglotz.lean#L257)
