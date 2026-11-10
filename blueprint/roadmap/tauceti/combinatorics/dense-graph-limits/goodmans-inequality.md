---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.goodman_triangle_density
statement: formalized
proof: formalized
---

# Goodman's inequality

For every graphon, triangle density is at least
`2 * t(K₂, W)^2 - t(K₂, W)`.

```lean
TauCeti.DenseGraphLimits.goodman_triangle_density.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ]
  (W : TauCeti.DenseGraphLimits.Graphon Ω μ) :
  2 * TauCeti.DenseGraphLimits.homDensity ⊤ W ^ 2 - TauCeti.DenseGraphLimits.homDensity ⊤ W ≤
    TauCeti.DenseGraphLimits.homDensity ⊤ W
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.goodman_triangle_density`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Applications.html#TauCeti.DenseGraphLimits.goodman_triangle_density).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.goodman_triangle_density`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Applications.html#TauCeti.DenseGraphLimits.goodman_triangle_density)
- [Source of `TauCeti.DenseGraphLimits.goodman_triangle_density` in TauCeti/Combinatorics/DenseGraphLimits/Applications.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/Applications.lean#L407)
