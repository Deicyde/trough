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

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Approximation by step functions](../../measures-and-integral-calculus/measure-theory/approximation-by-step-functions.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../../overview/topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../linear-algebra/fundamentals/complementary-subspaces.md)
- [Fatou's lemma](../../../overview/analysis/measures-and-integral-calculus/part-01/fatous-lemma.md)
- [Giry monad](../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Monotone convergence theorem (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/monotone-convergence-theorem.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Orthogonal projection](../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Pointwise convergence](../sequences-and-series-of-functions/pointwise-convergence.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)

## Sources

- [Mathlib documentation: `AntitoneOn.tsum_le_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SumIntegralComparisons.html#AntitoneOn.tsum_le_integral)
- [Source of `AntitoneOn.tsum_le_integral` in Mathlib/Analysis/SumIntegralComparisons.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SumIntegralComparisons.lean#L273)
- [Mathlib undergraduate list: Single Variable Real Analysis › Numerical series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L301)
