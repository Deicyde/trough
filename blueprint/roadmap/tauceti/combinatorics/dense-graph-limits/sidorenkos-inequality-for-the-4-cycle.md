---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four
statement: formalized
proof: formalized
---

# Sidorenko's inequality for the 4-cycle

The 4-cycle homomorphism density is at least the
fourth power of the edge density, on every probability carrier. This is the graphon form of the
`K_{2,2}` case in Y. Zhao, *Graph Theory and Additive Combinatorics*, Theorem 5.2.1.

```lean
TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ]
  (W : TauCeti.DenseGraphLimits.Graphon Ω μ) :
  TauCeti.DenseGraphLimits.homDensity (SimpleGraph.cycleGraph 4) W ≥
    TauCeti.DenseGraphLimits.homDensity ⊤ W ^ 4
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Applications.html#TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/Applications.html#TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four)
- [Source of `TauCeti.DenseGraphLimits.sidorenko_cycleGraph_four` in TauCeti/Combinatorics/DenseGraphLimits/Applications.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/Applications.lean#L430)
