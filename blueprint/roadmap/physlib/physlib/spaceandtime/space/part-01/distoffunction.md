---
declaration: module
origin: cited
lean: Space.distOfFunction, Space.distOfFunction_apply, Space.distOfFunction_zero_eq_zero, Space.distOfFunction_smul, Space.distOfFunction_smul_fun, Space.distOfFunction_mul_fun, Space.distOfFunction_neg, Space.distOfFunction_inner
statement: formalized
proof: formalized
---

# Distributions from functions on space

The module `Physlib.SpaceAndTime.Space.DistOfFunction`, [Physlib/SpaceAndTime/Space/DistOfFunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean): 11 declarations, 2 with a docstring.

## i. Overview

> In this module we define distributions on space constructed from functions
> `f : Space d → F` satisfying the condition `IsDistBounded f`.
>
> This gives a convenient way to construct distributions from functions, without needing
> to reference the underlying Schwartz maps.

## ii. Key results

> - `distOfFunction f hf` : The distribution on space constructed from the function
>   `f : Space d → F` satisfying the `IsDistBounded f` condition.

## iv. References

> * None.

## A. Definition of a distribution from a function

**`Space.distOfFunction`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L61).

> A distribution `Space d →d[ℝ] F` from a function
> `f : Space d → F` which satisfies the `IsDistBounded f` condition.

```lean
def distOfFunction {d : ℕ} (f : Space d → F) (hf : IsDistBounded f) :
    (Space d) →d[ℝ] F
```

**`Space.distOfFunction_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L79).

```lean
lemma distOfFunction_apply {d : ℕ} (f : Space d → F)
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) :
    distOfFunction f hf η = ∫ x, η x • f x
```

## B. Linarity properties of getting distributions from functions

**`Space.distOfFunction_zero_eq_zero`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L89).

```lean
lemma distOfFunction_zero_eq_zero {d : ℕ} :
    distOfFunction (fun _ : Space d => (0 : F)) (by fun_prop) = 0
```

**`Space.distOfFunction_smul`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L94).

```lean
lemma distOfFunction_smul {d : ℕ} (f : Space d → F)
    (hf : IsDistBounded f) (c : ℝ) :
    distOfFunction (c • f) (by fun_prop) = c • distOfFunction f hf
```

**`Space.distOfFunction_smul_fun`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L106).

```lean
lemma distOfFunction_smul_fun {d : ℕ} (f : Space d → F)
    (hf : IsDistBounded f) (c : ℝ) :
    distOfFunction (fun x => c • f x) (by fun_prop) = c • distOfFunction f hf
```

**`Space.distOfFunction_mul_fun`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L117).

```lean
lemma distOfFunction_mul_fun {d : ℕ} (f : Space d → ℝ)
    (hf : IsDistBounded f) (c : ℝ) :
    distOfFunction (fun x => c * f x) (by fun_prop) = c • distOfFunction f hf
```

**`Space.distOfFunction_neg`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L122).

```lean
lemma distOfFunction_neg {d : ℕ} (f : Space d → F)
    (hf : IsDistBounded (fun x => - f x)) :
    distOfFunction (fun x => - f x) hf = - distOfFunction f (by simpa using hf.neg)
```

## C. Properties related to inner products

**`Space.distOfFunction_inner`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L137).

```lean
lemma distOfFunction_inner {d n : ℕ} (f : Space d → EuclideanSpace ℝ (Fin n))
    (hf : IsDistBounded f)
    (η : 𝓢(Space d, ℝ)) (y : EuclideanSpace ℝ (Fin n)) :
    ⟪distOfFunction f hf η, y⟫_ℝ = ∫ x, η x * ⟪f x, y⟫_ℝ
```

## D. Derivatives

**`Space.distDeriv_distOfFunction`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L158).

> The distributional spatial derivative of the distribution associated to a differentiable
> function is the distribution associated to the corresponding pointwise spatial derivative.

```lean
lemma distDeriv_distOfFunction {d : ℕ} (μ : Fin d) (f : Space d → F)
    (hf : IsDistBounded f) (hf_deriv : IsDistBounded (∂[μ] f))
    (hf_diff : Differentiable ℝ f) :
    ∂ᵈ[μ] (distOfFunction f hf) = distOfFunction (∂[μ] f) hf_deriv
```

## E. Components

**`Space.distOfFunction_eculid_eval`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L181).

```lean
lemma distOfFunction_eculid_eval {d n : ℕ} (f : Space d → EuclideanSpace ℝ (Fin n))
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) (i : Fin n) :
    distOfFunction f hf η i = distOfFunction (fun x => f x i) (hf.pi_comp i) η
```

**`Space.distOfFunction_vector_eval`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean#L191).

```lean
lemma distOfFunction_vector_eval {d n : ℕ} (f : Space d → Lorentz.Vector n)
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) (i : Fin 1 ⊕ Fin n) :
    distOfFunction f hf η i = distOfFunction (fun x => f x i) (hf.vector_component i) η
```

## Depends on

- [Derivatives on Space](derivatives-basic.md)
- [Functions on `Space d` which can be made into distributions](isdistbounded.md)

## Sources

- [Physlib/SpaceAndTime/Space/DistOfFunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/DistOfFunction.lean)
