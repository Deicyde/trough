---
declaration: theorem
origin: cited
lean: TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split, TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_of_le_split
statement: formalized
proof: formalized
---

# Unrelaxed Borel strong Kantorovich duality over integrable potentials under an integrable split upper envelope

```lean
TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split.{u_1, u_2}
  {X : Type u_1} {Y : Type u_2} [MeasurableSpace X] [MeasurableSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} {c : X × Y → ENNReal}
  [TopologicalSpace X] [PolishSpace X] [BorelSpace X] [TopologicalSpace Y] [PolishSpace Y]
  [BorelSpace Y] [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν]
  {a : X → ENNReal} {b : Y → ENNReal} (hc : Measurable c) (ha : AEMeasurable a μ)
  (hb : AEMeasurable b ν) (haint : ∫⁻ (x : X), a x ∂μ ≠ ⊤) (hbint : ∫⁻ (y : Y), b y ∂ν ≠ ⊤)
  (hsplit : ∀ (z : X × Y), c z ≤ a z.1 + b z.2) :
  IsLUB
    {r |
      ∃ φ ψ,
        MeasureTheory.Integrable φ μ ∧
          MeasureTheory.Integrable ψ ν ∧
            TauCeti.DualFeasible (fun z => ↑(c z)) φ ψ ∧
              ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.transportCost c μ ν)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Beiglböck--Léonard--Schachermayer relaxed Kantorovich duality over integrable potentials](../part-01/beiglbock-leonard-schachermayer-relaxed-kantorov.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.html#TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split).

## Other forms

**Unrelaxed Borel strong Kantorovich duality over bounded measurable potentials under an integrable split upper envelope.** Formalized in Tau Ceti as [`TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_of_le_split`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.html#TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_of_le_split).

```lean
TauCeti.isLUB_ofReal_kantorovichDualValue_bounded_measurable_of_le_split.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [MeasurableSpace X] [MeasurableSpace Y] {μ : MeasureTheory.Measure X}
  {ν : MeasureTheory.Measure Y} {c : X × Y → ENNReal} [TopologicalSpace X] [PolishSpace X]
  [BorelSpace X] [TopologicalSpace Y] [PolishSpace Y] [BorelSpace Y]
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν] {a : X → ENNReal}
  {b : Y → ENNReal} (hc : Measurable c) (ha : AEMeasurable a μ) (hb : AEMeasurable b ν)
  (haint : ∫⁻ (x : X), a x ∂μ ≠ ⊤) (hbint : ∫⁻ (y : Y), b y ∂ν ≠ ⊤)
  (hsplit : ∀ (z : X × Y), c z ≤ a z.1 + b z.2) :
  IsLUB
    {r |
      ∃ φ ψ,
        Measurable φ ∧
          Measurable ψ ∧
            (∃ M, ∀ (x : X), |φ x| ≤ M) ∧
              (∃ M, ∀ (y : Y), |ψ y| ≤ M) ∧
                TauCeti.DualFeasible (fun z => ↑(c z)) φ ψ ∧
                  ENNReal.ofReal (TauCeti.kantorovichDualValue μ ν φ ψ) = r}
    (TauCeti.transportCost c μ ν)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.html#TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split)
- [Source of `TauCeti.isLUB_ofReal_kantorovichDualValue_integrable_of_measurable_of_le_split` in TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/OptimalTransport/Duality/Relaxed.lean#L277)
