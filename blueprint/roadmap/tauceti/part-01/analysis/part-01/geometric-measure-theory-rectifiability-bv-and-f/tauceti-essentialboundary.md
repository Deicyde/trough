---
declaration: def
origin: cited
lean: TauCeti.essentialBoundary
statement: formalized
---

# TauCeti.essentialBoundary

The **essential boundary** of `s` with respect to `μ`: the points at which `s` has neither
density one nor density zero. This is the measure-theoretic boundary `∂ᵉE`, which ignores
modifications of `E` by null sets. Since the complement of the support of `μ` lies in
`essentialExterior μ s` (see `HasDensityAt`), the essential boundary lies inside the support.

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
- [Source of `TauCeti.essentialBoundary` in TauCeti/MeasureTheory/Covering/EssentialBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Covering/EssentialBoundary.lean#L182)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
