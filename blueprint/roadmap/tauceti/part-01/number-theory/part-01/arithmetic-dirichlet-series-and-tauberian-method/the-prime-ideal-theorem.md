---
declaration: theorem
origin: cited
lean: TauCeti.primeIdealTheorem, TauCeti.primeCount_univ_isEquivalent_div_log
statement: formalized
proof: formalized
---

# The prime ideal theorem

For a number field `K`, Chebyshev's functions satisfy
`ψ_K(x) ~ x` and `ϑ_K(x) ~ x`, and the number `π_K(x)` of prime ideals of norm at most `x`
satisfies `π_K(x) ~ Li(x)`.

```lean
TauCeti.primeIdealTheorem.{u_1} (K : Type u_1) [Field K] [NumberField K] :
  (Asymptotics.IsEquivalent Filter.atTop (TauCeti.primePsi K Set.univ) fun x => x) ∧
    (Asymptotics.IsEquivalent Filter.atTop (TauCeti.primeTheta K Set.univ) fun x => x) ∧
      Asymptotics.IsEquivalent Filter.atTop (TauCeti.primeCount K Set.univ) TauCeti.Real.logIntegral
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Boundary data for all primes of a number field](boundary-data-for-all-primes-of-a-number-field.md)
- [The conditional prime ideal theorem](the-conditional-prime-ideal-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.primeIdealTheorem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.html#TauCeti.primeIdealTheorem).

## Other forms

**The prime ideal theorem, in the form `π_K(x) ~ x / log x`.** Formalized in Tau Ceti as [`TauCeti.primeCount_univ_isEquivalent_div_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.html#TauCeti.primeCount_univ_isEquivalent_div_log).

```lean
TauCeti.primeCount_univ_isEquivalent_div_log.{u_1} (K : Type u_1) [Field K] [NumberField K] :
  Asymptotics.IsEquivalent Filter.atTop (TauCeti.primeCount K Set.univ) fun x => x / Real.log x
```

## Sources

- [Tau Ceti documentation: `TauCeti.primeIdealTheorem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.html#TauCeti.primeIdealTheorem)
- [Source of `TauCeti.primeIdealTheorem` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.lean#L36)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ArithmeticDirichletSeries/STATUS.md)
