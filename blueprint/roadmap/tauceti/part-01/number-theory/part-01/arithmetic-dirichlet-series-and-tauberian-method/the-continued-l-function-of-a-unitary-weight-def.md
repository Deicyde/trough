---
declaration: def
origin: cited
lean: TauCeti.continuedLFunctionOfWeight
statement: formalized
---

# The continued L-function of a unitary weight, defined by partial summation

`s * ∫_{1}^{∞} (∑_{N(I) ≤ t} χ(I)) t ^ (-(s + 1)) dt`.

On `Re s > 1` it is the norm-regrouped L-series of `χ`
(`TauCeti.continuedLFunctionOfWeight_eq_LSeries`); under `TauCeti.HasCancellation χ` it is
holomorphic on `Re s > 1 - 1 / [K : ℚ]` (`TauCeti.differentiableOn_continuedLFunctionOfWeight`).
Where the integral does not converge it takes the junk value of Mathlib's Bochner integral.

```lean
TauCeti.continuedLFunctionOfWeight.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (χ : TauCeti.UnitaryIdealWeight K) (s : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.continuedLFunctionOfWeight`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation.html#TauCeti.continuedLFunctionOfWeight).

## Sources

- [Tau Ceti documentation: `TauCeti.continuedLFunctionOfWeight`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation.html#TauCeti.continuedLFunctionOfWeight)
- [Source of `TauCeti.continuedLFunctionOfWeight` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation.lean#L275)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ArithmeticDirichletSeries/STATUS.md)
