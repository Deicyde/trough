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
- [Source of `TauCeti.algebraicExtensionNormedField` in TauCeti/NumberTheory/LocalField/AlgebraicExtension/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/AlgebraicExtension/Basic.lean#L75)
- [Tau Ceti roadmap status: Local fields and ramification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalFieldsRamification/STATUS.md)
