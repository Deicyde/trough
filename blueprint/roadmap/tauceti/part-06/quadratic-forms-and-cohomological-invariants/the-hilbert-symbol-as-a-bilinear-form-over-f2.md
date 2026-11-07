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

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.QuaternionAlgebra.nonempty\_algEquiv\_matrix\_tfae](tauceti-quaternionalgebra-nonempty-algequiv-matr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertSymbolForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.html#TauCeti.hilbertSymbolForm).

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertSymbolForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.html#TauCeti.hilbertSymbolForm)
- [Source of `TauCeti.hilbertSymbolForm` in TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.lean#L93)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
