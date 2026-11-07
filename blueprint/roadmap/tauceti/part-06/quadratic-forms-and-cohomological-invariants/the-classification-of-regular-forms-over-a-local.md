---
declaration: def
origin: cited
lean: TauCeti.RegularFormClass.localInvariantsEquiv
statement: formalized
---

# The classification of regular forms over a local field, as an equivalence

Taking rank,
discriminant and local Hasse invariant is a bijection from regular-form classes over a
nonarchimedean local field onto admissible triples. Its inverse is the realization map.

```lean
TauCeti.RegularFormClass.localInvariantsEquiv.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Invertible 2] :
  TauCeti.RegularFormClass K ≃ { I // I.IsAdmissible }
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.QuaternionAlgebra.nonempty\_algEquiv\_matrix\_tfae](tauceti-quaternionalgebra-nonempty-algequiv-matr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.localInvariantsEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariantsEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.localInvariantsEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariantsEquiv)
- [Source of `TauCeti.RegularFormClass.localInvariantsEquiv` in TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean#L169)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
