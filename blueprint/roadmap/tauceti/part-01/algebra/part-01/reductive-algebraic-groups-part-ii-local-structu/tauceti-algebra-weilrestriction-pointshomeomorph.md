---
declaration: def
origin: cited
lean: TauCeti.Algebra.WeilRestriction.pointsHomeomorph
statement: formalized
---

# TauCeti.Algebra.WeilRestriction.pointsHomeomorph

Restriction of scalars identifies `A`-points of the Weil restriction with `B`-points,
homeomorphically when `B` carries its finite projective `A`-module topology.

```lean
TauCeti.Algebra.WeilRestriction.pointsHomeomorph.{u_1, u_2, u_3} (A : Type u_1) (B : Type u_2)
  (C : Type u_3) [CommRing A] [CommRing B] [CommRing C] [Algebra A B] [Algebra B C]
  [Module.Finite A B] [Module.Projective A B] [TopologicalSpace A] [IsTopologicalRing A]
  [TopologicalSpace B] [IsModuleTopology A B] :
  (TauCeti.Algebra.WeilRestriction A B C →ₐ[A] A) ≃ₜ (C →ₐ[B] B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.WeilRestriction.pointsHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/WeilRestriction.html#TauCeti.Algebra.WeilRestriction.pointsHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.WeilRestriction.pointsHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/WeilRestriction.html#TauCeti.Algebra.WeilRestriction.pointsHomeomorph)
- [Source of `TauCeti.Algebra.WeilRestriction.pointsHomeomorph` in TauCeti/Topology/Algebra/PointTopology/WeilRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/PointTopology/WeilRestriction.lean#L107)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
