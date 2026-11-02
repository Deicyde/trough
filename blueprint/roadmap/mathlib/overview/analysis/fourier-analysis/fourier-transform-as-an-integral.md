---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Real.fourier_eq
mathlib_file: Mathlib/Analysis/Fourier/FourierTransform.lean
---

# Fourier transform as an integral

Mathlib states this as `Real.fourier_eq`.

```lean
Real.fourier_eq.{u_1, u_3} {V : Type u_1} {E : Type u_3} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V]
  [FiniteDimensional ℝ V] (f : V → E) (w : V) :
  FourierTransform.fourier f w = ∫ (v : V), Real.fourierChar (-inner ℝ v w) • f v
```

## Depends on

- [Basis](../../linear-algebra/fundamentals/basis.md)
- [Bochner integral](../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Existence of orthonormal basis](../../linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-of-complex-numbers.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)
- [Lebesgue measure](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)

## Proof depends on

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Closed map](../../topology/general-topology/part-01/closed-map.md)
- [Complementary subspaces](../../../undergraduate/linear-algebra/fundamentals/complementary-subspaces.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Hilbert projection theorem](../../../undergraduate/topology/hilbert-spaces/hilbert-projection-theorem.md)
- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../undergraduate/topology/normed-vector-spaces-on-and/norms-p-on-n-and-n.md)
- [Orthogonal projection](../hilbert-spaces/orthogonal-projection.md)
- [Quotient space](../../linear-algebra/fundamentals/quotient-space.md)
- [Self-adjoint operator](../hilbert-spaces/self-adjoint-operator.md)

## Sources

- [Mathlib documentation: `Real.fourier_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FourierTransform.html#Real.fourier_eq)
- [Source of `Real.fourier_eq` in Mathlib/Analysis/Fourier/FourierTransform.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/FourierTransform.lean#L434)
- [Mathlib overview: Analysis › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L385)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L538)
