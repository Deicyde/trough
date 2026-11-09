---
declaration: theorem
origin: cited
lean: TauCeti.Relator.toWord_toFreeGroup
statement: formalized
proof: formalized
---

# The compiled word denotes the direct interpretation of the relator expression

Consequently, a reviewer may check the structured `Relator` against a published presentation while
the eventual `PresentedGroup` safely uses `FreeGroup.mk r.toWord` as its defining relation.

```lean
TauCeti.Relator.toWord_toFreeGroup.{u_1} {α : Type u_1} (r : TauCeti.Relator α) :
  FreeGroup.mk r.toWord = r.toFreeGroup
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Relator.toWord_toFreeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/Relator.html#TauCeti.Relator.toWord_toFreeGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Relator.toWord_toFreeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Presentation/Relator.html#TauCeti.Relator.toWord_toFreeGroup)
- [Source of `TauCeti.Relator.toWord_toFreeGroup` in TauCeti/GroupTheory/Presentation/Relator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Presentation/Relator.lean#L457)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CFSGStatement/STATUS.md)
