---
declaration: def
origin: cited
lean: TauCeti.LFunctions.primeIdealVonMangoldtBoundary
statement: formalized
---

# Boundary data for all primes of a number field

The von Mangoldt series of all primes of
`K` sums to `-ζ_K'(s)/ζ_K(s)` on `Re s > 1`, and `-ζ_K'(s)/ζ_K(s) - 1/(s - 1)` extends continuously
to `Re s ≥ 1` (`TauCeti.exists_continuousOn_eq_neg_deriv_dedekindZeta_div_sub`).

```lean
TauCeti.LFunctions.primeIdealVonMangoldtBoundary.{u_1} (K : Type u_1) [Field K] [NumberField K] :
  TauCeti.PrimeBoundaryRemainder K Set.univ 1
```

## Depends on

- [Boundary data for the prime Dirichlet series of `S`](boundary-data-for-the-prime-dirichlet-series-of.md)

## Proof depends on

- [The analytic Euler product](the-analytic-euler-product.md)
- [The Dedekind zeta function has no zeros on the line `Re s = 1` away from its pole](the-dedekind-zeta-function-has-no-zeros-on-the-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.primeIdealVonMangoldtBoundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/PrimeIdealBoundary.html#TauCeti.LFunctions.primeIdealVonMangoldtBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.primeIdealVonMangoldtBoundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/PrimeIdealBoundary.html#TauCeti.LFunctions.primeIdealVonMangoldtBoundary)
- [Source of `TauCeti.LFunctions.primeIdealVonMangoldtBoundary` in TauCeti/NumberTheory/LFunctions/PrimeIdealBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/PrimeIdealBoundary.lean#L39)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ArithmeticDirichletSeries/STATUS.md)
