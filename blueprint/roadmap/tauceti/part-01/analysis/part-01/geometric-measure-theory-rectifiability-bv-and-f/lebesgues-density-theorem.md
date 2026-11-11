---
declaration: theorem
origin: cited
lean: TauCeti.ae_hasDensityAt_indicator, MeasureTheory.NullMeasurableSet.ae_tendsto_measure_inter_div, TauCeti.essentialExterior_ae_eq, TauCeti.essentialInterior_ae_eq, TauCeti.measure_essentialBoundary
statement: formalized
proof: formalized
---

# Lebesgue's density theorem

At almost every point a null-measurable set has density one
or zero, according to whether the point lies in the set.

```lean
TauCeti.ae_hasDensityAt_indicator.{u_1} {α : Type u_1} [MetricSpace α] [MeasurableSpace α]
  [SecondCountableTopology α] [BorelSpace α] [HasBesicovitchCovering α]
  {μ : MeasureTheory.Measure α} [MeasureTheory.IsLocallyFiniteMeasure μ] {s : Set α}
  (hs : MeasureTheory.NullMeasurableSet s μ) :
  ∀ᵐ (x : α) ∂μ, TauCeti.HasDensityAt μ s x (s.indicator 1 x)
```

## Depends on

- [TauCeti.essentialBoundary](tauceti-essentialboundary.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_hasDensityAt_indicator`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.ae_hasDensityAt_indicator).

## Other forms

**Lebesgue's density theorem for a null-measurable set `s`.** Formalized in Tau Ceti as [`MeasureTheory.NullMeasurableSet.ae_tendsto_measure_inter_div`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/Besicovitch.html#MeasureTheory.NullMeasurableSet.ae_tendsto_measure_inter_div).

```lean
MeasureTheory.NullMeasurableSet.ae_tendsto_measure_inter_div.{u_1} {α : Type u_1}
  [MeasurableSpace α] {μ : MeasureTheory.Measure α} {s : Set α} [MetricSpace α]
  [SecondCountableTopology α] [BorelSpace α] [HasBesicovitchCovering α]
  [MeasureTheory.IsLocallyFiniteMeasure μ] (hs : MeasureTheory.NullMeasurableSet s μ) :
  ∀ᵐ (x : α) ∂μ,
    Filter.Tendsto (fun r => μ (s ∩ Metric.closedBall x r) / μ (Metric.closedBall x r))
      (nhdsWithin 0 (Set.Ioi 0)) (nhds (s.indicator 1 x))
```

**Lebesgue's density theorem.** Formalized in Tau Ceti as [`TauCeti.essentialExterior_ae_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.essentialExterior_ae_eq).

```lean
TauCeti.essentialExterior_ae_eq.{u_1} {α : Type u_1} [MetricSpace α] [MeasurableSpace α]
  [SecondCountableTopology α] [BorelSpace α] [HasBesicovitchCovering α]
  {μ : MeasureTheory.Measure α} [MeasureTheory.IsLocallyFiniteMeasure μ] {s : Set α}
  (hs : MeasureTheory.NullMeasurableSet s μ) : TauCeti.essentialExterior μ s =ᵐ[μ] sᶜ
```

**Lebesgue's density theorem.** Formalized in Tau Ceti as [`TauCeti.essentialInterior_ae_eq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.essentialInterior_ae_eq).

```lean
TauCeti.essentialInterior_ae_eq.{u_1} {α : Type u_1} [MetricSpace α] [MeasurableSpace α]
  [SecondCountableTopology α] [BorelSpace α] [HasBesicovitchCovering α]
  {μ : MeasureTheory.Measure α} [MeasureTheory.IsLocallyFiniteMeasure μ] {s : Set α}
  (hs : MeasureTheory.NullMeasurableSet s μ) : TauCeti.essentialInterior μ s =ᵐ[μ] s
```

**Lebesgue's density theorem.** Formalized in Tau Ceti as [`TauCeti.measure_essentialBoundary`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.measure_essentialBoundary).

```lean
TauCeti.measure_essentialBoundary.{u_1} {α : Type u_1} [MetricSpace α] [MeasurableSpace α]
  [SecondCountableTopology α] [BorelSpace α] [HasBesicovitchCovering α]
  {μ : MeasureTheory.Measure α} [MeasureTheory.IsLocallyFiniteMeasure μ] {s : Set α}
  (hs : MeasureTheory.NullMeasurableSet s μ) : μ (TauCeti.essentialBoundary μ s) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.ae_hasDensityAt_indicator`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.ae_hasDensityAt_indicator)
- [Source of `TauCeti.ae_hasDensityAt_indicator` in TauCeti/MeasureTheory/Covering/EssentialBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Covering/EssentialBoundary.lean#L400)
