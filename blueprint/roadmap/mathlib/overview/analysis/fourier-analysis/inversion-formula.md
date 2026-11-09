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

- [Borel sigma-algebra](../measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Complex number](../../general-algebra/numbers/complex-number.md)
- [Finite-dimensionality](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Vector-valued integrable function (Bochner integral)](../measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)

## Proof depends on

- [Fourier theorem](../../../thousand-plus/analysis/43-abstract-harmonic-analysis/fourier-theorem.md)

## Sources

- [Mathlib documentation: `Continuous.fourierInv_fourier_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Inversion.html#Continuous.fourierInv_fourier_eq)
- [Source of `Continuous.fourierInv_fourier_eq` in Mathlib/Analysis/Fourier/Inversion.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Fourier/Inversion.lean#L172)
- [Mathlib overview: Analysis › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L386)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L541)
- [1000+ theorems list: Q3984053](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L2650)
- [1000+ theorems project: Q3984053](https://1000-plus.github.io/all.html?length=-1#Q3984053)
- [Wikipedia: Fourier inversion theorem](https://en.wikipedia.org/wiki/Fourier_inversion_theorem)
- [Wikidata: Q3984053](https://www.wikidata.org/wiki/Q3984053)
