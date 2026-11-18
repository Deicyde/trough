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

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The local square theorem bounds the defect of a unit](../local-field/the-local-square-theorem-bounds-the-defect-of-a.md)
- [The splitting criterion for quaternion algebras](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/part-01/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertSymbolForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.html#TauCeti.hilbertSymbolForm).

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertSymbolForm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.html#TauCeti.hilbertSymbolForm)
- [Source of `TauCeti.hilbertSymbolForm` in TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/QuadraticForm/HilbertSymbolForm.lean#L93)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
