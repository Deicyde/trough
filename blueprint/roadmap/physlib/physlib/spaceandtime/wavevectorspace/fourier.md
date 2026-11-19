---
declaration: module
origin: cited
lean: WaveVectorSpace.fourierIntegral, WaveVectorSpace.fourierIntegral_def, WaveVectorSpace.fourierIntegral_eq, WaveVectorSpace.fourierIntegralInv, WaveVectorSpace.fourierIntegralInv_def, WaveVectorSpace.fourierIntegralInv_eq, WaveVectorSpace.fourierIntegral_congr_ae, WaveVectorSpace.fourierIntegralInv_congr_ae
statement: formalized
proof: formalized
---

# Fourier transforms between `Space` and `WaveVectorSpace`

The module `Physlib.SpaceAndTime.WaveVectorSpace.Fourier`, [Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean): 36 declarations (4 instances with no name), 12 with a docstring.

## i. Overview

> The purpose of this module is to provide a means to work with Fourier transforms in a way
> that is both dimensionally consistent and flexible enough to allow various conventions.
>
> The two main definitions are `fourierIntegral a b : (Space d → E) → WaveVectorSpace d → E`
> and `fourierIntegralInv a b : (WaveVectorSpace d → E) → Space d → E` which amount to the following
> integral transformations depending on two parameters `a b : ℝ`:
>
> $$
> \tilde{f}(k) :=
>   \sqrt{\frac{|b|}{(2\pi)^{1-a}}}
>   \int f(x)\,\mathrm{e}^{\mathrm{i}bk\cdot x} \,\mathrm{d}^dx
> \;,\qquad
> f(x) :=
>   \sqrt{\frac{|b|}{(2\pi)^{1+a}}}
>   \int \tilde{f}(k)\,\mathrm{e}^{-\mathrm{i}bk\cdot x} \,\mathrm{d}^dk
> \;.
> $$
>
> These are implemented as rescaled/dilated versions of `VectorFourier.fourierIntegral`
> and most results require that the input function be integrable.
>
> Results which hold for all `a` and `b` should be written in terms of `fourierIntegral a b`.
> Opening the `FourierTransform` namespace allows one to use the notation `𝓕` and `𝓕⁻`
> with default values $(a,b) = (0,1)$; to use this notation with a different convention include
> the line `open scoped FourierTransform[a][b]` (*e.g.* `open scoped FourierTransform1n1`
> for $(a,b) = (1,-1)$). If a common convention is missing it can be added below in section B.

## ii. Key results

> - `fourierIntegral a b` : the Fourier integral with real parameters `a` and `b`,
>   corresponding to a choice of convention, which maps a function `f : Space d → E`
>   to its Fourier transform of type `WaveVectorSpace d → E`.
> - `fourierIntegralInv a b` : the inverse Fourier integral with real parameters `a` and `b`,
>   corresponding to a choice of convention, which maps a function `g : WaveVectorSpace d → E`
>   to its Fourier transform of type `Space d → E`.
> - `deriv_fourierIntegral` / `deriv_fourierIntegralInv` : for a suitably nice function
>   `f : Space d → E` the derivative along the `i`ᵗʰ coordinate direction of its Fourier integral
>   is the Fourier integral of the function `x ↦ (b * I * x i) • f x`, and similarly for functions
>   `WaveVectorSpace d → E` and the inverse Fourier integral.

## iv. References

> The parametrization in terms of `a b : ℝ` follows that given here:
>
> * Weisstein, Eric W. "Fourier Transform." From MathWorld--A Wolfram Resource.
>   [ref: mathworld\_fourier\_transform]

## A. Fourier integrals

### A.1. Two-parameter definitions

**`WaveVectorSpace.fourierIntegral`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L107).

> The Fourier integral over `Space`,
>
> `√(|b| / (2 * π) ^ (1 - a)) • ∫ x, exp (b * (k ⬝ᵥ x) * I) • f x ∂volume`,
>
> parametrized by `a b : ℝ`.

```lean
noncomputable def fourierIntegral (f : Space d → E) (k : WaveVectorSpace d) : E
```

**`WaveVectorSpace.fourierIntegral_def`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L111).

```lean
lemma fourierIntegral_def (f : Space d → E) :
    fourierIntegral a b f
      = √(|b| / (2 * π) ^ (1 - a))
        • VectorFourier.fourierIntegral 𝐞 volume
          (-(b / (2 * π)) • pairingCLM.flip).toLinearMap₁₂ f
```

**`WaveVectorSpace.fourierIntegral_eq`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L118).

```lean
lemma fourierIntegral_eq (f : Space d → E) (k : WaveVectorSpace d) :
    fourierIntegral a b f k
      = √(|b| / (2 * π) ^ (1 - a)) • ∫ x : Space d, cexp (b * (k ⬝ᵥ x) * I) • f x
```

**`WaveVectorSpace.fourierIntegralInv`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L130).

> The inverse Fourier integral over `WaveVectorSpace`,
>
> `√(|b| / (2 * π) ^ (1 + a)) • ∫ k, exp (-b * (k ⬝ᵥ x) * I) • g k ∂volume`,
>
> parametrized by `a b : ℝ`.

```lean
noncomputable def fourierIntegralInv (g : WaveVectorSpace d → E) (x : Space d) : E
```

**`WaveVectorSpace.fourierIntegralInv_def`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L134).

```lean
lemma fourierIntegralInv_def (g : WaveVectorSpace d → E) :
    fourierIntegralInv a b g
      = √(|b| / (2 * π) ^ (1 + a))
        • VectorFourier.fourierIntegral 𝐞 volume ((b / (2 * π)) • pairingCLM).toLinearMap₁₂ g
```

**`WaveVectorSpace.fourierIntegralInv_eq`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L140).

```lean
lemma fourierIntegralInv_eq (g : WaveVectorSpace d → E) (x : Space d) :
    fourierIntegralInv a b g x
      = √(|b| / (2 * π) ^ (1 + a)) • ∫ k : WaveVectorSpace d, cexp (-b * (k ⬝ᵥ x) * I) • g k
```

### A.2. Basic properties

**`WaveVectorSpace.fourierIntegral_congr_ae`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L150).

```lean
lemma fourierIntegral_congr_ae {f₁ f₂ : Space d → E} (hf : f₁ =ᵐ[volume] f₂) :
    fourierIntegral a b f₁ = fourierIntegral a b f₂
```

**`WaveVectorSpace.fourierIntegralInv_congr_ae`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L154).

```lean
lemma fourierIntegralInv_congr_ae {g₁ g₂ : WaveVectorSpace d → E} (hg : g₁ =ᵐ[volume] g₂) :
    fourierIntegralInv a b g₁ = fourierIntegralInv a b g₂
```

#### A.2.1. Linearity

**`WaveVectorSpace.fourierIntegral_const_smul`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L163).

```lean
lemma fourierIntegral_const_smul (f : Space d → E) (c : ℂ) :
    fourierIntegral a b (c • f) = c • fourierIntegral a b f
```

**`WaveVectorSpace.fourierIntegralInv_const_smul`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L167).

```lean
lemma fourierIntegralInv_const_smul (f : WaveVectorSpace d → E) (c : ℂ) :
    fourierIntegralInv a b (c • f) = c • fourierIntegralInv a b f
```

**`WaveVectorSpace.fourierIntegral_add`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L171).

```lean
lemma fourierIntegral_add {f₁ f₂ : Space d → E} (hf₁ : Integrable f₁) (hf₂ : Integrable f₂) :
    fourierIntegral a b (f₁ + f₂) = fourierIntegral a b f₁ + fourierIntegral a b f₂
```

**`WaveVectorSpace.fourierIntegralInv_add`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L177).

```lean
lemma fourierIntegralInv_add
    {g₁ g₂ : WaveVectorSpace d → E} (hg₁ : Integrable g₁) (hg₂ : Integrable g₂) :
    fourierIntegralInv a b (g₁ + g₂) = fourierIntegralInv a b g₁ + fourierIntegralInv a b g₂
```

#### A.2.2. Continuity

**`WaveVectorSpace.fourierIntegral_continuous`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L188).

```lean
lemma fourierIntegral_continuous {f : Space d → E} (hf : Integrable f) :
    Continuous (fourierIntegral a b f)
```

**`WaveVectorSpace.fourierIntegralInv_continuous`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L193).

```lean
lemma fourierIntegralInv_continuous {g : WaveVectorSpace d → E} (hg : Integrable g) :
    Continuous (fourierIntegralInv a b g)
```

#### A.2.3. Integration of continuous linear maps

**`WaveVectorSpace.fourierIntegral_continuousLinearMap_apply`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L209).

> Given a CLM-valued function of space, `f : Space d → F →L[ℝ] E`,
> evaluating its Fourier integral at `v : F` is the same as taking
> the Fourier integral of `x ↦ f x v`.

```lean
lemma fourierIntegral_continuousLinearMap_apply
    {f : Space d → F →L[ℝ] E} (hf : Integrable f) (k : WaveVectorSpace d) (v : F) :
    fourierIntegral a b f k v = fourierIntegral a b (f · v) k
```

**`WaveVectorSpace.fourierIntegralInv_continuousLinearMap_apply`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L218).

> Given a CLM-valued function of wavevector, `g : WaveVectorSpace d → F →L[ℝ] E`,
> evaluating its inverse Fourier integral at `v : F` is the same as taking
> the inverse Fourier integral of `k ↦ g k v`.

```lean
lemma fourierIntegralInv_continuousLinearMap_apply
    {g : WaveVectorSpace d → F →L[ℝ] E} (hg : Integrable g) (x : Space d) (v : F) :
    fourierIntegralInv a b g x v = fourierIntegralInv a b (g · v) x
```

### A.3. Derivatives

#### A.3.1. Fourier multipliers

**`WaveVectorSpace.fderivFourierIntegrand`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L237).

> Send a function `f : Space d → E` to the function `f : Space d → Hom (WaveVectorSpace d, E)`
> given by `x ↦ k ↦ b * I * (k ⬝ᵥ x) • f x`. This is designed so that the Fourier transform of
> `fderivFourierIntegrand b f` is the `fderiv` of the Fourier transform of `f`.

```lean
noncomputable def fderivFourierIntegrand (f : Space d → E) (x : Space d) :
    WaveVectorSpace d →L[ℝ] E
```

**`WaveVectorSpace.fderivFourierInvIntegrand`**, a def, [line 245](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L245).

> Send a function `g : WaveVectorSpace d → E` to the function
> `g : WaveVectorSpace d → Hom (Space d, E)` given by `k ↦ x ↦ -b * I * (k ⬝ᵥ x) • g k`.
> This is designed so that the inverse Fourier transform of `fderivFourierInvIntegrand b g`
> is the `fderiv` of the inverse Fourier transform of `g`.

```lean
noncomputable def fderivFourierInvIntegrand (g : WaveVectorSpace d → E) (k : WaveVectorSpace d) :
    Space d →L[ℝ] E
```

**`WaveVectorSpace.fderivFourierIntegrand_eq`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L249).

```lean
lemma fderivFourierIntegrand_eq (f : Space d → E) :
    fderivFourierIntegrand b f = fun x ↦ (b * I) • x.dual.smulRight (f x)
```

**`WaveVectorSpace.fderivFourierInvIntegrand_eq`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L253).

```lean
lemma fderivFourierInvIntegrand_eq (g : WaveVectorSpace d → E) :
    fderivFourierInvIntegrand b g = fun k ↦ -(b * I) • k.dual.smulRight (g k)
```

**`WaveVectorSpace.fderivFourierIntegrand_apply`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L258).

```lean
lemma fderivFourierIntegrand_apply (f : Space d → E) (x : Space d) (k : WaveVectorSpace d) :
    fderivFourierIntegrand b f x k = (b * I) • (k ⬝ᵥ x) • f x
```

**`WaveVectorSpace.fderivFourierInvIntegrand_apply`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L263).

```lean
lemma fderivFourierInvIntegrand_apply
    (g : WaveVectorSpace d → E) (k : WaveVectorSpace d) (x : Space d) :
    fderivFourierInvIntegrand b g k x = -(b * I) • (k ⬝ᵥ x) • g k
```

**`WaveVectorSpace.opNorm_fderivFourierIntegrand`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L269).

```lean
lemma opNorm_fderivFourierIntegrand (f : Space d → E) (x : Space d) :
    ‖fderivFourierIntegrand b f x‖ = |b| * ‖x‖ * ‖f x‖
```

**`WaveVectorSpace.opNorm_fderivFourierInvIntegrand`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L274).

```lean
lemma opNorm_fderivFourierInvIntegrand (g : WaveVectorSpace d → E) (k : WaveVectorSpace d) :
    ‖fderivFourierInvIntegrand b g k‖ = |b| * ‖k‖ * ‖g k‖
```

**`WaveVectorSpace.aestronglyMeasurable_fderivFourierIntegrand`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L279).

```lean
lemma aestronglyMeasurable_fderivFourierIntegrand {f : Space d → E} (hf : AEStronglyMeasurable f) :
    AEStronglyMeasurable (fderivFourierIntegrand b f)
```

**`WaveVectorSpace.aestronglyMeasurable_fderivFourierInvIntegrand`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L285).

```lean
lemma aestronglyMeasurable_fderivFourierInvIntegrand
    {g : WaveVectorSpace d → E} (hg : AEStronglyMeasurable g) :
    AEStronglyMeasurable (fderivFourierInvIntegrand b g)
```

**`WaveVectorSpace.integrable_fderivFourierIntegrand`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L291).

```lean
lemma integrable_fderivFourierIntegrand {f : Space d → E}
    (hf : AEStronglyMeasurable f) (hf' : Integrable fun x ↦ ‖x‖ * ‖f x‖) :
    Integrable (fderivFourierIntegrand b f)
```

**`WaveVectorSpace.integrable_fderivFourierInvIntegrand`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L296).

```lean
lemma integrable_fderivFourierInvIntegrand {g : WaveVectorSpace d → E}
    (hg : AEStronglyMeasurable g) (hg' : Integrable fun k ↦ ‖k‖ * ‖g k‖) :
    Integrable (fderivFourierInvIntegrand b g)
```

#### A.3.2. Fréchet derivatives

**`WaveVectorSpace.fderiv_fourierIntegral`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L305).

```lean
lemma fderiv_fourierIntegral
    {f : Space d → E} (hf : Integrable f) (hf' : Integrable fun x ↦ ‖x‖ * ‖f x‖) :
    fderiv ℝ (fourierIntegral a b f) = fourierIntegral a b (fderivFourierIntegrand b f)
```

**`WaveVectorSpace.fderiv_fourierIntegralInv`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L315).

```lean
lemma fderiv_fourierIntegralInv
    {g : WaveVectorSpace d → E} (hg : Integrable g) (hg' : Integrable (fun k ↦ ‖k‖ * ‖g k‖)) :
    fderiv ℝ (fourierIntegralInv a b g)
      = fourierIntegralInv a b (fderivFourierInvIntegrand b g)
```

#### A.3.3. Partial derivatives

**`WaveVectorSpace.deriv_fourierIntegral`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L333).

> The partial derivative of the Fourier transform of `f` along coordinate `i`
> is the Fourier transform of `x ↦ (b * I * x i) • f x`, provided both integrals exist.

```lean
lemma deriv_fourierIntegral (i : Fin d)
    {f : Space d → E} (hf : Integrable f) (hf' : Integrable fun x ↦ ‖x‖ * ‖f x‖) :
    ∂[i] (fourierIntegral a b f) = fourierIntegral a b fun x ↦ (b * I * x i) • f x
```

**`WaveVectorSpace.deriv_fourierIntegralInv`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L344).

> The partial derivative of the inverse Fourier transform of `g` along coordinate `i`
> is the inverse Fourier transform of `k ↦ (-b * I * k i) • g k`, provided both integrals exist.

```lean
lemma deriv_fourierIntegralInv (i : Fin d)
    {g : WaveVectorSpace d → E} (hg : Integrable g) (hg' : Integrable fun k ↦ ‖k‖ * ‖g k‖) :
    ∂[i] (fourierIntegralInv a b g) = fourierIntegralInv a b fun k ↦ -(b * I * k i) • g k
```

## B. Fourier instances

### B.1. `(a, b) = (0, 1)` (default)

> $$
> \tilde{f}(k) := \frac{1}{\sqrt{2\pi}} \int f(x)\,\mathrm{e}^{\mathrm{i}k\cdot x} \,\mathrm{d}x
> \;,\qquad
> f(x) := \frac{1}{\sqrt{2\pi}} \int \tilde{f}(k)\,\mathrm{e}^{-\mathrm{i}k\cdot x} \,\mathrm{d}k
> $$

**An instance with no name**, [line 380](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L380).

> Notation for the Fourier transform `fourierIntegral 0 1`.

```lean
scoped instance : FourierTransform (Space d → E) (WaveVectorSpace d → E)
```

**An instance with no name**, [line 384](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L384).

> Notation for the inverse Fourier transform `fourierIntegralInv 0 1`.

```lean
scoped instance : FourierTransformInv (WaveVectorSpace d → E) (Space d → E)
```

### B.2. `(a, b) = (1, -1)`

> $$
> \tilde{f}(k) := \int f(x)\,\mathrm{e}^{-\mathrm{i}k\cdot x} \,\mathrm{d}x
> \;,\qquad
> f(x) := \frac{1}{2\pi} \int \tilde{f}(k)\,\mathrm{e}^{\mathrm{i}k\cdot x} \,\mathrm{d}k
> $$

**An instance with no name**, [line 401](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L401).

> Notation for the Fourier transform `fourierIntegral 1 (-1)`.

```lean
scoped instance : FourierTransform (Space d → E) (WaveVectorSpace d → E)
```

**An instance with no name**, [line 405](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L405).

> Notation for the inverse Fourier transform `fourierIntegralInv 1 (-1)`.

```lean
scoped instance : FourierTransformInv (WaveVectorSpace d → E) (Space d → E)
```

## Depends on

- [Duality of `Space` and `WaveVectorSpace`](dualpairing.md)

## Sources

- [Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean)
