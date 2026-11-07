---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier
statement: formalized
proof: formalized
---

# Carathéodory's continuity theorem, as a characterization

A holomorphic injection of a disc
onto a bounded region extends continuously to the closed disc if and only if the boundary of the
region is locally connected.

```lean
TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier {f : ℂ → ℂ} {c : ℂ}
  {r : ℝ} (hr : 0 < r) (hf : DifferentiableOn ℂ f (Metric.ball c r))
  (hinj : Set.InjOn f (Metric.ball c r)) (hb : Bornology.IsBounded (f '' Metric.ball c r)) :
  (∃ F, ContinuousOn F (Metric.closedBall c r) ∧ Set.EqOn F f (Metric.ball c r)) ↔
    LocallyConnectedSpace ↑(frontier (f '' Metric.ball c r))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Contour.windingNumber](../contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-windingnumber.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier)
- [Source of `TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier` in TauCeti/Analysis/Complex/Conformal/Caratheodory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Caratheodory.lean#L220)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
