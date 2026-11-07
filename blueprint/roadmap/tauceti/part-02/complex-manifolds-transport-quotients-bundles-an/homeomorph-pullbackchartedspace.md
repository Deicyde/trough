---
declaration: def
origin: cited
lean: Homeomorph.pullbackChartedSpace
statement: formalized
---

# Homeomorph.pullbackChartedSpace

The charted-space structure on `N` pulled back along a homeomorphism `e : N ≃ₜ M`: the atlas
is `{e.transOpenPartialHomeomorph c | c ∈ atlas H M}` and the chart at `x` is the chart of `M` at
`e x` precomposed with `e`.

```lean
Homeomorph.pullbackChartedSpace.{u_1, u_2, u_3} {H : Type u_1} [TopologicalSpace H] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace H M] {N : Type u_3} [TopologicalSpace N] (e : N ≃ₜ M) :
  ChartedSpace H N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Homeomorph.pullbackChartedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/PullbackGroupoid.html#Homeomorph.pullbackChartedSpace).

## Sources

- [Tau Ceti documentation: `Homeomorph.pullbackChartedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/PullbackGroupoid.html#Homeomorph.pullbackChartedSpace)
- [Source of `Homeomorph.pullbackChartedSpace` in TauCeti/Geometry/Manifold/PullbackGroupoid.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/PullbackGroupoid.lean#L82)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
