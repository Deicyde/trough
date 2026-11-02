---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: mellinInv_mellin_eq
mathlib_file: Mathlib/Analysis/MellinInversion.lean
---

# Mellin inversion theorem

The inverse Mellin transform of the Mellin transform applied to `x > 0` is x.

```lean
mellinInv_mellin_eq.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E]
  (σ : ℝ) (f : ℝ → E) {x : ℝ} (hx : 0 < x) (hf : MellinConvergent f ↑σ)
  (hFf : Complex.VerticalIntegrable (mellin f) σ MeasureTheory.volume) (hfx : ContinuousAt f x) :
  mellinInv σ (mellin f) x = f x
```

## Depends on

- [Bochner integral](../../../../overview/analysis/measures-and-integral-calculus/part-01/bochner-integral.md)
- [Field $\C$ of complex numbers](../../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md)
- [Lebesgue measure (Measures and integral calculus)](../../../../overview/analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Proof depends on

- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Euclidean domain](../../../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Fourier theorem](../../43-abstract-harmonic-analysis/fourier-theorem.md)

## Sources

- [Mathlib documentation: `mellinInv_mellin_eq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/MellinInversion.html#mellinInv_mellin_eq)
- [Source of `mellinInv_mellin_eq` in Mathlib/Analysis/MellinInversion.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/MellinInversion.lean#L91)
- [1000+ theorems list: Q6813106](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3556)
- [1000+ theorems project: Q6813106](https://1000-plus.github.io/?length=-1#Q6813106)
- [Wikipedia: Mellin inversion theorem](https://en.wikipedia.org/wiki/Mellin_inversion_theorem)
- [Wikidata: Q6813106](https://www.wikidata.org/wiki/Q6813106)
