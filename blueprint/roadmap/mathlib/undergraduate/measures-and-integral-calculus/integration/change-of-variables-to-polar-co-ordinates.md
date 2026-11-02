---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: integral_comp_polarCoord_symm
mathlib_file: Mathlib/Analysis/SpecialFunctions/PolarCoord.lean
---

# Change of variables to polar co-ordinates

Mathlib states this as `integral_comp_polarCoord_symm`.

```lean
integral_comp_polarCoord_symm.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (f : ℝ × ℝ → E) :
  ∫ (p : ℝ × ℝ) in polarCoord.target, p.1 • f (↑polarCoord.symm p) = ∫ (p : ℝ × ℝ), f p
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Giry monad](../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Lebesgue measure](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [$C^k$ function](../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Change of variables formula](../../../overview/analysis/measures-and-integral-calculus/part-02/change-of-variables-formula.md)
- [Completion of an abelian topological group](../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Decomposition into transpositions](../../group-theory/permutation-group/decomposition-into-transpositions.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Matrix exponential](../../linear-algebra/exponential/matrix-exponential.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `integral_comp_polarCoord_symm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/PolarCoord.html#integral_comp_polarCoord_symm)
- [Source of `integral_comp_polarCoord_symm` in Mathlib/Analysis/SpecialFunctions/PolarCoord.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/SpecialFunctions/PolarCoord.lean#L139)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L526)
