---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IntervalIntegrable.ae_hasDerivAt_integral
mathlib_file: Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.lean
---

# Differentiability of integrals with respect to parameters

The (local) interval version of the *Lebesgue Differentiation Theorem*: if `f : ℝ → E` is
interval integrable on `a..b`, then for almost every `x ∈ uIcc a b`, for any `c ∈ uIcc a b`, the
derivative of `∫ (t : ℝ) in c..x, f t` at `x` is equal to `f x`.

```lean
IntervalIntegrable.ae_hasDerivAt_integral.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] {f : ℝ → E} {a b : ℝ}
  (hf : IntervalIntegrable f MeasureTheory.volume a b) :
  ∀ᵐ (x : ℝ),
    x ∈ Set.uIcc a b → ∀ c ∈ Set.uIcc a b, HasDerivAt (fun x => ∫ (t : ℝ) in c..x, f t) (f x) x
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Derivative at a point](../../single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Lebesgue measure](../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Affine space](../../../overview/geometry/affine-and-euclidean-geometry/affine-space.md)
- [Complementary subspaces](../../linear-algebra/fundamentals/complementary-subspaces.md)
- [Determinant of endomorphisms](../../linear-algebra/multilinearity/determinant-of-endomorphisms.md)
- [Differentiable function between normed vector spaces](../../../overview/analysis/differentiability/differentiable-function-between-normed-vector-sp.md)
- [Dimension theorem for vector spaces](../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/dimension-theorem-for-vector-spaces.md)
- [Gaussian elimination](../../linear-algebra/matrices/gaussian-elimination.md)
- [Giry monad](../../../overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Lebesgue's decomposition theorem](../../../thousand-plus/geometry-and-topology/54-general-topology/part-01/lebesgues-decomposition-theorem.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../../../overview/analysis/hilbert-spaces/orthogonal-projection.md)
- [Probability measure](../../../overview/probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Product of finitely many measures](../../../overview/analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Quotient ring](../../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Self-adjoint operator](../../../overview/analysis/hilbert-spaces/self-adjoint-operator.md)
- [Stieltjes measure](../../../overview/analysis/measures-and-integral-calculus/part-01/stieltjes-measure.md)
- [Vitali covering theorem](../../../thousand-plus/analysis/28-measure-and-integration/part-02/vitali-covering-theorem.md)

## Sources

- [Mathlib documentation: `IntervalIntegrable.ae_hasDerivAt_integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.html#IntervalIntegrable.ae_hasDerivAt_integral)
- [Source of `IntervalIntegrable.ae_hasDerivAt_integral` in Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/IntervalIntegral/LebesgueDifferentiationThm.lean#L64)
- [Mathlib undergraduate list: Measures and integral calculus › Integration](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L520)
