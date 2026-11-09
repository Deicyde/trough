---
declaration: def
origin: cited
lean: TauCeti.GroupPresentation.homEquiv
statement: formalized
---

# TauCeti.GroupPresentation.homEquiv

Homomorphisms from a finite presentation correspond to generator assignments satisfying
its transcribed relators. No generation or injectivity condition is imposed on the assignment.

```lean
TauCeti.GroupPresentation.homEquiv.{u_1} (P : TauCeti.GroupPresentation) {G : Type u_1} [Group G] :
  (P.Group →* G) ≃ { f // ∀ t ∈ P.transcribed, (FreeGroup.lift f) t.toFreeGroup = 1 }
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The compiled word denotes the direct interpretation of the relator expression](the-compiled-word-denotes-the-direct-interpretat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupPresentation.homEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/GroupPresentation.html#TauCeti.GroupPresentation.homEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupPresentation.homEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/GroupPresentation.html#TauCeti.GroupPresentation.homEquiv)
- [Source of `TauCeti.GroupPresentation.homEquiv` in TauCeti/GroupTheory/Presentation/GroupPresentation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Presentation/GroupPresentation.lean#L193)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CFSGStatement/STATUS.md)
