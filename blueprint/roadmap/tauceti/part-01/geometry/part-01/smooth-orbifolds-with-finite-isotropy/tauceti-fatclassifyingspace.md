---
declaration: def
origin: cited
lean: TauCeti.fatClassifyingSpace
statement: formalized
---

# TauCeti.fatClassifyingSpace

The fat classifying space of a category whose total arrows carry a topology: the fat
realization of its topological nerve, with degeneracies forgotten.

```lean
TauCeti.fatClassifyingSpace.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [TopologicalSpace (Quiver.Total C)] : TopCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fatClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/Nerve.html#TauCeti.fatClassifyingSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.fatClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/Nerve.html#TauCeti.fatClassifyingSpace)
- [Source of `TauCeti.fatClassifyingSpace` in TauCeti/Topology/CategoryTheory/Nerve.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/CategoryTheory/Nerve.lean#L150)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
