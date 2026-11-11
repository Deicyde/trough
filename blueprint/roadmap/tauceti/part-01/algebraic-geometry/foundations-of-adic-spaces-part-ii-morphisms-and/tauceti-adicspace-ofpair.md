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

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.ofPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.ofPair).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.ofPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.ofPair)
- [Source of `TauCeti.AdicSpace.ofPair` in TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean#L307)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
