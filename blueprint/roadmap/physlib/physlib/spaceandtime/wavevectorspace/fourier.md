---
declaration: module
origin: cited
lean: WaveVectorSpace.fourierIntegral, WaveVectorSpace.fourierIntegral_def, WaveVectorSpace.fourierIntegral_eq, WaveVectorSpace.fourierIntegral_eq_smul_fourier_comp, WaveVectorSpace.fourierIntegralInv, WaveVectorSpace.fourierIntegralInv_def, WaveVectorSpace.fourierIntegralInv_eq, WaveVectorSpace.fourierIntegralInv_eq_smul_fourierInv_comp
statement: formalized
proof: formalized
---

# Fourier transforms between `Space` and `WaveVectorSpace`

The module `Physlib.SpaceAndTime.WaveVectorSpace.Fourier`, [Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean): 38 declarations (6 instances with no name), 20 with a docstring; 2 private, not shown.

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
>   \left(\frac{|b|}{(2\pi)^{1-a}}\right)^{d/2}
>   \int f(x)\,\mathrm{e}^{\mathrm{i}bk\cdot x} \,\mathrm{d}^dx
> \;,\qquad
> f(x) :=
>   \left(\frac{|b|}{(2\pi)^{1+a}}\right)^{d/2}
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
> - `fourierIntegral_deriv` / `fourierIntegralInv_deriv` : for a suitably nice function
>   `f : Space d → E` the Fourier integral of its `i`ᵗʰ derivative is `-b * I * k i` times its Fourier
>   integral, and similarly for functions `WaveVectorSpace d → E` and the inverse Fourier integral.
> - `fourierIntegralInv_fourierIntegral_eq` / `fourierIntegral_fourierIntegralInv_eq` :
>   for suitably nice functions `f : Space d → E` and `g : WaveVectorSpace d → E`,
>   the identities `fourierIntegralInv a b (fourierIntegral a b f) = f`
>   and `fourierIntegral a b (fourierIntegralInv a b g) = g`, respectively.

## iv. References

> The parametrization in terms of `a b : ℝ` follows that given here:
>
> * Weisstein, Eric W. "Fourier Transform." From MathWorld--A Wolfram Resource.
>   [ref: mathworld\_fourier\_transform]

## A. Fourier integrals

### A.1. Two-parameter definitions

**`WaveVectorSpace.fourierIntegral`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L115).

> The Fourier integral over `Space`,
>
> `(|b| / (2 * π) ^ (1 - a)) ^ (d / 2 : ℝ) • ∫ x, exp (b * (k ⬝ᵥ x) * I) • f x ∂volume`,
>
> parametrized by `a b : ℝ`.

```lean
noncomputable def fourierIntegral (f : Space d → E) (k : WaveVectorSpace d) : E
```

**`WaveVectorSpace.fourierIntegral_def`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L119).

```lean
lemma fourierIntegral_def (f : Space d → E) :
    fourierIntegral a b f
      = (|b| / (2 * π) ^ (1 - a)) ^ (d / 2 : ℝ)
        • VectorFourier.fourierIntegral 𝐞 volume
          (-(b / (2 * π)) • pairingCLM.flip).toLinearMap₁₂ f
```

**`WaveVectorSpace.fourierIntegral_eq`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L126).

```lean
lemma fourierIntegral_eq (f : Space d → E) (k : WaveVectorSpace d) :
    fourierIntegral a b f k
      = (|b| / (2 * π) ^ (1 - a)) ^ (d / 2 : ℝ) • ∫ x : Space d, cexp (b * (k ⬝ᵥ x) * I) • f x
```

**`WaveVectorSpace.fourierIntegral_eq_smul_fourier_comp`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L136).

> Expresses the Fourier integral in terms of the Fourier transform on Euclidean space
> `𝓢 : (EuclideanSpace ℝ (Fin d) → E) → EuclideanSpace ℝ (Fin d) → E`
> by mapping through the standard bases of `Space d` and `WaveVectorSpace d`.

```lean
lemma fourierIntegral_eq_smul_fourier_comp (f : Space d → E) :
    fourierIntegral a b f
      = (|b| / (2 * π) ^ (1 - a)) ^ (d / 2 : ℝ)
        • 𝓕 (f ∘ Space.basis.repr.symm) ∘ (-(b / (2 * π)) • basis.repr.toLinearMap)
```

**`WaveVectorSpace.fourierIntegralInv`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L158).

> The inverse Fourier integral over `WaveVectorSpace`,
>
> `(|b| / (2 * π) ^ (1 + a)) ^ (d / 2 : ℝ) • ∫ k, exp (-b * (k ⬝ᵥ x) * I) • g k ∂volume`,
>
> parametrized by `a b : ℝ`.

```lean
noncomputable def fourierIntegralInv (g : WaveVectorSpace d → E) (x : Space d) : E
```

**`WaveVectorSpace.fourierIntegralInv_def`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L162).

```lean
lemma fourierIntegralInv_def (g : WaveVectorSpace d → E) :
    fourierIntegralInv a b g
      = (|b| / (2 * π) ^ (1 + a)) ^ (d / 2 : ℝ)
        • VectorFourier.fourierIntegral 𝐞 volume ((b / (2 * π)) • pairingCLM).toLinearMap₁₂ g
```

**`WaveVectorSpace.fourierIntegralInv_eq`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L168).

```lean
lemma fourierIntegralInv_eq (g : WaveVectorSpace d → E) (x : Space d) :
    fourierIntegralInv a b g x
      = (|b| / (2 * π) ^ (1 + a)) ^ (d / 2 : ℝ)
        • ∫ k : WaveVectorSpace d, cexp (-b * (k ⬝ᵥ x) * I) • g k
```

**`WaveVectorSpace.fourierIntegralInv_eq_smul_fourierInv_comp`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L179).

> Expresses the inverse Fourier integral in terms of the inverse Fourier transform
> on Euclidean space `𝓢 : (EuclideanSpace ℝ (Fin d) → E) → EuclideanSpace ℝ (Fin d) → E`
> by mapping through the standard bases of `Space d` and `WaveVectorSpace d`.

```lean
lemma fourierIntegralInv_eq_smul_fourierInv_comp (g : WaveVectorSpace d → E) :
    fourierIntegralInv a b g
      = (|b| / (2 * π) ^ (1 + a)) ^ (d / 2 : ℝ)
        • 𝓕⁻ (g ∘ basis.repr.symm) ∘ (-(b / (2 * π)) • Space.basis.repr.toLinearMap)
```

### A.2. Basic properties

**`WaveVectorSpace.fourierIntegral_congr_ae`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L200).

```lean
lemma fourierIntegral_congr_ae {f₁ f₂ : Space d → E} (hf : f₁ =ᵐ[volume] f₂) :
    fourierIntegral a b f₁ = fourierIntegral a b f₂
```

**`WaveVectorSpace.fourierIntegralInv_congr_ae`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L204).

```lean
lemma fourierIntegralInv_congr_ae {g₁ g₂ : WaveVectorSpace d → E} (hg : g₁ =ᵐ[volume] g₂) :
    fourierIntegralInv a b g₁ = fourierIntegralInv a b g₂
```

#### A.2.1. Linearity

**`WaveVectorSpace.fourierIntegral_const_smul`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L213).

```lean
lemma fourierIntegral_const_smul (f : Space d → E) (c : ℂ) :
    fourierIntegral a b (c • f) = c • fourierIntegral a b f
```

**`WaveVectorSpace.fourierIntegralInv_const_smul`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L217).

```lean
lemma fourierIntegralInv_const_smul (f : WaveVectorSpace d → E) (c : ℂ) :
    fourierIntegralInv a b (c • f) = c • fourierIntegralInv a b f
```

**`WaveVectorSpace.fourierIntegral_add`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L221).

```lean
lemma fourierIntegral_add {f₁ f₂ : Space d → E} (hf₁ : Integrable f₁) (hf₂ : Integrable f₂) :
    fourierIntegral a b (f₁ + f₂) = fourierIntegral a b f₁ + fourierIntegral a b f₂
```

**`WaveVectorSpace.fourierIntegralInv_add`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L227).

```lean
lemma fourierIntegralInv_add
    {g₁ g₂ : WaveVectorSpace d → E} (hg₁ : Integrable g₁) (hg₂ : Integrable g₂) :
    fourierIntegralInv a b (g₁ + g₂) = fourierIntegralInv a b g₁ + fourierIntegralInv a b g₂
```

#### A.2.2. Continuity

**`WaveVectorSpace.fourierIntegral_continuous`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L238).

```lean
lemma fourierIntegral_continuous {f : Space d → E} (hf : Integrable f) :
    Continuous (fourierIntegral a b f)
```

**`WaveVectorSpace.fourierIntegralInv_continuous`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L243).

```lean
lemma fourierIntegralInv_continuous {g : WaveVectorSpace d → E} (hg : Integrable g) :
    Continuous (fourierIntegralInv a b g)
```

#### A.2.3. Integration of continuous linear maps

**`WaveVectorSpace.fourierIntegral_continuousLinearMap_apply`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L259).

> Given a CLM-valued function of space, `f : Space d → F →L[ℝ] E`,
> evaluating its Fourier integral at `v : F` is the same as taking
> the Fourier integral of `x ↦ f x v`.

```lean
lemma fourierIntegral_continuousLinearMap_apply
    {f : Space d → F →L[ℝ] E} (hf : Integrable f) (k : WaveVectorSpace d) (v : F) :
    fourierIntegral a b f k v = fourierIntegral a b (f · v) k
```

**`WaveVectorSpace.fourierIntegralInv_continuousLinearMap_apply`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L268).

> Given a CLM-valued function of wavevector, `g : WaveVectorSpace d → F →L[ℝ] E`,
> evaluating its inverse Fourier integral at `v : F` is the same as taking
> the inverse Fourier integral of `k ↦ g k v`.

```lean
lemma fourierIntegralInv_continuousLinearMap_apply
    {g : WaveVectorSpace d → F →L[ℝ] E} (hg : Integrable g) (x : Space d) (v : F) :
    fourierIntegralInv a b g x v = fourierIntegralInv a b (g · v) x
```

### A.3. Derivatives

#### A.3.1. Fréchet derivatives

**`WaveVectorSpace.fderiv_fourierIntegral`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L284).

```lean
lemma fderiv_fourierIntegral
    {f : Space d → E} (hf : Integrable f) (hf' : Integrable fun x ↦ ‖x‖ * ‖f x‖) :
    fderiv ℝ (fourierIntegral a b f)
      = fourierIntegral a b (fun x ↦ (b * I) • x.dual.smulRight (f x))
```

**`WaveVectorSpace.fderiv_fourierIntegralInv`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L295).

```lean
lemma fderiv_fourierIntegralInv
    {g : WaveVectorSpace d → E} (hg : Integrable g) (hg' : Integrable (fun k ↦ ‖k‖ * ‖g k‖)) :
    fderiv ℝ (fourierIntegralInv a b g)
      = fourierIntegralInv a b (fun k ↦ -(b * I) • k.dual.smulRight (g k))
```

**`WaveVectorSpace.fourierIntegral_fderiv`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L307).

```lean
lemma fourierIntegral_fderiv {f : Space d → E} (hf : Integrable f) (hf' : Differentiable ℝ f)
    (hf'' : Integrable (fderiv ℝ f)) (k : WaveVectorSpace d) :
    fourierIntegral a b (fderiv ℝ f) k = -(b * I) • k.dual.smulRight (fourierIntegral a b f k)
```

**`WaveVectorSpace.fourierIntegralInv_fderiv`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L315).

```lean
lemma fourierIntegralInv_fderiv {g : WaveVectorSpace d → E}
    (hg : Integrable g) (hg' : Differentiable ℝ g) (hg'' : Integrable (fderiv ℝ g)) (x : Space d) :
    fourierIntegralInv a b (fderiv ℝ g) x
      = (b * I) • x.dual.smulRight (fourierIntegralInv a b g x)
```

#### A.3.2. Partial derivatives

**`WaveVectorSpace.deriv_fourierIntegral`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L330).

> The partial derivative of the Fourier transform of `f` along coordinate `i`
> is the Fourier transform of `x ↦ (b * I * x i) • f x`, provided both integrals exist.

```lean
lemma deriv_fourierIntegral (i : Fin d)
    {f : Space d → E} (hf : Integrable f) (hf' : Integrable fun x ↦ ‖x‖ * ‖f x‖) :
    ∂[i] (fourierIntegral a b f) = fourierIntegral a b fun x ↦ (b * I * x i) • f x
```

**`WaveVectorSpace.deriv_fourierIntegralInv`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L341).

> The partial derivative of the inverse Fourier transform of `g` along coordinate `i`
> is the inverse Fourier transform of `k ↦ (-b * I * k i) • g k`, provided both integrals exist.

```lean
lemma deriv_fourierIntegralInv (i : Fin d)
    {g : WaveVectorSpace d → E} (hg : Integrable g) (hg' : Integrable fun k ↦ ‖k‖ * ‖g k‖) :
    ∂[i] (fourierIntegralInv a b g) = fourierIntegralInv a b fun k ↦ -(b * I * k i) • g k
```

**`WaveVectorSpace.fourierIntegral_deriv`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L354).

> The Fourier transform of the partial derivative of `f` along coordinate `i`
> is `-b * I * kᵢ` times the Fourier transform of `f`.
>
> That is, the Fourier transform maps derivatives to multiplication.

```lean
lemma fourierIntegral_deriv (i : Fin d) {f : Space d → E}
    (hf : Integrable f) (hf' : Differentiable ℝ f) (hf'' : Integrable (fderiv ℝ f)) :
    fourierIntegral a b (∂[i] f) = -(b * I) • coord i • fourierIntegral a b f
```

**`WaveVectorSpace.fourierIntegralInv_deriv`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L365).

> The inverse Fourier transform of the partial derivative of `g` along coordinate `i`
> is `b * I * xᵢ` times the inverse Fourier transform of `g`.
>
> That is, the inverse Fourier transform maps derivatives to multiplication.

```lean
lemma fourierIntegralInv_deriv (i : Fin d) {g : WaveVectorSpace d → E}
    (hg : Integrable g) (hg' : Differentiable ℝ g) (hg'' : Integrable (fderiv ℝ g)) :
    fourierIntegralInv a b (∂[i] g) = (b * I) • Space.coord i • fourierIntegralInv a b g
```

#### A.3.3. (Continuous) differentiability

**`WaveVectorSpace.differentiable_fourierIntegral`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L379).

> If both `f` and `‖x‖ * ‖f x‖` are integrable,
> then the Fourier integral of `f` is differentiable.

```lean
lemma differentiable_fourierIntegral
    {f : Space d → E} (hf : Integrable f) (hf' : Integrable fun x ↦ ‖x‖ * ‖f x‖) :
    Differentiable ℝ (fourierIntegral a b f)
```

**`WaveVectorSpace.differentiable_fourierIntegralInv`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L386).

> If both `g` and `‖k‖ * ‖g k‖` are integrable,
> then the inverse Fourier integral of `g` is differentiable.

```lean
lemma differentiable_fourierIntegralInv
    {g : WaveVectorSpace d → E} (hg : Integrable g) (hg' : Integrable fun k ↦ ‖k‖ * ‖g k‖) :
    Differentiable ℝ (fourierIntegralInv a b g)
```

**`WaveVectorSpace.contDiff_fourierIntegral`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L392).

> If `‖x‖^n * ‖f x‖` is integrable for all `n ≤ N`, then the Fourier integral of `f` is `C^N`.

```lean
lemma contDiff_fourierIntegral {f : Space d → E} {N : ℕ∞}
    (hf : ∀ (n : ℕ), n ≤ N → Integrable (fun x ↦ ‖x‖ ^ n * ‖f x‖)) :
    ContDiff ℝ N (fourierIntegral a b f)
```

**`WaveVectorSpace.contDiff_fourierIntegralInv`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L399).

> If `‖k‖^n * ‖g k‖` is integrable for all `n ≤ N`,
> then the inverse Fourier integral of `g` is `C^N`.

```lean
lemma contDiff_fourierIntegralInv {g : WaveVectorSpace d → E} {N : ℕ∞}
    (hg : ∀ (n : ℕ), n ≤ N → Integrable (fun k ↦ ‖k‖ ^ n * ‖g k‖)) :
    ContDiff ℝ N (fourierIntegralInv a b g)
```

### A.4. Inversion

**An instance with no name**, [line 412](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L412).

```lean
local instance : FourierSMul ℝ (ℝᵈ → E) (ℝᵈ → E)
```

**An instance with no name**, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L415).

```lean
local instance : FourierInvSMul ℝ (ℝᵈ → E) (ℝᵈ → E)
```

**`WaveVectorSpace.fourierIntegralInv_fourierIntegral_eq`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L436).

> The Fourier inversion formula:
> `𝓕⁻ (𝓕 f) = f` for a suitably nice function `f : Space d → E`.

```lean
lemma fourierIntegralInv_fourierIntegral_eq (hb : b ≠ 0) [CompleteSpace E] {f : Space d → E}
    (h : Continuous f) (hf : Integrable f) (hf' : Integrable (fourierIntegral a b f)) :
    fourierIntegralInv a b (fourierIntegral a b f) = f
```

**`WaveVectorSpace.fourierIntegral_fourierIntegralInv_eq`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L479).

> The Fourier inversion formula:
> `𝓕 (𝓕⁻ g) = g` for a suitably nice function `g : WaveVectorSpace d → E`.

```lean
lemma fourierIntegral_fourierIntegralInv_eq
    (hb : b ≠ 0) [CompleteSpace E] {g : WaveVectorSpace d → E}
    (h : Continuous g) (hg : Integrable g) (hg' : Integrable (fourierIntegralInv a b g)) :
    fourierIntegral a b (fourierIntegralInv a b g) = g
```

## B. Fourier instances

### B.1. `(a, b) = (0, 1)` (default)

> $$
> \tilde{f}(k) := \frac{1}{(2\pi)^{d/2}} \int f(x)\,\mathrm{e}^{\mathrm{i}k\cdot x} \,\mathrm{d}x
> \;,\qquad
> f(x) := \frac{1}{(2\pi)^{d/2}} \int \tilde{f}(k)\,\mathrm{e}^{-\mathrm{i}k\cdot x} \,\mathrm{d}k
> $$

**An instance with no name**, [line 551](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L551).

> Notation for the Fourier transform `fourierIntegral 0 1`.

```lean
scoped instance : FourierTransform (Space d → E) (WaveVectorSpace d → E)
```

**An instance with no name**, [line 555](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L555).

> Notation for the inverse Fourier transform `fourierIntegralInv 0 1`.

```lean
scoped instance : FourierTransformInv (WaveVectorSpace d → E) (Space d → E)
```

### B.2. `(a, b) = (1, -1)`

> $$
> \tilde{f}(k) := \int f(x)\,\mathrm{e}^{-\mathrm{i}k\cdot x} \,\mathrm{d}x
> \;,\qquad
> f(x) := \frac{1}{(2\pi)^d} \int \tilde{f}(k)\,\mathrm{e}^{\mathrm{i}k\cdot x} \,\mathrm{d}k
> $$

**An instance with no name**, [line 572](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L572).

> Notation for the Fourier transform `fourierIntegral 1 (-1)`.

```lean
scoped instance : FourierTransform (Space d → E) (WaveVectorSpace d → E)
```

**An instance with no name**, [line 576](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean#L576).

> Notation for the inverse Fourier transform `fourierIntegralInv 1 (-1)`.

```lean
scoped instance : FourierTransformInv (WaveVectorSpace d → E) (Space d → E)
```

## Depends on

- [Duality of `Space` and `WaveVectorSpace`](dualpairing.md)

## Sources

- [Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Fourier.lean)
