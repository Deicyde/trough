---
declaration: structure
origin: cited
lean: TauCeti.GTopology
statement: formalized
---

# TauCeti.GTopology

Admissible covers on a family of subsets closed under finite intersections and containing
the whole space. The family is represented by an order embedding `ι`, preserving intersections
and the largest open. Covering families are sets, so repetitions and indexing choices carry
no additional data.

```lean
TauCeti.GTopology.{u, v} {X : Type u} {B : Type v} [SemilatticeInf B] [OrderTop B]
  (ι : B ↪o Set X) : Type v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GTopology`](https://taucetiproject.org/docs/TauCeti/Topology/GTopology/Basic.html#TauCeti.GTopology).

## Sources

- [Tau Ceti documentation: `TauCeti.GTopology`](https://taucetiproject.org/docs/TauCeti/Topology/GTopology/Basic.html#TauCeti.GTopology)
- [Source of `TauCeti.GTopology` in TauCeti/Topology/GTopology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/GTopology/Basic.lean#L49)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
