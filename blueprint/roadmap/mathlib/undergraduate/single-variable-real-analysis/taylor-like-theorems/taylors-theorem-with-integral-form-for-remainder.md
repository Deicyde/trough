---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: taylor_integral_remainder_of_absolutelyContinuous
mathlib_file: Mathlib/Analysis/Calculus/Taylor.lean
---

# Taylor's theorem with integral form for remainder (Taylor-like theorems)

**Taylor's theorem** with the Integral form of the remainder.

We assume that `f` is `n`-times continuously differentiable on the closed set `uIcc x₀ x` and
its `n`-th derivative is absolutely continuous on `uIcc x₀ x`. Then
$$f(x) - (P_n f)(x₀, x) = \int_{x_0}^x \frac{f^{(n+1)}(t) (x - t)^n}{n!} dt,$$
where $P_n f$ denotes the Taylor polynomial of degree $n$ and $f^{(n+1)}$ is the $n+1$-th iterated
derivative.

```lean
taylor_integral_remainder_of_absolutelyContinuous {f : ℝ → ℝ} {x x₀ : ℝ} {n : ℕ}
  (hf₁ : ContDiffOn ℝ (↑n) f (Set.uIcc x₀ x))
  (hf₂ : AbsolutelyContinuousOnInterval (iteratedDerivWithin n f (Set.uIcc x₀ x)) x₀ x) :
  f x - taylorWithinEval f n (Set.uIcc x₀ x) x₀ x =
    ∫ (t : ℝ) in x₀..x, (x - t) ^ n / ↑n.factorial * iteratedDerivWithin (n + 1) f (Set.uIcc x₀ x) t
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Radius of convergence](../../single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [$C^k$ function](../../../overview/analysis/differentiability/c-k-function.md)
- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Affine function](../../../overview/geometry/affine-and-euclidean-geometry/affine-function.md)
- [Completion of an abelian topological group](../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Derivative of a composition of functions (Analysis)](../../../overview/analysis/differentiability/derivative-of-a-composition-of-functions.md)
- [Differentiability of integrals with respect to parameters](../../measures-and-integral-calculus/integration/differentiability-of-integrals-with-respect-to-p.md)
- [Differentiable functions](../../multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Euclidean affine space](../../../overview/geometry/affine-and-euclidean-geometry/euclidean-affine-space.md)
- [Holomorphic functions](../../single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Polynomial functions](../elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `taylor_integral_remainder_of_absolutelyContinuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Taylor.html#taylor_integral_remainder_of_absolutelyContinuous)
- [Source of `taylor_integral_remainder_of_absolutelyContinuous` in Mathlib/Analysis/Calculus/Taylor.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Taylor.lean#L503)
- [Mathlib undergraduate list: Single Variable Real Analysis › Taylor-like theorems](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L326)
