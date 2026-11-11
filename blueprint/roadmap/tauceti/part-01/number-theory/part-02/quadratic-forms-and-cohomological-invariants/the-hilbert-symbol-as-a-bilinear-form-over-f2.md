---
declaration: def
origin: cited
lean: TauCeti.hilbertSymbolForm
statement: formalized
---

# The Hilbert symbol as a bilinear form over `𝔽₂`

Over a nonarchimedean local field in which
`2` is invertible, the Hilbert symbol on square classes, read in `ZMod 2` through the dictionary
`+1 ↦ 0`, `-1 ↦ 1`, is a `ZMod 2`-bilinear form on `Kˣ/(Kˣ)²`. Its sign is the symbol
(`TauCeti.hilbertSign_hilbertSymbolForm`).

```lean
TauCeti.hilbertSymbolForm.{u_1} (K : Type u_1) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Invertible 2] :
  LinearMap.BilinForm (ZMod 2) (TauCeti.SquareClassGroup K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The splitting criterion for quaternion algebras](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertSymbolForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.html#TauCeti.hilbertSymbolForm).

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertSymbolForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.html#TauCeti.hilbertSymbolForm)
- [Source of `TauCeti.hilbertSymbolForm` in TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.lean#L93)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
