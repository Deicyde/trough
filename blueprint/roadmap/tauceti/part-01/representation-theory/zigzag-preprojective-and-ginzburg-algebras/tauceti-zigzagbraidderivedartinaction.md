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
  [HasDerivedCategory
      (TauCeti.GradedModuleCat ((TauCeti.zigzagAlgebraInternalGrading k G).piece ℤ))] :
  TauCeti.ArtinGroup G.coxeterMatrix →*
    TauCeti.AutoequivalenceClass
      (DerivedCategory
        (TauCeti.GradedModuleCat ((TauCeti.zigzagAlgebraInternalGrading k G).piece ℤ)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagBraidDerivedArtinAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.html#TauCeti.zigzagBraidDerivedArtinAction).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagBraidDerivedArtinAction`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.html#TauCeti.zigzagBraidDerivedArtinAction)
- [Source of `TauCeti.zigzagBraidDerivedArtinAction` in TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Zigzag/Braid/Module/Derived/Action.lean#L46)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
