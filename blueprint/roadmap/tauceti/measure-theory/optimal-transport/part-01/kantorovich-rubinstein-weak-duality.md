---
declaration: theorem
origin: cited
lean: TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one
statement: formalized
proof: formalized
---

# Kantorovich–Rubinstein weak duality

The difference of the expectations of an integrable
`1`-Lipschitz real function under two measures is at most their `1`-Wasserstein distance. No
measurability of the ground distance and no finiteness of the measures is needed.

```lean
TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one.{u} {X : Type u} [MeasurableSpace X]
  {μ ν : MeasureTheory.Measure X} [PseudoEMetricSpace X] {f : X → ℝ} (hf : LipschitzWith 1 f)
  (hμ : MeasureTheory.Integrable f μ) (hν : MeasureTheory.Integrable f ν) :
  ENNReal.ofReal (∫ (x : X), f x ∂μ - ∫ (x : X), f x ∂ν) ≤ TauCeti.wassersteinEDist 1 μ ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one).

## Sources

- [Tau Ceti documentation: `TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one)
- [Source of `TauCeti.ofReal_integral_sub_integral_le_wassersteinEDist_one` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean#L89)
