---
declaration: def
origin: cited
lean: TauCeti.zigzagBraidDerivedArtinAction
statement: formalized
---

# TauCeti.zigzagBraidDerivedArtinAction

The graph Artin group acts on natural-isomorphism classes of the derived vertex
autoequivalences, through the existing Artin presentation.

```lean
TauCeti.zigzagBraidDerivedArtinAction.{u, w, z} (k : Type w) [CommRing k] {V : Type u}
  (G : SimpleGraph V) [Finite V]
  [HasDerivedCategory (TauCeti.GradedModuleCat (TauCeti.zigzagAlgebraInternalGrading k G).piece)] :
  TauCeti.ArtinGroup G.coxeterMatrix →*
    TauCeti.AutoequivalenceClass
      (DerivedCategory (TauCeti.GradedModuleCat (TauCeti.zigzagAlgebraInternalGrading k G).piece))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagBraidDerivedArtinAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.html#TauCeti.zigzagBraidDerivedArtinAction).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagBraidDerivedArtinAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.html#TauCeti.zigzagBraidDerivedArtinAction)
- [Source of `TauCeti.zigzagBraidDerivedArtinAction` in TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.lean#L46)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
