---
declaration: def
origin: cited
lean: TauCeti.CoveringSpace.mk
statement: formalized
---

# TauCeti.CoveringSpace.mk

Construct a covering space over `X` from a covering map `p`. The definition is `@[expose]`d
so that its total space is `E` and its projection is `p` by `rfl` in downstream modules.

```lean
TauCeti.CoveringSpace.mk.{u} {X E : TopCat} (p : E ⟶ X)
  (hp : IsCoveringMap ⇑(CategoryTheory.ConcreteCategory.hom p)) : TauCeti.CoveringSpace X
```

## Depends on

- [TauCeti.CoveringSpace](tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CoveringSpace.mk`](https://taucetiproject.org/docs/TauCeti/Topology/Covering/Category.html#TauCeti.CoveringSpace.mk).

## Sources

- [Tau Ceti documentation: `TauCeti.CoveringSpace.mk`](https://taucetiproject.org/docs/TauCeti/Topology/Covering/Category.html#TauCeti.CoveringSpace.mk)
- [Source of `TauCeti.CoveringSpace.mk` in TauCeti/Topology/Covering/Category.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Covering/Category.lean#L131)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/UniversalCovers/STATUS.md)
