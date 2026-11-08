---
declaration: theorem
origin: cited
lean: TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero, TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero_of_finrank_le_add_two
statement: formalized
proof: formalized
---

# Sard's theorem on the locus where the derivative vanishes

Let `f` be a map between
finite-dimensional real normed spaces with nontrivial target, and let `s` be a set at each point
of which `f` is `C^n` and the Fréchet derivative of `f` vanishes. If
`((finrank ℝ E * finrank ℝ E + 1 : ℕ) : ℕ∞ω) ≤ n`, then `f '' s` has additive Haar measure zero.

No relation between the two dimensions is required, beyond a nontrivial (positive-dimensional)
target: the vanishing of the derivative, rather than a dimension count, is what the higher
derivatives are used against. The smoothness bound is sufficient, not the sharp exponent of the
Morse--Sard theorem.

```lean
TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero.{u_1, u_2} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] [Nontrivial F]
  (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] {E : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {f : E → F} {s : Set E} {n : WithTop ℕ∞}
  (hk : ↑(Module.finrank ℝ E * Module.finrank ℝ E + 1) ≤ n) (hf : ∀ x ∈ s, ContDiffAt ℝ n f x)
  (hs : ∀ x ∈ s, fderiv ℝ f x = 0) : ν (f '' s) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sard's lemma on the flat stratum](sards-lemma-on-the-flat-stratum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.html#TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero).

## Other forms

**Sard's theorem on the locus where the derivative vanishes, at the sharp regularity, in codimension at most two.** Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero_of_finrank_le_add_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.html#TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero_of_finrank_le_add_two).

```lean
TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero_of_finrank_le_add_two.{u_1, u_2} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] [MeasurableSpace F]
  [BorelSpace F] [Nontrivial F] (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {f : E → F} {s : Set E}
  {n : WithTop ℕ∞} (hcodim : Module.finrank ℝ E ≤ Module.finrank ℝ F + 2)
  (hk : ↑(Module.finrank ℝ E - Module.finrank ℝ F + 1) ≤ n) (hf : ∀ x ∈ s, ContDiffAt ℝ n f x)
  (hs : ∀ x ∈ s, fderiv ℝ f x = 0) : ν (f '' s) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.html#TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero)
- [Source of `TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero` in TauCeti/Analysis/Calculus/Sard/VanishingDerivative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.lean#L213)
