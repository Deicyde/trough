---
declaration: theorem
origin: cited
lean: TauCeti.toReal_transportCost_eq_sSup, TauCeti.isLUB_kantorovichDualValue_integrable, TauCeti.isLUB_ofReal_kantorovichDualValue_continuous_of_lowerSemicontinuous, TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_lowerSemicontinuous, TauCeti.transportCost_eq_ofReal_sSup, TauCeti.isLUB_kantorovichDualValue_continuous, TauCeti.isGreatest_kantorovichDualValue_integrable
statement: formalized
proof: formalized
---

# Strong Kantorovich duality for probability measures

**Strong Kantorovich duality for probability measures**, read as an equality between the
primal value and the supremum of the dual values over the continuous potentials.

```lean
TauCeti.toReal_transportCost_eq_sSup.{u, v} {X : Type u} {Y : Type v} [PseudoMetricSpace X]
  [CompactSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] [PseudoMetricSpace Y]
  [CompactSpace Y] [MeasurableSpace Y] [OpensMeasurableSpace Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ℝ} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hc : Continuous c) (hc0 : ∀ (z : X × Y), 0 ≤ c z) :
  (TauCeti.transportCost (fun z => ENNReal.ofReal (c z)) μ ν).toReal =
    sSup
      {r |
        ∃ φ ψ,
          Continuous φ ∧
            Continuous ψ ∧
              (∀ (x : X) (y : Y), φ x + ψ y ≤ c (x, y)) ∧ TauCeti.kantorovichDualValue μ ν φ ψ = r}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Approximate Kantorovich duality on compact spaces](../part-01/approximate-kantorovich-duality-on-compact-space.md)
- [The theorem of Rockafellar and Rüschendorf](the-theorem-of-rockafellar-and-ruschendorf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.toReal_transportCost_eq_sSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.toReal_transportCost_eq_sSup).

## Other forms

**Strong Kantorovich duality against the integrable dual class.** Formalized in Tau Ceti as [`TauCeti.isLUB_kantorovichDualValue_integrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.isLUB_kantorovichDualValue_integrable).

```lean
TauCeti.isLUB_kantorovichDualValue_integrable.{u, v} {X : Type u} {Y : Type v} [PseudoMetricSpace X]
  [CompactSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] [PseudoMetricSpace Y]
  [CompactSpace Y] [MeasurableSpace Y] [OpensMeasurableSpace Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ℝ} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hc : Continuous c) (hc0 : ∀ (z : X × Y), 0 ≤ c z) :
  IsLUB
    {r |
      ∃ φ ψ,
        MeasureTheory.Integrable φ μ ∧
          MeasureTheory.Integrable ψ ν ∧
            (∀ (x : X) (y : Y), φ x + ψ y ≤ c (x, y)) ∧ TauCeti.kantorovichDualValue μ ν φ ψ = r}
    (TauCeti.transportCost (fun z => ENNReal.ofReal (c z)) μ ν).toReal
```

**Strong Kantorovich duality for lower-semicontinuous costs on compact metrizable spaces.** Formalized in Tau Ceti as [`TauCeti.isLUB_ofReal_kantorovichDualValue_continuous_of_lowerSemicontinuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/LowerSemicontinuous.html#TauCeti.isLUB_ofReal_kantorovichDualValue_continuous_of_lowerSemicontinuous).

```lean
TauCeti.isLUB_ofReal_kantorovichDualValue_continuous_of_lowerSemicontinuous.{u, v} {X : Type u}
  {Y : Type v} [TopologicalSpace X] [MeasurableSpace X] [TopologicalSpace Y] [MeasurableSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] {c : X × Y → ENNReal} [TopologicalSpace.MetrizableSpace X]
  [CompactSpace X] [BorelSpace X] [TopologicalSpace.MetrizableSpace Y] [CompactSpace Y]
  [BorelSpace Y] (hc : LowerSemicontinuous c) :
  IsLUB
    {r |
      ∃ φ ψ,
        Continuous φ ∧
          Continuous ψ ∧
            TauCeti.DualFeasible (fun z => ↑(c z)) φ ψ ∧
              ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.transportCost c μ ν)
```

**Strong Kantorovich duality for nonnegative lower-semicontinuous costs on Polish spaces.** Formalized in Tau Ceti as [`TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_lowerSemicontinuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/LowerSemicontinuous.html#TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_lowerSemicontinuous).

```lean
TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_lowerSemicontinuous.{u, v} {X : Type u}
  {Y : Type v} [TopologicalSpace X] [MeasurableSpace X] [TopologicalSpace Y] [MeasurableSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] {c : X × Y → ENNReal} [PolishSpace X] [BorelSpace X]
  [PolishSpace Y] [BorelSpace Y] (hc : LowerSemicontinuous c) :
  IsLUB
    {r |
      ∃ φ ψ,
        MeasureTheory.Integrable φ μ ∧
          MeasureTheory.Integrable ψ ν ∧
            TauCeti.DualFeasible (fun z => ↑(c z)) φ ψ ∧
              ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.transportCost c μ ν)
```

**Strong Kantorovich duality for probability measures, read in `ℝ≥0∞`.** Formalized in Tau Ceti as [`TauCeti.transportCost_eq_ofReal_sSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.transportCost_eq_ofReal_sSup).

```lean
TauCeti.transportCost_eq_ofReal_sSup.{u, v} {X : Type u} {Y : Type v} [PseudoMetricSpace X]
  [CompactSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] [PseudoMetricSpace Y]
  [CompactSpace Y] [MeasurableSpace Y] [OpensMeasurableSpace Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ℝ} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hc : Continuous c) (hc0 : ∀ (z : X × Y), 0 ≤ c z) :
  TauCeti.transportCost (fun z => ENNReal.ofReal (c z)) μ ν =
    ENNReal.ofReal
      (sSup
        {r |
          ∃ φ ψ,
            Continuous φ ∧
              Continuous ψ ∧
                (∀ (x : X) (y : Y), φ x + ψ y ≤ c (x, y)) ∧
                  TauCeti.kantorovichDualValue μ ν φ ψ = r})
```

**Strong Kantorovich duality on compact pseudometrizable spaces.** Formalized in Tau Ceti as [`TauCeti.isLUB_kantorovichDualValue_continuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.isLUB_kantorovichDualValue_continuous).

```lean
TauCeti.isLUB_kantorovichDualValue_continuous.{u, v} {X : Type u} {Y : Type v} [PseudoMetricSpace X]
  [CompactSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] [PseudoMetricSpace Y]
  [CompactSpace Y] [MeasurableSpace Y] [OpensMeasurableSpace Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ℝ} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hc : Continuous c) (hc0 : ∀ (z : X × Y), 0 ≤ c z) :
  IsLUB
    {r |
      ∃ φ ψ,
        Continuous φ ∧
          Continuous ψ ∧
            (∀ (x : X) (y : Y), φ x + ψ y ≤ c (x, y)) ∧ TauCeti.kantorovichDualValue μ ν φ ψ = r}
    (TauCeti.transportCost (fun z => ENNReal.ofReal (c z)) μ ν).toReal
```

**Strong Kantorovich duality with dual attainment on Polish spaces.** Formalized in Tau Ceti as [`TauCeti.isGreatest_kantorovichDualValue_integrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Attainment.html#TauCeti.isGreatest_kantorovichDualValue_integrable).

```lean
TauCeti.isGreatest_kantorovichDualValue_integrable.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [MeasurableSpace X] [TopologicalSpace Y] [MeasurableSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} {c : X × Y → ℝ} [PolishSpace X]
  [BorelSpace X] [PolishSpace Y] [BorelSpace Y] [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hc : Continuous c) (hc0 : ∀ (z : X × Y), 0 ≤ c z)
  (hcb : BddAbove (Set.range c)) :
  IsGreatest
    {r |
      ∃ φ ψ,
        MeasureTheory.Integrable φ μ ∧
          MeasureTheory.Integrable ψ ν ∧
            (∀ (x : X) (y : Y), φ x + ψ y ≤ c (x, y)) ∧ TauCeti.kantorovichDualValue μ ν φ ψ = r}
    (TauCeti.transportCost (fun z => ENNReal.ofReal (c z)) μ ν).toReal
```

## Sources

- [Tau Ceti documentation: `TauCeti.toReal_transportCost_eq_sSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.html#TauCeti.toReal_transportCost_eq_sSup)
- [Source of `TauCeti.toReal_transportCost_eq_sSup` in TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/Duality/Compact.lean#L428)
