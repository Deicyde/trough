---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_eq_of_uniform_approx, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_eq_of_same_target, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_le, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_sq, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_le_of_bound, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_sq_eq_integral, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_add, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_neg
statement: formalized
proof: formalized
---

# The bounded functional calculus of a spectral measure

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.BoundedIntegralAlgebra`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean): 20 declarations, 1 with a docstring.

> The bounded integral against a spectral measure is a unital ⋆-homomorphism.

## i. Overview

> The integral of a bounded measurable function against a weak spectral measure does not depend on the
> approximating simple functions. It is a unital `⋆`-homomorphism from bounded measurable functions to
> bounded operators, with `‖(∫ f dμ) x‖² = ∫ |f|² dμₓ`. A spectral measure is determined by its
> bounded integrals.

## ii. Key results

> - `boundedIntegral_add`, `boundedIntegral_mul`, `boundedIntegral_star` : the integral is a
>   `⋆`-homomorphism.
> - `boundedIntegral_norm_sq_eq_integral` : `‖(∫ f dμ) x‖² = ∫ |f|² dμₓ`.
> - `ext_of_boundedIntegral_eq` : a spectral measure is determined by its bounded integrals.

## iv. References

> * None.

## A. Independence from the approximating sequence

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_eq_of_uniform_approx`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L62).

```lean
lemma boundedIntegral_eq_of_uniform_approx [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) (hbdd : ∃ C, ∀ x, ‖f x‖ ≤ C)
    {s : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε) :
    boundedIntegral μS f hf hbdd = boundedIntegralOfUniformApprox μS f s hs
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_eq_of_same_target`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L75).

```lean
lemma boundedIntegral_eq_of_same_target [Nonempty α]
    {f : α → ℂ} {s t : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (ht : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖t n x - f x‖ < ε)
    (hf : Measurable f) (hbdd : ∃ C, ∀ x, ‖f x‖ ≤ C) :
    boundedIntegralOfUniformApprox μS f s hs = boundedIntegral μS f hf hbdd
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_le`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L85).

```lean
lemma boundedIntegral_norm_le [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) (hbdd : ∃ C, ∀ x, ‖f x‖ ≤ C) :
    ∃ C : ℝ, ‖ContinuousLinearMapWOT.toCLM (boundedIntegral μS f hf hbdd)‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_sq`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L93).

```lean
lemma boundedIntegral_norm_sq [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) (hbdd : ∃ C, ∀ x, ‖f x‖ ≤ C) (x : H) :
    ENNReal.ofReal (‖boundedIntegral μS f hf hbdd x‖ ^ 2) =
      ∫⁻ z, ENNReal.ofReal (‖f z‖ ^ 2) ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_le_of_bound`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L163).

```lean
lemma boundedIntegral_norm_le_of_bound [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) {C : ℝ} (hC : 0 ≤ C)
    (hCf : ∀ x, ‖f x‖ ≤ C) :
    ‖ContinuousLinearMapWOT.toCLM
      (boundedIntegral μS f hf (⟨C, hCf⟩ : ∃ C : ℝ, ∀ x, ‖f x‖ ≤ C))‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_norm_sq_eq_integral`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L201).

```lean
lemma boundedIntegral_norm_sq_eq_integral [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) (hbdd : ∃ C : ℝ, ∀ x, ‖f x‖ ≤ C) (x : H) :
    ‖boundedIntegral μS f hf hbdd x‖ ^ 2 =
      ∫ z, ‖f z‖ ^ 2 ∂μS.diagonalMeasure x
```

## B. The algebra of the integral

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_add`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L225).

```lean
lemma boundedIntegralOfUniformApprox_add [Nonempty α]
    {f g : α → ℂ} {s t : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (ht : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖t n x - g x‖ < ε)
    (hsg : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x,
      ‖(s n + t n) x - (f + g) x‖ < ε) :
    boundedIntegralOfUniformApprox μS (f + g) (fun n => s n + t n) hsg =
      boundedIntegralOfUniformApprox μS f s hs +
        boundedIntegralOfUniformApprox μS g t ht
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_neg`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L268).

```lean
lemma boundedIntegralOfUniformApprox_neg [Nonempty α]
    {f : α → ℂ} {s : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (hneg : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x,
      ‖(-s n) x - (-f x)‖ < ε) :
    boundedIntegralOfUniformApprox μS (fun x => -f x) (fun n => -s n) hneg =
      -boundedIntegralOfUniformApprox μS f s hs
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_neg`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L295).

```lean
lemma boundedIntegral_neg [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) :
    boundedIntegral μS (fun x => -f x) (continuous_neg.measurable.comp hf)
        (by
          rcases hbf with ⟨C, hC⟩
          exact ⟨C, fun x => by simpa using hC x⟩) =
      -boundedIntegral μS f hf hbf
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_add`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L323).

```lean
lemma boundedIntegral_add [Nonempty α]
    {f g : α → ℂ} (hf : Measurable f) (hg : Measurable g)
    (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) (hbg : ∃ C, ∀ x, ‖g x‖ ≤ C) :
    boundedIntegral μS (f + g) (hf.add hg)
        (by
          rcases hbf with ⟨Cf, hCf⟩
          rcases hbg with ⟨Cg, hCg⟩
          refine ⟨Cf + Cg, fun x => ?_⟩
          exact (norm_add_le _ _).trans (add_le_add (hCf x) (hCg x))) =
      boundedIntegral μS f hf hbf + boundedIntegral μS g hg hbg
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_const`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L356).

```lean
lemma boundedIntegral_const [Nonempty α] (c : ℂ) :
    boundedIntegral μS (fun _ : α => c) measurable_const
        (⟨‖c‖, fun _ => le_rfl⟩) = c • (1 : H →WOT[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_congr`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L380).

```lean
lemma boundedIntegral_congr [Nonempty α]
    {f g : α → ℂ} (hf : Measurable f) (hg : Measurable g)
    (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) (hbg : ∃ C, ∀ x, ‖g x‖ ≤ C)
    (hfg : ∀ x, f x = g x) :
    boundedIntegral μS f hf hbf = boundedIntegral μS g hg hbg
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_indicator`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L395).

```lean
lemma boundedIntegral_indicator [Nonempty α] {S : Set α} (hS : MeasurableSet S) :
    boundedIntegral μS (S.indicator (fun _ : α => (1 : ℂ)))
        (measurable_const.indicator hS)
        (⟨1, fun x => by by_cases hx : x ∈ S <;> simp [hx]⟩) = μS S
```

## C. Extensionality by the integral

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.ext_of_boundedIntegral_eq`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L432).

> A bounded spectral integral determines a weak spectral measure. In particular, this gives a
> usable uniqueness principle for any construction which agrees with the canonical integral on
> bounded Borel multipliers.

```lean
lemma ext_of_boundedIntegral_eq [Nonempty α]
    {μS νS : WOTSpectralMeasure α H}
    (h : ∀ (f : α → ℂ) (hf : Measurable f) (hfb : ∃ C : ℝ, ∀ a, ‖f a‖ ≤ C),
      μS.boundedIntegral f hf hfb = νS.boundedIntegral f hf hfb) :
    μS = νS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_sub`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L449).

```lean
lemma boundedIntegral_sub [Nonempty α]
    {f g : α → ℂ} (hf : Measurable f) (hg : Measurable g)
    (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) (hbg : ∃ C, ∀ x, ‖g x‖ ≤ C) :
    boundedIntegral μS (f - g) (hf.sub hg)
        (by
          rcases hbf with ⟨Cf, hCf⟩
          rcases hbg with ⟨Cg, hCg⟩
          refine ⟨Cf + Cg, fun x => ?_⟩
          exact (norm_sub_le _ _).trans (add_le_add (hCf x) (hCg x))) =
      boundedIntegral μS f hf hbf - boundedIntegral μS g hg hbg
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_mul`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L491).

```lean
lemma boundedIntegralOfUniformApprox_mul [Nonempty α]
    {f g : α → ℂ} {s t : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (ht : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖t n x - g x‖ < ε)
    (hprod : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x,
      ‖(s n * t n) x - (f * g) x‖ < ε) :
    boundedIntegralOfUniformApprox μS (f * g) (fun n => s n * t n) hprod =
      boundedIntegralOfUniformApprox μS f s hs *
        boundedIntegralOfUniformApprox μS g t ht
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_mul`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L539).

```lean
lemma boundedIntegral_mul [Nonempty α]
    {f g : α → ℂ} (hf : Measurable f) (hg : Measurable g)
    (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) (hbg : ∃ C, ∀ x, ‖g x‖ ≤ C) :
    boundedIntegral μS (f * g) (hf.mul hg)
        (by
          rcases hbf with ⟨Cf, hCf⟩
          rcases hbg with ⟨Cg, hCg⟩
          let a₀ : α := Classical.choice (inferInstance : Nonempty α)
          have hCf0 : 0 ≤ Cf := (norm_nonneg (f a₀)).trans (hCf a₀)
          refine ⟨Cf * Cg, fun x => ?_⟩
          rw [Pi.mul_apply, norm_mul]
          exact mul_le_mul (hCf x) (hCg x) (norm_nonneg _) hCf0) =
      boundedIntegral μS f hf hbf * boundedIntegral μS g hg hbg
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_smul`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L602).

```lean
lemma boundedIntegral_smul [Nonempty α] (c : ℂ) {f : α → ℂ} (hf : Measurable f)
    (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) :
    boundedIntegral μS (fun x => c * f x)
        (measurable_const.mul hf)
        (by
          rcases hbf with ⟨C, hC⟩
          refine ⟨‖c‖ * C, fun x => ?_⟩
          rw [norm_mul]
          exact mul_le_mul_of_nonneg_left (hC x) (norm_nonneg c)) =
      c • boundedIntegral μS f hf hbf
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegralOfUniformApprox_star`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L623).

```lean
lemma boundedIntegralOfUniformApprox_star [Nonempty α]
    {f : α → ℂ} {s : ℕ → SimpleFunc α ℂ}
    (hs : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x, ‖s n x - f x‖ < ε)
    (hstar : ∀ ε > 0, ∃ N, ∀ n ≥ N, ∀ x,
      ‖(star (s n)) x - star (f x)‖ < ε) :
    boundedIntegralOfUniformApprox μS (fun x => star (f x)) (fun n => star (s n)) hstar =
      star (boundedIntegralOfUniformApprox μS f s hs)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_star`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean#L662).

```lean
lemma boundedIntegral_star [Nonempty α]
    {f : α → ℂ} (hf : Measurable f) (hbf : ∃ C, ∀ x, ‖f x‖ ≤ C) :
    boundedIntegral μS (fun x => star (f x)) (continuous_star.measurable.comp hf)
        (by
          rcases hbf with ⟨C, hC⟩
          exact ⟨C, fun x => by simpa using hC x⟩) =
      star (boundedIntegral μS f hf hbf)
```

## Depends on

- [Integrating bounded functions against a spectral measure](unbounded-boundedintegral.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/BoundedIntegralAlgebra.lean)
