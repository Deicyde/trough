---
declaration: module
origin: cited
lean: FourierMultiplier.hasTemperateGrowth_comp_of_bounded, FourierMultiplier.fourierMultiplierCLM_add, FourierMultiplier.multiplier_comm, FourierMultiplier.multiplier_apply_eq, FourierMultiplier.hasDerivAt_multiplierFamily, FourierMultiplier.lineDeriv_fourierMultiplier, FourierMultiplier.continuous_multiplierFamily_apply, FourierMultiplier.hasLineDerivAt_lineDerivOp
statement: formalized
proof: formalized
---

# Fourier multipliers on Schwartz functions

The module `PhyslibAlpha.Mathematics.Distribution.FourierMultiplier`, [PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean): 11 declarations, 8 with a docstring.

> Sums and commutation of Fourier multipliers and their derivatives in a parameter.

## i. Overview

> Sums and commutation of Fourier multipliers and their derivatives in a parameter. Compositions with
> bounded smooth functions have temperate growth.

## ii. Key results

> - `continuous_multiplierFamily_apply` : The evolution of fixed Schwartz data is jointly continuous
>   in time and position, for every multiplier family that is jointly continuous and locally dominated
>   against the Fourier transform of the data.
> - `hasTemperateGrowth_comp_of_bounded` : Composition of a smooth function with bounded derivatives
>   on `[0, ∞)` with a nonnegative function of temperate growth has temperate growth.
> - `functional_fourier` : A continuous linear functional commutes with the Fourier transform of a
>   Schwartz function.
> - `hasDerivAt_multiplierFamily` : Differentiation in time of a family of Fourier multipliers, under
>   the Fourier integral.

## iv. References

> None.

## A. The Klein–Gordon propagation multiplier

> Lemmas: `hasTemperateGrowth_comp_of_bounded`.

## B. The free Klein–Gordon evolution and its group law

> Lemmas: `fourierMultiplierCLM_add`.

## C. The free Klein–Gordon evolution as a one-parameter group

> Lemmas: `multiplier_comm`.

## D. The homogeneous Klein–Gordon evolution of Schwartz data

> Lemmas: `multiplier_apply_eq`, `hasDerivAt_multiplierFamily`, `lineDeriv_fourierMultiplier`,
> `continuous_multiplierFamily_apply`.

## E. Finite propagation speed for the homogeneous Klein–Gordon evolution

> Lemmas: `hasLineDerivAt_lineDerivOp`, `functional_fourier`, `integrable_fourier_integrand`.

## F. The retarded solution as a tempered distribution in space

> Lemmas: `fourier_smul_fourierInv_of_even`.

**`FourierMultiplier.hasTemperateGrowth_comp_of_bounded`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L90).

> Composition of a smooth function with bounded derivatives on `[0, ∞)` with a nonnegative
> function of temperate growth has temperate growth.

```lean
lemma hasTemperateGrowth_comp_of_bounded {g : ℝ → ℝ} (hg : ContDiff ℝ ∞ g) {C : ℝ}
    (hC : ∀ n : ℕ, ∀ y : ℝ, 0 ≤ y → |iteratedDeriv n g y| ≤ C) {q : E → ℝ}
    (hq : q.HasTemperateGrowth) (hq0 : ∀ ξ, 0 ≤ q ξ) : (fun ξ => g (q ξ)).HasTemperateGrowth
```

**`FourierMultiplier.fourierMultiplierCLM_add`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L110).

```lean
lemma fourierMultiplierCLM_add {g₁ g₂ : E → ℂ} (h₁ : g₁.HasTemperateGrowth)
    (h₂ : g₂.HasTemperateGrowth) (f : 𝓢(E, F)) :
    SchwartzMap.fourierMultiplierCLM F (g₁ + g₂) f =
      SchwartzMap.fourierMultiplierCLM F g₁ f + SchwartzMap.fourierMultiplierCLM F g₂ f
```

**`FourierMultiplier.multiplier_comm`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L120).

```lean
lemma multiplier_comm {g₁ g₂ : E → ℂ} (h₁ : g₁.HasTemperateGrowth) (h₂ : g₂.HasTemperateGrowth)
    (f : 𝓢(E, F)) :
    SchwartzMap.fourierMultiplierCLM F g₁ (SchwartzMap.fourierMultiplierCLM F g₂ f) =
      SchwartzMap.fourierMultiplierCLM F g₂ (SchwartzMap.fourierMultiplierCLM F g₁ f)
```

**`FourierMultiplier.multiplier_apply_eq`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L135).

> The pointwise Fourier integral of a Fourier multiplier with temperate growth.

```lean
lemma multiplier_apply_eq {g : E → ℂ} (hg : g.HasTemperateGrowth) (a : 𝓢(E, F)) (x : E) :
    SchwartzMap.fourierMultiplierCLM F g a x =
      ∫ ξ : E, (𝐞 (inner ℝ ξ x) : ℂ) • (g ξ • 𝓕 a ξ)
```

**`FourierMultiplier.hasDerivAt_multiplierFamily`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L144).

> Differentiation in time of a family of Fourier multipliers, under the Fourier integral.

```lean
lemma hasDerivAt_multiplierFamily (a : 𝓢(E, F)) (x : E) (gfam gfam' : ℝ → E → ℂ)
    (hg : ∀ r, (gfam r).HasTemperateGrowth) (hg' : ∀ r, (gfam' r).HasTemperateGrowth)
    (hd : ∀ ξ r, HasDerivAt (fun r' => gfam r' ξ) (gfam' r ξ) r) (τ : ℝ)
    (B : E → ℝ) (hB : MeasureTheory.Integrable B MeasureTheory.volume)
    (hb : ∀ ξ r, r ∈ Metric.ball τ 1 → ‖gfam' r ξ‖ * ‖𝓕 a ξ‖ ≤ B ξ) :
    HasDerivAt (fun r => SchwartzMap.fourierMultiplierCLM F (gfam r) a x)
      (SchwartzMap.fourierMultiplierCLM F (gfam' τ) a x) τ
```

**`FourierMultiplier.lineDeriv_fourierMultiplier`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L182).

> Directional derivatives of Schwartz functions commute with Fourier multipliers.

```lean
lemma lineDeriv_fourierMultiplier {g : E → ℂ} (hg : g.HasTemperateGrowth) (m : E)
    (f : 𝓢(E, F)) :
    ∂_{m} (SchwartzMap.fourierMultiplierCLM F g f) =
      SchwartzMap.fourierMultiplierCLM F g (∂_{m} f)
```

**`FourierMultiplier.continuous_multiplierFamily_apply`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L202).

> The evolution of fixed Schwartz data is jointly continuous in time and position, for every
> multiplier family that is jointly continuous and locally dominated against the Fourier transform of
> the data.

```lean
lemma continuous_multiplierFamily_apply (a : 𝓢(E, F)) (g : ℝ → E → ℂ)
    (hg : Continuous fun p : ℝ × E => g p.1 p.2) (hgt : ∀ r, (g r).HasTemperateGrowth)
    (hb : ∀ R : ℝ, ∃ q : E → ℝ, MeasureTheory.Integrable q MeasureTheory.volume ∧
      ∀ r ξ, |r| ≤ R → ‖g r ξ‖ * ‖𝓕 a ξ‖ ≤ q ξ) :
    Continuous fun p : ℝ × E => SchwartzMap.fourierMultiplierCLM F (g p.1) a p.2
```

**`FourierMultiplier.hasLineDerivAt_lineDerivOp`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L237).

```lean
lemma hasLineDerivAt_lineDerivOp (f : 𝓢(E, ℂ)) (m x : E) :
    HasLineDerivAt ℝ (⇑f) (∂_{m} f x) x m
```

**`FourierMultiplier.functional_fourier`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L249).

> A continuous linear functional commutes with the Fourier transform of a Schwartz function.

```lean
lemma functional_fourier (ℓ : F →L[ℂ] ℂ) (g : 𝓢(E, F)) (ξ : E) :
    ℓ (𝓕 g ξ) = 𝓕 (SchwartzMap.postcompCLM (𝕜 := ℂ) (E := E) ℓ g) ξ
```

**`FourierMultiplier.integrable_fourier_integrand`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L266).

> The Fourier integrand of a multiplier applied to Schwartz data is integrable.

```lean
lemma integrable_fourier_integrand {g : E → ℂ} (hg : g.HasTemperateGrowth) (a : 𝓢(E, F)) (x : E) :
    MeasureTheory.Integrable (fun ξ : E => (𝐞 (inner ℝ ξ x) : ℂ) • (g ξ • 𝓕 a ξ))
      MeasureTheory.volume
```

**`FourierMultiplier.fourier_smul_fourierInv_of_even`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean#L284).

> An even multiplier acts the same on a function and on its transpose.

```lean
lemma fourier_smul_fourierInv_of_even {G : Type*} [NormedAddCommGroup G] [NormedSpace ℂ G]
    (m : E → ℂ) (hm : ∀ x, m (-x) = m x) (g : E → G) (y : E) :
    𝓕 (fun x => m x • 𝓕⁻ g x) y = 𝓕⁻ (fun x => m x • 𝓕 g x) y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/FourierMultiplier.lean)
