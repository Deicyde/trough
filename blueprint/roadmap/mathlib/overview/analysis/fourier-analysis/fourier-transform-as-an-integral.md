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

- [Bochner integral](../measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)

## Sources

- [Mathlib documentation: `Real.fourier_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/FourierTransform.html#Real.fourier_eq)
- [Source of `Real.fourier_eq` in Mathlib/Analysis/Fourier/FourierTransform.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/FourierTransform.lean#L434)
- [Mathlib overview: Analysis › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L385)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L538)
