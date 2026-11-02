---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: taylor_mean_remainder_lagrange, taylor_mean_remainder_cauchy, map_add_eq_sum_add_integral_iteratedFDeriv
mathlib_file: Mathlib/Analysis/Calculus/Taylor.lean
---

# Taylor's theorem with Lagrange form for remainder

Mathlib records this with 3 declarations.

`taylor_mean_remainder_lagrange`: **Taylor's theorem** with the Lagrange form of the remainder.

We assume that `f` is `n`-times continuously differentiable in the closed set `uIcc x₀ x` and
`n+1`-times differentiable on the open set `uIoo x₀ x`. Then there exists an `x' ∈ uIoo x₀ x` such
that
$$f(x) - (P_n f)(x₀, x) = \frac{f^{(n+1)}(x') (x - x₀)^{n+1}}{(n+1)!},$$
where $P_n f$ denotes the Taylor polynomial of degree $n$ and $f^{(n+1)}$ is the $n+1$-th iterated
derivative.

```lean
taylor_mean_remainder_lagrange {f : ℝ → ℝ} {x x₀ : ℝ} {n : ℕ} (hx : x₀ ≠ x)
  (hf : ContDiffOn ℝ (↑n) f (Set.uIcc x₀ x))
  (hf' : DifferentiableOn ℝ (iteratedDerivWithin n f (Set.uIcc x₀ x)) (Set.uIoo x₀ x)) :
  ∃ x' ∈ Set.uIoo x₀ x,
    f x - taylorWithinEval f n (Set.uIcc x₀ x) x₀ x =
      iteratedDerivWithin (n + 1) f (Set.uIcc x₀ x) x' * (x - x₀) ^ (n + 1) / ↑(n + 1).factorial
```

`taylor_mean_remainder_cauchy`: **Taylor's theorem** with the Cauchy form of the remainder.

We assume that `f` is `n`-times continuously differentiable on the closed set `uIcc x₀ x` and
`n+1`-times differentiable on the open set `uIoo x₀ x`. Then there exists an `x' ∈ uIoo x₀ x` such
that
$$f(x) - (P_n f)(x₀, x) = \frac{f^{(n+1)}(x') (x - x')^n (x-x₀)}{n!},$$
where $P_n f$ denotes the Taylor polynomial of degree $n$ and $f^{(n+1)}$ is the $n+1$-th iterated
derivative.

```lean
taylor_mean_remainder_cauchy {f : ℝ → ℝ} {x x₀ : ℝ} {n : ℕ} (hx : x₀ ≠ x)
  (hf : ContDiffOn ℝ (↑n) f (Set.uIcc x₀ x))
  (hf' : DifferentiableOn ℝ (iteratedDerivWithin n f (Set.uIcc x₀ x)) (Set.uIoo x₀ x)) :
  ∃ x' ∈ Set.uIoo x₀ x,
    f x - taylorWithinEval f n (Set.uIcc x₀ x) x₀ x =
      iteratedDerivWithin (n + 1) f (Set.uIcc x₀ x) x' * (x - x') ^ n / ↑n.factorial * (x - x₀)
```

`map_add_eq_sum_add_integral_iteratedFDeriv`: *Taylor's theorem with remainder in integral form*. If `f` is `n + 1` times continuously
differentiable, then `f (x + y)` is given by
`∑ k in 0..n, D^k f(x; y,..,y) / k! + 1/n! ∫ t in 0..1, (1 - t) ^ n • D^{n+1}f (x + t • y; y,..,y)`,
where `D^k f` denotes the iterated derivative of `f`.

In the case that `n = 1`, this is a reformulation of the fundamental theorem of calculus, namely
`f (x + y) = f x + ∫ t in 0..1, D f(x + t • y; y)`.

```lean
map_add_eq_sum_add_integral_iteratedFDeriv.{u_2, u_3} {E : Type u_2} {F : Type u_3}
  [NormedAddCommGroup E] [NormedAddCommGroup F] [NormedSpace ℝ E] [NormedSpace ℝ F] {f : E → F}
  {x y : E} {n : ℕ} [CompleteSpace F]
  (hf : ∀ t ∈ Set.Icc 0 1, ContDiffAt ℝ (↑n + 1) f (x + t • y)) :
  f (x + y) =
    (∑ k ∈ Finset.range (n + 1), (↑k.factorial)⁻¹ • (iteratedFDeriv ℝ k f x) fun x => y) +
      (↑n.factorial)⁻¹ •
        ∫ (t : ℝ) in 0..1, (1 - t) ^ n • (iteratedFDeriv ℝ (n + 1) f (x + t • y)) fun x => y
```

## Depends on

- [Algebra of endomorphisms of a vector space](../../linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Differentials (linear tangent functions)](../../multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)
- [Holomorphic functions](../../single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Radius of convergence](../../single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Derivative at a point](../differentiability/derivative-at-a-point.md)
- [Differentiable functions](../../multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Polynomial functions](../elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `taylor_mean_remainder_lagrange`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Taylor.html#taylor_mean_remainder_lagrange)
- [Source of `taylor_mean_remainder_lagrange` in Mathlib/Analysis/Calculus/Taylor.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Taylor.lean#L322)
- [Mathlib documentation: `taylor_mean_remainder_cauchy`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/Taylor.html#taylor_mean_remainder_cauchy)
- [Source of `taylor_mean_remainder_cauchy` in Mathlib/Analysis/Calculus/Taylor.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/Taylor.lean#L363)
- [Mathlib documentation: `map_add_eq_sum_add_integral_iteratedFDeriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/TaylorIntegral.html#map_add_eq_sum_add_integral_iteratedFDeriv)
- [Source of `map_add_eq_sum_add_integral_iteratedFDeriv` in Mathlib/Analysis/Calculus/TaylorIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/TaylorIntegral.lean#L62)
- [Mathlib undergraduate list: Single Variable Real Analysis › Taylor-like theorems](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L327)
- [Freek Wiedijk's 100 theorems, no. 35](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L183)
- [1000+ theorems list: Q1137206](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1399)
- [1000+ theorems project: Q1137206](https://1000-plus.github.io/?length=-1#Q1137206)
- [Wikipedia: Taylor's theorem](https://en.wikipedia.org/wiki/Taylor's_theorem)
- [Wikidata: Q1137206](https://www.wikidata.org/wiki/Q1137206)
