---
declaration: theorem
origin: cited
lean: TauCeti.wassersteinEDist_one_eq_iSup, TauCeti.wassersteinEDist_one_eq_iSup_of_compactSpace, TauCeti.wassersteinEDist_one_eq_iSup_apply_eq_zero
statement: formalized
proof: formalized
---

# Kantorovich–Rubinstein duality

For probability measures with finite first moments on a
second-countable pseudometric space whose measurable structure is standard Borel and contains the
open sets — in particular on a Polish metric space with its Borel σ-algebra — the
`1`-Wasserstein distance is the supremum of the differences of expectations of the `1`-Lipschitz
real functions.

```lean
TauCeti.wassersteinEDist_one_eq_iSup.{u} {X : Type u} [MeasurableSpace X]
  {μ ν : MeasureTheory.Measure X} [PseudoMetricSpace X] [OpensMeasurableSpace X]
  [SecondCountableTopology X] [StandardBorelSpace X] [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hμ : TauCeti.HasFiniteMoment 1 μ)
  (hν : TauCeti.HasFiniteMoment 1 ν) :
  TauCeti.wassersteinEDist 1 μ ν =
    ⨆ f, ⨆ (_ : LipschitzWith 1 f), ENNReal.ofReal (∫ (x : X), f x ∂μ - ∫ (x : X), f x ∂ν)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Approximate Kantorovich duality on compact spaces](approximate-kantorovich-duality-on-compact-space.md)
- [Kantorovich–Rubinstein weak duality](kantorovich-rubinstein-weak-duality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.wassersteinEDist_one_eq_iSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.wassersteinEDist_one_eq_iSup).

## Other forms

**Kantorovich–Rubinstein duality on a compact space.** Formalized in Tau Ceti as [`TauCeti.wassersteinEDist_one_eq_iSup_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.wassersteinEDist_one_eq_iSup_of_compactSpace).

```lean
TauCeti.wassersteinEDist_one_eq_iSup_of_compactSpace.{u} {X : Type u} [MeasurableSpace X]
  {μ ν : MeasureTheory.Measure X} [PseudoMetricSpace X] [CompactSpace X] [OpensMeasurableSpace X]
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν] :
  TauCeti.wassersteinEDist 1 μ ν =
    ⨆ f, ⨆ (_ : LipschitzWith 1 f), ENNReal.ofReal (∫ (x : X), f x ∂μ - ∫ (x : X), f x ∂ν)
```

**Kantorovich–Rubinstein duality, normalized at a basepoint.** Formalized in Tau Ceti as [`TauCeti.wassersteinEDist_one_eq_iSup_apply_eq_zero`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.wassersteinEDist_one_eq_iSup_apply_eq_zero).

```lean
TauCeti.wassersteinEDist_one_eq_iSup_apply_eq_zero.{u} {X : Type u} [MeasurableSpace X]
  {μ ν : MeasureTheory.Measure X} [PseudoMetricSpace X] [OpensMeasurableSpace X]
  [SecondCountableTopology X] [StandardBorelSpace X] [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hμ : TauCeti.HasFiniteMoment 1 μ)
  (hν : TauCeti.HasFiniteMoment 1 ν) (x₀ : X) :
  TauCeti.wassersteinEDist 1 μ ν =
    ⨆ f,
      ⨆ (_ : LipschitzWith 1 f),
        ⨆ (_ : f x₀ = 0), ENNReal.ofReal (∫ (x : X), f x ∂μ - ∫ (x : X), f x ∂ν)
```

## Sources

- [Tau Ceti documentation: `TauCeti.wassersteinEDist_one_eq_iSup`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.html#TauCeti.wassersteinEDist_one_eq_iSup)
- [Source of `TauCeti.wassersteinEDist_one_eq_iSup` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/KantorovichRubinstein.lean#L267)
