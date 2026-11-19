---
declaration: theorem
origin: cited
lean: TauCeti.ContinuousAut.isClosed_isConj
statement: formalized
proof: formalized
---

# TauCeti.ContinuousAut.isClosed_isConj

For a topologically finitely generated profinite group, the automorphisms carrying `x` into
the conjugacy class of `y` form a closed set.

```lean
TauCeti.ContinuousAut.isClosed_isConj.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hG : TauCeti.IsTopologicallyFinitelyGenerated G) (x y : G) : IsClosed {φ | IsConj (φ x) y}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContinuousAut.isClosed_isConj`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/Congruence.html#TauCeti.ContinuousAut.isClosed_isConj).

## Sources

- [Tau Ceti documentation: `TauCeti.ContinuousAut.isClosed_isConj`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/Congruence.html#TauCeti.ContinuousAut.isClosed_isConj)
- [Source of `TauCeti.ContinuousAut.isClosed_isConj` in TauCeti/Topology/Algebra/Group/ContinuousAut/Congruence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/ContinuousAut/Congruence.lean#L310)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
