---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Integrable.fourierInv_fourier_eq, Continuous.fourierInv_fourier_eq
mathlib_file: Mathlib/Analysis/Fourier/Inversion.lean
---

# Fourier theorem

Mathlib records this with 2 declarations.

`MeasureTheory.Integrable.fourierInv_fourier_eq`: **Fourier inversion formula**: If a function `f` on a finite-dimensional real inner product
space is integrable, and its Fourier transform `𝓕 f` is also integrable, then `𝓕⁻ (𝓕 f) = f` at
continuity points of `f`.

```lean
MeasureTheory.Integrable.fourierInv_fourier_eq.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MeasurableSpace V] [BorelSpace V]
  [FiniteDimensional ℝ V] [NormedAddCommGroup E] [NormedSpace ℂ E] {f : V → E} [CompleteSpace E]
  (hf : MeasureTheory.Integrable f MeasureTheory.volume)
  (h'f : MeasureTheory.Integrable (FourierTransform.fourier f) MeasureTheory.volume) {v : V}
  (hv : ContinuousAt f v) : FourierTransformInv.fourierInv (FourierTransform.fourier f) v = f v
```

`Continuous.fourierInv_fourier_eq`: **Fourier inversion formula**: If a function `f` on a finite-dimensional real inner product
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

The wikipedia page is really vague; it's not clear what is meant here. While mathlib has some material already, there is space for more advanced results.

## Depends on

- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Vector-valued integrable function (Bochner integral)](../../../overview/analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)

## Proof depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Carathéodory's theorem (measure theory)](../28-measure-and-integration/part-01/caratheodorys-theorem-measure-theory.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Completeness of R](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Exponential](../../../overview/analysis/special-functions/exponential.md)
- [Field $\C$ of complex numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../../overview/analysis/normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Measurable function](../../../overview/analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Squeeze theorem](../26-real-functions/part-03/squeeze-theorem.md)
- [The Binomial Theorem](../../../hundred-theorems/part-03/the-binomial-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-05/the-triangle-inequality.md)
- [Topology of a metric space](../../../undergraduate/topology/topology-and-metric-spaces/topology-of-a-metric-space.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Integrable.fourierInv_fourier_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Inversion.html#MeasureTheory.Integrable.fourierInv_fourier_eq)
- [Source of `MeasureTheory.Integrable.fourierInv_fourier_eq` in Mathlib/Analysis/Fourier/Inversion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/Inversion.lean#L163)
- [Mathlib documentation: `Continuous.fourierInv_fourier_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Inversion.html#Continuous.fourierInv_fourier_eq)
- [Source of `Continuous.fourierInv_fourier_eq` in Mathlib/Analysis/Fourier/Inversion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/Inversion.lean#L172)
- [1000+ theorems list: Q179467](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L86)
- [1000+ theorems project: Q179467](https://1000-plus.github.io/all.html?length=-1#Q179467)
- [Wikipedia: Fourier theorem](https://en.wikipedia.org/wiki/Fourier_theorem)
- [Wikidata: Q179467](https://www.wikidata.org/wiki/Q179467)
