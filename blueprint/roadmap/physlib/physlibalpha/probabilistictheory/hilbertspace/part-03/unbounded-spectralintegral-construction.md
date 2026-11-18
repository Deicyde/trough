---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.realTruncationFunction, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoffSet, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoffSet_mono, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoffSet_iUnion, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction_measurable, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction_bounded, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.realTruncationFunction_measurable
statement: formalized
proof: formalized
---

# Integrating unbounded functions against a spectral measure

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.SpectralIntegral.Construction`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean): 67 declarations, 14 with a docstring.

> The maximal spectral integral `∫ f dμ` of an unbounded function, built from bounded truncations.

## i. Overview

> For a real measurable function `f` and a spectral measure `μ`, the integral `∫ f dμ` is defined on
> the vectors `x` with `∫ f² dμₓ < ∞`, as the limit of the bounded integrals of the truncations of
> `f`. It is densely defined, closable, symmetric and essentially self-adjoint. The construction is
> carried out for the identity function `λ ↦ λ`, and a general `f` is handled by pushing `μ` forward
> along `f`.

## ii. Key results

> - `truncationFunction` : the spectral variable `λ` truncated to `[-n, n]`.
> - `truncationIntegral` : the bounded integral of the `n`-th truncation.
> - `spectralSquareMomentSubmodule` : the vectors of finite second moment, as a submodule.
> - `maximalSpectralIntegral` : the integral `∫ λ dμ` on its maximal domain.
> - `maximalSpectralIntegral_isSymmetric` : the maximal integral is symmetric.
> - `maximalSpectralIntegral_hasDenseDomain` : its domain is dense.
> - `maximalSpectralIntegral_isClosable` : it is closable.
> - `measurableSpectralIntegral` : the integral of a measurable real function `f`, obtained by
>   pushing the spectral measure forward along `f`.
> - `boundedIntegral_tendsto_of_pointwise_tendsto_of_bound` : bounded spectral integrals converge
>   when the integrands converge pointwise under a uniform bound.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L64).

> The bounded real spectral variable truncated to `[-n,n]`.

```lean
def truncationFunction (n : ℕ) : ℝ → ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.realTruncationFunction`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L68).

> The real-truncation indicator function, real-valued, at cutoff `n`.

```lean
def realTruncationFunction (n : ℕ) : ℝ → ℝ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoffSet`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L72).

> The spectral cutoff set `[-n, n]`.

```lean
def spectralCutoffSet (n : ℕ) : Set ℝ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoffSet_mono`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L74).

```lean
lemma spectralCutoffSet_mono : Monotone spectralCutoffSet
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoffSet_iUnion`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L79).

```lean
lemma spectralCutoffSet_iUnion : ⋃ n, spectralCutoffSet n = Set.univ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction_measurable`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L85).

```lean
lemma truncationFunction_measurable (n : ℕ) : Measurable (truncationFunction n)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction_bounded`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L88).

```lean
lemma truncationFunction_bounded (n : ℕ) :
    ∃ C : ℝ, ∀ r, ‖truncationFunction n r‖ ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.realTruncationFunction_measurable`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L97).

```lean
lemma realTruncationFunction_measurable (n : ℕ) :
    Measurable (realTruncationFunction n)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.realTruncationFunction_bounded`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L101).

```lean
lemma realTruncationFunction_bounded (n : ℕ) :
    ∃ C : ℝ, ∀ r, |realTruncationFunction n r| ≤ C
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.realTruncationFunction_complex_eq`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L109).

```lean
lemma realTruncationFunction_complex_eq (n : ℕ) :
    (fun r => (realTruncationFunction n r : ℂ)) = truncationFunction n
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction_eventually_eq`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L115).

```lean
lemma truncationFunction_eventually_eq (r : ℝ) :
    ∀ᶠ n : ℕ in Filter.atTop, truncationFunction n r = (r : ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationFunction_tendsto`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L123).

```lean
lemma truncationFunction_tendsto (r : ℝ) :
    Filter.Tendsto (fun n : ℕ => truncationFunction n r) Filter.atTop (𝓝 (r : ℂ))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_inner_tendsto_complexWeakIntegral`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L127).

```lean
lemma truncationIntegral_inner_tendsto_complexWeakIntegral
    (μS : WOTSpectralMeasure ℝ H) (x y : H)
    (hfi : (μS.scalarMeasure x y).Integrable id) :
    Filter.Tendsto
      (fun n : ℕ => ∫ᵛ r, truncationFunction n r ∂[
        ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ); μS.scalarMeasure x y])
      Filter.atTop (𝓝 (μS.complexWeakIntegral (fun r : ℝ => (r : ℂ)) x y))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integral_indicator_real_eq_complex`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L160).

```lean
lemma integral_indicator_real_eq_complex
    {α : Type*} [MeasurableSpace α] (μ : MeasureTheory.VectorMeasure α ℂ)
    (c : ℝ) (s : Set α) :
    (∫ᵛ x, s.indicator (fun _ => (c : ℂ)) x
      ∂[ContinuousLinearMap.lsmul ℝ ℂ; μ]) =
      ∫ᵛ x, (s.indicator (fun _ => c) x : ℂ)
        ∂[ContinuousLinearMap.lsmul ℝ ℂ; μ]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.integral_real_eq_complex`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L173).

```lean
lemma integral_real_eq_complex
    {α : Type*} [MeasurableSpace α] (μ : MeasureTheory.VectorMeasure α ℂ)
    {g : α → ℝ} (hg : μ.Integrable g) :
    ∫ᵛ x, g x ∂[ContinuousLinearMap.lsmul ℝ ℝ (E := ℂ); μ] =
      ∫ᵛ x, (g x : ℂ) ∂[ContinuousLinearMap.lsmul ℝ ℂ; μ]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L250).

> The bounded operator obtained by integrating the `n`-th truncated spectral variable.

```lean
noncomputable def truncationIntegral (μS : WOTSpectralMeasure ℝ H) (n : ℕ) : H →WOT[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_sub_apply`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L254).

```lean
lemma truncationIntegral_sub_apply (μS : WOTSpectralMeasure ℝ H) (n m : ℕ) (x : H) :
    truncationIntegral μS n x - truncationIntegral μS m x =
      boundedIntegral μS (fun r => truncationFunction n r - truncationFunction m r)
        ((truncationFunction_measurable n).sub (truncationFunction_measurable m))
        (by
          rcases truncationFunction_bounded n with ⟨Cn, hCn⟩
          rcases truncationFunction_bounded m with ⟨Cm, hCm⟩
          refine ⟨Cn + Cm, fun r => ?_⟩
          exact (norm_sub_le _ _).trans (add_le_add (hCn r) (hCm r))) x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_add_le`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L270).

```lean
lemma diagonalMeasure_add_le (μS : WOTSpectralMeasure ℝ H) (x y : H) :
    μS.diagonalMeasure (x + y) ≤
      (μS.diagonalMeasure x + μS.diagonalMeasure x) +
        (μS.diagonalMeasure y + μS.diagonalMeasure y)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralSquareMomentDomain_zero`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L285).

```lean
lemma spectralSquareMomentDomain_zero (μS : WOTSpectralMeasure ℝ H) :
    (0 : H) ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralSquareMomentDomain_add`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L292).

```lean
lemma spectralSquareMomentDomain_add (μS : WOTSpectralMeasure ℝ H) {x y : H}
    (hx : x ∈ spectralSquareMomentDomain μS)
    (hy : y ∈ spectralSquareMomentDomain μS) :
    x + y ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralSquareMomentDomain_smul`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L301).

```lean
lemma spectralSquareMomentDomain_smul (μS : WOTSpectralMeasure ℝ H) (c : ℂ) {x : H}
    (hx : x ∈ spectralSquareMomentDomain μS) :
    c • x ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralSquareMomentSubmodule`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L309).

> The vectors of finite second moment, as a submodule.

```lean
def spectralSquareMomentSubmodule (μS : WOTSpectralMeasure ℝ H) : Submodule ℂ H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_sub_norm_sq`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L315).

```lean
lemma truncationIntegral_sub_norm_sq (μS : WOTSpectralMeasure ℝ H) (n m : ℕ) (x : H) :
    ENNReal.ofReal (‖truncationIntegral μS n x - truncationIntegral μS m x‖ ^ 2) =
      ∫⁻ r, ENNReal.ofReal
        (‖truncationFunction n r - truncationFunction m r‖ ^ 2)
        ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_sub_norm_sq_le`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L329).

```lean
lemma truncationIntegral_sub_norm_sq_le (μS : WOTSpectralMeasure ℝ H) (n m : ℕ) (x : H) :
    ENNReal.ofReal (‖truncationIntegral μS n x - truncationIntegral μS m x‖ ^ 2) ≤
      2 * (∫⁻ r, ENNReal.ofReal
        (‖truncationFunction n r - (r : ℂ)‖ ^ 2) ∂μS.diagonalMeasure x) +
        2 * (∫⁻ r, ENNReal.ofReal
          (‖truncationFunction m r - (r : ℂ)‖ ^ 2) ∂μS.diagonalMeasure x)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncation_error_lintegral_tendsto_zero`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L386).

```lean
lemma truncation_error_lintegral_tendsto_zero
    (μS : WOTSpectralMeasure ℝ H) (x : H)
    (hx : Integrable (fun r : ℝ => r ^ 2) (μS.diagonalMeasure x)) :
    Filter.Tendsto
      (fun n : ℕ => ∫⁻ r, ENNReal.ofReal
        (‖truncationFunction n r - (r : ℂ)‖ ^ 2) ∂μS.diagonalMeasure x)
      Filter.atTop (𝓝 0)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_cauchy`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L449).

```lean
lemma truncationIntegral_cauchy (μS : WOTSpectralMeasure ℝ H) {x : H}
    (hx : x ∈ spectralSquareMomentDomain μS) :
    CauchySeq (fun n : ℕ => truncationIntegral μS n x)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncation_norm_lintegral_tendsto`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L504).

```lean
lemma truncation_norm_lintegral_tendsto
    (μS : WOTSpectralMeasure ℝ H) (x : H)
    (hx : Integrable (fun r : ℝ => r ^ 2) (μS.diagonalMeasure x)) :
    Filter.Tendsto
      (fun n : ℕ => ∫⁻ r, ENNReal.ofReal
        (‖truncationFunction n r‖ ^ 2) ∂μS.diagonalMeasure x)
      Filter.atTop
      (𝓝 (∫⁻ r, ENNReal.ofReal (r ^ 2) ∂μS.diagonalMeasure x))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationLimit`**, a def, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L557).

> The limit of the truncated spectral integrals, for `x` in the finite-second-moment domain.

```lean
noncomputable def truncationLimit (μS : WOTSpectralMeasure ℝ H)
    (x : spectralSquareMomentSubmodule μS) : H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationLimit_tendsto`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L561).

```lean
lemma truncationLimit_tendsto (μS : WOTSpectralMeasure ℝ H)
    (x : spectralSquareMomentSubmodule μS) :
    Filter.Tendsto (fun n : ℕ => truncationIntegral μS n x) Filter.atTop
      (𝓝 (truncationLimit μS x))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationLimit_add`**, a lemma, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L567).

```lean
lemma truncationLimit_add (μS : WOTSpectralMeasure ℝ H)
    (x y : spectralSquareMomentSubmodule μS) :
    truncationLimit μS (x + y) = truncationLimit μS x + truncationLimit μS y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationLimit_smul`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L577).

```lean
lemma truncationLimit_smul (μS : WOTSpectralMeasure ℝ H)
    (c : ℂ) (x : spectralSquareMomentSubmodule μS) :
    truncationLimit μS (c • x) = c • truncationLimit μS x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_norm_sq`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L587).

```lean
lemma truncationIntegral_norm_sq (μS : WOTSpectralMeasure ℝ H) (n : ℕ) (x : H) :
    ENNReal.ofReal (‖truncationIntegral μS n x‖ ^ 2) =
      ∫⁻ r, ENNReal.ofReal (‖truncationFunction n r‖ ^ 2)
        ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_star`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L594).

```lean
lemma truncationIntegral_star (μS : WOTSpectralMeasure ℝ H) (n : ℕ) :
    star (truncationIntegral μS n) = truncationIntegral μS n
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_inner_swap`**, a lemma, [line 612](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L612).

```lean
lemma truncationIntegral_inner_swap (μS : WOTSpectralMeasure ℝ H) (n : ℕ)
    (x y : H) :
    ⟪truncationIntegral μS n x, y⟫_ℂ = ⟪x, truncationIntegral μS n y⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral`**, a def, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L623).

> The maximal operator obtained from a real weak spectral measure by norm convergence of bounded
> truncations.  Its domain is exactly the square-moment submodule.

```lean
noncomputable def maximalSpectralIntegral
    (μS : WOTSpectralMeasure ℝ H) : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isSymmetric`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L630).

```lean
lemma maximalSpectralIntegral_isSymmetric (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).IsSymmetric
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoff_mem_spectralSquareMomentDomain`**, a lemma, [line 651](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L651).

```lean
lemma spectralCutoff_mem_spectralSquareMomentDomain
    (μS : WOTSpectralMeasure ℝ H) (x : H) {C : ℝ} (_hC : 0 ≤ C) :
    μS (Set.Icc (-C) C) x ∈ spectralSquareMomentDomain μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.diagonalMeasure_cutoff_compl_tendsto_zero`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L676).

```lean
lemma diagonalMeasure_cutoff_compl_tendsto_zero
    (μS : WOTSpectralMeasure ℝ H) (x : H) :
    Filter.Tendsto
      (fun n : ℕ => μS.diagonalMeasure x (spectralCutoffSet n)ᶜ)
      Filter.atTop (𝓝 0)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.spectralCutoff_tendsto`**, a lemma, [line 701](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L701).

```lean
lemma spectralCutoff_tendsto (μS : WOTSpectralMeasure ℝ H) (x : H) :
    Filter.Tendsto
      (fun n : ℕ => μS (spectralCutoffSet n) x) Filter.atTop (𝓝 x)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_hasDenseDomain`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L740).

```lean
lemma maximalSpectralIntegral_hasDenseDomain (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).HasDenseDomain
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isClosable`**, a lemma, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L750).

```lean
lemma maximalSpectralIntegral_isClosable (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).IsClosable
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isUnbounded`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L758).

```lean
lemma maximalSpectralIntegral_isUnbounded (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).IsUnbounded
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_closure_isClosed`**, a lemma, [line 763](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L763).

```lean
lemma maximalSpectralIntegral_closure_isClosed (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).closure.IsClosed
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_closure_isSymmetric`**, a lemma, [line 767](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L767).

```lean
lemma maximalSpectralIntegral_closure_isSymmetric (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).closure.IsSymmetric
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isEssentiallySelfAdjoint_iff`**, a lemma, [line 772](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L772).

```lean
lemma maximalSpectralIntegral_isEssentiallySelfAdjoint_iff (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).IsEssentiallySelfAdjoint ↔
      IsSelfAdjoint (maximalSpectralIntegral μS).closure
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isSelfAdjoint_of_range_eq_top`**, a lemma, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L777).

> If `T ± i` have full range for the integral `T` of the identity, then `T` is self-adjoint.

```lean
lemma maximalSpectralIntegral_isSelfAdjoint_of_range_eq_top
    (μS : WOTSpectralMeasure ℝ H)
    (hadd : (maximalSpectralIntegral μS + Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤)
    (hsub : (maximalSpectralIntegral μS - Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤) :
    IsSelfAdjoint (maximalSpectralIntegral μS)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_closure_eq_self`**, a lemma, [line 790](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L790).

> The closure of the canonical PVM realization is self-adjoint under the same resolvent
> surjectivity hypotheses.  The stronger conclusion is exposed separately because downstream
> models usually start with an operator on a smaller core and identify its closure with this
> canonical realization.

```lean
lemma maximalSpectralIntegral_closure_eq_self
    (μS : WOTSpectralMeasure ℝ H)
    (hadd : (maximalSpectralIntegral μS + Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤)
    (hsub : (maximalSpectralIntegral μS - Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤) :
    (maximalSpectralIntegral μS).closure = maximalSpectralIntegral μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_isEssentiallySelfAdjoint_of_range_eq_top`**, a lemma, [line 798](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L798).

```lean
lemma maximalSpectralIntegral_isEssentiallySelfAdjoint_of_range_eq_top
    (μS : WOTSpectralMeasure ℝ H)
    (hadd : (maximalSpectralIntegral μS + Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤)
    (hsub : (maximalSpectralIntegral μS - Complex.I • (1 : H →ₗ.[ℂ] H)).toFun.range = ⊤) :
    (maximalSpectralIntegral μS).IsEssentiallySelfAdjoint
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_norm_sq`**, a lemma, [line 807](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L807).

```lean
lemma maximalSpectralIntegral_norm_sq (μS : WOTSpectralMeasure ℝ H)
    (x : H) (hx : x ∈ (maximalSpectralIntegral μS).domain) :
    ENNReal.ofReal (‖(maximalSpectralIntegral μS) ⟨x, hx⟩‖ ^ 2) =
      ∫⁻ r, ENNReal.ofReal (r ^ 2) ∂μS.diagonalMeasure x
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_domain`**, a lemma, [line 827](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L827).

```lean
lemma maximalSpectralIntegral_domain (μS : WOTSpectralMeasure ℝ H) :
    (maximalSpectralIntegral μS).domain = spectralSquareMomentSubmodule μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_apply`**, a lemma, [line 830](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L830).

```lean
lemma maximalSpectralIntegral_apply (μS : WOTSpectralMeasure ℝ H)
    (x : H) (hx : x ∈ (maximalSpectralIntegral μS).domain) :
    (maximalSpectralIntegral μS) ⟨x, hx⟩ = truncationLimit μS ⟨x, hx⟩
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_inner_projection`**, a lemma, [line 833](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L833).

```lean
lemma scalarMeasure_inner_projection (μS : WOTSpectralMeasure ℝ H)
    (x y : H) (S : Set ℝ) (_hS : MeasurableSet S) :
    ⟪y, μS S x⟫_ℂ = ⟪μS S y, μS S x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_variation_le_diagonal_add`**, a lemma, [line 855](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L855).

```lean
lemma scalarMeasure_variation_le_diagonal_add (μS : WOTSpectralMeasure ℝ H)
    (x y : H) :
    (μS.scalarMeasure x y).variation ≤ μS.diagonalMeasure x + μS.diagonalMeasure y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.scalarMeasure_isFiniteVariation`**, a lemma, [line 871](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L871).

```lean
lemma scalarMeasure_isFiniteVariation (μS : WOTSpectralMeasure ℝ H)
    (x y : H) : IsFiniteMeasure (μS.scalarMeasure x y).variation
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_inner_tendsto_weakIntegral`**, a lemma, [line 877](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L877).

```lean
lemma truncationIntegral_inner_tendsto_weakIntegral
    (μS : WOTSpectralMeasure ℝ H) (x y : H)
    (hfi : (μS.scalarMeasure x y).Integrable id) :
    Filter.Tendsto
      (fun n : ℕ => ∫ᵛ r, realTruncationFunction n r ∂[
        ContinuousLinearMap.lsmul ℝ ℝ (E := ℂ); μS.scalarMeasure x y])
      Filter.atTop (𝓝 (μS.weakIntegral id x y))
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_inner`**, a lemma, [line 916](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L916).

```lean
lemma boundedIntegral_inner
    {α : Type*} [MeasurableSpace α] [Nonempty α]
    (μS : WOTSpectralMeasure α H) {f : α → ℂ} (hf : Measurable f)
    (hfb : ∃ C : ℝ, ∀ a, ‖f a‖ ≤ C) (x y : H)
    (hfinite : IsFiniteMeasure (μS.scalarMeasure x y).variation) :
    ⟪y, boundedIntegral μS f hf hfb x⟫_ℂ =
      ∫ᵛ a, f a ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        μS.scalarMeasure x y]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.truncationIntegral_inner`**, a lemma, [line 933](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L933).

```lean
lemma truncationIntegral_inner (μS : WOTSpectralMeasure ℝ H) (n : ℕ)
    (x y : H) :
    ⟪y, truncationIntegral μS n x⟫_ℂ =
      ∫ᵛ r, truncationFunction n r ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        μS.scalarMeasure x y]
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.maximalSpectralIntegral_weak_truncation_reconstruction`**, a lemma, [line 941](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L941).

```lean
lemma maximalSpectralIntegral_weak_truncation_reconstruction
    (μS : WOTSpectralMeasure ℝ H) (x : H)
    (hx : x ∈ (maximalSpectralIntegral μS).domain) (y : H) :
    Filter.Tendsto
      (fun n : ℕ => ∫ᵛ r, truncationFunction n r ∂[
        ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ); μS.scalarMeasure x y])
      Filter.atTop (𝓝 (⟪y, (maximalSpectralIntegral μS) ⟨x, hx⟩⟫_ℂ))
```

## A. Measurable real functional calculus

> The maximal construction is not tied to the coordinate function.  For a measurable real
> multiplier `f`, push the PVM forward along `f` and apply the same construction to the new
> spectral variable.  This is the concrete operator realization of the representation-free
> `PVM.map` operation used by the affiliated-observable API.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral`**, a def, [line 970](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L970).

> The maximal unbounded operator obtained by integrating a measurable real function against a
> weak spectral measure.  It is defined by PVM pushforward, so no second truncation construction is
> needed for each multiplier.

```lean
noncomputable def measurableSpectralIntegral (μS : WOTSpectralMeasure ℝ H)
    (f : ℝ → ℝ) (hf : Measurable f) : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_id`**, a lemma, [line 975](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L975).

```lean
lemma measurableSpectralIntegral_id (μS : WOTSpectralMeasure ℝ H) :
    measurableSpectralIntegral μS id measurable_id = maximalSpectralIntegral μS
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_comp`**, a lemma, [line 980](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L980).

```lean
lemma measurableSpectralIntegral_comp
    (μS : WOTSpectralMeasure ℝ H) (f g : ℝ → ℝ)
    (hf : Measurable f) (hg : Measurable g) :
    measurableSpectralIntegral (μS.map f hf) g hg =
      measurableSpectralIntegral μS (g ∘ f) (hg.comp hf)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_domain`**, a lemma, [line 991](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L991).

```lean
lemma measurableSpectralIntegral_domain (μS : WOTSpectralMeasure ℝ H)
    (f : ℝ → ℝ) (hf : Measurable f) :
    (measurableSpectralIntegral μS f hf).domain =
      spectralSquareMomentSubmodule (μS.map f hf)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.mem_measurableSpectralIntegral_domain_iff`**, a lemma, [line 999](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L999).

> The domain of `∫ f dE` is exactly the square-integrability domain of `f` against every
> vector-state spectral measure.

```lean
lemma mem_measurableSpectralIntegral_domain_iff (μS : WOTSpectralMeasure ℝ H)
    (f : ℝ → ℝ) (hf : Measurable f) (x : H) :
    x ∈ (measurableSpectralIntegral μS f hf).domain ↔
      Integrable (fun r : ℝ => f r ^ 2) (μS.diagonalMeasure x)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_domain_eq_top_of_bounded`**, a lemma, [line 1013](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L1013).

> A bounded measurable real multiplier has no unbounded domain restriction.  This is the
> bounded-to-unbounded boundary in the reusable calculus: the same pushforward construction handles
> both cases, and boundedness turns its square-moment domain into `⊤`.

```lean
lemma measurableSpectralIntegral_domain_eq_top_of_bounded
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f)
    (hfb : ∃ C : ℝ, 0 ≤ C ∧ ∀ r : ℝ, |f r| ≤ C) :
    (measurableSpectralIntegral μS f hf).domain = ⊤
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.measurableSpectralIntegral_inner_eq_complexWeakIntegral`**, a lemma, [line 1029](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L1029).

> Weak reconstruction for a measurable real multiplier.  The only integrability assumption is
> the natural one on the original scalar spectral measure; the pushforward identity transports it
> to the coordinate function of the new PVM.

```lean
lemma measurableSpectralIntegral_inner_eq_complexWeakIntegral
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f)
    (x : H) (hx : x ∈ (measurableSpectralIntegral μS f hf).domain) (y : H)
    (hfi : (μS.scalarMeasure x y).Integrable f) :
    ⟪y, (measurableSpectralIntegral μS f hf) ⟨x, hx⟩⟫_ℂ =
      μS.complexWeakIntegral (fun r : ℝ => (f r : ℂ)) x y
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_ofReal_eq_measurableSpectralIntegral`**, a lemma, [line 1057](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L1057).

> For a bounded real function the bounded integral and the maximal integral are the same operator.

```lean
lemma boundedIntegral_ofReal_eq_measurableSpectralIntegral
    (μS : WOTSpectralMeasure ℝ H) (f : ℝ → ℝ) (hf : Measurable f)
    (hfb : ∃ C : ℝ, 0 ≤ C ∧ ∀ r : ℝ, |f r| ≤ C) (x : H) :
    boundedIntegral μS (fun r : ℝ => (f r : ℂ))
        (Complex.measurable_ofReal.comp hf)
        (by
          rcases hfb with ⟨C, _hC, hCbound⟩
          exact ⟨C, fun r => by
            simpa [Complex.norm_real, Real.norm_eq_abs] using hCbound r⟩) x =
      (measurableSpectralIntegral μS f hf)
        ⟨x, by
          rw [measurableSpectralIntegral_domain_eq_top_of_bounded μS f hf hfb]
          exact Submodule.mem_top⟩
```

## B. Convergence of bounded spectral multipliers

> The next lemma is the reusable norm-convergence principle behind the resolvent construction.  It
> only uses the PVM norm-square identity, so it is also useful for bounded functional calculus
> approximations unrelated to the Cayley transform.

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.boundedIntegral_tendsto_of_pointwise_tendsto_of_bound`**, a lemma, [line 1101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean#L1101).

```lean
lemma boundedIntegral_tendsto_of_pointwise_tendsto_of_bound
    {α : Type*} [MeasurableSpace α] [Nonempty α]
    (μS : WOTSpectralMeasure α H)
    {f : α → ℂ} {g : ℕ → α → ℂ} (x : H)
    (hf : Measurable f) (hg : ∀ n, Measurable (g n))
    (hfb : ∃ C : ℝ, ∀ a, ‖f a‖ ≤ C)
    (hgb : ∃ C : ℝ, ∀ n a, ‖g n a‖ ≤ C)
    (hlim : ∀ a, Filter.Tendsto (fun n => g n a) Filter.atTop (𝓝 (f a))) :
    Filter.Tendsto
      (fun n => boundedIntegral μS (g n) (hg n) (by
        rcases hgb with ⟨C, hC⟩
        exact ⟨C, hC n⟩) x)
      Filter.atTop
      (𝓝 (boundedIntegral μS f hf hfb x))
```

## Depends on

- [The spectral theorem, stated](../part-02/unbounded-selfadjointspectraltheorem.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/SpectralIntegral/Construction.lean)
