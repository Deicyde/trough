---
declaration: theorem
origin: cited
lean: HasFPowerSeriesAt.coeff_mul
statement: formalized
proof: formalized
---

# The Cauchy product formula for power series coefficients

If `f`, `g` and `f * g` have
the power series `p`, `q` and `r` at `a`, then the `n`-th coefficient of `r` is
`∑_{i + j = n} p.coeff i * q.coeff j`.

```lean
HasFPowerSeriesAt.coeff_mul.{u_1, u_2} {𝕜 : Type u_1} {A : Type u_2} [NontriviallyNormedField 𝕜]
  [NormedRing A] [NormedAlgebra 𝕜 A] {f g : 𝕜 → A} {a : 𝕜} {p q r : FormalMultilinearSeries 𝕜 𝕜 A}
  (hf : HasFPowerSeriesAt f p a) (hg : HasFPowerSeriesAt g q a)
  (hfg : HasFPowerSeriesAt (f * g) r a) (n : ℕ) :
  r.coeff n = ∑ x ∈ Finset.HasAntidiagonal.antidiagonal n, p.coeff x.1 * q.coeff x.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasFPowerSeriesAt.coeff_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/TaylorSeries.html#HasFPowerSeriesAt.coeff_mul).

## Sources

- [Tau Ceti documentation: `HasFPowerSeriesAt.coeff_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/TaylorSeries.html#HasFPowerSeriesAt.coeff_mul)
- [Source of `HasFPowerSeriesAt.coeff_mul` in TauCeti/Analysis/Analytic/TaylorSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Analytic/TaylorSeries.lean#L75)
