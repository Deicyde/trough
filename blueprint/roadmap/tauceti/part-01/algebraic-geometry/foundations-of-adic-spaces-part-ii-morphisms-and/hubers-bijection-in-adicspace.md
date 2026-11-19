---
declaration: def
origin: cited
lean: TauCeti.AdicSpace.ofPairHomEquiv
statement: formalized
---

# Huber's bijection in `AdicSpace`

morphisms `Spa(B, B⁺) ⟶ Spa(A, A⁺)` in `AdicSpace`
between complete Hausdorff sheafy Huber pairs correspond bijectively to morphisms of Huber pairs
`(A, A⁺) → (B, B⁺)`.

```lean
TauCeti.AdicSpace.ofPairHomEquiv.{u} {A : Type u} [CommRing A] [UniformSpace A]
  [IsUniformAddGroup A] [IsTopologicalRing A] [CompleteSpace A] [T0Space A]
  [TauCeti.Huber.IsHuberRing A] {B : Type u} [CommRing B] [UniformSpace B] [IsUniformAddGroup B]
  [IsTopologicalRing B] [CompleteSpace B] [T0Space B] [TauCeti.Huber.IsHuberRing B]
  {S : TauCeti.Huber.Pair A} {T : TauCeti.Huber.Pair B}
  (hS : TauCeti.Huber.IsSheafyForEveryPresentation S.plus)
  (hT : TauCeti.Huber.IsSheafyForEveryPresentation T.plus) :
  (TauCeti.AdicSpace.ofPair T hT ⟶ TauCeti.AdicSpace.ofPair S hS) ≃ S.Hom T
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)
- [TauCeti.AdicSpace.ofPair](tauceti-adicspace-ofpair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.ofPairHomEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.ofPairHomEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.ofPairHomEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.html#TauCeti.AdicSpace.ofPairHomEquiv)
- [Source of `TauCeti.AdicSpace.ofPairHomEquiv` in TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Affinoid.lean#L452)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
