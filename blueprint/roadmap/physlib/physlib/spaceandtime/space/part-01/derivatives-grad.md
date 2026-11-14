---
declaration: module
origin: cited
lean: Space.grad, Space.grad_zero, Space.grad_add, Space.grad_fun_add_const, Space.grad_const, Space.grad_smul, Space.grad_neg, Space.grad_eq_sum
statement: formalized
proof: formalized
---

# Gradient of functions and distributions on `Space d`

The module `Physlib.SpaceAndTime.Space.Derivatives.Grad`, [Physlib/SpaceAndTime/Space/Derivatives/Grad.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean): 40 declarations, 5 with a docstring.

## i. Overview

> This module defines and proves basic properties of the gradient operator
> on functions from `Space d` to `ℝ` and on distributions from `Space d` to `ℝ`.
>
> The gradient operator returns a vector field whose components are the partial derivatives
> of the input function with respect to each spatial coordinate.

## ii. Key results

> - `grad` : The gradient operator on functions from `Space d` to `ℝ`.
> - `distGrad` : The gradient operator on distributions from `Space d` to `ℝ`.

## iv. References

> * None.

## A. The gradient of functions on `Space d`

**`Space.grad`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L72).

> The vector calculus operator `grad`.

```lean
noncomputable def grad {d} (f : Space d → ℝ) :
  Space d → EuclideanSpace ℝ (Fin d)
```

### A.1. Gradient of the zero function

**`Space.grad_zero`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L85).

```lean
lemma grad_zero : ∇ (0 : Space d → ℝ) = 0
```

### A.2. Gradient distributes over addition

**`Space.grad_add`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L97).

```lean
lemma grad_add (f1 f2 : Space d → ℝ)
    (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    ∇ (f1 + f2) = ∇ f1 + ∇ f2
```

**`Space.grad_fun_add_const`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L107).

```lean
lemma grad_fun_add_const (f : Space d → ℝ) (c : ℝ) :
    ∇ (fun x => f x + c) = ∇ f
```

### A.3. Gradient of a constant function

**`Space.grad_const`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L119).

```lean
lemma grad_const : ∇ (fun _ : Space d => c) = 0
```

### A.4. Gradient distributes over scalar multiplication

**`Space.grad_smul`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L131).

```lean
lemma grad_smul (f : Space d → ℝ) (k : ℝ)
    (hf : Differentiable ℝ f) :
    ∇ (k • f) = k • ∇ f
```

### A.5. Gradient distributes over negation

**`Space.grad_neg`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L147).

```lean
lemma grad_neg (f : Space d → ℝ) :
    ∇ (- f) = - ∇ f
```

### A.6. Expansion in terms of basis vectors

**`Space.grad_eq_sum`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L161).

```lean
lemma grad_eq_sum {d} (f : Space d → ℝ) (x : Space d) :
    ∇ f x = ∑ i, ∂[i] f x • EuclideanSpace.single i 1
```

### A.7. Components of the gradient

**`Space.grad_apply`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L174).

```lean
lemma grad_apply {d} (f : Space d → ℝ) (x : Space d) (i : Fin d) :
    (∇ f x) i = ∂[i] f x
```

### A.8. Inner product with a gradient

**`Space.grad_inner_single`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L186).

```lean
lemma grad_inner_single {d} (f : Space d → ℝ) (x : Space d) (i : Fin d) :
    ⟪∇ f x, EuclideanSpace.single i 1⟫_ℝ = ∂[i] f x
```

**`Space.grad_inner_eq`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L190).

```lean
lemma grad_inner_eq {d} (f : Space d → ℝ) (x : Space d) (y : EuclideanSpace ℝ (Fin d)) :
    ⟪∇ f x, y⟫_ℝ = ∑ i, y i * ∂[i] f x
```

**`Space.inner_grad_eq`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L194).

```lean
lemma inner_grad_eq {d} (f : Space d → ℝ) (x : EuclideanSpace ℝ (Fin d)) (y : Space d) :
    ⟪x, ∇ f y⟫_ℝ = ∑ i, x i * ∂[i] f y
```

**`Space.grad_inner_repr_eq`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L198).

```lean
lemma grad_inner_repr_eq {d} (f : Space d → ℝ) (x y : Space d) :
    ⟪∇ f x, (Space.basis).repr y⟫_ℝ = fderiv ℝ f x y
```

**`Space.repr_grad_inner_eq`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L202).

```lean
lemma repr_grad_inner_eq {d} (f : Space d → ℝ) (x y : Space d) :
    ⟪(Space.basis).repr x, ∇ f y⟫_ℝ = fderiv ℝ f y x
```

### A.9. Gradient is equal to `gradient` from Mathlib

**`Space.grad_eq_gradient`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L212).

```lean
lemma grad_eq_gradient {d} (f : Space d → ℝ) :
    ∇ f = basis.repr ∘ gradient f
```

**`Space.gradient_eq_grad`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L219).

```lean
lemma gradient_eq_grad {d} (f : Space d → ℝ) :
    gradient f = basis.repr.symm ∘ ∇ f
```

**`Space.gradient_apply_eq_grad`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L225).

```lean
lemma gradient_apply_eq_grad {d} (f : Space d → ℝ) (x : Space d) :
    gradient f x = basis.repr.symm (∇ f x)
```

**`Space.gradient_eq_sum`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L230).

```lean
lemma gradient_eq_sum {d} (f : Space d → ℝ) (x : Space d) :
    gradient f x = ∑ i, ∂[i] f x • basis i
```

**`Space.euclid_gradient_eq_sum`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L234).

```lean
lemma euclid_gradient_eq_sum {d} (f : EuclideanSpace ℝ (Fin d) → ℝ) (x : EuclideanSpace ℝ (Fin d)) :
    gradient f x = ∑ i, fderiv ℝ f x (EuclideanSpace.single i 1) • EuclideanSpace.single i 1
```

**`DifferentiableAt.hasGradientAt_grad`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L244).

```lean
lemma _root_.DifferentiableAt.hasGradientAt_grad {d} {f : Space d → ℝ} (x : Space d)
    (hf : DifferentiableAt ℝ f x) :
    HasGradientAt f (basis.repr.symm (∇ f x)) x
```

### A.10. Value of gradient in the direction of the position vector

**`Space.grad_inner_space_unit_vector`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L257).

> The gradient in the direction of the space position.

```lean
lemma grad_inner_space_unit_vector {d} (x : Space d) (f : Space d → ℝ) (hd : Differentiable ℝ f) :
    ⟪∇ f x, ‖x‖⁻¹ • basis.repr x⟫_ℝ = _root_.deriv (fun r => f (r • ‖x‖⁻¹ • x)) ‖x‖
```

**`Space.grad_inner_space`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L277).

```lean
lemma grad_inner_space {d} (x : Space d) (f : Space d → ℝ) (hd : Differentiable ℝ f) :
    ⟪∇ f x, basis.repr x⟫_ℝ = ‖x‖ * _root_.deriv (fun r => f (r • ‖x‖⁻¹ • x)) ‖x‖
```

**`Space.grad_smul_inner_space`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L286).

```lean
lemma grad_smul_inner_space {d} (x : Space d) (f : Space d → ℝ) (hd : Differentiable ℝ f) (t : ℝ)
    (ht : 0 < t) :
    ⟪∇ f (t • x), basis.repr x⟫_ℝ = _root_.deriv (fun r => f (r • x)) t
```

**`Space.eq_integral_grad`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L316).

```lean
lemma eq_integral_grad {f : Space → ℝ} (hf : ContDiff ℝ 1 f) :
    f = (fun x => ∫ t in (0 : ℝ)..1, ⟪∇ f (t • x), basis.repr x⟫_ℝ ∂(volume)
      + f 0)
```

### A.11. Gradient of the norm squared function

**`Space.grad_norm_sq`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L351).

```lean
lemma grad_norm_sq (x : Space d) :
    ∇ (fun x => ‖x‖ ^ 2) x = (2 : ℝ) • basis.repr x
```

### A.12. Gradient of the inner product function

**`Space.grad_inner`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L364).

> The gradient of the inner product is given by `2 • x`.

```lean
lemma grad_inner {d : ℕ} :
    ∇ (fun y : Space d => ⟪y, y⟫_ℝ) = fun z => (2 : ℝ) • basis.repr z
```

**`Space.grad_inner_left`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L370).

```lean
lemma grad_inner_left {d : ℕ} (x : Space d) :
    ∇ (fun y : Space d => ⟪y, x⟫_ℝ) = fun _ => basis.repr x
```

**`Space.grad_inner_right`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L375).

```lean
lemma grad_inner_right {d : ℕ} (x : Space d) :
    ∇ (fun y : Space d => ⟪x, y⟫_ℝ) = fun _ => basis.repr x
```

### A.13. Integrability with bounded functions

**`Space.integrable_isDistBounded_inner_grad_schwartzMap`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L390).

```lean
lemma integrable_isDistBounded_inner_grad_schwartzMap {d : ℕ}
    {f : Space d → EuclideanSpace ℝ (Fin d)}
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) :
    Integrable (fun x => ⟪f x, Space.grad η x⟫_ℝ) volume
```

**`Space.integrable_isDistBounded_inner_grad_schwartzMap_spherical`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L412).

```lean
lemma integrable_isDistBounded_inner_grad_schwartzMap_spherical {d : ℕ}
    {f : Space d → EuclideanSpace ℝ (Fin d)}
    (hf : IsDistBounded f) (η : 𝓢(Space d, ℝ)) :
    Integrable ((fun x => ⟪f x.1, Space.grad η x.1⟫_ℝ)
      ∘ (homeomorphUnitSphereProd (Space d)).symm)
      ((volume (α := Space d)).toSphere.prod
      (Measure.volumeIoiPow (Module.finrank ℝ (Space d) - 1)))
```

### A.14. Differentiability of gradient

**`Space.contDiff_grad`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L442).

```lean
lemma contDiff_grad {n} {f : Space → ℝ} (hf : ContDiff ℝ (n + 1) f) :
    ContDiff ℝ n (fun x => ∇ f x)
```

## B. Gradient of distributions

### B.1. The definition

**`Space.distGrad`**, a def, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L463).

> The gradient of a distribution `(Space d) →d[ℝ] ℝ` as a distribution
> `(Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d))`.

```lean
noncomputable def distGrad {d} :
    ((Space d) →d[ℝ] ℝ) →ₗ[ℝ] (Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d))
```

### B.2. The gradient of inner products

**`Space.distGrad_inner_eq`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L483).

```lean
lemma distGrad_inner_eq {d} (f : (Space d) →d[ℝ] ℝ) (η : 𝓢(Space d, ℝ))
    (y : EuclideanSpace ℝ (Fin d)) : ⟪∇ᵈ f η, y⟫_ℝ = fderivD ℝ f η (basis.repr.symm y)
```

**`Space.distGrad_eq_of_inner`**, a lemma, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L491).

```lean
lemma distGrad_eq_of_inner {d} (f : (Space d) →d[ℝ] ℝ)
    (g : (Space d) →d[ℝ] EuclideanSpace ℝ (Fin d))
    (h : ∀ η y, fderivD ℝ f η y = ⟪g η, basis.repr y⟫_ℝ) :
    ∇ᵈ f = g
```

### B.3. The gradient as a sum over basis vectors

**`Space.distGrad_eq_sum_basis`**, a lemma, [line 505](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L505).

```lean
lemma distGrad_eq_sum_basis {d} (f : (Space d) →d[ℝ] ℝ) (η : 𝓢(Space d, ℝ)) :
    ∇ᵈ f η =
      ∑ i, - f (SchwartzMap.evalCLM ℝ (Space d) ℝ (basis i) (fderivCLM ℝ (Space d) ℝ η)) •
      EuclideanSpace.single i 1
```

### B.4. The underlying function of the gradient distribution

**`Space.distGrad_toFun_eq_distDeriv`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L527).

```lean
lemma distGrad_toFun_eq_distDeriv {d} (f : (Space d) →d[ℝ] ℝ) :
    (∇ᵈ f).toFun = fun ε => WithLp.toLp 2 fun i => ∂ᵈ[i] f ε
```

### B.5. The gradient applied to a Schwartz function

**`Space.distGrad_apply`**, a lemma, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L543).

```lean
lemma distGrad_apply {d} (f : (Space d) →d[ℝ] ℝ) (ε : 𝓢(Space d, ℝ)) :
    (∇ᵈ f) ε = fun i => ∂ᵈ[i] f ε
```

### B.6. Gradient of constant distributions

**`Space.distGrad_const`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L555).

```lean
lemma distGrad_const {d} (c : ℝ) :
    ∇ᵈ (Distribution.const ℝ (Space d) c) = 0
```

### B.7. The gradient of a Schwartz map

**`Space.gradSchwartz`**, a def, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L567).

> The gradient on Scwhwartz maps.

```lean
noncomputable def gradSchwartz {d} : 𝓢(Space d, ℝ) →L[ℝ] 𝓢(Space d, EuclideanSpace ℝ (Fin d))
```

**`Space.gradSchwartz_apply_eq_grad`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean#L573).

```lean
lemma gradSchwartz_apply_eq_grad {d} (η : 𝓢(Space d, ℝ)) (x : Space d) :
    gradSchwartz η x = ∇ η x
```

## Depends on

- [Derivatives on Space](derivatives-basic.md)
- [Functions on `Space d` which can be made into distributions](isdistbounded.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/Grad.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Grad.lean)
