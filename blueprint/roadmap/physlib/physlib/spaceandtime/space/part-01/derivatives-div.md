---
declaration: module
origin: cited
lean: Space.div, Space.div_eq_sum_fderiv, Space.div_zero, Space.div_const, Space.div_add, Space.div_smul, Space.div_linear_map, Space.distDiv
statement: formalized
proof: formalized
---

# Divergence on Space

The module `Physlib.SpaceAndTime.Space.Derivatives.Div`, [Physlib/SpaceAndTime/Space/Derivatives/Div.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean): 11 declarations, 3 with a docstring.

## i. Overview

> In this module we define the divergence operator on functions and
> distributions from `Space d` to `EuclideanSpace ℝ (Fin d)`, and prove various basic
> properties about it.

## ii. Key results

> - `div` : The divergence operator on functions from `Space d` to `EuclideanSpace ℝ (Fin d)`.
> - `distDiv` : The divergence operator on distributions from `Space d` to `EuclideanSpace ℝ (Fin d)`.
> - `distDiv_ofFunction` : The divergence of a distribution from a bounded function.

## iv. References

> * None.

## A. The divergence on functions

**`Space.div`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L58).

> The vector calculus operator `div`.

```lean
noncomputable def div {d} (f : Space d → EuclideanSpace ℝ (Fin d)) :
    Space d → ℝ
```

**`Space.div_eq_sum_fderiv`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L68).

```lean
lemma div_eq_sum_fderiv {d} (f : Space d → EuclideanSpace ℝ (Fin d))
    (hf : Differentiable ℝ f) (x : Space d) :
    (∇ ⬝ f) x = ∑ i, fderiv ℝ f x (basis i) i
```

### A.1. The divergence on the zero function

**`Space.div_zero`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L86).

```lean
lemma div_zero : ∇ ⬝ (0 : Space d → EuclideanSpace ℝ (Fin d)) = 0
```

### A.2. The divergence on a constant function

**`Space.div_const`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L99).

```lean
lemma div_const : ∇ ⬝ (fun _ : Space d => v) = 0
```

### A.3. The divergence distributes over addition

**`Space.div_add`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L111).

```lean
lemma div_add (f1 f2 : Space d → EuclideanSpace ℝ (Fin d))
    (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    ∇ ⬝ (f1 + f2) = ∇ ⬝ f1 + ∇ ⬝ f2
```

### A.4. The divergence distributes over scalar multiplication

**`Space.div_smul`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L133).

```lean
lemma div_smul (f : Space d → EuclideanSpace ℝ (Fin d)) (k : ℝ)
    (hf : Differentiable ℝ f) :
    ∇ ⬝ (k • f) = k • ∇ ⬝ f
```

### A.5. The divergence of a linear map is a linear map

**`Space.div_linear_map`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L154).

```lean
lemma div_linear_map (f : W → Space 3 → EuclideanSpace ℝ (Fin 3))
    (hf : ∀ w, Differentiable ℝ (f w))
    (hf' : IsLinearMap ℝ f) :
    IsLinearMap ℝ (fun w => ∇ ⬝ (f w))
```

## B. Divergence of distributions

**`Space.distDiv`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L178).

> The divergence of a distribution `(Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d))` as a distribution
> `(Space d) →d[ℝ] ℝ`.

```lean
noncomputable def distDiv {d} :
    ((Space d) →d[ℝ] (EuclideanSpace ℝ (Fin d))) →ₗ[ℝ] (Space d) →d[ℝ] ℝ
```

### B.1. Basic equalities

**`Space.distDiv_apply_eq_sum_fderivD`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L209).

```lean
lemma distDiv_apply_eq_sum_fderivD {d}
    (f : (Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) (η : 𝓢(Space d, ℝ)) :
    (∇ᵈ ⬝ f) η = ∑ i, fderivD ℝ f η (basis i) i
```

**`Space.distDiv_apply_eq_sum_distDeriv`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L214).

```lean
lemma distDiv_apply_eq_sum_distDeriv {d}
    (f : (Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) (η : 𝓢(Space d, ℝ)) :
    (∇ᵈ ⬝ f) η = ∑ i, ∂ᵈ[i] f η i
```

### B.2. Divergence on distributions from bounded functions

**`Space.distDiv_ofFunction`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean#L227).

> The divergence of a distribution from a bounded function.

```lean
lemma distDiv_ofFunction {d : ℕ} {f : Space d → EuclideanSpace ℝ (Fin d)}
    {hf : IsDistBounded f} (η : 𝓢(Space d, ℝ)) :
    (∇ᵈ ⬝ (distOfFunction f hf)) η =
    - ∫ x : Space d, ⟪f x, ∇ η x⟫_ℝ
```

## Depends on

- [Gradient of functions and distributions on `Space d`](derivatives-grad.md)
- [Distributions from functions on space](distoffunction.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/Div.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Div.lean)
