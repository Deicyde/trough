---
declaration: module
origin: cited
lean: TauCeti.WithNegStar, TauCeti.WithNegStar.star_eq_neg, TauCeti.WithNegStar.toNegStar, TauCeti.WithNegStar.ofNegStar, TauCeti.WithNegStar.ofNegStar_toNegStar, TauCeti.WithNegStar.toNegStar_ofNegStar, TauCeti.IsPositiveDefiniteSub, TauCeti.isPositiveDefiniteSub_iff_forall_sum_nonneg
statement: formalized
proof: formalized
---

# Positive-definite functions on an additive commutative group

The module `PhyslibAlpha.Mathematics.TauCeti.Analysis.PositiveDefinite.AddGroup`, [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean): 46 declarations (4 instances with no name), 39 with a docstring.

> On an additive commutative group `G` the classical positive-definiteness condition for `F : G → ℂ`
> reads `∑_{i,j} cᵢ · conj(cⱼ) · F(aᵢ - aⱼ) ≥ 0`: the involution is negation, so the kernel is the
> translation-invariant `K(a, b) = F(a - b)`.

## i. Overview

> On an additive commutative group `G` the classical positive-definiteness condition for
> `F : G → ℂ` reads `∑_{i,j} cᵢ · conj(cⱼ) · F(aᵢ - aⱼ) ≥ 0`: the involution is negation, so the
> kernel is the translation-invariant `K(a, b) = F(a - b)`. Mathlib's `star` on a real vector space
> is the identity, not negation, so the generic involutive predicate
> `TauCeti.IsPositiveDefinite` does *not* express this condition for the canonical instances on
> `ℝ` or on a Euclidean space. This file supplies the subtraction-form predicate
> `TauCeti.IsPositiveDefiniteSub` that does, and connects it to the generic theory.
>
> The connection runs through the type synonym `TauCeti.WithNegStar G`, a copy of `G` carrying the
> negation involution `star a = -a` as a genuine `StarAddMonoid` instance. Installing that
> involution on `G` itself would clash with Mathlib's star conventions, so it is installed on the
> synonym instead, and `TauCeti.isPositiveDefiniteSub_iff_isPositiveDefinite` transports statements
> across. The synonym is public: a generic lemma with no transfer lemma here can still be applied to
> `fun a : WithNegStar G => F (WithNegStar.ofNegStar a)`.
>
> This advances `TauCetiRoadmap/OneParameterSemigroups/README.md`, Part C, Objects, which asks for
> `IsPositiveDefinite` to be defined generically and then *instantiated* on a finite-dimensional real
> inner-product space with the involution `a⋆ = -a`, and the `API to develop` items (closure
> properties, the value bounds at the origin, continuity at `0` implying uniform continuity, the
> PD-function ↔ PD-kernel equivalence `F(a - b)`, and normalization) at that instantiation. It is
> the predicate in which Bochner's theorem is stated, in
> `TauCeti/Analysis/Bochner/BochnerTheorem.lean`.

## ii. Key results

> * `TauCeti.WithNegStar`: the type synonym carrying the negation involution.
> * `TauCeti.IsPositiveDefiniteSub`: the subtraction-form positive-definiteness predicate.
> * `TauCeti.isPositiveDefiniteSub_iff_forall_sum_nonneg`: the defining finite-family condition.
> * `TauCeti.isPositiveDefiniteSub_iff_isPositiveDefinite`: the transfer to the generic predicate.
> * `TauCeti.isPositiveDefiniteSub_iff_posSemidef`: the PD-function ↔ PD-kernel equivalence.
> * `TauCeti.isPositiveDefinite_iff_isPositiveDefiniteSub`: agreement with the generic predicate on
>   a group whose own involution is negation.
> * `TauCeti.IsPositiveDefiniteSub.map_zero_nonneg`, `map_zero_re_nonneg`, `map_zero_eq_ofReal_re`,
>   `map_neg`, `conj_symm`, `normSq_le`, `norm_apply_le_map_zero_re`: values at and around the
>   origin.
> * `TauCeti.IsPositiveDefiniteSub.add`, `const_mul`, `real_smul`, `mul`, `sum`, `prod`,
>   `TauCeti.isPositiveDefiniteSub_const`: closure properties.
> * `TauCeti.IsPositiveDefiniteSub.comp_addMonoidHom`, `comp_smul`, `comp_neg`: pullbacks.
> * `TauCeti.IsPositiveDefiniteSub.of_tendsto`: pointwise limits.
> * `TauCeti.IsPositiveDefiniteSub.normalize`: normalization to value `1` at the origin.
> * `TauCeti.IsPositiveDefiniteSub.uniformContinuous_of_continuousAt_zero`: continuity at `0`
>   implies uniform continuity.

## iv. References

> * C. Berg, J. P. R. Christensen, P. Ressel, *Harmonic Analysis on Semigroups* (GTM 100, 1984),
>   Chapter 3.
> * W. Rudin, *Fourier Analysis on Groups* (1962), §1.4.

## A. Development

### A.1. The negation involution

**`TauCeti.WithNegStar`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L101).

> `WithNegStar G` is a type synonym for an additive commutative group `G`, carrying the negation
> involution `star a = -a`.
>
> Mathlib pins no negation `StarAddMonoid` instance on an additive group — on a real vector space
> `star` is the identity — so the involution used by classical positive definiteness is installed on
> this synonym rather than on `G` itself.

```lean
def WithNegStar (G : Type*) : Type _
```

**An instance with no name**, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L109).

```lean
instance : AddCommGroup (WithNegStar G)
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L111).

```lean
instance : Star (WithNegStar G)
```

**`TauCeti.WithNegStar.star_eq_neg`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L114).

```lean
lemma star_eq_neg (a : WithNegStar G) : star a = -a
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L116).

```lean
instance : StarAddMonoid (WithNegStar G)
```

**`TauCeti.WithNegStar.toNegStar`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L121).

> The identity additive equivalence from `G` to its negation-involution copy.

```lean
def toNegStar : G ≃+ WithNegStar G
```

**`TauCeti.WithNegStar.ofNegStar`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L124).

> The identity additive equivalence from the negation-involution copy of `G` back to `G`.

```lean
def ofNegStar : WithNegStar G ≃+ G
```

**`TauCeti.WithNegStar.ofNegStar_toNegStar`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L127).

```lean
lemma ofNegStar_toNegStar (a : G) : ofNegStar (toNegStar a) = a
```

**`TauCeti.WithNegStar.toNegStar_ofNegStar`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L131).

```lean
lemma toNegStar_ofNegStar (a : WithNegStar G) : toNegStar (ofNegStar a) = a
```

**An instance with no name**, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L140).

```lean
instance : SeminormedAddCommGroup (WithNegStar G)
```

### A.2. The subtraction-form predicate

**`TauCeti.IsPositiveDefiniteSub`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L159).

> A function `F : G → ℂ` on an additive commutative group is **positive definite** when, for
> every finite family of scalars `c : Fin n → ℂ` and points `v : Fin n → G`, the Hermitian form
> `∑_{i,j} c i · conj (c j) * F (v i - v j)` is a nonnegative real number (using the order on `ℂ`
> for which `0 ≤ z` means `z` is real and nonnegative).
>
> This is the classical translation-invariant condition, the one Bochner's theorem is stated in. It
> is `TauCeti.IsPositiveDefinite` for the negation involution; see
> `TauCeti.isPositiveDefiniteSub_iff_isPositiveDefinite`.

```lean
def IsPositiveDefiniteSub (F : G → ℂ) : Prop
```

**`TauCeti.isPositiveDefiniteSub_iff_forall_sum_nonneg`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L165).

> The defining finite-family characterization, for building a positive-definite function
> directly from the quadratic-form condition.

```lean
lemma isPositiveDefiniteSub_iff_forall_sum_nonneg :
    IsPositiveDefiniteSub F ↔ ∀ (n : ℕ) (c : Fin n → ℂ) (v : Fin n → G),
      0 ≤ ∑ i, ∑ j, c i * conj (c j) * F (v i - v j)
```

**`TauCeti.isPositiveDefiniteSub_iff_isPositiveDefinite`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L172).

> Subtraction-form positive definiteness is the generic involutive predicate for the negation
> involution, read on the type synonym `TauCeti.WithNegStar`.

```lean
lemma isPositiveDefiniteSub_iff_isPositiveDefinite :
    IsPositiveDefiniteSub F ↔
      IsPositiveDefinite fun a : WithNegStar G => F (WithNegStar.ofNegStar a)
```

**`TauCeti.IsPositiveDefiniteSub.isPositiveDefinite`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L185).

> The generic involutive predicate attached to a subtraction-form positive-definite function.
> This is the workhorse for transporting the generic API.

```lean
lemma isPositiveDefinite (hF : IsPositiveDefiniteSub F) :
    IsPositiveDefinite fun a : WithNegStar G => F (WithNegStar.ofNegStar a)
```

**`TauCeti.IsPositiveDefiniteSub.sum_nonneg`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L190).

> Positive-definiteness holds for an arbitrary finite index type, not just `Fin n`.

```lean
lemma sum_nonneg (hF : IsPositiveDefiniteSub F) {ι : Type*} [Fintype ι] (c : ι → ℂ) (v : ι → G) :
    0 ≤ ∑ i, ∑ j, c i * conj (c j) * F (v i - v j)
```

**`TauCeti.IsPositiveDefiniteSub.posSemidef`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L197).

> A subtraction-form positive-definite function gives the translation-invariant
> positive-definite kernel `K(a, b) = F (a - b)`.

```lean
lemma posSemidef (hF : IsPositiveDefiniteSub F) :
    Matrix.PosSemidef fun a b : G => F (a - b)
```

**`TauCeti.IsPositiveDefiniteSub.of_posSemidef`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L211).

> A function whose translation-invariant kernel `K(a, b) = F (a - b)` is positive definite is
> positive definite.

```lean
lemma of_posSemidef (hK : Matrix.PosSemidef fun a b : G => F (a - b)) :
    IsPositiveDefiniteSub F
```

**`TauCeti.isPositiveDefiniteSub_iff_posSemidef`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L228).

> The PD-function ↔ PD-kernel equivalence in its classical translation-invariant form: `F` is
> positive definite if and only if the kernel `K(a, b) = F (a - b)` is positive definite.

```lean
lemma isPositiveDefiniteSub_iff_posSemidef :
    IsPositiveDefiniteSub F ↔ Matrix.PosSemidef fun a b : G => F (a - b)
```

**`TauCeti.isPositiveDefinite_iff_isPositiveDefiniteSub`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L234).

> On a group whose own involution is negation, the generic involutive predicate and the
> subtraction-form predicate agree.

```lean
lemma isPositiveDefinite_iff_isPositiveDefiniteSub [StarAddMonoid G]
    (hstar : ∀ a : G, star a = -a) : IsPositiveDefinite F ↔ IsPositiveDefiniteSub F
```

### A.3. Values at and around the origin

**`TauCeti.IsPositiveDefiniteSub.map_zero_nonneg`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L243).

> The value of a positive-definite function at `0` is real and nonnegative.

```lean
lemma map_zero_nonneg (hF : IsPositiveDefiniteSub F) : 0 ≤ F 0
```

**`TauCeti.IsPositiveDefiniteSub.map_zero_im`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L248).

> The value of a positive-definite function at `0` has zero imaginary part.

```lean
lemma map_zero_im (hF : IsPositiveDefiniteSub F) : (F 0).im = 0
```

**`TauCeti.IsPositiveDefiniteSub.map_zero_re_nonneg`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L252).

> The real part of the value of a positive-definite function at `0` is nonnegative.

```lean
lemma map_zero_re_nonneg (hF : IsPositiveDefiniteSub F) : 0 ≤ (F 0).re
```

**`TauCeti.IsPositiveDefiniteSub.map_zero_eq_ofReal_re`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L257).

> The value at the origin of a positive-definite function is the real number `(F 0).re`, viewed
> as a complex number.

```lean
lemma map_zero_eq_ofReal_re (hF : IsPositiveDefiniteSub F) : F 0 = ((F 0).re : ℂ)
```

**`TauCeti.IsPositiveDefiniteSub.map_zero_re_pos_of_ne_zero`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L262).

> If a positive-definite function is nonzero at the origin, then the real part of that value is
> strictly positive.

```lean
lemma map_zero_re_pos_of_ne_zero (hF : IsPositiveDefiniteSub F) (h0 : F 0 ≠ 0) :
    0 < (F 0).re
```

**`TauCeti.IsPositiveDefiniteSub.conj_symm`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L269).

> A positive-definite function is conjugate symmetric: `conj (F (b - a)) = F (a - b)`.

```lean
lemma conj_symm (hF : IsPositiveDefiniteSub F) (a b : G) : conj (F (b - a)) = F (a - b)
```

**`TauCeti.IsPositiveDefiniteSub.map_neg`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L274).

> A positive-definite function satisfies `F (-a) = conj (F a)`.

```lean
lemma map_neg (hF : IsPositiveDefiniteSub F) (a : G) : F (-a) = conj (F a)
```

**`TauCeti.IsPositiveDefiniteSub.normSq_le`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L279).

> The Cauchy–Schwarz inequality for a positive-definite function: the squared norm of any value
> is bounded by the square of the value at the origin.

```lean
lemma normSq_le (hF : IsPositiveDefiniteSub F) (a b : G) :
    Complex.normSq (F (a - b)) ≤ (F 0).re * (F 0).re
```

**`TauCeti.IsPositiveDefiniteSub.norm_apply_le_map_zero_re`**, a lemma, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L285).

> A positive-definite function is bounded by its value at the origin.

```lean
lemma norm_apply_le_map_zero_re (hF : IsPositiveDefiniteSub F) (a : G) : ‖F a‖ ≤ (F 0).re
```

**`TauCeti.IsPositiveDefiniteSub.apply_eq_zero_of_map_zero_re_eq_zero`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L291).

> **A positive-definite function with `(F 0).re = 0` vanishes identically.**

```lean
lemma apply_eq_zero_of_map_zero_re_eq_zero (hF : IsPositiveDefiniteSub F) (h0 : (F 0).re = 0)
    (a : G) : F a = 0
```

### A.4. Closure properties

**`TauCeti.IsPositiveDefiniteSub.add`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L299).

> Positive-definite functions are closed under addition.

```lean
lemma add (hF : IsPositiveDefiniteSub F) (hH : IsPositiveDefiniteSub H) :
    IsPositiveDefiniteSub fun x => F x + H x
```

**`TauCeti.IsPositiveDefiniteSub.const_mul`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L306).

> Positive-definite functions are closed under multiplication by a nonnegative complex
> scalar.

```lean
lemma const_mul {k : ℂ} (hk : 0 ≤ k) (hF : IsPositiveDefiniteSub F) :
    IsPositiveDefiniteSub fun x => k * F x
```

**`TauCeti.IsPositiveDefiniteSub.real_smul`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L311).

> Positive-definite functions are closed under multiplication by a nonnegative real scalar.

```lean
lemma real_smul {r : ℝ} (hr : 0 ≤ r) (hF : IsPositiveDefiniteSub F) :
    IsPositiveDefiniteSub fun x => r • F x
```

**`TauCeti.IsPositiveDefiniteSub.mul`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L316).

> Positive-definite functions are closed under pointwise multiplication (Schur product).

```lean
lemma mul (hF : IsPositiveDefiniteSub F) (hH : IsPositiveDefiniteSub H) :
    IsPositiveDefiniteSub fun x => F x * H x
```

**`TauCeti.IsPositiveDefiniteSub.sum`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L322).

> Positive-definite functions are closed under finite sums.

```lean
lemma sum {ι : Type*} {s : Finset ι} {F : ι → G → ℂ}
    (hF : ∀ i ∈ s, IsPositiveDefiniteSub (F i)) :
    IsPositiveDefiniteSub fun x => ∑ i ∈ s, F i x
```

**`TauCeti.IsPositiveDefiniteSub.prod`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L329).

> Positive-definite functions are closed under finite products (Schur products).

```lean
lemma prod {ι : Type*} {s : Finset ι} {F : ι → G → ℂ}
    (hF : ∀ i ∈ s, IsPositiveDefiniteSub (F i)) :
    IsPositiveDefiniteSub fun x => ∏ i ∈ s, F i x
```

### A.5. Pullbacks

**`TauCeti.IsPositiveDefiniteSub.comp_addMonoidHom`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L340).

> Positive definiteness is preserved by precomposition with an additive homomorphism; no
> compatibility with an involution is needed, since an additive homomorphism automatically
> commutes with negation.

```lean
lemma comp_addMonoidHom {N : Type*} [AddCommGroup N] (hF : IsPositiveDefiniteSub F)
    (φ : N →+ G) : IsPositiveDefiniteSub fun x => F (φ x)
```

**`TauCeti.IsPositiveDefiniteSub.comp_smul`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L346).

> Positive definiteness is preserved by rescaling the argument.

```lean
lemma comp_smul {R : Type*} [DistribSMul R G] (hF : IsPositiveDefiniteSub F) (r : R) :
    IsPositiveDefiniteSub fun x => F (r • x)
```

**`TauCeti.IsPositiveDefiniteSub.comp_neg`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L352).

> Positive definiteness is preserved by negating the argument.

```lean
lemma comp_neg (hF : IsPositiveDefiniteSub F) : IsPositiveDefiniteSub fun x => F (-x)
```

### A.6. Limits

**`TauCeti.IsPositiveDefiniteSub.of_tendsto`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L359).

> Positive definiteness is preserved under pointwise limits along a nontrivial filter.

```lean
lemma of_tendsto {ι : Type*} {l : Filter ι} [NeBot l] {F : ι → G → ℂ} {H : G → ℂ}
    (hF : ∀ᶠ i in l, IsPositiveDefiniteSub (F i))
    (hlim : ∀ x : G, Tendsto (fun i => F i x) l (𝓝 (H x))) :
    IsPositiveDefiniteSub H
```

### A.7. Normalization

**`TauCeti.IsPositiveDefiniteSub.normalize`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L371).

> Multiplying a positive-definite function by the reciprocal of its real value at the origin
> preserves positive definiteness.

```lean
lemma normalize (hF : IsPositiveDefiniteSub F) :
    IsPositiveDefiniteSub fun x => (((F 0).re)⁻¹ : ℂ) * F x
```

**`TauCeti.IsPositiveDefiniteSub.normalize_apply_zero`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L378).

> The normalized function has value `1` at the origin.

```lean
lemma normalize_apply_zero (hF : IsPositiveDefiniteSub F) (h0 : F 0 ≠ 0) :
    (((F 0).re)⁻¹ : ℂ) * F 0 = 1
```

**`TauCeti.IsPositiveDefiniteSub.norm_normalize_apply_le_one`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L386).

> A normalized positive-definite function is bounded by `1`.

```lean
lemma norm_normalize_apply_le_one (hF : IsPositiveDefiniteSub F) (a : G) :
    ‖(((F 0).re)⁻¹ : ℂ) * F a‖ ≤ 1
```

### A.8. Continuity

**`TauCeti.IsPositiveDefiniteSub.uniformContinuous_of_continuousAt_zero`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L401).

> A positive-definite function on a seminormed additive commutative group is uniformly
> continuous as soon as it is continuous at the origin.

```lean
lemma uniformContinuous_of_continuousAt_zero (hF : IsPositiveDefiniteSub F)
    (hcont : ContinuousAt F 0) : UniformContinuous F
```

**`TauCeti.IsPositiveDefiniteSub.continuous_of_continuousAt_zero`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L408).

> A positive-definite function on a seminormed additive commutative group is continuous as soon
> as it is continuous at the origin.

```lean
lemma continuous_of_continuousAt_zero (hF : IsPositiveDefiniteSub F)
    (hcont : ContinuousAt F 0) : Continuous F
```

**`TauCeti.isPositiveDefiniteSub_const`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L415).

> A nonnegative real constant is a positive-definite function.

```lean
lemma isPositiveDefiniteSub_const {k : ℂ} (hk : 0 ≤ k) :
    IsPositiveDefiniteSub (fun _ : G => k)
```

**`TauCeti.isPositiveDefiniteSub_zero`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean#L420).

> The zero function is positive definite.

```lean
lemma isPositiveDefiniteSub_zero : IsPositiveDefiniteSub (fun _ : G => (0 : ℂ))
```

## Depends on

- [Positive-definite functions on an involutive additive monoid](analysis-positivedefinite-basic.md)

## Proof depends on

- [Continuity of positive-definite functions](analysis-positivedefinite-continuity.md)
- [Weighted closure for positive-definite functions](../part-02/analysis-positivedefinite-function-closure.md)
- [The positive-definite function ↔ positive-definite kernel correspondence](../part-02/analysis-positivedefinite-function-kernel.md)
- [Limits of positive-definite functions](analysis-positivedefinite-limits.md)
- [Normalizing positive-definite functions](analysis-positivedefinite-normalize.md)

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Analysis/PositiveDefinite/AddGroup.lean)
