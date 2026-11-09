---
declaration: def
origin: cited
lean: TauCeti.algebraicExtensionNormedField
statement: formalized
---

# TauCeti.algebraicExtensionNormedField

The normed-field structure on an algebraic extension `M` of a nonarchimedean local field `K`
given by the spectral norm of `M/K` with respect to the normalized absolute value of `K`.

```lean
TauCeti.algebraicExtensionNormedField.{u_1, u_2} (K : Type u_1) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (M : Type u_2) [Field M] [Algebra K M]
  [Algebra.IsAlgebraic K M] : NormedField M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.algebraicExtensionNormedField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/AlgebraicExtension/Basic.html#TauCeti.algebraicExtensionNormedField).

## Sources

- [Tau Ceti documentation: `TauCeti.algebraicExtensionNormedField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/AlgebraicExtension/Basic.html#TauCeti.algebraicExtensionNormedField)
- [Source of `TauCeti.algebraicExtensionNormedField` in TauCeti/NumberTheory/LocalField/AlgebraicExtension/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/AlgebraicExtension/Basic.lean#L74)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalFieldsRamification/STATUS.md)
