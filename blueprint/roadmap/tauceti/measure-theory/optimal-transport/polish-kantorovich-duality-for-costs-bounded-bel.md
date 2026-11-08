---
declaration: theorem
origin: cited
lean: TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow
statement: formalized
proof: formalized
---

# Polish Kantorovich duality for costs bounded below

If the nonnegative residual of an
integrable split lower bound is lower semicontinuous, the signed primal value is the least upper
bound of the values of all integrable feasible real potentials. The value may be negative or
`∞`; no integrable split upper envelope or dual attainment is assumed.

```lean
TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow.{u, v} {X : Type u}
  {Y : Type v} [MeasurableSpace X] [MeasurableSpace Y] {c : X × Y → EReal}
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} [TopologicalSpace X] [PolishSpace X]
  [BorelSpace X] [TopologicalSpace Y] [PolishSpace Y] [BorelSpace Y]
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν]
  (h : TauCeti.IntegrableSplitLowerBound c μ ν) (hres : LowerSemicontinuous h.residual) :
  IsLUB
    {r |
      ∃ φ ψ,
        MeasureTheory.Integrable φ μ ∧
          MeasureTheory.Integrable ψ ν ∧
            TauCeti.DualFeasible c φ ψ ∧ ↑(TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.transportCostBddBelow c μ ν h)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Strong Kantorovich duality against the integrable dual class](strong-kantorovich-duality-against-the-integrabl.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/BoundedBelow.html#TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow).

## Sources

- [Tau Ceti documentation: `TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/BoundedBelow.html#TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow)
- [Source of `TauCeti.isLUB_kantorovichDualValue_of_lowerSemicontinuous_residual_bddBelow` in TauCeti/MeasureTheory/OptimalTransport/Duality/BoundedBelow.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Duality/BoundedBelow.lean#L103)
