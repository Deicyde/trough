---
declaration: theorem
origin: cited
lean: TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero
statement: formalized
proof: formalized
---

# Sard's theorem on the locus where the derivative vanishes

Let `f` be a map between
finite-dimensional real normed spaces with nontrivial target, and let `s` be a set at each point
of which `f` is `C^n` and its Fréchet derivative vanishes. If `k ≤ n` and
`finrank ℝ E ≤ k * finrank ℝ F`, then `f '' s` has additive Haar measure zero. The set `s` need
not be open or measurable.

```lean
TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero.{u_1, u_2} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] [Nontrivial F]
  (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] {E : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {f : E → F} {s : Set E} {k : ℕ} {n : WithTop ℕ∞}
  (hf : ∀ x ∈ s, ContDiffAt ℝ n f x) (hk : ↑k ≤ n)
  (hdim : Module.finrank ℝ E ≤ k * Module.finrank ℝ F) (hs : ∀ x ∈ s, fderiv ℝ f x = 0) :
  ν (f '' s) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse criticality lemma](../part-01/the-morse-criticality-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.html#TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.html#TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero)
- [Source of `TauCeti.addHaar_image_eq_zero_of_fderiv_eq_zero` in TauCeti/Analysis/Calculus/Sard/VanishingDerivative.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Sard/VanishingDerivative.lean#L90)
