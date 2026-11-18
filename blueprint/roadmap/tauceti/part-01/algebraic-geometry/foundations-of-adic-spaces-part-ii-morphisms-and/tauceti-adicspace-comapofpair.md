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

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.comapOfPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.comapOfPair).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.comapOfPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.comapOfPair)
- [Source of `TauCeti.AdicSpace.comapOfPair` in TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean#L331)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
