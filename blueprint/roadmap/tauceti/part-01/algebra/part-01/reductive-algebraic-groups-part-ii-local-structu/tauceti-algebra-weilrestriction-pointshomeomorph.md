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
  [Module.Finite A B] [Module.Projective A B] [Algebra.FinitePresentation B C] [TopologicalSpace A]
  [IsTopologicalRing A] [TopologicalSpace B] [IsModuleTopology A B] :
  (TauCeti.Algebra.WeilRestriction A B C →ₐ[A] A) ≃ₜ (C →ₐ[B] B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.WeilRestriction.pointsHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/WeilRestriction.html#TauCeti.Algebra.WeilRestriction.pointsHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.WeilRestriction.pointsHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/WeilRestriction.html#TauCeti.Algebra.WeilRestriction.pointsHomeomorph)
- [Source of `TauCeti.Algebra.WeilRestriction.pointsHomeomorph` in TauCeti/Topology/Algebra/PointTopology/WeilRestriction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/PointTopology/WeilRestriction.lean#L108)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
