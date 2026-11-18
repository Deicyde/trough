---
declaration: theorem
origin: cited
lean: TauCeti.PointTopology.isTopologicalGroup
statement: formalized
proof: formalized
---

# TauCeti.PointTopology.isTopologicalGroup

The points `WithConv (H →ₐ[k] R)` of a Hopf algebra, with the convolution group structure and
the point topology, form a topological group when the coefficients form a topological semiring.

```lean
TauCeti.PointTopology.isTopologicalGroup.{u_1, u_2, u_3} {k : Type u_1} {H : Type u_2}
  {R : Type u_3} [CommSemiring k] [Semiring H] [CommSemiring R] [Algebra k R] [TopologicalSpace R]
  [HopfAlgebra k H] [IsTopologicalSemiring R] : IsTopologicalGroup (WithConv (H →ₐ[k] R))
```

## Depends on

- [TauCeti.PointTopology.instTopologicalSpaceWithConv](tauceti-pointtopology-insttopologicalspacewithco.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PointTopology.isTopologicalGroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/Group.html#TauCeti.PointTopology.isTopologicalGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.PointTopology.isTopologicalGroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/PointTopology/Group.html#TauCeti.PointTopology.isTopologicalGroup)
- [Source of `TauCeti.PointTopology.isTopologicalGroup` in TauCeti/Topology/Algebra/PointTopology/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/PointTopology/Group.lean#L100)
- [Tau Ceti roadmap status: Reductive algebraic groups, part II — local structure and arithmetic models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroupsPartII/STATUS.md)
