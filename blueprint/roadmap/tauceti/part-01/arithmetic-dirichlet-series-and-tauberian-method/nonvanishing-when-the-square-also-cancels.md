---
declaration: theorem
origin: cited
lean: TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq
statement: formalized
proof: formalized
---

# Nonvanishing when the square also cancels

If a unitary weight `χ` and its pointwise
square `χ ^ 2` both have cancellation, the continued L-function of `χ` has no zeros on the closed
half-plane `Re s ≥ 1`.

```lean
TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {χ : TauCeti.UnitaryIdealWeight K} (hχ : TauCeti.HasCancellation χ)
  (hχ₂ : TauCeti.HasCancellation (χ ^ 2)) {s : ℂ} (hs : 1 ≤ s.re) :
  TauCeti.continuedLFunctionOfWeight χ s ≠ 0
```

## Depends on

- [The continued L-function of a unitary weight](the-continued-l-function-of-a-unitary-weight.md)

## Proof depends on

- [The analytic Euler product](the-analytic-euler-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation/Nonvanishing.html#TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation/Nonvanishing.html#TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq)
- [Source of `TauCeti.continuedLFunctionOfWeight_ne_zero_of_hasCancellation_sq` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation/Nonvanishing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/Cancellation/Nonvanishing.lean#L81)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
