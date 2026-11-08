---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.mantel_triangle_free
statement: formalized
proof: formalized
---

# Mantel's inequality for graphons

A graphon with zero triangle density has edge
density at most `1 / 2`.

```lean
TauCeti.DenseGraphLimits.mantel_triangle_free.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ]
  (W : TauCeti.DenseGraphLimits.Graphon Ω μ)
  (htriangle : TauCeti.DenseGraphLimits.homDensity ⊤ W = 0) :
  TauCeti.DenseGraphLimits.homDensity ⊤ W ≤ 1 / 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Goodman's inequality](goodmans-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.mantel_triangle_free`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Applications.html#TauCeti.DenseGraphLimits.mantel_triangle_free).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.mantel_triangle_free`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Applications.html#TauCeti.DenseGraphLimits.mantel_triangle_free)
- [Source of `TauCeti.DenseGraphLimits.mantel_triangle_free` in TauCeti/Combinatorics/DenseGraphLimits/Applications.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/Applications.lean#L419)
