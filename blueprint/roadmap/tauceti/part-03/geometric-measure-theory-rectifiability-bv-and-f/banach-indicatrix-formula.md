---
declaration: theorem
origin: cited
lean: ContinuousOn.eVariationOn_eq_lintegral_encard
statement: formalized
proof: formalized
---

# Banach indicatrix formula

The variation of a continuous curve on `[a, b]` is the raw
one-dimensional Hausdorff integral of the extended cardinality of its fibers. No Lipschitz or
bounded-variation hypothesis is needed: both sides are infinite together. Pauses and repeated
traversals are allowed, and infinite fibers have infinite multiplicity.

```lean
ContinuousOn.eVariationOn_eq_lintegral_encard.{u_1} {X : Type u_1} [EMetricSpace X]
  [MeasurableSpace X] [BorelSpace X] {γ : ℝ → X} {a b : ℝ} (hγ : ContinuousOn γ (Set.Icc a b)) :
  eVariationOn γ (Set.Icc a b) =
    ∫⁻ (y : X), ↑(Set.Icc a b ∩ γ ⁻¹' {y}).encard ∂MeasureTheory.Measure.hausdorffMeasure 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousOn.eVariationOn_eq_lintegral_encard`](https://taucetiproject.org/docs/TauCeti/Topology/EMetricSpace/CurveLength.html#ContinuousOn.eVariationOn_eq_lintegral_encard).

## Sources

- [Tau Ceti documentation: `ContinuousOn.eVariationOn_eq_lintegral_encard`](https://taucetiproject.org/docs/TauCeti/Topology/EMetricSpace/CurveLength.html#ContinuousOn.eVariationOn_eq_lintegral_encard)
- [Source of `ContinuousOn.eVariationOn_eq_lintegral_encard` in TauCeti/Topology/EMetricSpace/CurveLength.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/EMetricSpace/CurveLength.lean#L209)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
