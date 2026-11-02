---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: tendsto_integral_exp_smul_cocompact
mathlib_file: Mathlib/Analysis/Fourier/RiemannLebesgueLemma.lean
---

# Riemann-Lebesgue lemma

Riemann-Lebesgue lemma for functions on a finite-dimensional real vector space, formulated via
dual space.

```lean
tendsto_integral_exp_smul_cocompact.{u_1, u_2} {E : Type u_1} {V : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℂ E] (f : V → E) [AddCommGroup V] [TopologicalSpace V] [IsTopologicalAddGroup V]
  [T2Space V] [MeasurableSpace V] [BorelSpace V] [_root_.Module ℝ V] [ContinuousSMul ℝ V]
  [FiniteDimensional ℝ V] (μ : MeasureTheory.Measure V) [μ.IsAddHaarMeasure] :
  Filter.Tendsto (fun w => ∫ (v : V), Real.fourierChar (-w v) • f v ∂μ)
    (Filter.cocompact (StrongDual ℝ V)) (nhds 0)
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Dual of a normed space](../../../overview/analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Continuity of the sum of a series of functions](../../single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Dominated convergence theorem](../../../overview/analysis/measures-and-integral-calculus/part-01/dominated-convergence-theorem.md)
- [Fréchet-Riesz representation of the dual of a Hilbert space](../../../overview/analysis/hilbert-spaces/frechet-riesz-representation-of-the-dual-of-a-hi.md)
- [Fubini's theorem](../../../overview/analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Riemann-Lebesgue lemma](../../../overview/analysis/fourier-analysis/riemann-lebesgue-lemma.md)

## Sources

- [Mathlib documentation: `tendsto_integral_exp_smul_cocompact`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/RiemannLebesgueLemma.html#tendsto_integral_exp_smul_cocompact)
- [Source of `tendsto_integral_exp_smul_cocompact` in Mathlib/Analysis/Fourier/RiemannLebesgueLemma.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/RiemannLebesgueLemma.lean#L242)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L533)
