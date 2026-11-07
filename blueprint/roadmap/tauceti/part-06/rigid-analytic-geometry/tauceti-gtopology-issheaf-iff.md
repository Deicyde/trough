---
declaration: theorem
origin: cited
lean: TauCeti.GTopology.isSheaf_iff
statement: formalized
proof: formalized
---

# TauCeti.GTopology.isSheaf\_iff

The site sheaf condition is precisely unique gluing of matching families on all admissible
covers. `Presieve.IsSheafFor` is Mathlib's existence-and-uniqueness condition for amalgamations.

```lean
TauCeti.GTopology.isSheaf_iff.{u, v, w} {X : Type u} {B : Type v} [SemilatticeInf B] [OrderTop B]
  {ι : B ↪o Set X} (G : TauCeti.GTopology ι) (P : CategoryTheory.Functor Bᵒᵖ (Type w)) :
  CategoryTheory.Presieve.IsSheaf G.grothendieckTopology P ↔
    ∀ (U : B) (S : Set B),
      G.Covers U S → CategoryTheory.Presieve.IsSheafFor P (TauCeti.GTopology.coverPresieve U S)
```

## Depends on

- [TauCeti.GTopology](tauceti-gtopology.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GTopology.isSheaf_iff`](https://taucetiproject.org/docs/TauCeti/Topology/GTopology/Basic.html#TauCeti.GTopology.isSheaf_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GTopology.isSheaf_iff`](https://taucetiproject.org/docs/TauCeti/Topology/GTopology/Basic.html#TauCeti.GTopology.isSheaf_iff)
- [Source of `TauCeti.GTopology.isSheaf_iff` in TauCeti/Topology/GTopology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/GTopology/Basic.lean#L238)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
