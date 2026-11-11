---
declaration: theorem
origin: cited
lean: TauCeti.GTopology.isSheaf_iff
statement: formalized
proof: formalized
---

# TauCeti.GTopology.isSheaf_iff

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
- [Source of `TauCeti.GTopology.isSheaf_iff` in TauCeti/Topology/GTopology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/GTopology/Basic.lean#L238)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
