---
declaration: def
origin: cited
lean: TauCeti.EulerProductData.convolution
statement: formalized
---

# TauCeti.EulerProductData.convolution

Convolve two ideal coefficient systems. This operation multiplies local series and is
distinct from the pointwise multiplication instance on `EulerProductData`.

```lean
TauCeti.EulerProductData.convolution.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (D E : TauCeti.EulerProductData K) : TauCeti.EulerProductData K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.EulerProductData.convolution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Basic.html#TauCeti.EulerProductData.convolution).

## Sources

- [Tau Ceti documentation: `TauCeti.EulerProductData.convolution`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Basic.html#TauCeti.EulerProductData.convolution)
- [Source of `TauCeti.EulerProductData.convolution` in TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/EulerProduct/Convolution/Basic.lean#L110)
- [Tau Ceti roadmap status: Arithmetic Dirichlet series and Tauberian methods](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ArithmeticDirichletSeries/STATUS.md)
