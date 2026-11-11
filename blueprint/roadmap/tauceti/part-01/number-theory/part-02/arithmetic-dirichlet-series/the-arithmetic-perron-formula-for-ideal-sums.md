---
declaration: theorem
origin: cited
lean: TauCeti.perronFormula, TauCeti.tendsto_truncatedPerron_LSeries_natCast
statement: formalized
proof: formalized
---

# The arithmetic Perron formula for ideal sums

Where the `L`-series of the norm
coefficients of `f` converges absolutely on the line `Re s = c`, the truncated Perron integral
tends, as the height grows, to the ideal sum `∑_{N(I) ≤ x} f(I)` in which each ideal of norm
exactly `x` carries half weight.  The two readings of this limit are
`TauCeti.perronFormula_of_forall_absNorm_ne` and `TauCeti.perronFormula_natCast`.

```lean
TauCeti.perronFormula.{u_1} {K : Type u_1} [Field K] [NumberField K]
  {f : TauCeti.IdealArithmeticFunction K} {x c : ℝ} (hx : 0 < x) (hc : 0 < c)
  (h : LSeriesSummable ⇑((TauCeti.normCoeff K) f) ↑c) :
  Filter.Tendsto
    (fun T =>
      (↑(2 * Real.pi))⁻¹ *
        ∫ (t : ℝ) in -T..T,
          LSeries (⇑((TauCeti.normCoeff K) f)) (↑c + ↑t * Complex.I) *
            TauCeti.perronIntegrand x c t)
    Filter.atTop
    (nhds (∑ I ∈ TauCeti.idealsLE K x, f I * TauCeti.perronStep (x / ↑(Ideal.absNorm ↑I))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The limiting arithmetic Perron formula](the-limiting-arithmetic-perron-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.perronFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.perronFormula).

## Other forms

**The arithmetic Perron formula at an integer endpoint.** Formalized in Tau Ceti as [`TauCeti.tendsto_truncatedPerron_LSeries_natCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Formula.html#TauCeti.tendsto_truncatedPerron_LSeries_natCast).

```lean
TauCeti.tendsto_truncatedPerron_LSeries_natCast {f : ℕ → ℂ} {c : ℝ} {N : ℕ} (hN : 0 < N)
  (hc : 0 < c) (h : LSeriesSummable f ↑c) :
  Filter.Tendsto
    (fun T =>
      (↑(2 * Real.pi))⁻¹ *
        ∫ (t : ℝ) in -T..T, LSeries f (↑c + ↑t * Complex.I) * TauCeti.perronIntegrand (↑N) c t)
    Filter.atTop (nhds (∑ n ∈ Finset.Ico 1 N, f n + f N / 2))
```

## Sources

- [Tau Ceti documentation: `TauCeti.perronFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.perronFormula)
- [Source of `TauCeti.perronFormula` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.lean#L156)
