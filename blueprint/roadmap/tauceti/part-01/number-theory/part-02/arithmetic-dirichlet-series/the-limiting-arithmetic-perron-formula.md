---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_truncatedPerron_LSeries
statement: formalized
proof: formalized
---

# The limiting arithmetic Perron formula

As the truncation height grows the integral tends
to the series of sharp steps `∑' n, f n * perronStep (x / n)`.  This holds at every positive `x`,
integer endpoints included; `TauCeti.tsum_mul_perronStep_natCast` evaluates the limit there.

```lean
TauCeti.tendsto_truncatedPerron_LSeries {f : ℕ → ℂ} {x c : ℝ} (hx : 0 < x) (hc : 0 < c)
  (h : LSeriesSummable f ↑c) :
  Filter.Tendsto
    (fun T =>
      (↑(2 * Real.pi))⁻¹ *
        ∫ (t : ℝ) in -T..T, LSeries f (↑c + ↑t * Complex.I) * TauCeti.perronIntegrand x c t)
    Filter.atTop (nhds (∑' (n : ℕ), f n * TauCeti.perronStep (x / ↑n)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The truncated Perron formula off the norms](the-truncated-perron-formula-off-the-norms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_truncatedPerron_LSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.html#TauCeti.tendsto_truncatedPerron_LSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_truncatedPerron_LSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.html#TauCeti.tendsto_truncatedPerron_LSeries)
- [Source of `TauCeti.tendsto_truncatedPerron_LSeries` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.lean#L286)
