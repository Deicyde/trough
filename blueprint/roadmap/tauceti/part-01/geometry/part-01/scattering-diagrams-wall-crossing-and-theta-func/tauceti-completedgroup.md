---
declaration: def
origin: cited
lean: TauCeti.completedGroup
statement: formalized
---

# TauCeti.completedGroup

The compatible-family subgroup of a tower, indexed by natural numbers.

```lean
TauCeti.completedGroup.{u} (F : CategoryTheory.Functor ℕᵒᵖ GrpCat) :
  Subgroup ((k : ℕ) → ↑(F.obj (Opposite.op k)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.completedGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/CompletedGroup/Basic.html#TauCeti.completedGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.completedGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/CompletedGroup/Basic.html#TauCeti.completedGroup)
- [Source of `TauCeti.completedGroup` in TauCeti/GroupTheory/CompletedGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/CompletedGroup/Basic.lean#L37)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
