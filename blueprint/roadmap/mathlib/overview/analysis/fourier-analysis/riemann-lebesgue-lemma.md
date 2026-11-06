# Riemann-Lebesgue lemma (Analysis)

Riemann-Lebesgue lemma for functions on a real inner-product space: the integral
`∫ v, exp (-2 * π * ⟪w, v⟫ * I) • f v` tends to 0 as `w → ∞`.

```lean
tendsto_integral_exp_inner_smul_cocompact.{u_1, u_2} {E : Type u_1} {V : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] (f : V → E) [NormedAddCommGroup V] [MeasurableSpace V]
  [BorelSpace V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] :
  Filter.Tendsto (fun w => ∫ (v : V), Real.fourierChar (-inner ℝ v w) • f v) (Filter.cocompact V)
    (nhds 0)
```

## Depends on

- [Bochner integral](../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)

## Proof depends on

- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/field-c-of-complex-numbers.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Measurable function](../measures-and-integral-calculus/part-01/measurable-function.md)
- [The Binomial Theorem](../../../hundred-theorems/part-02/the-binomial-theorem.md)
- [Uniformly continuous function](../../topology/uniform-notions/uniformly-continuous-function.md)
- [Urysohn's lemma](../../topology/general-topology/part-02/urysohns-lemma.md)

## Sources

- [Mathlib documentation: `tendsto_integral_exp_inner_smul_cocompact`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/RiemannLebesgueLemma.html#tendsto_integral_exp_inner_smul_cocompact)
- [Source of `tendsto_integral_exp_inner_smul_cocompact` in Mathlib/Analysis/Fourier/RiemannLebesgueLemma.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/RiemannLebesgueLemma.lean#L175)
- [Mathlib overview: Analysis › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L387)
