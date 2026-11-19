---
declaration: theorem
origin: cited
lean: TauCeti.mongeCost_eq_transportCost_of_continuous
statement: formalized
proof: formalized
---

# Pratelli's theorem

For an atomless finite source measure, a nonempty target type and a
continuous cost `c : X × Y → [0, ∞]` on second-countable standard Borel spaces, for instance
Polish spaces, the Monge and Kantorovich values agree, whether finite or not. The cost may be
unbounded and take the value `∞`, and the Monge infimum need not be attained.

```lean
TauCeti.mongeCost_eq_transportCost_of_continuous.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [SecondCountableTopology X] [MeasurableSpace X] [OpensMeasurableSpace X]
  [StandardBorelSpace X] [TopologicalSpace Y] [SecondCountableTopology Y] [MeasurableSpace Y]
  [OpensMeasurableSpace Y] [StandardBorelSpace Y] [Nonempty Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ENNReal} [MeasureTheory.IsFiniteMeasure μ]
  [MeasureTheory.NullSingletonClass μ] (hc : Continuous c) :
  TauCeti.mongeCost c μ ν = TauCeti.transportCost c μ ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sierpiński's theorem](../measure/sierpinskis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mongeCost_eq_transportCost_of_continuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Pratelli.html#TauCeti.mongeCost_eq_transportCost_of_continuous).

## Sources

- [Tau Ceti documentation: `TauCeti.mongeCost_eq_transportCost_of_continuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Pratelli.html#TauCeti.mongeCost_eq_transportCost_of_continuous)
- [Source of `TauCeti.mongeCost_eq_transportCost_of_continuous` in TauCeti/MeasureTheory/OptimalTransport/Pratelli.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/OptimalTransport/Pratelli.lean#L333)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OptimalTransport/STATUS.md)
