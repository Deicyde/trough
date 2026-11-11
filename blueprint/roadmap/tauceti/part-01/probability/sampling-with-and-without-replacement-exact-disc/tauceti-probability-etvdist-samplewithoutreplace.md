---
declaration: theorem
origin: cited
lean: TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq
statement: formalized
proof: formalized
---

# TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq

For a distinct-valued population, Mathlib's total variation distance between the sampling
laws is twice the exact collision probability. The embedding assumption also covers empty
sample and population indices: both laws then have mass one and the distance is zero.

```lean
TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq.{u_1, u_2, u_3}
  {ι : Type u_1} {κ : Type u_2} {α : Type u_3} [MeasurableSpace κ] [MeasurableSingletonClass κ]
  [MeasurableSpace α] [Fintype ι] [Fintype κ] {x : κ → α} (hx : Function.Injective x) (e : ι ↪ κ)
  (hI : MeasurableSet {f | Function.Injective f}) :
  MeasureTheory.etvDist
      (TauCeti.Probability.sampleWithoutReplacement (MeasureTheory.Measure.dirac x))
      (TauCeti.Probability.sampleWithReplacement (MeasureTheory.Measure.dirac x)) =
    2 *
      (1 - ↑((Fintype.card κ).descFactorial (Fintype.card ι)) / ↑(Fintype.card κ) ^ Fintype.card ι)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Probability.iSup_sampleWithoutReplacement_sub_sampleWithReplacement_dirac_eq](tauceti-probability-isup-samplewithoutreplacemen.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Distinct.html#TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq`](https://taucetiproject.org/docs/TauCeti/Probability/PopulationSampling/Distinct.html#TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq)
- [Source of `TauCeti.Probability.etvDist_sampleWithoutReplacement_sampleWithReplacement_dirac_eq` in TauCeti/Probability/PopulationSampling/Distinct.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/PopulationSampling/Distinct.lean#L106)
- [Tau Ceti roadmap status: Sampling with and without replacement, exact discrepancy for finite populations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteSamplingDiscrepancy/STATUS.md)
