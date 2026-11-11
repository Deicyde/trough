---
declaration: theorem
origin: cited
lean: TauCeti.isCompact_setOfPred_isMultiCoupling
statement: formalized
proof: formalized
---

# Prokhorov's theorem for multi-couplings

The multi-couplings of finitely many tight
probability measures form a weakly compact set: it is tight, hence relatively compact, and
closed.

```lean
TauCeti.isCompact_setOfPred_isMultiCoupling.{u_1, u_2} {ι : Type u_1} {X : ι → Type u_2}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → MeasurableSpace (X i)] [Finite ι]
  [∀ (i : ι), OpensMeasurableSpace (X i)]
  [∀ (i : ι), T1Space (MeasureTheory.ProbabilityMeasure (X i))] [BorelSpace ((i : ι) → X i)]
  [T2Space ((i : ι) → X i)] {μ : (i : ι) → MeasureTheory.ProbabilityMeasure (X i)}
  (hμ : ∀ (i : ι), MeasureTheory.IsTightMeasureSet {↑(μ i)}) :
  IsCompact {π | TauCeti.Measure.IsMultiCoupling ↑π fun i => ↑(μ i)}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isCompact_setOfPred_isMultiCoupling`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Existence.html#TauCeti.isCompact_setOfPred_isMultiCoupling).

## Sources

- [Tau Ceti documentation: `TauCeti.isCompact_setOfPred_isMultiCoupling`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Existence.html#TauCeti.isCompact_setOfPred_isMultiCoupling)
- [Source of `TauCeti.isCompact_setOfPred_isMultiCoupling` in TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Existence.lean#L106)
