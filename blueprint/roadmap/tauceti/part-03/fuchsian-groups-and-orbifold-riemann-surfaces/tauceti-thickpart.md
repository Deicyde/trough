---
declaration: def
origin: cited
lean: TauCeti.thickPart
statement: formalized
---

# TauCeti.thickPart

The **`ε`-thick part** of an action on a metric space: the points moved a distance at least
`ε` by every nonidentity element. For `0 < ε` it excludes every point with nontrivial
stabilizer.

```lean
TauCeti.thickPart.{u_1, u_2} (G : Type u_1) {X : Type u_2} [Group G] [PseudoMetricSpace X]
  [MulAction G X] (ε : ℝ) : Set X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.thickPart`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/ThickPart.html#TauCeti.thickPart).

## Sources

- [Tau Ceti documentation: `TauCeti.thickPart`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/ThickPart.html#TauCeti.thickPart)
- [Source of `TauCeti.thickPart` in TauCeti/Topology/MetricSpace/ThickPart.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/MetricSpace/ThickPart.lean#L40)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
