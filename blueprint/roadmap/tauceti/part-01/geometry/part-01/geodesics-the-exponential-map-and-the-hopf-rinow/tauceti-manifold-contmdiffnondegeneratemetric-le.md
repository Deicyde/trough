---
declaration: def
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection
statement: formalized
---

# TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection

The Levi-Civita connection of a smooth symmetric nondegenerate metric. It is chosen to
vanish on vector fields that are not differentiable at the evaluation point.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] (g : TauCeti.Manifold.ContMDiffNondegenerateMetric)
  [FiniteDimensional ℝ E] : CovariantDerivative I E fun x => TangentSpace I x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Existence.html#TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Existence.html#TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetric.leviCivitaConnection` in TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/CovariantDerivative/LeviCivita/Nondegenerate/Existence.lean#L114)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HopfRinow/STATUS.md)
