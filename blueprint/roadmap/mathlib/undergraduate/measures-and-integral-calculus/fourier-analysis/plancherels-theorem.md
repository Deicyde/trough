# Plancherel’s theorem

Plancherel's theorem for Schwartz functions.

```lean
SchwartzMap.integral_inner_fourier_fourier.{u_3, u_4} {V : Type u_3} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] {H : Type u_4}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] (f g : SchwartzMap V H) :
  ∫ (ξ : V), inner ℂ ((FourierTransform.fourier f) ξ) ((FourierTransform.fourier g) ξ) =
    ∫ (x : V), inner ℂ (f x) (g x)
```

## Depends on

- [Bochner integral](../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Inner product space, over $R$ or $C$](../../../overview/analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Lebesgue measure (Measure theory)](../measure-theory/lebesgue-measure.md)
- [Schwartz space](../../../overview/analysis/distribution-theory/schwartz-space.md)

## Proof depends on

- [Inversion formula](../../../overview/analysis/fourier-analysis/inversion-formula.md)

## Sources

- [Mathlib documentation: `SchwartzMap.integral_inner_fourier_fourier`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.html#SchwartzMap.integral_inner_fourier_fourier)
- [Source of `SchwartzMap.integral_inner_fourier_fourier` in Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/SchwartzSpace/Fourier.lean#L303)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L540)
- [1000+ theorems list: Q2096184](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2014)
- [1000+ theorems project: Q2096184](https://1000-plus.github.io/all.html?length=-1#Q2096184)
- [Wikipedia: Plancherel theorem](https://en.wikipedia.org/wiki/Plancherel_theorem)
- [Wikidata: Q2096184](https://www.wikidata.org/wiki/Q2096184)
