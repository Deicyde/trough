---
declaration: theorem
origin: cited
lean: TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz
statement: formalized
proof: formalized
---

# Bounded-Lipschitz Kantorovich–Rubinstein duality with attainment

The cost capped at
`2 * R` is the greatest difference of integrals of a `1`-Lipschitz function bounded by `R`,
for finite measures of equal mass. Both constraints are separate; this is the maximum-norm
convention, not their sum.

```lean
TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz.{u} {X : Type u}
  [MeasurableSpace X] {μ ν : MeasureTheory.Measure X} [PseudoMetricSpace X] {R : ℝ} [PolishSpace X]
  [BorelSpace X] [MeasureTheory.IsFiniteMeasure μ] [MeasureTheory.IsFiniteMeasure ν] (hR : 0 ≤ R)
  (hmass : μ Set.univ = ν Set.univ) :
  IsGreatest
    {r |
      ∃ f,
        LipschitzWith 1 f ∧
          (∀ (x : X), ‖f x‖ ≤ R) ∧ ENNReal.ofReal (∫ (x : X), f x ∂μ - ∫ (x : X), f x ∂ν) = r}
    (TauCeti.transportCost (fun z => ENNReal.ofReal (min (dist z.1 z.2) (2 * R))) μ ν)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The theorem of Rockafellar and Rüschendorf](../part-02/the-theorem-of-rockafellar-and-ruschendorf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz).

## Sources

- [Tau Ceti documentation: `TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz)
- [Source of `TauCeti.isGreatest_ofReal_integral_sub_integral_boundedLipschitz` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean#L505)
