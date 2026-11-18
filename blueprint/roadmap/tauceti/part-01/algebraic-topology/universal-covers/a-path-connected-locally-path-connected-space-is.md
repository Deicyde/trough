---
declaration: theorem
origin: cited
lean: TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace
statement: formalized
proof: formalized
---

# A path-connected, locally path-connected space is semilocally simply connected if and only if it admits a simply connected covering space

The forward direction is the universal-cover construction, the reverse direction is
`TauCeti.SemilocallySimplyConnectedSpace.of_isCoveringMap`; surjectivity of the covering map is
automatic here, by `IsCoveringMap.comp_subtypeVal_pathComponent_surjective`, because the base is
path-connected and a simply connected total space is nonempty.

```lean
TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace.{u}
  (X : Type u) [TopologicalSpace X] [PathConnectedSpace X] [LocallyPathConnectedSpace X] :
  TauCeti.SemilocallySimplyConnectedSpace X ↔ ∃ E x p, IsCoveringMap p ∧ SimplyConnectedSpace E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/SemilocallySimplyConnected.html#TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/SemilocallySimplyConnected.html#TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace)
- [Source of `TauCeti.semilocallySimplyConnectedSpace_iff_exists_isCoveringMap_and_simplyConnectedSpace` in TauCeti/AlgebraicTopology/UniversalCover/SemilocallySimplyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/UniversalCover/SemilocallySimplyConnected.lean#L46)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
