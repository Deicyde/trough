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
- [Source of `TauCeti.GTopology` in TauCeti/Topology/GTopology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/GTopology/Basic.lean#L49)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
