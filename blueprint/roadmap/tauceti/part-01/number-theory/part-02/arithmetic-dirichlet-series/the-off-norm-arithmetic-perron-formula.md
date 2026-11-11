---
declaration: theorem
origin: cited
lean: TauCeti.norm_truncatedPerron_LSeries_sub_sum_le
statement: formalized
proof: formalized
---

# The off-norm arithmetic Perron formula

When `x` is not a natural number at which `f` is
nonzero, the truncated integral differs from the sharp partial sum `∑_{n < x} f n` by at most the
series of the smoothed-step kernel errors, a series that absolute convergence on the line makes
summable.

```lean
TauCeti.norm_truncatedPerron_LSeries_sub_sum_le {f : ℕ → ℂ} {x c T : ℝ} (hx : 0 < x) (hc : 0 < c)
  (hT : 0 < T) (hoff : ∀ (n : ℕ), f n ≠ 0 → x ≠ ↑n) (h : LSeriesSummable f ↑c) :
  ‖((↑(2 * Real.pi))⁻¹ *
          ∫ (t : ℝ) in -T..T, LSeries f (↑c + ↑t * Complex.I) * TauCeti.perronIntegrand x c t) -
        ∑ n ∈ Finset.Ico 1 ⌈x⌉₊, f n‖ ≤
    ∑' (n : ℕ), ‖f n‖ * ((x / ↑n) ^ c / (Real.pi * T * |Real.log (x / ↑n)|))
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [The truncated Perron formula off the norms](the-truncated-perron-formula-off-the-norms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_truncatedPerron_LSeries_sub_sum_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.html#TauCeti.norm_truncatedPerron_LSeries_sub_sum_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_truncatedPerron_LSeries_sub_sum_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.html#TauCeti.norm_truncatedPerron_LSeries_sub_sum_le)
- [Source of `TauCeti.norm_truncatedPerron_LSeries_sub_sum_le` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.lean#L225)
