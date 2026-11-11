---
declaration: theorem
origin: cited
lean: TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left
statement: formalized
proof: formalized
---

# Unconditional affinoid fibre product over a stably sheafy left factor (Wedhorn, Theorem 8.56)

when `B` is stably sheafy and `A → C` is topologically of finite type, the completed
tensor product `(B, B⁺) ⊗̂_A (C, C⁺)` is automatically sheafy and gives a pullback square in
`AdicSpace`.

```lean
TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left.{u} {A B C : Type u} [CommRing A]
  [UniformSpace A] [IsUniformAddGroup A] [IsTopologicalRing A] [CompleteSpace A] [T0Space A]
  [TauCeti.Huber.IsHuberRing A] [CommRing B] [UniformSpace B] [IsUniformAddGroup B]
  [IsTopologicalRing B] [CompleteSpace B] [T0Space B] [TauCeti.Huber.IsHuberRing B] [CommRing C]
  [UniformSpace C] [IsUniformAddGroup C] [IsTopologicalRing C] [CompleteSpace C] [T0Space C]
  [TauCeti.Huber.IsHuberRing C] [Algebra A B] [Algebra A C]
  [TauCeti.Huber.IsAdicHom (algebraMap A B)] [TauCeti.Huber.IsAdicHom (algebraMap A C)]
  {S : TauCeti.Huber.Pair A} {T : TauCeti.Huber.Pair B} {U : TauCeti.Huber.Pair C}
  (hS : TauCeti.Huber.IsSheafyForEveryPresentation S.plus)
  (hU : TauCeti.Huber.IsSheafyForEveryPresentation U.plus) (hB : TauCeti.Huber.IsStablySheafyRing B)
  (hC : TauCeti.Huber.IsTopologicallyFiniteType (algebraMap A C)) (f : S.Hom T) (g : S.Hom U)
  (hf : f.toRingHom = algebraMap A B) (hg : g.toRingHom = algebraMap A C) :
  CategoryTheory.IsPullback
    (TauCeti.AdicSpace.comapOfPair ⋯ ⋯ (TauCeti.Huber.Pair.completedTensor.inl A T U))
    (TauCeti.AdicSpace.comapOfPair hU ⋯ (TauCeti.Huber.Pair.completedTensor.inr A T U))
    (TauCeti.AdicSpace.comapOfPair hS ⋯ f) (TauCeti.AdicSpace.comapOfPair hS hU g)
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)
- [The completed tensor product `(B, B⁺) ⊗̂_A (C, C⁺)` of Huber pairs along adic structure maps](the-completed-tensor-product-b-b-a-c-c-of-huber.md)
- [TauCeti.AdicSpace.comapOfPair](tauceti-adicspace-comapofpair.md)
- [TauCeti.AdicSpace.ofPair](tauceti-adicspace-ofpair.md)

## Proof depends on

- [Fibre product of affinoid adic spaces](fibre-product-of-affinoid-adic-spaces.md)
- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.html#TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.html#TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left)
- [Source of `TauCeti.AdicSpace.affinoid_isPullback_of_isStablySheafyRing_left` in TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean#L481)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
