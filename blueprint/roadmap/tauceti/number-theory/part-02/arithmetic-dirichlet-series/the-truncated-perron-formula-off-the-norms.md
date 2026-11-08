---
declaration: theorem
origin: cited
lean: TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le, TauCeti.truncatedPerron_LSeries
statement: formalized
proof: formalized
---

# The truncated Perron formula off the norms

If `x > 0` is not the absolute norm of a
nonzero ideal, then at every positive height `T` the truncated Perron integral differs from the
inclusive ideal sum `∑_{N(I) ≤ x} f(I)` by at most the series of the smoothed-step kernel errors at
the ratios `x / n`.

```lean
TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {f : TauCeti.IdealArithmeticFunction K} {x c T : ℝ} (hx : 0 < x) (hc : 0 < c)
  (hT : 0 < T)
  (hoff :
    ∀ (I : ↥(nonZeroDivisors (Ideal (NumberField.RingOfIntegers K)))), ↑(Ideal.absNorm ↑I) ≠ x)
  (h : LSeriesSummable ⇑((TauCeti.normCoeff K) f) ↑c) :
  ‖((↑(2 * Real.pi))⁻¹ *
          ∫ (t : ℝ) in -T..T,
            LSeries (⇑((TauCeti.normCoeff K) f)) (↑c + ↑t * Complex.I) *
              TauCeti.perronIntegrand x c t) -
        TauCeti.idealSummatory K f x‖ ≤
    ∑' (n : ℕ), ‖((TauCeti.normCoeff K) f) n‖ * ((x / ↑n) ^ c / (Real.pi * T * |Real.log (x / ↑n)|))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The off-norm arithmetic Perron formula](the-off-norm-arithmetic-perron-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le).

## Other forms

**The truncated Perron formula for an `L`-series.** Formalized in Tau Ceti as [`TauCeti.truncatedPerron_LSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.html#TauCeti.truncatedPerron_LSeries).

```lean
TauCeti.truncatedPerron_LSeries {f : ℕ → ℂ} {x c T : ℝ} (hx : 0 < x) (hc : 0 < c) (hT : 0 ≤ T)
  (h : LSeriesSummable f ↑c) :
  (↑(2 * Real.pi))⁻¹ *
      ∫ (t : ℝ) in -T..T, LSeries f (↑c + ↑t * Complex.I) * TauCeti.perronIntegrand x c t =
    ∑' (n : ℕ), f n * TauCeti.truncatedPerronKernel (x / ↑n) c T
```

## Sources

- [Tau Ceti documentation: `TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le)
- [Source of `TauCeti.norm_truncatedPerron_LSeries_normCoeff_sub_idealSummatory_le` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.lean#L217)
