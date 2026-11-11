---
declaration: theorem
origin: cited
lean: TauCeti.AdicSpace.affinoid_isPullback
statement: formalized
proof: formalized
---

# Fibre product of affinoid adic spaces

**Fibre product of affinoid adic spaces** (Huber 1994, Proposition 3.7; Huber 1996,
Proposition 1.2.2; Wedhorn, Theorem 8.56): let `(A, A⁺)`, `(B, B⁺)` and `(C, C⁺)` be sheafy
complete Hausdorff Huber pairs and `f : (A, A⁺) → (B, B⁺)`, `g : (A, A⁺) → (C, C⁺)` adic morphisms
of Huber pairs. Whenever the completed tensor product `(B, B⁺) ⊗̂_A (C, C⁺)` is sheafy, its adic
spectrum is the pullback of `Spa(B, B⁺) ⟶ Spa(A, A⁺)` and `Spa(C, C⁺) ⟶ Spa(A, A⁺)` in
`AdicSpace`.

```lean
TauCeti.AdicSpace.affinoid_isPullback.{u} {A B C : Type u} [CommRing A] [UniformSpace A]
  [IsUniformAddGroup A] [IsTopologicalRing A] [CompleteSpace A] [T0Space A]
  [TauCeti.Huber.IsHuberRing A] [CommRing B] [UniformSpace B] [IsUniformAddGroup B]
  [IsTopologicalRing B] [CompleteSpace B] [T0Space B] [TauCeti.Huber.IsHuberRing B] [CommRing C]
  [UniformSpace C] [IsUniformAddGroup C] [IsTopologicalRing C] [CompleteSpace C] [T0Space C]
  [TauCeti.Huber.IsHuberRing C] [Algebra A B] [Algebra A C]
  [TauCeti.Huber.IsAdicHom (algebraMap A B)] [TauCeti.Huber.IsAdicHom (algebraMap A C)]
  {S : TauCeti.Huber.Pair A} {T : TauCeti.Huber.Pair B} {U : TauCeti.Huber.Pair C}
  (hS : TauCeti.Huber.IsSheafyForEveryPresentation S.plus)
  (hT : TauCeti.Huber.IsSheafyForEveryPresentation T.plus)
  (hU : TauCeti.Huber.IsSheafyForEveryPresentation U.plus)
  (hTU : TauCeti.Huber.IsSheafyForEveryPresentation (TauCeti.Huber.Pair.completedTensor A T U).plus)
  (f : S.Hom T) (g : S.Hom U) (hf : f.toRingHom = algebraMap A B)
  (hg : g.toRingHom = algebraMap A C) :
  CategoryTheory.IsPullback
    (TauCeti.AdicSpace.comapOfPair hT hTU (TauCeti.Huber.Pair.completedTensor.inl A T U))
    (TauCeti.AdicSpace.comapOfPair hU hTU (TauCeti.Huber.Pair.completedTensor.inr A T U))
    (TauCeti.AdicSpace.comapOfPair hS hT f) (TauCeti.AdicSpace.comapOfPair hS hU g)
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](../foundations-of-adic-spaces/adic-spaces-wedhorn-definition-8-22.md)
- [The completed tensor product `(B, B⁺) ⊗̂_A (C, C⁺)` of Huber pairs along adic structure maps](the-completed-tensor-product-b-b-a-c-c-of-huber.md)
- [TauCeti.AdicSpace.comapOfPair](tauceti-adicspace-comapofpair.md)
- [TauCeti.AdicSpace.ofPair](tauceti-adicspace-ofpair.md)

## Proof depends on

- [Ideals contained in supports](../foundations-of-adic-spaces/ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicSpace.affinoid_isPullback`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.html#TauCeti.AdicSpace.affinoid_isPullback).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicSpace.affinoid_isPullback`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.html#TauCeti.AdicSpace.affinoid_isPullback)
- [Source of `TauCeti.AdicSpace.affinoid_isPullback` in TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Pullback/Affinoid.lean#L459)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
