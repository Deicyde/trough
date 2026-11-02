---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: AntitoneOn.tsum_le_integral
mathlib_file: Mathlib/Analysis/SumIntegralComparisons.lean
---

# Comparison of a series and an integral

**Integral test**: bounds the sum of a nonnegative antitone function by an integral.

```lean
AntitoneOn.tsum_le_integral {f : ℝ → ℝ} (anti : AntitoneOn f (Set.Ici 0))
  (integrable : MeasureTheory.IntegrableOn f (Set.Ioi 0) MeasureTheory.volume)
  (nonneg : ∀ t ∈ Set.Ioi 0, 0 ≤ f t) : ∑' (n : ℕ), f ↑n ≤ f 0 + ∫ (x : ℝ) in Set.Ioi 0, f x
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `AntitoneOn.tsum_le_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SumIntegralComparisons.html#AntitoneOn.tsum_le_integral)
- [Source of `AntitoneOn.tsum_le_integral` in Mathlib/Analysis/SumIntegralComparisons.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SumIntegralComparisons.lean#L273)
- [Mathlib undergraduate list: Single Variable Real Analysis › Numerical series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L301)
