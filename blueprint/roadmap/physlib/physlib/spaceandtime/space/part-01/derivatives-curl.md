---
declaration: module
origin: cited
lean: Space.curl, Space.curl_zero, Space.curl_const, Space.curl_add, Space.curl_smul, Space.curl_neg, Space.curl_sub, Space.curl_linear_map
statement: formalized
proof: formalized
---

# Curl on Space

The module `Physlib.SpaceAndTime.Space.Derivatives.Curl`, [Physlib/SpaceAndTime/Space/Derivatives/Curl.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean): 25 declarations, 7 with a docstring; 10 private, not shown.

## i. Overview

> In this module we define the curl of functions and distributions on 3-dimensional
> space `Space 3`.
>
> We also prove some basic vector-identities involving of the curl operator.

## ii. Key results

> - `curl` : The curl operator on functions from `Space 3` to `EuclideanSpace ℝ (Fin 3)`.
> - `distCurl` : The curl operator on distributions from `Space 3` to `EuclideanSpace ℝ (Fin 3)`.
> - `div_of_curl_eq_zero` : The divergence of the curl of a function is zero.
> - `distCurl_distGrad_eq_zero` : The curl of the gradient of a distribution is zero.
> - `curl_eq_sum_leviCivitaSymbol` : The components of the curl as a contraction with the
>   Levi-Civita symbol.

## iv. References

> * None.

## A. The curl on functions

**`Space.curl`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L72).

> The vector calculus operator `curl`.

```lean
noncomputable def curl (f : Space → EuclideanSpace ℝ (Fin 3)) :
    Space → EuclideanSpace ℝ (Fin 3)
```

### A.1. The curl on the zero function

**`Space.curl_zero`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L90).

```lean
lemma curl_zero : ∇ ⨯ (0 : Space → EuclideanSpace ℝ (Fin 3)) = 0
```

### A.2. The curl on a constant function

**`Space.curl_const`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L103).

```lean
lemma curl_const : ∇ ⨯ (fun _ : Space => v₃) = 0
```

### A.3. Basic operations on curl

**`Space.curl_add`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L116).

```lean
lemma curl_add (f1 f2 : Space → EuclideanSpace ℝ (Fin 3))
    (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    ∇ ⨯ (f1 + f2) = ∇ ⨯ f1 + ∇ ⨯ f2
```

**`Space.curl_smul`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L129).

```lean
lemma curl_smul (f : Space → EuclideanSpace ℝ (Fin 3)) (k : ℝ)
    (hf : Differentiable ℝ f) :
    ∇ ⨯ (k • f) = k • ∇ ⨯ f
```

**`Space.curl_neg`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L139).

```lean
lemma curl_neg (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : Differentiable ℝ f) :
    ∇ ⨯ (-f) = -∇ ⨯ f
```

**`Space.curl_sub`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L144).

```lean
lemma curl_sub (f1 f2 : Space → EuclideanSpace ℝ (Fin 3))
    (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    ∇ ⨯ (f1 - f2) = ∇ ⨯ f1 - ∇ ⨯ f2
```

### A.4. The curl of a linear map is a linear map

**`Space.curl_linear_map`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L158).

```lean
lemma curl_linear_map (f : W → Space 3 → EuclideanSpace ℝ (Fin 3))
    (hf : ∀ w, Differentiable ℝ (f w))
    (hf' : IsLinearMap ℝ f) :
    IsLinearMap ℝ (fun w => ∇ ⨯ (f w))
```

### A.5. Preliminary lemmas about second derivatives

**`Space.deriv_coord_2nd_add`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L177).

> Second derivatives distribute coordinate-wise over addition (all three components for div).

```lean
lemma deriv_coord_2nd_add (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 2 f) :
    ∂[i] (fun x => ∂[u] (fun x => f x u) x + (∂[v] (fun x => f x v) x + ∂[w] (fun x => f x w) x)) =
    (∂[i] (∂[u] (fun x => f x u))) + (∂[i] (∂[v] (fun x => f x v))) +
    (∂[i] (∂[w] (fun x => f x w)))
```

**`Space.deriv_coord_2nd_sub`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L189).

> Second derivatives distribute coordinate-wise over subtraction (two components for curl).

```lean
lemma deriv_coord_2nd_sub (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 2 f) :
    ∂[u] (fun x => ∂[v] (fun x => f x w) x - ∂[w] (fun x => f x v) x) =
    (∂[u] (∂[v] (fun x => f x w))) - (∂[u] (∂[w] (fun x => f x v)))
```

### A.6. The div of a curl is zero

**`Space.div_of_curl_eq_zero`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L205).

```lean
lemma div_of_curl_eq_zero (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 2 f) :
    ∇ ⬝ (∇ ⨯ f) = 0
```

### A.7. The curl of a grad is zero

**`Space.curl_of_grad_eq_zero`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L227).

```lean
lemma curl_of_grad_eq_zero (f : Space → ℝ) (hf : ContDiff ℝ 2 f) :
    ∇ ⨯ (∇ f) = 0
```

### A.8. The curl of a curl

**`Space.curl_of_curl`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L241).

```lean
lemma curl_of_curl (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 2 f) :
    ∇ ⨯ (∇ ⨯ f) = ∇ (∇ ⬝ f) - Δᵥ f
```

> ### A.9. A divergence-free field is a curl
>
> We now prove that if the divergence of a function is zero,
> then it is equal to the curl of some function.
>
> This proof is involved, thus we have split it up into private definitions and lemmas.
> The proof is by explicit construction. If `f` has divergence zero,
> then we construct
> ```
> ∫ t in 0..1, (t • x) ⨯ f (t • x)
> ```
> and show that the curl of this is equal to `f`.
>
> We call the integrand of this function the `homotopyOperatorIntegrand`.
> We build API around this to help in our proof.

**`Space.eq_neg_curl_of_div_zero`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L484).

```lean
lemma eq_neg_curl_of_div_zero (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 1 f)
    (hdiv : ∇ ⬝ f = 0) :
    f = - curl (fun x => ∫ (t : ℝ) in 0..1, (t • basis.repr x) ⨯ₑ₃ f (t • x) ∂(volume))
```

**`Space.exists_curl_of_div_zero`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L532).

```lean
lemma exists_curl_of_div_zero (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 1 f)
    (hdiv : ∇ ⬝ f = 0) :
    ∃ g : Space → EuclideanSpace ℝ (Fin 3), f = curl g ∧ Differentiable ℝ g
```

> ### A.10. A curl-free field is a gradient
>
> We show that if the curl of a function is zero, then it is equal to the gradient of some function.
> The key lemma here is
> `Convex.exists_forall_hasFDerivAt_of_fderiv_symmetric`, which is
> a more general version of this result in Mathlib. We turn this here into something
> more familiar, to the physicists via `deriv_comm_of_curl_zero`.

**`Space.deriv_comm_of_curl_zero`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L561).

```lean
lemma deriv_comm_of_curl_zero (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : Differentiable ℝ f)
    (hcurl : curl f = 0) (x : Space) (i j : Fin 3) :
    ∂[i] f x j = ∂[j] f x i
```

**`Space.exists_grad_of_curl_zero`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L590).

```lean
lemma exists_grad_of_curl_zero (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : Differentiable ℝ f)
    (hcurl : curl f = 0) : ∃ g : Space → ℝ, f = grad g ∧ Differentiable ℝ g
```

**`Space.eq_grad_integral_of_curl_zero`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L644).

> A constructive form of the statement that if the curl of a function is zero,
> then it is equal to the grad of another function.
>
> In the context of e.g. electromagnetism the potential given by this lemma corresponds
> to that defined by the work done to move a unit charge from the origin to the
> point `x` along a straight line.

```lean
lemma eq_grad_integral_of_curl_zero (f : Space → EuclideanSpace ℝ (Fin 3)) (hf : ContDiff ℝ 1 f)
    (hcurl : curl f = 0) :
    f = grad (fun x => ∫ t in (0 : ℝ)..1, ⟪f (t • x), basis.repr x⟫_ℝ ∂(volume))
```

### A.11. The curl in terms of the Levi-Civita symbol

**`Space.curl_eq_sum_leviCivitaSymbol`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L669).

> The components of the curl as a contraction with the Levi-Civita symbol,
> `(∇ ⨯ f) x i = ∑ j k, ε_{ijk} ∂[j] fₖ x`.

```lean
lemma curl_eq_sum_leviCivitaSymbol (f : Space → EuclideanSpace ℝ (Fin 3))
    (x : Space) (i : Fin 3) :
    (∇ ⨯ f) x i = ∑ j, ∑ k, (leviCivitaSymbol ![i, j, k] : ℝ) * ∂[j] (fun y => f y k) x
```

## B. The curl on distributions

**`Space.distCurl`**, a def, [line 690](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L690).

> The curl of a distribution `Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))` as a distribution
> `Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))`.

```lean
noncomputable def distCurl : (Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))) →ₗ[ℝ]
    (Space) →d[ℝ] (EuclideanSpace ℝ (Fin 3))
```

### B.1. The components of the curl

**`Space.distCurl_coord_apply`**, a lemma, [line 723](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L723).

```lean
lemma distCurl_coord_apply {i : Fin 3}
    (f : Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))) (η : 𝓢(Space, ℝ)) :
    (∇ᵈ ⨯ f) η i = - f (SchwartzMap.evalCLM ℝ Space ℝ (basis (i+2)) (fderivCLM ℝ Space ℝ η)) (i+1)
    + f (SchwartzMap.evalCLM ℝ Space ℝ (basis (i+1)) (fderivCLM ℝ Space ℝ η)) (i+2)
```

**`Space.distCurl_apply_one`**, a lemma, [line 729](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L729).

```lean
lemma distCurl_apply_one (f : Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))) (η : 𝓢(Space, ℝ)) :
    (∇ᵈ ⨯ f) η 1 = - f (SchwartzMap.evalCLM ℝ Space ℝ (basis 0) (fderivCLM ℝ Space ℝ η)) 2
    + f (SchwartzMap.evalCLM ℝ Space ℝ (basis 2) (fderivCLM ℝ Space ℝ η)) 0
```

**`Space.distCurl_apply_two`**, a lemma, [line 734](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L734).

```lean
lemma distCurl_apply_two (f : Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))) (η : 𝓢(Space, ℝ)) :
    (∇ᵈ ⨯ f) η 2 = - f (SchwartzMap.evalCLM ℝ Space ℝ (basis 1) (fderivCLM ℝ Space ℝ η)) 0
    + f (SchwartzMap.evalCLM ℝ Space ℝ (basis 0) (fderivCLM ℝ Space ℝ η)) 1
```

### B.2. Basic equalities

**`Space.distCurl_apply`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L745).

```lean
lemma distCurl_apply (f : Space →d[ℝ] (EuclideanSpace ℝ (Fin 3))) (η : 𝓢(Space, ℝ)) :
    (∇ᵈ ⨯ f) η = WithLp.toLp 2 fun i =>
      - f (SchwartzMap.evalCLM ℝ Space ℝ (basis (i+2)) (fderivCLM ℝ Space ℝ η)) (i+1)
      + f (SchwartzMap.evalCLM ℝ Space ℝ (basis (i+1)) (fderivCLM ℝ Space ℝ η)) (i+2)
```

### B.3. The curl of a grad is zero

**`Space.distCurl_distGrad_eq_zero`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean#L760).

> The curl of a grad is equal to zero.

```lean
lemma distCurl_distGrad_eq_zero (f : (Space) →d[ℝ] ℝ) :
    ∇ᵈ ⨯ (∇ᵈ f) = 0
```

## Depends on

- [The Levi-Civita symbol in general dimension](../../../mathematics/levicivita/basic.md)
- [The Laplacian operator on `Space d`](derivatives-laplacian.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/Curl.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Curl.lean)
