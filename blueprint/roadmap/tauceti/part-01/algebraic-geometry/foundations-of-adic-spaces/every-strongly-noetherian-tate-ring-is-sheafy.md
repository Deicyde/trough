---
declaration: theorem
origin: cited
lean: TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian
statement: formalized
proof: formalized
---

# Every strongly noetherian Tate ring is sheafy

**Every strongly noetherian Tate ring is sheafy** in the sense of Wedhorn's Definition 8.26
(`TauCeti.Huber.IsSheafyRing`). This is Wedhorn's Theorem 8.28(b); `A` need not be complete or
Hausdorff. The identity of `Â` is topologically of finite type, so this is the case `B = Â` of
`TauCeti.Huber.isStablySheafyRing_of_isStronglyNoetherian`.

```lean
TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian.{v} {A : Type v} [CommRing A] [UniformSpace A]
  [IsUniformAddGroup A] [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A]
  [TauCeti.Huber.IsStronglyNoetherian A] : TauCeti.Huber.IsSheafyRing A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A finite module over a complete noetherian Tate ring has a strict finite presentation](a-finite-module-over-a-complete-noetherian-tate.md)
- [A rational localisation of a strongly noetherian Tate ring is strongly noetherian](a-rational-localisation-of-a-strongly-noetherian.md)
- [Henkel's open mapping theorem](../../../part-02/topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [Henkel's theorem in quotient form](../../../part-02/topology/algebra/part-01/henkels-theorem-in-quotient-form.md)
- [The open mapping theorem over a Tate ring](the-open-mapping-theorem-over-a-tate-ring.md)
- [Strong noetherianness passes to an algebra topologically of finite type over a Tate ring](strong-noetherianness-passes-to-an-algebra-topol.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.html#TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.html#TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian)
- [Source of `TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.lean#L132)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
