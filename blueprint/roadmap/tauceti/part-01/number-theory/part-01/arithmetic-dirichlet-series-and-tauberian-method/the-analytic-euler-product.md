---
declaration: theorem
origin: cited
lean: TauCeti.EulerProductData.hasProd_eulerFactor
statement: formalized
proof: formalized
---

# The analytic Euler product

If the ideal-indexed Dirichlet series of `D` converges
absolutely at `s`, then its local Euler factors have an unrestricted
infinite product over the height-one primes, and that product is the `LSeries` of the norm
coefficients of `D`.

The hypothesis is absolute convergence of the *ideal-indexed* series, not of the regrouped one:
regrouping can only improve convergence, and the finite partial products of the local factors are
sums over ideals, not over norms.

```lean
TauCeti.EulerProductData.hasProd_eulerFactor.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (D : TauCeti.EulerProductData K) {s : ℂ}
  (hs : Summable (TauCeti.idealTerm K D.toIdealArithmeticFunction s)) :
  HasProd (fun P => D.eulerFactor P s)
    (LSeries (⇑((TauCeti.normCoeff K) D.toIdealArithmeticFunction)) s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.EulerProductData.hasProd_eulerFactor`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Analytic.html#TauCeti.EulerProductData.hasProd_eulerFactor).

## Sources

- [Tau Ceti documentation: `TauCeti.EulerProductData.hasProd_eulerFactor`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Analytic.html#TauCeti.EulerProductData.hasProd_eulerFactor)
- [Source of `TauCeti.EulerProductData.hasProd_eulerFactor` in TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Analytic.lean#L383)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ArithmeticDirichletSeries/STATUS.md)
