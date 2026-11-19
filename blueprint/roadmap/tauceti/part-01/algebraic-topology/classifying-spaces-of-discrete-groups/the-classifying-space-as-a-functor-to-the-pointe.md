---
declaration: def
origin: cited
lean: TauCeti.classifyingSpaceHomotopyFunctor
statement: formalized
---

# The classifying space as a functor to the pointed homotopy category

It sends a
homomorphism to the pointed homotopy class of the strictly functorial map of Milnor's classifying
spaces, so `TauCeti.classifyingSpaceFunctor` refines it.

```lean
TauCeti.classifyingSpaceHomotopyFunctor.{u} :
  CategoryTheory.Functor GrpCat TauCeti.PointedHomotopyCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.classifyingSpaceHomotopyFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/HomotopyFunctor.html#TauCeti.classifyingSpaceHomotopyFunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.classifyingSpaceHomotopyFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/HomotopyFunctor.html#TauCeti.classifyingSpaceHomotopyFunctor)
- [Source of `TauCeti.classifyingSpaceHomotopyFunctor` in TauCeti/AlgebraicTopology/ClassifyingSpace/HomotopyFunctor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ClassifyingSpace/HomotopyFunctor.lean#L104)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
