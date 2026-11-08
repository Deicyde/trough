---
declaration: theorem
origin: cited
lean: BoundedVariationOn.exists_arclength_factorization
statement: formalized
proof: formalized
---

# BoundedVariationOn.exists_arclength_factorization

A continuous rectifiable curve factors through a 1-Lipschitz curve on its length interval.
The factor has exactly the parameter difference as variation on every subinterval, including
when the original curve has pauses or zero length. Values of the factor outside its length
interval are unspecified.

```lean
BoundedVariationOn.exists_arclength_factorization.{u_1} {X : Type u_1} [MetricSpace X] {γ : ℝ → X}
  {a b : ℝ} (hγ : BoundedVariationOn γ (Set.Icc a b)) (hcont : ContinuousOn γ (Set.Icc a b))
  (hab : a ≤ b) :
  ∃ g,
    LipschitzOnWith 1 g (Set.Icc 0 (eVariationOn γ (Set.Icc a b)).toReal) ∧
      Set.EqOn (g ∘ variationOnFromTo γ (Set.Icc a b) a) γ (Set.Icc a b) ∧
        ∀ u ∈ Set.Icc 0 (eVariationOn γ (Set.Icc a b)).toReal,
          ∀ v ∈ Set.Icc 0 (eVariationOn γ (Set.Icc a b)).toReal,
            u ≤ v → eVariationOn g (Set.Icc u v) = ENNReal.ofReal (v - u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`BoundedVariationOn.exists_arclength_factorization`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Arclength/Basic.html#BoundedVariationOn.exists_arclength_factorization).

## Sources

- [Tau Ceti documentation: `BoundedVariationOn.exists_arclength_factorization`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Arclength/Basic.html#BoundedVariationOn.exists_arclength_factorization)
- [Source of `BoundedVariationOn.exists_arclength_factorization` in TauCeti/Topology/MetricSpace/Arclength/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/MetricSpace/Arclength/Basic.lean#L100)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
