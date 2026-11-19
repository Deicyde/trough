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
- [Source of `TauCeti.simplyConnectedSpace_sphere` in TauCeti/AlgebraicTopology/Sphere/SimplyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Sphere/SimplyConnected.lean#L419)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
