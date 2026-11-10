---
declaration: theorem
origin: cited
lean: TauCeti.simplyConnectedSpace_sphere
statement: formalized
proof: formalized
---

# TauCeti.simplyConnectedSpace_sphere

Every sphere of nonnegative radius in a real normed space of rank greater than two is
simply connected.

```lean
TauCeti.simplyConnectedSpace_sphere.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (h : 2 < Module.rank ℝ E) (c : E) {r : ℝ} (hr : 0 ≤ r) : SimplyConnectedSpace ↑(Metric.sphere c r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.simplyConnectedSpace_sphere`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Sphere/SimplyConnected.html#TauCeti.simplyConnectedSpace_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.simplyConnectedSpace_sphere`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Sphere/SimplyConnected.html#TauCeti.simplyConnectedSpace_sphere)
- [Source of `TauCeti.simplyConnectedSpace_sphere` in TauCeti/AlgebraicTopology/Sphere/SimplyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Sphere/SimplyConnected.lean#L387)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/UniversalCovers/STATUS.md)
