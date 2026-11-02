---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: map_add_eq_sum_add_integral_iteratedFDeriv
mathlib_file: Mathlib/Analysis/Calculus/TaylorIntegral.lean
---

# Taylor's theorem with integral form for remainder (Differential calculus)

*Taylor's theorem with remainder in integral form*. If `f` is `n + 1` times continuously
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

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Differentials (linear tangent functions)](differentials-linear-tangent-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Radius of convergence](../../single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure-z.md)

## Proof depends on

- [Characteristic p](../../../overview/general-algebra/field-theory/characteristic-p.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Differentiable functions](differentiable-functions.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `map_add_eq_sum_add_integral_iteratedFDeriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/TaylorIntegral.html#map_add_eq_sum_add_integral_iteratedFDeriv)
- [Source of `map_add_eq_sum_add_integral_iteratedFDeriv` in Mathlib/Analysis/Calculus/TaylorIntegral.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/TaylorIntegral.lean#L62)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L469)
