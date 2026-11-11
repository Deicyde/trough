---
declaration: def
origin: cited
lean: TauCeti.AdicSpace.comapOfPair
statement: formalized
---

# TauCeti.AdicSpace.comapOfPair

The morphism `Spa(B, B⁺) ⟶ Spa(A, A⁺)` in `AdicSpace` induced contravariantly by a morphism of
sheafy Huber pairs `φ : (A, A⁺) → (B, B⁺)`.

```lean
TauCeti.AdicSpace.comapOfPair.{u} {A : Type u} [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] {B : Type u} [CommRing B] [TopologicalSpace B]
  [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B] {S : TauCeti.Huber.Pair A}
  {T : TauCeti.Huber.Pair B} (hS : TauCeti.Huber.IsSheafyForEveryPresentation S.plus)
  (hT : TauCeti.Huber.IsSheafyForEveryPresentation T.plus) (φ : S.Hom T) :
  TauCeti.AdicSpace.ofPair T hT ⟶ TauCeti.AdicSpace.ofPair S hS
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)
- [TauCeti.AdicSpace.ofPair](tauceti-adicspace-ofpair.md)

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.comapOfPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.comapOfPair).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.comapOfPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.comapOfPair)
- [Source of `TauCeti.AdicSpace.comapOfPair` in TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean#L331)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
