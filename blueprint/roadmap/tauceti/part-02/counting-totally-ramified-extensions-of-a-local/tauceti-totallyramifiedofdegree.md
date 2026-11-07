---
declaration: def
origin: cited
lean: TauCeti.totallyRamifiedOfDegree
statement: formalized
---

# TauCeti.totallyRamifiedOfDegree

Serre's `σ_K(n)`: the subextensions of `SeparableClosure K` that are totally ramified of
degree `n` over `K`.

```lean
TauCeti.totallyRamifiedOfDegree.{u_1} (K : Type u_1) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] (n : ℕ) : Set (IntermediateField K (SeparableClosure K))
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.totallyRamifiedOfDegree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Basic.html#TauCeti.totallyRamifiedOfDegree).

## Sources

- [Tau Ceti documentation: `TauCeti.totallyRamifiedOfDegree`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Basic.html#TauCeti.totallyRamifiedOfDegree)
- [Source of `TauCeti.totallyRamifiedOfDegree` in TauCeti/NumberTheory/LocalField/MassFormula/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Basic.lean#L109)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
