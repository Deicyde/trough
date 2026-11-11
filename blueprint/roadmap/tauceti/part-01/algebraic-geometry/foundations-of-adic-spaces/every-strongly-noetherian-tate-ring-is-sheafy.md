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
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Henkel's open mapping theorem](../../topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [Henkel's theorem in quotient form](../../topology/algebra/part-01/henkels-theorem-in-quotient-form.md)
- [Ideals contained in supports](ideals-contained-in-supports.md)
- [The open mapping theorem over a Tate ring](the-open-mapping-theorem-over-a-tate-ring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.html#TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.html#TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian)
- [Source of `TauCeti.Huber.isSheafyRing_of_isStronglyNoetherian` in TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/Spa/StructurePresheaf/StronglyNoetherian.lean#L132)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
