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

- [Local classification (O'Meara 63:20, Serre IV Thm 7)](local-classification-omeara-63-20-serre-iv-thm-7.md)
- [The splitting criterion for quaternion algebras](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.localInvariantsEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariantsEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.localInvariantsEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariantsEquiv)
- [Source of `TauCeti.RegularFormClass.localInvariantsEquiv` in TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean#L169)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
