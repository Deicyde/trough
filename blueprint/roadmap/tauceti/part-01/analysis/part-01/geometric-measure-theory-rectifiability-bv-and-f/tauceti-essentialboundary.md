---
declaration: def
origin: cited
lean: TauCeti.essentialBoundary
statement: formalized
---

# TauCeti.essentialBoundary

The **essential boundary** of `s` with respect to `μ`: the points at which `s` has neither
density one nor density zero. This is the measure-theoretic boundary `∂ᵉE`, which ignores
modifications of `E` by null sets.

```lean
TauCeti.essentialBoundary.{u_1} {α : Type u_1} [PseudoMetricSpace α] [MeasurableSpace α]
  (μ : MeasureTheory.Measure α) (s : Set α) : Set α
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.essentialBoundary`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.essentialBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.essentialBoundary`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Covering/EssentialBoundary.html#TauCeti.essentialBoundary)
- [Source of `TauCeti.essentialBoundary` in TauCeti/MeasureTheory/Covering/EssentialBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Covering/EssentialBoundary.lean#L140)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
