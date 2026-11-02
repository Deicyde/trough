---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: SchwartzMap.tsum_eq_tsum_fourier
mathlib_file: Mathlib/Analysis/Fourier/PoissonSummation.lean
---

# Poisson’s formula

**Poisson's summation formula** for Schwartz functions.

```lean
SchwartzMap.tsum_eq_tsum_fourier (f : SchwartzMap ℝ ℂ) (x : ℝ) :
  ∑' (n : ℤ), f (x + ↑n) = ∑' (n : ℤ), (FourierTransform.fourier f) ↑n * (fourier n) ↑x
```

## Depends on

- [Fourier transforms on $\mathcal{S}(\R^d)$](../spaces-s-r-d/fourier-transforms-on-s-r-d.md)

## Proof depends on

- [Absolutely convergent series in Banach spaces](../../../overview/analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Complementary subspaces](../../linear-algebra/fundamentals/complementary-subspaces.md)
- [Completion of an abelian topological group](../../../overview/topology/topological-algebra/completion-of-an-abelian-topological-group.md)
- [Fourier Series](../../../hundred-theorems/part-04/fourier-series.md)
- [Giry monad](../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Hilbert projection theorem](../../topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Holomorphic functions](../../single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Lebesgue measure (Measures and integral calculus)](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Orthogonal projection](../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Sequential space](../../../overview/topology/general-topology/part-01/sequential-space.md)
- [Stieltjes measure](../../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)
- [Sum of a Geometric Series](../../../hundred-theorems/part-04/sum-of-a-geometric-series.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-03/the-number-of-subsets-of-a-set.md)

## Sources

- [Mathlib documentation: `SchwartzMap.tsum_eq_tsum_fourier`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/PoissonSummation.html#SchwartzMap.tsum_eq_tsum_fourier)
- [Source of `SchwartzMap.tsum_eq_tsum_fourier` in Mathlib/Analysis/Fourier/PoissonSummation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/PoissonSummation.lean#L214)
- [Mathlib undergraduate list: Distribution calculus › Applications](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L626)
