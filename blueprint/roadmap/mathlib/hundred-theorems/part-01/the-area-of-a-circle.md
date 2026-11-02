---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Theorems100.area_disc
mathlib_file: Archive/Wiedijk100Theorems/AreaOfACircle.lean
---

# The Area of a Circle

**Area of a Circle**: The area of a disc with radius `r` is `π * r ^ 2`.

```lean
Theorems100.area_disc (r : NNReal) :
  MeasureTheory.volume (Theorems100.disc ↑r) = ↑NNReal.pi * ↑r ^ 2
```

## Depends on

- [Almost sure convergence](../../overview/probability-theory/convergence-of-a-sequence-of-random-variables/almost-sure-convergence.md)
- [Giry monad](../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Integral of positive measurable functions](../../overview/analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Measurable function](../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)

## Proof depends on

- [$C^k$ function](../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Algebra of endomorphisms of a vector space](../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Completion of an abelian topological group](../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Continuity (Complex-valued series)](../../undergraduate/single-variable-complex-analysis/complex-valued-series/continuity.md)
- [Derivative at a point](../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Derivative of a composition of functions (Analysis)](../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Derivative of the inverse of a function (Analysis)](../../overview/analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Derivative of the inverse of a function (Single Variable Real Analysis)](../../undergraduate/single-variable-real-analysis/differentiability/derivative-of-the-inverse-of-a-function.md)
- [Differentials (linear tangent functions)](../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Euclidean affine space](../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Fundamental Theorem of Integral Calculus](fundamental-theorem-of-integral-calculus.md)
- [Holomorphic functions](../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Matrix exponential](../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Sequential space](../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `Theorems100.area_disc`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/AreaOfACircle.html#Theorems100.area_disc)
- [Source of `Theorems100.area_disc` in Archive/Wiedijk100Theorems/AreaOfACircle.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/AreaOfACircle.lean#L84)
- [Freek Wiedijk's 100 theorems, no. 9](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L50)
