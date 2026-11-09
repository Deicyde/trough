---
declaration: theorem
origin: cited
lean: TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero, TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin, TauCeti.ContDiff.addHaar_image_flatStratum_eq_zero, TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero_of_finrank_le_mul, TauCeti.dimH_image_le_of_iteratedFDeriv_eq_zero, TauCeti.hausdorffMeasure_image_eq_zero_of_iteratedFDeriv_eq_zero
statement: formalized
proof: formalized
---

# Sard's lemma on the flat stratum

Let `f` be `C^{k+1}` on an open set `U` of a
finite-dimensional real normed space, and let `s ⊆ U` be a set at each point of which every
iterated derivative of order `1 ≤ i ≤ k` vanishes. If `finrank ℝ E < (k + 1) * finrank ℝ F`, then
`f '' s` has additive Haar measure zero.

This is the slice of finite-dimensional Sard that higher regularity buys: for a fixed pair of
dimensions with positive-dimensional target, the hypothesis holds as soon as `k` is large enough.

```lean
TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : E → F}
  {k : ℕ} {s : Set E} [FiniteDimensional ℝ E] [FiniteDimensional ℝ F] [MeasurableSpace F]
  [BorelSpace F] (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] {U : Set E} (hU : IsOpen U)
  (hf : ContDiffOn ℝ (↑(k + 1)) f U) (hsU : s ⊆ U)
  (hzero : ∀ x ∈ s, ∀ (i : ℕ), 1 ≤ i → i ≤ k → iteratedFDeriv ℝ i f x = 0)
  (hdim : Module.finrank ℝ E < (k + 1) * Module.finrank ℝ F) : ν (f '' s) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/FlatStratum.html#TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero).

## Other forms

**Sard's lemma in equal dimensions.** Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/EqualDimension.html#TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin).

```lean
TauCeti.addHaar_image_eq_zero_of_not_surjective_fderivWithin.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F] {s : Set E} {f : E → F}
  {f' : E → E →L[ℝ] F} (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure]
  (hdim : Module.finrank ℝ E = Module.finrank ℝ F) (hf' : ∀ x ∈ s, HasFDerivWithinAt f (f' x) s x)
  (hcrit : ∀ x ∈ s, ¬Function.Surjective ⇑(f' x)) : ν (f '' s) = 0
```

**Sard's lemma on the flat stratum, global form.** Formalized in Tau Ceti as [`TauCeti.ContDiff.addHaar_image_flatStratum_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/FlatStratum.html#TauCeti.ContDiff.addHaar_image_flatStratum_eq_zero).

```lean
TauCeti.ContDiff.addHaar_image_flatStratum_eq_zero.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : E → F}
  {k : ℕ} [FiniteDimensional ℝ E] [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F]
  (ν : MeasureTheory.Measure F) [ν.IsAddHaarMeasure] (hf : ContDiff ℝ (↑(k + 1)) f)
  (hdim : Module.finrank ℝ E < (k + 1) * Module.finrank ℝ F) :
  ν (f '' {x | ∀ (i : ℕ), 1 ≤ i → i ≤ k → iteratedFDeriv ℝ i f x = 0}) = 0
```

**Sard's lemma on the flat stratum at the sharp regularity.** Formalized in Tau Ceti as [`TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero_of_finrank_le_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/FlatStratum.html#TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero_of_finrank_le_mul).

```lean
TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero_of_finrank_le_mul.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {f : E → F} {k : ℕ} {s : Set E} [FiniteDimensional ℝ E] [MeasurableSpace F] [BorelSpace F]
  {U : Set E} [FiniteDimensional ℝ F] [Nontrivial F] (ν : MeasureTheory.Measure F)
  [ν.IsAddHaarMeasure] (hU : IsOpen U) (hf : ContDiffOn ℝ (↑k) f U) (hsU : s ⊆ U)
  (hzero : ∀ x ∈ s, ∀ (i : ℕ), 1 ≤ i → i ≤ k → iteratedFDeriv ℝ i f x = 0)
  (hdim : Module.finrank ℝ E ≤ k * Module.finrank ℝ F) : ν (f '' s) = 0
```

**Sard's lemma on the flat stratum, in Hausdorff dimension.** Formalized in Tau Ceti as [`TauCeti.dimH_image_le_of_iteratedFDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/FlatStratum.html#TauCeti.dimH_image_le_of_iteratedFDeriv_eq_zero).

```lean
TauCeti.dimH_image_le_of_iteratedFDeriv_eq_zero.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : E → F}
  {k : ℕ} {s : Set E} [SecondCountableTopology E] {U : Set E} (hU : IsOpen U)
  (hf : ContDiffOn ℝ (↑(k + 1)) f U) (hsU : s ⊆ U)
  (hzero : ∀ x ∈ s, ∀ (i : ℕ), 1 ≤ i → i ≤ k → iteratedFDeriv ℝ i f x = 0) :
  dimH (f '' s) ≤ dimH s / (↑k + 1)
```

**Sard's lemma on the flat stratum, in Hausdorff measure.** Formalized in Tau Ceti as [`TauCeti.hausdorffMeasure_image_eq_zero_of_iteratedFDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/FlatStratum.html#TauCeti.hausdorffMeasure_image_eq_zero_of_iteratedFDeriv_eq_zero).

```lean
TauCeti.hausdorffMeasure_image_eq_zero_of_iteratedFDeriv_eq_zero.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {f : E → F} {k : ℕ} {s : Set E} [FiniteDimensional ℝ E] [MeasurableSpace F] [BorelSpace F]
  {U : Set E} [Nontrivial E] (hU : IsOpen U) (hf : ContDiffOn ℝ (↑k) f U) (hsU : s ⊆ U) (hk : 0 < k)
  (hzero : ∀ x ∈ s, ∀ (i : ℕ), 1 ≤ i → i ≤ k → iteratedFDeriv ℝ i f x = 0) :
  (MeasureTheory.Measure.hausdorffMeasure (↑(Module.finrank ℝ E) / ↑k)) (f '' s) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/FlatStratum.html#TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero)
- [Source of `TauCeti.addHaar_image_eq_zero_of_iteratedFDeriv_eq_zero` in TauCeti/Analysis/Calculus/Sard/FlatStratum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Sard/FlatStratum.lean#L209)
