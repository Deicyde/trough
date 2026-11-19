---
declaration: theorem
origin: cited
lean: TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost, TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_relaxedTransportCost
statement: formalized
proof: formalized
---

# Beiglböck--Léonard--Schachermayer relaxed Kantorovich duality over integrable potentials

For any Borel measurable cost `c : X × Y → ℝ≥0∞` on a product of Polish spaces and any two
probability measures, `relaxedTransportCost c μ ν` is the least upper bound of the positive parts
of the dual values of feasible integrable potential pairs `(φ, ψ)`.

```lean
TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [MeasurableSpace X] [MeasurableSpace Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ENNReal} [TopologicalSpace X] [PolishSpace X]
  [BorelSpace X] [TopologicalSpace Y] [PolishSpace Y] [BorelSpace Y]
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν]
  (hc : Measurable c) :
  IsLUB
    {r |
      ∃ φ ψ,
        MeasureTheory.Integrable φ μ ∧
          MeasureTheory.Integrable ψ ν ∧
            TauCeti.DualFeasible (fun z => ↑(c z)) φ ψ ∧
              ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.relaxedTransportCost c μ ν)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Strong Kantorovich duality for probability measures](../part-02/strong-kantorovich-duality-for-probability-measu.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.html#TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost).

## Other forms

**Beiglböck--Léonard--Schachermayer relaxed Kantorovich duality over bounded measurable potentials.** Formalized in Tau Ceti as [`TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_relaxedTransportCost`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.html#TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_relaxedTransportCost).

```lean
TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_relaxedTransportCost.{u_1, u_2}
  {X : Type u_1} {Y : Type u_2} [MeasurableSpace X] [MeasurableSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} {c : X × Y → ENNReal}
  [TopologicalSpace X] [PolishSpace X] [BorelSpace X] [TopologicalSpace Y] [PolishSpace Y]
  [BorelSpace Y] [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν]
  (hc : Measurable c) :
  IsLUB
    {r |
      ∃ φ ψ,
        Measurable φ ∧
          Measurable ψ ∧
            (∃ M, ∀ (x : X), |φ x| ≤ M) ∧
              (∃ M, ∀ (y : Y), |ψ y| ≤ M) ∧
                TauCeti.DualFeasible (fun z => ↑(c z)) φ ψ ∧
                  ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.relaxedTransportCost c μ ν)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.html#TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost)
- [Source of `TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_relaxedTransportCost` in TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.lean#L224)
