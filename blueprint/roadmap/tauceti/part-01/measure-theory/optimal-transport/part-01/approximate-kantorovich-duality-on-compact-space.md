---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuous_forall_add_le_transportCost_le
statement: formalized
proof: formalized
---

# Approximate Kantorovich duality on compact spaces

For probability measures on compact
pseudometric spaces, a continuous nonnegative cost, and every `ε > 0`, there is a pair of
*continuous* potentials satisfying the Kantorovich constraint whose value is within `ε` of the
primal transport cost. Together with weak duality this closes the duality gap.

```lean
TauCeti.exists_continuous_forall_add_le_transportCost_le.{u, v} {X : Type u} {Y : Type v}
  [PseudoMetricSpace X] [CompactSpace X] [MeasurableSpace X] [OpensMeasurableSpace X]
  [PseudoMetricSpace Y] [CompactSpace Y] [MeasurableSpace Y] [OpensMeasurableSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} {c : X × Y → ℝ}
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν] (hc : Continuous c)
  (hc0 : ∀ (z : X × Y), 0 ≤ c z) {ε : ℝ} (hε : 0 < ε) :
  ∃ φ ψ,
    Continuous φ ∧
      Continuous ψ ∧
        (∀ (x : X) (y : Y), φ x + ψ y ≤ c (x, y)) ∧
          TauCeti.transportCost (fun z => ENNReal.ofReal (c z)) μ ν ≤
            ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ + ε)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuous_forall_add_le_transportCost_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.exists_continuous_forall_add_le_transportCost_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuous_forall_add_le_transportCost_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.exists_continuous_forall_add_le_transportCost_le)
- [Source of `TauCeti.exists_continuous_forall_add_le_transportCost_le` in TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.lean#L319)
