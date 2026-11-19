---
declaration: def
origin: cited
lean: TauCeti.Almost.Module
statement: formalized
---

# TauCeti.Almost.Module

The category of **almost `V`-modules** for a basic setup `S = (V, m)` (Gabber–Ramero (2.2.2),
Scholze, *Perfectoid spaces*, Definition 4.3): the Serre quotient of `ModuleCat V` by the almost
zero modules, i.e. the localization of `ModuleCat V` at the almost isomorphisms. Its Hom-types
live in the universe of the `V`-modules.

```lean
TauCeti.Almost.Module.{u} {V : Type u} [CommRing V] (S : TauCeti.Almost.BasicSetup V) : Type (u + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Almost.Module`](https://taucetiproject.org/docs/TauCeti/RingTheory/Almost/Module.html#TauCeti.Almost.Module).

## Sources

- [Tau Ceti documentation: `TauCeti.Almost.Module`](https://taucetiproject.org/docs/TauCeti/RingTheory/Almost/Module.html#TauCeti.Almost.Module)
- [Source of `TauCeti.Almost.Module` in TauCeti/RingTheory/Almost/Module.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Almost/Module.lean#L76)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)
