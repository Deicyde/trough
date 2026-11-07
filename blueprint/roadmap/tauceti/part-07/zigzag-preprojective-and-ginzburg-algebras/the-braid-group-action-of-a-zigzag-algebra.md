---
declaration: def
origin: cited
lean: TauCeti.zigzagBraidArtinAction
statement: formalized
---

# The braid group action of a zigzag algebra

The Artin group of the graph `G` acts on the
homotopy category of graded `Z`-modules, by sending the standard generator at a vertex `i` to the
class of tensoring with the braid complex `Bᵢ`.

```lean
TauCeti.zigzagBraidArtinAction.{u, w} (k : Type w) [CommRing k] {V : Type u} (G : SimpleGraph V)
  [Finite V] :
  TauCeti.ArtinGroup G.coxeterMatrix →*
    TauCeti.AutoequivalenceClass
      (HomotopyCategory
        (TauCeti.GradedModuleCat ((TauCeti.zigzagAlgebraInternalGrading k G).piece ℤ))
        (ComplexShape.up ℤ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagBraidArtinAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Action.html#TauCeti.zigzagBraidArtinAction).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagBraidArtinAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Action.html#TauCeti.zigzagBraidArtinAction)
- [Source of `TauCeti.zigzagBraidArtinAction` in TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Action.lean#L156)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
