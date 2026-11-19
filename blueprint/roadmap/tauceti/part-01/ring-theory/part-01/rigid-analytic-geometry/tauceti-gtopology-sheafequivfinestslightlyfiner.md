---
declaration: def
origin: cited
lean: TauCeti.GTopology.sheafEquivFinestSlightlyFiner
statement: formalized
---

# TauCeti.GTopology.sheafEquivFinestSlightlyFiner

Every sheaf on a G-topology extends uniquely to the finest slightly finer G-topology
[BGR, 9.1.2/2 and 9.2.3/1].

```lean
TauCeti.GTopology.sheafEquivFinestSlightlyFiner.{u, v, w, w'} {X : Type u} {B : Type v}
  [SemilatticeInf B] [OrderTop B] {ι : B ↪o Set X} (G : TauCeti.GTopology ι) (A : Type w)
  [CategoryTheory.Category.{w', w} A]
  [∀ (V : (TauCeti.GTopology.GeneratedOpens ι)ᵒᵖ),
      CategoryTheory.Limits.HasLimitsOfShape
        (CategoryTheory.StructuredArrow V G.finestSlightlyFinerId.comapFunctor.op) A] :
  CategoryTheory.Sheaf G.grothendieckTopology A ≌
    CategoryTheory.Sheaf G.finestSlightlyFiner.grothendieckTopology A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GTopology.sheafEquivFinestSlightlyFiner`](https://taucetiproject.org/docs/TauCeti/Topology/GTopology/SlightlyFiner.html#TauCeti.GTopology.sheafEquivFinestSlightlyFiner).

## Sources

- [Tau Ceti documentation: `TauCeti.GTopology.sheafEquivFinestSlightlyFiner`](https://taucetiproject.org/docs/TauCeti/Topology/GTopology/SlightlyFiner.html#TauCeti.GTopology.sheafEquivFinestSlightlyFiner)
- [Source of `TauCeti.GTopology.sheafEquivFinestSlightlyFiner` in TauCeti/Topology/GTopology/SlightlyFiner.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/GTopology/SlightlyFiner.lean#L299)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
