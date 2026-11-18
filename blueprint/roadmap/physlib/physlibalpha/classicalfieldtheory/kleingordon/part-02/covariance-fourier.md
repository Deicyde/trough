---
declaration: module
origin: cited
lean: KleinGordon.lorentzSplit, KleinGordon.lorentzSplit_apply, KleinGordon.abs_det_lorentzSplit, KleinGordon.freqAct, KleinGordon.freqAct_apply, KleinGordon.fourier_freqAct, KleinGordon.partSource, KleinGordon.partSource_apply
statement: formalized
proof: formalized
---

# Lorentz covariance of the causal kernel on the Fourier side

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.Covariance.Fourier`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean): 20 declarations, 12 with a docstring.

> The Fourier transform of the causal propagator kernel is invariant under orthochronous Lorentz
> transformations acting on the frequencies by the inverse transpose. It is odd under the others.

## i. Overview

> The covariance of the causal kernel is proved on test functions (`causalKernel_actDist`). Density
> carries it to the tempered extension. The Fourier transform of a tempered functional `T` is
> `g ↦ T (𝓕 g)`. For a Lorentz transformation `Λ` the transform of `g ∘ (Λ⁻¹)ᵀ` is `𝓕 g ∘ Λ`
> because `|det Λ| = 1`. So a functional with `T (φ ∘ Λ) = c * T φ` has a transform with
> `T̂ (g ∘ (Λ⁻¹)ᵀ) = c * T̂ g`. No second Fourier theory enters. The transport is one lemma about
> any tempered functional.

## ii. Key results

> - `lorentzSplit` : a Lorentz transformation on the split space.
> - `freqAct` : the induced action on Schwartz functions of the frequency by `(Λ⁻¹)ᵀ`.
> - `fourierDist` : the Fourier transform of a tempered functional.
> - `fourierDist_freqAct` : covariance of a functional transports to its transform.
> - `temperedCausal` : the tempered causal propagator kernel.
> - `fourierDist_temperedCausal_freqAct` : the transform of the causal kernel is invariant under
>   orthochronous transformations.
> - `fourierDist_temperedCausal_freqAct_of_not` : it changes sign under the others.

## iv. References

> None.

## A. The action on frequencies

> - `lorentzSplit` : a Lorentz transformation on the split space.
> - `abs_det_lorentzSplit` : its determinant has absolute value one.
> - `freqAct` : the induced action on Schwartz functions of the frequency.
> - `fourier_freqAct` : the transform of the transformed function.

## B. Transport of covariance

> - `fourierDist` : the Fourier transform of a tempered functional.
> - `fourierDist_freqAct` : covariance of a functional transports to its transform.

## C. The tempered causal kernel

> - `temperedCausal` : the tempered causal propagator kernel.
> - `temperedCausal_comp` : its covariance on Schwartz functions.

## D. The causal kernel on the Fourier side

> - `fourierDist_temperedCausal_freqAct` : invariance under orthochronous transformations.
> - `fourierDist_temperedCausal_freqAct_of_not` : sign change under the others.

**`KleinGordon.lorentzSplit`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L86).

> A Lorentz transformation as a linear equivalence of the split space.

```lean
def lorentzSplit (Λ : LorentzGroup d) : SplitSpace d ≃L[ℝ] SplitSpace d
```

**`KleinGordon.lorentzSplit_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L89).

```lean
lemma lorentzSplit_apply (Λ : LorentzGroup d) (ξ : SplitSpace d) :
    lorentzSplit Λ ξ = (splitEquiv d).symm (lorentzCLE Λ (splitEquiv d ξ))
```

**`KleinGordon.abs_det_lorentzSplit`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L93).

> The determinant of a Lorentz transformation of the split space has absolute value one.

```lean
lemma abs_det_lorentzSplit (Λ : LorentzGroup d) :
    |LinearMap.det (lorentzSplit Λ : SplitSpace d →ₗ[ℝ] SplitSpace d)| = 1
```

**`KleinGordon.freqAct`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L102).

> **The action on frequencies.** A Lorentz transformation acts on Schwartz functions of the
> frequency by the inverse transpose.

```lean
def freqAct (Λ : LorentzGroup d) : 𝓢(SplitSpace d, ℂ) →L[ℂ] 𝓢(SplitSpace d, ℂ)
```

**`KleinGordon.freqAct_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L105).

```lean
lemma freqAct_apply (Λ : LorentzGroup d) (g : 𝓢(SplitSpace d, ℂ)) (ξ : SplitSpace d) :
    freqAct Λ g ξ = g (Fourier.invTranspose (lorentzSplit Λ) ξ)
```

**`KleinGordon.fourier_freqAct`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L109).

> **The transform of the transformed function.**

```lean
lemma fourier_freqAct (Λ : LorentzGroup d) (g : 𝓢(SplitSpace d, ℂ)) (ξ : SplitSpace d) :
    𝓕 (freqAct Λ g) ξ = 𝓕 g (lorentzSplit Λ ξ)
```

**`KleinGordon.partSource`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L118).

> The real or imaginary part of a complex Schwartz function of the split space as a real
> Schwartz function of spacetime.

```lean
def partSource (part : ℂ →L[ℝ] ℝ) : 𝓢(SplitSpace d, ℂ) →L[ℝ] 𝓢(SpaceTime d, ℝ)
```

**`KleinGordon.partSource_apply`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L122).

```lean
lemma partSource_apply (part : ℂ →L[ℝ] ℝ) (h : 𝓢(SplitSpace d, ℂ)) (x : SpaceTime d) :
    partSource part h x = part (h ((splitEquiv d).symm x))
```

**`KleinGordon.fourierDist`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L127).

> **The Fourier transform of a tempered functional.** It sends `g` to the functional applied to
> the real and the imaginary part of `𝓕 g`.

```lean
def fourierDist (T : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ) (g : 𝓢(SplitSpace d, ℂ)) : ℂ
```

**`KleinGordon.partSource_lorentz`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L130).

```lean
lemma partSource_lorentz (part : ℂ →L[ℝ] ℝ) (Λ : LorentzGroup d) (h : 𝓢(SplitSpace d, ℂ)) :
    partSource part (SchwartzMap.compCLMOfContinuousLinearEquiv ℂ (lorentzSplit Λ) h) =
      SchwartzMap.compCLMOfContinuousLinearEquiv ℝ (lorentzCLE Λ) (partSource part h)
```

**`KleinGordon.fourierDist_freqAct`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L138).

> **Covariance of a functional transports to its transform.** If `T (φ ∘ Λ) = c * T φ` then
> the transform of `T` at `g ∘ (Λ⁻¹)ᵀ` is `c` times its value at `g`.

```lean
lemma fourierDist_freqAct (T : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ) (Λ : LorentzGroup d) (c : ℝ)
    (hT : ∀ φ : 𝓢(SpaceTime d, ℝ),
      T (SchwartzMap.compCLMOfContinuousLinearEquiv ℝ (lorentzCLE Λ) φ) = c * T φ)
    (g : 𝓢(SplitSpace d, ℂ)) : fourierDist T (freqAct Λ g) = c * fourierDist T g
```

**`KleinGordon.temperedAdvanced`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L151).

> The advanced kernel as a tempered functional: the retarded one reflected through the origin.

```lean
def temperedAdvanced (d : ℕ) (m : ℝ) : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ
```

**`KleinGordon.temperedCausal`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L156).

> **The tempered causal propagator kernel.**

```lean
def temperedCausal (d : ℕ) (m : ℝ) : 𝓢(SpaceTime d, ℝ) →L[ℝ] ℝ
```

**`KleinGordon.compCLM_neg_ofTestFunction`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L159).

```lean
lemma compCLM_neg_ofTestFunction (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    SchwartzMap.compCLMOfContinuousLinearEquiv ℝ (ContinuousLinearEquiv.neg ℝ)
      (ofTestFunction φ) = ofTestFunction (actTestFunction (pointReflection 0)⁻¹ φ)
```

**`KleinGordon.temperedAdvanced_ofTestFunction`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L165).

```lean
lemma temperedAdvanced_ofTestFunction (m : ℝ) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    temperedAdvanced d m (ofTestFunction φ) = advancedPointSource m (0 : SpaceTime d) φ
```

**`KleinGordon.temperedCausal_ofTestFunction`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L175).

```lean
lemma temperedCausal_ofTestFunction (m : ℝ) (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    temperedCausal d m (ofTestFunction φ) = causalKernel m φ
```

**`KleinGordon.compCLM_lorentz_ofTestFunction`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L181).

```lean
lemma compCLM_lorentz_ofTestFunction (Λ : LorentzGroup d)
    (φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ)) :
    SchwartzMap.compCLMOfContinuousLinearEquiv ℝ (lorentzCLE Λ) (ofTestFunction φ) =
      ofTestFunction (actTestFunction (⟨0, Λ⟩ : PoincareGroup d)⁻¹ φ)
```

**`KleinGordon.temperedCausal_comp`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L192).

> **Covariance of the tempered causal kernel.** If the causal kernel on test functions picks up
> the factor `c` under `Λ` then so does its tempered extension on Schwartz functions.

```lean
lemma temperedCausal_comp (m : ℝ) (Λ : LorentzGroup d) (c : ℝ)
    (h : ∀ φ : 𝓓((⊤ : Opens (SpaceTime d)), ℝ),
      causalKernel m (actTestFunction (⟨0, Λ⟩ : PoincareGroup d)⁻¹ φ) = c * causalKernel m φ)
    (φ : 𝓢(SpaceTime d, ℝ)) :
    temperedCausal d m (SchwartzMap.compCLMOfContinuousLinearEquiv ℝ (lorentzCLE Λ) φ) =
      c * temperedCausal d m φ
```

**`KleinGordon.fourierDist_temperedCausal_freqAct`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L209).

> **The causal kernel on the Fourier side is Lorentz invariant.** Its transform is unchanged
> when an orthochronous Lorentz transformation acts on the frequencies by the inverse transpose.

```lean
lemma fourierDist_temperedCausal_freqAct (m : ℝ) {Λ : LorentzGroup d}
    (hΛ : LorentzGroup.IsOrthochronous Λ) (g : 𝓢(SplitSpace d, ℂ)) :
    fourierDist (temperedCausal d m) (freqAct Λ g) = fourierDist (temperedCausal d m) g
```

**`KleinGordon.fourierDist_temperedCausal_freqAct_of_not`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean#L221).

> **The causal kernel on the Fourier side is odd under time reversal.** Its transform changes
> sign when a non-orthochronous Lorentz transformation acts on the frequencies.

```lean
lemma fourierDist_temperedCausal_freqAct_of_not (m : ℝ) {Λ : LorentzGroup d}
    (hΛ : ¬ LorentzGroup.IsOrthochronous Λ) (g : 𝓢(SplitSpace d, ℂ)) :
    fourierDist (temperedCausal d m) (freqAct Λ g) = -fourierDist (temperedCausal d m) g
```

## Depends on

- [The causal propagator kernel](covariance-causalkernel.md)
- [The Fourier form of the tempered retarded kernel](retardedkernel-fourierform.md)
- [The Fourier transform under a linear change of variables](../../../mathematics/part-02/fourier/linearchange.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/Covariance/Fourier.lean)
