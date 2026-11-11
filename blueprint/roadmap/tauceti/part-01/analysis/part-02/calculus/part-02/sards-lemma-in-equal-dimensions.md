---
declaration: theorem
origin: cited
lean: TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin
statement: formalized
proof: formalized
---

# Sard's lemma in equal dimensions

Let `E` and `F` be finite-dimensional real normed
spaces of equal dimension. If `f` is differentiable along `s` with derivative `f'`, and `f'` is
nowhere surjective on `s`, then `f '' s` has additive Haar measure zero in `F`.

Unlike the endomorphism version in Mathlib, the domain and codomain need not be the same normed
space and may carry unrelated norms and Haar measure normalizations.

```lean
TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {s : Set E} {f : E → F}
  {f' : E → E →L[ℝ] F} (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure]
  (hdim : Module.finrank ℝ E = Module.finrank ℝ F) (hf' : ∀ x ∈ s, HasFDerivWithinAt f (f' x) s x)
  (hcrit : ∀ x ∈ s, ¬Function.Surjective ⇑(f' x)) : ν (f '' s) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/EqualDimension.html#TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin).

## Sources

- [Tau Ceti documentation: `TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/EqualDimension.html#TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin)
- [Source of `TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin` in TauCeti/Analysis/Calculus/Sard/EqualDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Sard/EqualDimension.lean#L68)
