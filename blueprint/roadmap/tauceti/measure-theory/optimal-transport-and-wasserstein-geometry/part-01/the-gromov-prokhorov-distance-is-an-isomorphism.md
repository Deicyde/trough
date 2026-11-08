---
declaration: theorem
origin: cited
lean: TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left
statement: formalized
proof: formalized
---

# The Gromov–Prokhorov distance is an isomorphism invariant

Metric-measure spaces related by
a measure-preserving isometry are at the same Gromov–Prokhorov distance from every measure.

```lean
TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left.{u_5, u_6, u_7} {X : Type u_5}
  {Y : Type u_6} {Z : Type u_7} [MetricSpace X] [MeasurableSpace X] [CompleteSpace X]
  [SecondCountableTopology X] [BorelSpace X] [MetricSpace Y] [MeasurableSpace Y] [CompleteSpace Y]
  [SecondCountableTopology Y] [BorelSpace Y] [PseudoEMetricSpace Z] [MeasurableSpace Z]
  {M : TauCeti.MetricMeasureSpace X} {N : TauCeti.MetricMeasureSpace Y}
  (e : TauCeti.MeasurePreservingIsometry M N) (ρ : MeasureTheory.Measure Z) :
  TauCeti.gromovProkhorovEDist N.reference ρ = TauCeti.gromovProkhorovEDist M.reference ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/GromovProkhorov.html#TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left).

## Sources

- [Tau Ceti documentation: `TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/GromovProkhorov.html#TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left)
- [Source of `TauCeti.MeasurePreservingIsometry.gromovProkhorovEDist_left` in TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/GromovProkhorov.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/MetricMeasure/GromovProkhorov.lean#L410)
