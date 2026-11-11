---
declaration: theorem
origin: cited
lean: TauCeti.perronFormula_of_forall_absNorm_ne, TauCeti.perronFormula_natCast
statement: formalized
proof: formalized
---

# The Perron formula off the norms

If `x > 0` is not the absolute norm of a nonzero ideal,
the truncated Perron integral tends to the inclusive ideal sum `∑_{N(I) ≤ x} f(I)`.

```lean
TauCeti.perronFormula_of_forall_absNorm_ne.{u_1} {K : Type u_1} [Field K] [NumberField K]
  {f : TauCeti.IdealArithmeticFunction K} {x c : ℝ} (hx : 0 < x) (hc : 0 < c)
  (hoff :
    ∀ (I : ↥(nonZeroDivisors (Ideal (NumberField.RingOfIntegers K)))), ↑(Ideal.absNorm ↑I) ≠ x)
  (h : LSeriesSummable ⇑((TauCeti.normCoeff K) f) ↑c) :
  Filter.Tendsto
    (fun T =>
      (↑(2 * Real.pi))⁻¹ *
        ∫ (t : ℝ) in -T..T,
          LSeries (⇑((TauCeti.normCoeff K) f)) (↑c + ↑t * Complex.I) *
            TauCeti.perronIntegrand x c t)
    Filter.atTop (nhds (TauCeti.idealSummatory K f x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The arithmetic Perron formula for ideal sums](the-arithmetic-perron-formula-for-ideal-sums.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.perronFormula_of_forall_absNorm_ne`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.perronFormula_of_forall_absNorm_ne).

## Other forms

**The Perron formula at an integer endpoint.** Formalized in Tau Ceti as [`TauCeti.perronFormula_natCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.perronFormula_natCast).

```lean
TauCeti.perronFormula_natCast.{u_1} {K : Type u_1} [Field K] [NumberField K]
  {f : TauCeti.IdealArithmeticFunction K} {c : ℝ} {N : ℕ} (hN : 0 < N) (hc : 0 < c)
  (h : LSeriesSummable ⇑((TauCeti.normCoeff K) f) ↑c) :
  Filter.Tendsto
    (fun T =>
      (↑(2 * Real.pi))⁻¹ *
        ∫ (t : ℝ) in -T..T,
          LSeries (⇑((TauCeti.normCoeff K) f)) (↑c + ↑t * Complex.I) *
            TauCeti.perronIntegrand (↑N) c t)
    Filter.atTop (nhds (TauCeti.idealSummatory K f ↑N - ((TauCeti.normCoeff K) f) N / 2))
```

## Sources

- [Tau Ceti documentation: `TauCeti.perronFormula_of_forall_absNorm_ne`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.html#TauCeti.perronFormula_of_forall_absNorm_ne)
- [Source of `TauCeti.perronFormula_of_forall_absNorm_ne` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ArithmeticDirichletSeries/Perron/Ideal.lean#L178)
