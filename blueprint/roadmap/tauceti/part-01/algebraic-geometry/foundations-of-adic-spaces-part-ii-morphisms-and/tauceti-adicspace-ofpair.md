---
declaration: def
origin: cited
lean: TauCeti.AdicSpace.ofPair
statement: formalized
---

# TauCeti.AdicSpace.ofPair

The canonical affinoid adic space `Spa(A, A⁺)` attached to a Huber pair `S` whose plus ring
satisfies `IsSheafyForEveryPresentation`. Up to canonical isomorphism
(`ofPairIsoOfPresentation`), it is independent of any choice of compatible pair of definition.

```lean
TauCeti.AdicSpace.ofPair.{u} {A : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
  [TauCeti.Huber.IsHuberRing A] (S : TauCeti.Huber.Pair A)
  (hS : TauCeti.Huber.IsSheafyForEveryPresentation S.plus) : TauCeti.AdicSpace
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.ofPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.ofPair).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.ofPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.ofPair)
- [Source of `TauCeti.AdicSpace.ofPair` in TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean#L307)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
