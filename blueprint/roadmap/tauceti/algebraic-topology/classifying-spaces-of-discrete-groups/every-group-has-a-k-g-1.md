---
declaration: theorem
origin: cited
lean: TauCeti.exists_isEilenbergMacLaneSpaceOne
statement: formalized
proof: formalized
---

# Every group has a `K(G, 1)`

**Every group has a `K(G, 1)`**, in its own universe, satisfying the standing hypotheses of
covering-space theory: local path-connectedness and semilocal simple connectivity. No hypothesis
on the group is needed.

```lean
TauCeti.exists_isEilenbergMacLaneSpaceOne.{u} (G : Type u) [Group G] :
  ∃ X x x_1,
    LocallyPathConnectedSpace X ∧
      TauCeti.SemilocallySimplyConnectedSpace X ∧ TauCeti.IsEilenbergMacLaneSpaceOne G X x_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental group at `x` acts on every homotopy group based at `x`](../universal-covers/the-fundamental-group-at-x-acts-on-every-homotop.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isEilenbergMacLaneSpaceOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/EilenbergMacLane.html#TauCeti.exists_isEilenbergMacLaneSpaceOne).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isEilenbergMacLaneSpaceOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/EilenbergMacLane.html#TauCeti.exists_isEilenbergMacLaneSpaceOne)
- [Source of `TauCeti.exists_isEilenbergMacLaneSpaceOne` in TauCeti/AlgebraicTopology/ClassifyingSpace/EilenbergMacLane.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/EilenbergMacLane.lean#L117)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
