---
declaration: theorem
origin: cited
lean: TauCeti.transportCost_truncated_dist_eq_iSup
statement: formalized
proof: formalized
---

# Bounded-Lipschitz duality in supremum form

A uniform bound `R` on the test functions
corresponds to truncation of the ground distance at `2 * R`, for finite measures of equal mass.

```lean
TauCeti.transportCost_truncated_dist_eq_iSup.{u} {X : Type u} [MeasurableSpace X]
  {μ ν : MeasureTheory.Measure X} [PseudoMetricSpace X] {R : ℝ} [PolishSpace X] [BorelSpace X]
  [MeasureTheory.IsFiniteMeasure μ] [MeasureTheory.IsFiniteMeasure ν] (hR : 0 ≤ R)
  (hmass : μ Set.univ = ν Set.univ) :
  TauCeti.transportCost (fun z => ENNReal.ofReal (min (dist z.1 z.2) (2 * R))) μ ν =
    ⨆ f,
      ⨆ (_ : LipschitzWith 1 f),
        ⨆ (_ : ∀ (x : X), ‖f x‖ ≤ R), ENNReal.ofReal (∫ (x : X), f x ∂μ - ∫ (x : X), f x ∂ν)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The theorem of Rockafellar and Rüschendorf](../../optimal-transport/the-theorem-of-rockafellar-and-ruschendorf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.transportCost_truncated_dist_eq_iSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.transportCost_truncated_dist_eq_iSup).

## Sources

- [Tau Ceti documentation: `TauCeti.transportCost_truncated_dist_eq_iSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.transportCost_truncated_dist_eq_iSup)
- [Source of `TauCeti.transportCost_truncated_dist_eq_iSup` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean#L519)
