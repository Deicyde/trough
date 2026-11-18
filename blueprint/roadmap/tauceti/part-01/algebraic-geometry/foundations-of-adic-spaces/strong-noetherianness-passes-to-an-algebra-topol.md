---
declaration: theorem
origin: cited
lean: TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian
statement: formalized
proof: formalized
---

# Strong noetherianness passes to an algebra topologically of finite type over a Tate ring

Over a strongly noetherian Tate ring `A`, a Hausdorff nonarchimedean ring `B`
admitting a map `φ : A →+* B` topologically of finite type is again strongly noetherian.

```lean
TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian.{u_1, u_2} {A : Type u_1} [CommRing A]
  [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsTateRing A]
  [TauCeti.Huber.IsStronglyNoetherian A] {B : Type u_2} [CommRing B] [UniformSpace B]
  [IsUniformAddGroup B] [NonarchimedeanRing B] [T0Space B] {φ : A →+* B}
  (hφ : TauCeti.Huber.IsTopologicallyFiniteType φ) : TauCeti.Huber.IsStronglyNoetherian B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TopologicallyFiniteType/Basic.html#TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/TopologicallyFiniteType/Basic.html#TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian)
- [Source of `TauCeti.Huber.IsTopologicallyFiniteType.isStronglyNoetherian` in TauCeti/RingTheory/Huber/TopologicallyFiniteType/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/TopologicallyFiniteType/Basic.lean#L975)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
