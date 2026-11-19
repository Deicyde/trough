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

- [The analytic Euler product](the-analytic-euler-product.md)
- [Boundary data for the prime Dirichlet series of `S`](boundary-data-for-the-prime-dirichlet-series-of.md)
- [The conditional prime ideal theorem](the-conditional-prime-ideal-theorem.md)
- [The Dedekind zeta function has no zeros on the line `Re s = 1` away from its pole](the-dedekind-zeta-function-has-no-zeros-on-the-l.md)

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
- [Source of `TauCeti.primeIdealTheorem` in TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ArithmeticDirichletSeries/Prime/PrimeIdealTheorem.lean#L36)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ArithmeticDirichletSeries/STATUS.md)
