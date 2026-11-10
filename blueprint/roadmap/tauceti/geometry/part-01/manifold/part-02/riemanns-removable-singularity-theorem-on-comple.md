---
declaration: theorem
origin: cited
lean: TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE
statement: formalized
proof: formalized
---

# Riemann's removable singularity theorem on complex curves

A map between complex curves
that is continuous at `x` and holomorphic at every point of a punctured neighbourhood of `x` is
holomorphic at `x`. This is Mathlib's
`Complex.differentiableOn_compl_singleton_and_continuousAt_iff` read in charts.

```lean
TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  {f : X → Y} {x : X} [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y] (hc : ContinuousAt f x)
  (hf : ∀ᶠ (y : X) in nhdsWithin x {x}ᶜ, MDiffAt f y) : MDiffAt f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Chart.html#TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE).

## Sources

- [Tau Ceti documentation: `TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/Chart.html#TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE)
- [Source of `TauCeti.mdifferentiableAt_of_continuousAt_of_eventually_nhdsNE` in TauCeti/Geometry/Manifold/Complex/Chart.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/Chart.lean#L227)
