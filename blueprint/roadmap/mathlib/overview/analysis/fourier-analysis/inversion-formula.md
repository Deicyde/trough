---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Continuous.fourierInv_fourier_eq
mathlib_file: Mathlib/Analysis/Fourier/Inversion.lean
---

# Inversion formula

**Fourier inversion formula**: If a function `f` on a finite-dimensional real inner product
space is continuous, integrable, and its Fourier transform `𝓕 f` is also integrable,
then `𝓕⁻ (𝓕 f) = f`.

```lean
Continuous.fourierInv_fourier_eq.{u_1, u_2} {V : Type u_1} {E : Type u_2} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V] [FiniteDimensional ℝ V]
  [NormedAddCommGroup E] [NormedSpace ℂ E] {f : V → E} [CompleteSpace E] (h : Continuous f)
  (hf : MeasureTheory.Integrable f MeasureTheory.volume)
  (h'f : MeasureTheory.Integrable (FourierTransform.fourier f) MeasureTheory.volume) :
  FourierTransformInv.fourierInv (FourierTransform.fourier f) = f
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
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Fourier theorem](../../../thousand-plus/analysis/43-abstract-harmonic-analysis/fourier-theorem.md)

## Sources

- [Mathlib documentation: `Continuous.fourierInv_fourier_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Inversion.html#Continuous.fourierInv_fourier_eq)
- [Source of `Continuous.fourierInv_fourier_eq` in Mathlib/Analysis/Fourier/Inversion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/Inversion.lean#L172)
- [Mathlib overview: Analysis › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L386)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L541)
- [1000+ theorems list: Q3984053](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2650)
- [1000+ theorems project: Q3984053](https://1000-plus.github.io/?length=-1#Q3984053)
- [Wikipedia: Fourier inversion theorem](https://en.wikipedia.org/wiki/Fourier_inversion_theorem)
- [Wikidata: Q3984053](https://www.wikidata.org/wiki/Q3984053)
