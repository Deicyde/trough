---
declaration: structure
origin: cited
lean: TauCeti.IsLocalTiling
statement: formalized
---

# TauCeti.IsLocalTiling

A **local tiling** by a closed path-connected tile `P`: for each `x ∈ P`, `N x` is a set of
local neighbours, the elements `h` such that `h • P` is one of the tiles around `x`. The
identity is a neighbour, `x ∈ h • P` for each neighbour `h`, the neighbours of `x` seen from the
tile `h • P` are the translates `h⁻¹ • N x`, and each point of `P` lies in a tiling chart made of
its own neighbours.

```lean
TauCeti.IsLocalTiling.{u_1, u_2} {G : Type u_1} {X : Type u_2} [Group G] [MulAction G X]
  [TopologicalSpace X] (P : Set X) (N : X → Set G) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocalTiling`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/LocalTiling.html#TauCeti.IsLocalTiling).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocalTiling`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/LocalTiling.html#TauCeti.IsLocalTiling)
- [Source of `TauCeti.IsLocalTiling` in TauCeti/Topology/Algebra/GroupAction/LocalTiling.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/GroupAction/LocalTiling.lean#L116)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
