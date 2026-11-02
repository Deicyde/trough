---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: SchwartzMap.fourierTransformCLM
mathlib_file: Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean
---

# Fourier transforms on $\mathcal{S}(\R^d)$

The Fourier transform on a real inner product space, as a continuous linear map on the
Schwartz space.

This definition is only to define the Fourier transform, use `FourierTransform.fourierCLM` instead.

```lean
SchwartzMap.fourierTransformCLM.{u_1, u_2, u_3} (𝕜 : Type u_1) [RCLike 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [NormedSpace 𝕜 E] [SMulCommClass ℂ 𝕜 E] {V : Type u_3}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] : SchwartzMap V E →L[𝕜] SchwartzMap V E
```

## Depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Carathéodory's theorem (measure theory)](../../../thousand-plus/analysis/28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Completeness of R](../../single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Existence of orthonormal basis](../../../overview/linear-algebra/finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)
- [Field $\C$ of complex numbers](../../ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Lebesgue measure (Measure theory)](../../measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Linear independence](../../linear-algebra/fundamentals/linear-independence.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)

## Sources

- [Mathlib documentation: `SchwartzMap.fourierTransformCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.html#SchwartzMap.fourierTransformCLM)
- [Source of `SchwartzMap.fourierTransformCLM` in Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean#L48)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L611)
