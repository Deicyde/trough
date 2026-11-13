---
declaration: module
origin: cited
lean: TauCeti.IsPositiveDefinite, TauCeti.IsPositiveDefinite.sum_nonneg, TauCeti.IsPositiveDefinite.quadForm_two_nonneg, TauCeti.IsPositiveDefinite.add_star_self_nonneg, TauCeti.IsPositiveDefinite.add_star_self_im, TauCeti.IsPositiveDefinite.add_star_self_re_nonneg, TauCeti.IsPositiveDefinite.map_zero_nonneg, TauCeti.IsPositiveDefinite.map_zero_im
statement: formalized
proof: formalized
---

# Positive-definite functions on an involutive additive monoid

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.Basic`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean): 25 declarations, 25 with a docstring.

> A complex-valued function `F` on an additive monoid `M` equipped with an involution `star` (an
> `AddMonoid` with a `StarAddMonoid` structure) is **positive definite** when, for every finite family
> `(cᵢ, aᵢ)` of scalars `cᵢ : ℂ` and points `aᵢ : M`, the Hermitian form `∑\_\{i,j} cᵢ · conj(cⱼ) · F(aᵢ
> + aⱼ⋆)` is a nonnegative real number.

## i. Overview

> A complex-valued function `F` on an additive monoid `M` equipped with an involution `star`
> (an `AddMonoid` with a `StarAddMonoid` structure) is **positive definite** when, for every
> finite family `(cᵢ, aᵢ)` of scalars `cᵢ : ℂ` and points `aᵢ : M`, the Hermitian form
> `∑_{i,j} cᵢ · conj(cⱼ) · F(aᵢ + aⱼ⋆)` is a nonnegative real number. The involution `aⱼ⋆` inside
> the argument is what makes this the right notion on an involutive semigroup (Berg–Christensen–
> Ressel): on a finite-dimensional real inner-product space with `a⋆ = -a` it specialises to the
> classical translation-invariant positive-definiteness `∑ cᵢ conj(cⱼ) F(aᵢ - aⱼ) ≥ 0`, and on the
> product monoid `ℝ≥0 × V` it produces the BCR involution `(t, a)⋆ = (t, -a)`.
>
> This file introduces the predicate `TauCeti.IsPositiveDefinite` at this general level and develops
> its basic algebraic API: the value at `0` is real and nonnegative, the function is conjugate
> symmetric in the involution, it satisfies the Cauchy–Schwarz inequality coming from the `2 × 2`
> sub-form, and the class is closed under sums and nonnegative complex scalar multiples, with the
> Schur pointwise product closure and nonnegative constants as examples.
>
> This is the `Objects` and first `API to develop` slice of Part C of the `OneParameterSemigroups`
> roadmap in TauCetiRoadmap: "positive-definite functions and Bochner's theorem". Mathlib has
> related APIs for positive-semidefinite matrices, bilinear and linear maps, and RKHS kernels, but
> not for positive-definite functions on an involutive monoid, so the predicate and its API are built
> here. The continuity theory and Bochner's representation theorem are later milestones.

## ii. Key results

> * `TauCeti.IsPositiveDefinite`: the positive-definiteness predicate for `F : M → ℂ`.
> * `TauCeti.IsPositiveDefinite.sum_nonneg`: nonnegativity for arbitrary finite families.
> * `TauCeti.IsPositiveDefinite.quadForm_two_nonneg`: nonnegativity of the `2 × 2` sub-form.
> * `TauCeti.IsPositiveDefinite.map_zero_nonneg`: `0 ≤ F 0`.
> * `TauCeti.IsPositiveDefinite.map_zero_im`: `(F 0).im = 0`.
> * `TauCeti.IsPositiveDefinite.map_zero_re_nonneg`: `0 ≤ (F 0).re`.
> * `TauCeti.IsPositiveDefinite.map_zero_eq_ofReal_re`: `F 0 = ((F 0).re : ℂ)`.
> * `TauCeti.IsPositiveDefinite.map_zero_re_pos_of_ne_zero`: if `F 0 ≠ 0`, then
>   `0 < (F 0).re`.
> * `TauCeti.IsPositiveDefinite.conj_symm`: `conj (F (b + a⋆)) = F (a + b⋆)`.
> * `TauCeti.IsPositiveDefinite.normSq_le`: the Cauchy–Schwarz inequality
>   `‖F (a + b⋆)‖² ≤ (F (a + a⋆)).re * (F (b + b⋆)).re`.
> * `TauCeti.IsPositiveDefinite.norm_apply_le_map_zero_re_of_add_star_eq_zero`: `‖F a‖ ≤ (F 0).re`
>   when `a + star a = 0`, with the additive-group corollary
>   `TauCeti.IsPositiveDefinite.norm_apply_le_map_zero_re_of_star_eq_neg` for `star a = -a`.
> * `TauCeti.IsPositiveDefinite.apply_eq_zero_of_map_zero_re_eq_zero`: `(F 0).re = 0` forces
>   `F` to vanish identically.
> * `TauCeti.IsPositiveDefinite.posSemidef`: a positive-definite function gives the
>   positive-definite kernel `fun a b => F (a + star b)`.
> * `TauCeti.IsPositiveDefinite.of_posSemidef`: conversely, if the kernel
>   `fun a b => F (a + star b)` is positive definite then `F` is positive definite.
> * `TauCeti.IsPositiveDefinite.add`, `TauCeti.IsPositiveDefinite.sum`,
>   `TauCeti.IsPositiveDefinite.const_mul`, `TauCeti.IsPositiveDefinite.mul`,
>   `TauCeti.IsPositiveDefinite.prod`, `TauCeti.isPositiveDefinite_const`: closure properties and
>   examples.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.

## A. Development

**`TauCeti.IsPositiveDefinite`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L94).

> A function `F : M → ℂ` on an involutive additive monoid is **positive definite** when, for
> every finite family of scalars `c : Fin n → ℂ` and points `v : Fin n → M`, the Hermitian form
> `∑_{i,j} c i · conj (c j) · F (v i + star (v j))` is a nonnegative real number (using the order on
> `ℂ` for which `0 ≤ z` means `z` is real and nonnegative).

```lean
def IsPositiveDefinite (F : M → ℂ) : Prop
```

**`TauCeti.IsPositiveDefinite.sum_nonneg`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L103).

> Positive-definiteness holds for an arbitrary finite index type, not just `Fin n`: for every
> finite family of scalars `c : ι → ℂ` and points `v : ι → M`, the Hermitian form
> `∑_{i,j} c i · conj (c j) · F (v i + star (v j))` is a nonnegative real number.

```lean
lemma sum_nonneg (hF : IsPositiveDefinite F) {ι : Type*} [Fintype ι] (c : ι → ℂ) (v : ι → M) :
    0 ≤ ∑ i, ∑ j, c i * conj (c j) * F (v i + star (v j))
```

**`TauCeti.IsPositiveDefinite.quadForm_two_nonneg`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L114).

> The `2 × 2` Hermitian sub-form of a positive-definite function at the points `a, b` with
> coefficients `c₀, c₁` is nonnegative.

```lean
lemma quadForm_two_nonneg (hF : IsPositiveDefinite F) (a b : M) (c₀ c₁ : ℂ) :
    0 ≤ c₀ * conj c₀ * F (a + star a) + c₀ * conj c₁ * F (a + star b)
      + c₁ * conj c₀ * F (b + star a) + c₁ * conj c₁ * F (b + star b)
```

**`TauCeti.IsPositiveDefinite.add_star_self_nonneg`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L123).

> A positive-definite function takes a real, nonnegative value at every "norm point"
> `a + star a`.

```lean
lemma add_star_self_nonneg (hF : IsPositiveDefinite F) (a : M) : 0 ≤ F (a + star a)
```

**`TauCeti.IsPositiveDefinite.add_star_self_im`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L129).

> The value of a positive-definite function at a "norm point" `a + star a` has zero imaginary
> part.

```lean
lemma add_star_self_im (hF : IsPositiveDefinite F) (a : M) : (F (a + star a)).im = 0
```

**`TauCeti.IsPositiveDefinite.add_star_self_re_nonneg`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L134).

> The value of a positive-definite function at a "norm point" `a + star a` has nonnegative real
> part.

```lean
lemma add_star_self_re_nonneg (hF : IsPositiveDefinite F) (a : M) : 0 ≤ (F (a + star a)).re
```

**`TauCeti.IsPositiveDefinite.map_zero_nonneg`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L138).

> The value of a positive-definite function at `0` is real and nonnegative.

```lean
lemma map_zero_nonneg (hF : IsPositiveDefinite F) : 0 ≤ F 0
```

**`TauCeti.IsPositiveDefinite.map_zero_im`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L143).

> The value of a positive-definite function at `0` has zero imaginary part.

```lean
lemma map_zero_im (hF : IsPositiveDefinite F) : (F 0).im = 0
```

**`TauCeti.IsPositiveDefinite.map_zero_re_nonneg`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L147).

> The real part of the value of a positive-definite function at `0` is nonnegative.

```lean
lemma map_zero_re_nonneg (hF : IsPositiveDefinite F) : 0 ≤ (F 0).re
```

**`TauCeti.IsPositiveDefinite.map_zero_eq_ofReal_re`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L152).

> The value at the origin of a positive-definite function is equal to the real number
> `(F 0).re`, viewed as a complex number.

```lean
lemma map_zero_eq_ofReal_re (hF : IsPositiveDefinite F) : F 0 = ((F 0).re : ℂ)
```

**`TauCeti.IsPositiveDefinite.map_zero_re_pos_of_ne_zero`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L159).

> If a positive-definite function is nonzero at the origin, then the real part of that value is
> strictly positive.

```lean
lemma map_zero_re_pos_of_ne_zero (hF : IsPositiveDefinite F) (h0 : F 0 ≠ 0) :
    0 < (F 0).re
```

**`TauCeti.IsPositiveDefinite.conj_symm`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L171).

> A positive-definite function is conjugate symmetric in the involution:
> `conj (F (b + star a)) = F (a + star b)`.

```lean
lemma conj_symm (hF : IsPositiveDefinite F) (a b : M) :
    conj (F (b + star a)) = F (a + star b)
```

**`TauCeti.IsPositiveDefinite.posSemidef`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L192).

> A positive-definite function `F` induces the positive-definite kernel `K(a, b) = F(a + b⋆)`.
> This is the forward half of the function ↔ kernel correspondence.

```lean
lemma posSemidef (hF : IsPositiveDefinite F) :
    Matrix.PosSemidef (fun a b => F (a + star b))
```

**`TauCeti.IsPositiveDefinite.of_posSemidef`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L205).

> If the kernel `K(a, b) = F(a + b⋆)` is positive definite, then so is the function `F`. This is
> the reverse half of the function ↔ kernel correspondence.

```lean
lemma of_posSemidef
    (hK : Matrix.PosSemidef (fun a b => F (a + star b))) : IsPositiveDefinite F
```

**`TauCeti.IsPositiveDefinite.normSq_le`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L217).

> The Cauchy–Schwarz inequality for a positive-definite function: the squared norm of an
> off-diagonal value is bounded by the product of the two diagonal values.

```lean
lemma normSq_le (hF : IsPositiveDefinite F) (a b : M) :
    Complex.normSq (F (a + star b))
      ≤ (F (a + star a)).re * (F (b + star b)).re
```

**`TauCeti.IsPositiveDefinite.norm_apply_le_map_zero_re_of_add_star_eq_zero`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L224).

> If `a + star a = 0`, then a positive-definite function is bounded at `a` by its value at
> zero.

```lean
lemma norm_apply_le_map_zero_re_of_add_star_eq_zero (hF : IsPositiveDefinite F)
    (a : M) (ha : a + star a = 0) : ‖F a‖ ≤ (F 0).re
```

**`TauCeti.IsPositiveDefinite.apply_eq_zero_of_map_zero_re_eq_zero`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L237).

> **A positive-definite function with `(F 0).re = 0` vanishes identically.**
>
> No hypothesis on the point is required, and none on the ambient structure beyond an
> involutive additive monoid (`AddMonoid` and `StarAddMonoid`).

```lean
lemma apply_eq_zero_of_map_zero_re_eq_zero (hF : IsPositiveDefinite F)
    (h0 : (F 0).re = 0) (a : M) : F a = 0
```

**`TauCeti.IsPositiveDefinite.norm_apply_le_map_zero_re_of_star_eq_neg`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L250).

> If the involution negates the point `a`, then a positive-definite function is bounded at `a`
> by its value at zero. In particular this applies on an additive group whose involution is
> negation.

```lean
lemma norm_apply_le_map_zero_re_of_star_eq_neg (hH : IsPositiveDefinite H)
    (a : N) (hstar_a : star a = -a) : ‖H a‖ ≤ (H 0).re
```

**`TauCeti.IsPositiveDefinite.add`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L257).

> Positive-definite functions are closed under addition.

```lean
lemma add (hF : IsPositiveDefinite F) (hG : IsPositiveDefinite G) :
    IsPositiveDefinite (fun x => F x + G x)
```

**`TauCeti.IsPositiveDefinite.const_mul`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L263).

> Positive-definite functions are closed under multiplication by a nonnegative complex scalar.

```lean
lemma const_mul {k : ℂ} (hk : 0 ≤ k) (hF : IsPositiveDefinite F) :
    IsPositiveDefinite (fun x => k * F x)
```

**`TauCeti.IsPositiveDefinite.mul`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L269).

> Positive-definite functions are closed under pointwise multiplication (Schur product).

```lean
lemma mul (hF : IsPositiveDefinite F) (hG : IsPositiveDefinite G) :
    IsPositiveDefinite (fun x => F x * G x)
```

**`TauCeti.isPositiveDefinite_const`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L277).

> A nonnegative real constant is a positive-definite function.

```lean
lemma isPositiveDefinite_const {k : ℂ} (hk : 0 ≤ k) :
    IsPositiveDefinite (fun _ : M => k)
```

**`TauCeti.isPositiveDefinite_zero`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L283).

> The zero function is positive definite.

```lean
lemma isPositiveDefinite_zero : IsPositiveDefinite (fun _ : M => (0 : ℂ))
```

**`TauCeti.IsPositiveDefinite.sum`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L289).

> Positive-definite functions are closed under finite sums.

```lean
lemma sum {ι : Type*} {s : Finset ι} {F : ι → M → ℂ} (hF : ∀ i ∈ s, IsPositiveDefinite (F i)) :
    IsPositiveDefinite (fun x => ∑ i ∈ s, F i x)
```

**`TauCeti.IsPositiveDefinite.prod`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean#L297).

> Positive-definite functions are closed under finite products (Schur product).

```lean
lemma prod {ι : Type*} {s : Finset ι} {F : ι → M → ℂ} (hF : ∀ i ∈ s, IsPositiveDefinite (F i)) :
    IsPositiveDefinite (fun x => ∏ i ∈ s, F i x)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Analytic bounds for positive-semidefinite matrices](analysis-matrix-possemidef.md)
- [Positive-semidefinite matrix algebra](../part-02/linearalgebra-matrix-possemidef.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/Basic.lean)
