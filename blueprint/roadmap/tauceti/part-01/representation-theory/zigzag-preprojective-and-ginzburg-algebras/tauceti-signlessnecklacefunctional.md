---
declaration: def
origin: cited
lean: TauCeti.signlessNecklaceFunctional
statement: formalized
---

# TauCeti.signlessNecklaceFunctional

The **signless necklace functional**: for a weight `W` on necklaces satisfying the signless
necklace relations, the necklace functional descends to the signless preprojective algebra. It
sends the class of a closed path to the weight of its necklace, and kills commutators.

```lean
TauCeti.signlessNecklaceFunctional.{u, w} (k : Type w) {V : Type u} (G : SimpleGraph V) [CommRing k]
  [(v : V) → Fintype ↑(G.neighborSet v)] (W : Cycle V → k) [Finite V]
  (hW : TauCeti.IsSignlessNecklaceWeight G W) :
  TauCeti.signlessPreprojectiveAlgebra k (TauCeti.DoubledQuiver G) →ₗ[k] k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.signlessNecklaceFunctional`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/Signless/Necklace.html#TauCeti.signlessNecklaceFunctional).

## Sources

- [Tau Ceti documentation: `TauCeti.signlessNecklaceFunctional`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Preprojective/Signless/Necklace.html#TauCeti.signlessNecklaceFunctional)
- [Source of `TauCeti.signlessNecklaceFunctional` in TauCeti/RepresentationTheory/Quiver/Preprojective/Signless/Necklace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Preprojective/Signless/Necklace.lean#L274)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
