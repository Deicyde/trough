---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.geom_mean_le_arith_mean_weighted
mathlib_file: Mathlib/Analysis/MeanInequalities.lean
---

# Arithmetic Mean/Geometric Mean

**AM-GM inequality**: The geometric mean is less than or equal to the arithmetic mean, weighted
version for real-valued nonnegative functions.

```lean
Real.geom_mean_le_arith_mean_weighted.{u} {ι : Type u} (s : Finset ι) (w z : ι → ℝ)
  (hw : ∀ i ∈ s, 0 ≤ w i) (hw' : ∑ i ∈ s, w i = 1) (hz : ∀ i ∈ s, 0 ≤ z i) :
  ∏ i ∈ s, z i ^ w i ≤ ∑ i ∈ s, w i * z i
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Real number](../../overview/general-algebra/numbers/real-number.md)
- [Set](../../overview/data-structures/sets/set.md)

## Proof depends on

- [Jensen's inequality (finite sum version)](../../overview/analysis/convexity/jensens-inequality-finite-sum-version.md)
- [Logarithm](../../overview/analysis/special-functions/logarithm.md)
- [Ordered ring](../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Real.geom_mean_le_arith_mean_weighted`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/MeanInequalities.html#Real.geom_mean_le_arith_mean_weighted)
- [Source of `Real.geom_mean_le_arith_mean_weighted` in Mathlib/Analysis/MeanInequalities.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/MeanInequalities.lean#L127)
- [Freek Wiedijk's 100 theorems, no. 38](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L199)
