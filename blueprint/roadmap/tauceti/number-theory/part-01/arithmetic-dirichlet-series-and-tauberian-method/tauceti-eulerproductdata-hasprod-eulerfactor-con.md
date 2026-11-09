---
declaration: theorem
origin: cited
lean: TauCeti.EulerProductData.hasProd_eulerFactor_convolution
statement: formalized
proof: formalized
---

# TauCeti.EulerProductData.hasProd_eulerFactor_convolution

The Euler factors of a convolution have an unrestricted product equal to the product of
the original norm-regrouped Dirichlet series, whenever both ideal-indexed series converge
absolutely.

```lean
TauCeti.EulerProductData.hasProd_eulerFactor_convolution.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (D E : TauCeti.EulerProductData K) {s : ℂ}
  (hD : Summable (TauCeti.idealTerm K D.toIdealArithmeticFunction s))
  (hE : Summable (TauCeti.idealTerm K E.toIdealArithmeticFunction s)) :
  HasProd (fun P => (D.convolution E).eulerFactor P s)
    (LSeries (⇑((TauCeti.normCoeff K) D.toIdealArithmeticFunction)) s *
      LSeries (⇑((TauCeti.normCoeff K) E.toIdealArithmeticFunction)) s)
```

## Depends on

- [TauCeti.EulerProductData.convolution](tauceti-eulerproductdata-convolution.md)

## Proof depends on

- [The analytic Euler product](the-analytic-euler-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.EulerProductData.hasProd_eulerFactor_convolution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Analytic.html#TauCeti.EulerProductData.hasProd_eulerFactor_convolution).

## Sources

- [Tau Ceti documentation: `TauCeti.EulerProductData.hasProd_eulerFactor_convolution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Analytic.html#TauCeti.EulerProductData.hasProd_eulerFactor_convolution)
- [Source of `TauCeti.EulerProductData.hasProd_eulerFactor_convolution` in TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Analytic.lean#L69)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
