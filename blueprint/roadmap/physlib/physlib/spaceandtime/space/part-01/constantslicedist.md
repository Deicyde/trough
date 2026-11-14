---
declaration: module
origin: cited
lean: Space.schwartzMap_slice_bound, Space.schwartzMap_mul_iteratedFDeriv_integrable_slice_symm, Space.schwartzMap_integrable_slice_symm, Space.schwartzMap_fderiv_integrable_slice_symm, Space.schwartzMap_fderiv_left_integrable_slice_symm, Space.schwartzMap_iteratedFDeriv_norm_slice_symm_integrable, Space.schwartzMap_iteratedFDeriv_slice_symm_integrable, Space.continuous_schwartzMap_slice_integral
statement: formalized
proof: formalized
---

# Constant slice distributions

The module `Physlib.SpaceAndTime.Space.ConstantSliceDist`, [Physlib/SpaceAndTime/Space/ConstantSliceDist.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean): 21 declarations, 2 with a docstring.

## i. Overview

> In this module we define the lift of distributions on `Space d` to distributions
> on `Space d.succ` which are constant between slices in the `i`th direction.
>
> This is used, for example, to define distributions which are translationally invariant
> in the `i`th direction.
>
> Examples of distributions which can be constructed in this way include the dirac deltas for
> lines and planes, rather then points.

## ii. Key results

> - `sliceSchwartz` : The continuous linear map which takes a Schwartz map on
>   `Space d.succ` and gives a Schwartz map on `Space d` by integrating over the `i`th direction.
> - `constantSliceDist` : The distribution on `Space d.succ` formed by a distribution on `Space d`
>   which is translationally invariant in the `i`th direction.

## iv. References

> * None.

## A. Schwartz maps

### A.1. Bounded condition for derivatives of Schwartz maps on slices

**`Space.schwartzMap_slice_bound`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L78).

```lean
lemma schwartzMap_slice_bound {n m} {d : ℕ} (i : Fin d.succ) :
    ∃ rt, ∀ (η : 𝓢(Space d.succ, ℝ)), ∃ k,
    Integrable (fun x : ℝ => ‖((1 + ‖x‖) ^ rt)⁻¹‖) volume ∧
    (∀ (x : Space d), ∀ r, ‖(slice i).symm (r, x)‖ ^ m *
      ‖iteratedFDeriv ℝ n ⇑η ((slice i).symm (r, x))‖ ≤ k * ‖(1 + ‖r‖) ^ (rt)‖⁻¹)
      ∧ k = (2 ^ (rt + m, n).1 * ((Finset.Iic (rt + m, n)).sup
        fun m => SchwartzMap.seminorm ℝ m.1 m.2) η)
```

### A.2. Integrability for of Schwartz maps on slices

**`Space.schwartzMap_mul_iteratedFDeriv_integrable_slice_symm`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L145).

```lean
lemma schwartzMap_mul_iteratedFDeriv_integrable_slice_symm {d : ℕ} (n m : ℕ)
    (η : 𝓢(Space d.succ, ℝ))
    (x : Space d) (i : Fin d.succ) :
    Integrable (fun r => ‖(slice i).symm (r, x)‖ ^ m *
    ‖iteratedFDeriv ℝ n ⇑η ((slice i).symm (r, x))‖) volume
```

**`Space.schwartzMap_integrable_slice_symm`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L168).

```lean
lemma schwartzMap_integrable_slice_symm {d : ℕ} (i : Fin d.succ) (η : 𝓢(Space d.succ, ℝ))
    (x : Space d) : Integrable (fun r => η ((slice i).symm (r, x))) volume
```

**`Space.schwartzMap_fderiv_integrable_slice_symm`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L174).

```lean
lemma schwartzMap_fderiv_integrable_slice_symm {d : ℕ} (η : 𝓢(Space d.succ, ℝ)) (x : Space d)
    (i : Fin d.succ) :
    Integrable (fun r => fderiv ℝ (fun x => η (((slice i).symm (r, x)))) x) volume
```

**`Space.schwartzMap_fderiv_left_integrable_slice_symm`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L198).

```lean
lemma schwartzMap_fderiv_left_integrable_slice_symm {d : ℕ} (η : 𝓢(Space d.succ, ℝ)) (x : Space d)
    (i : Fin d.succ) :
    Integrable (fun r => fderiv ℝ (fun r => η (((slice i).symm (r, x)))) r 1) volume
```

**`Space.schwartzMap_iteratedFDeriv_norm_slice_symm_integrable`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L214).

```lean
lemma schwartzMap_iteratedFDeriv_norm_slice_symm_integrable {n} {d : ℕ} (η : 𝓢(Space d.succ, ℝ))
    (x : Space d) (i : Fin d.succ) :
    Integrable (fun r => ‖iteratedFDeriv ℝ n ⇑η (((slice i).symm (r, x)))‖) volume
```

**`Space.schwartzMap_iteratedFDeriv_slice_symm_integrable`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L220).

```lean
lemma schwartzMap_iteratedFDeriv_slice_symm_integrable {n} {d : ℕ} (η : 𝓢(Space d.succ, ℝ))
    (x : Space d) (i : Fin d.succ) :
    Integrable (fun r => iteratedFDeriv ℝ n ⇑η (((slice i).symm (r, x)))) volume
```

### A.3. Continiuity of integrations of slices of Schwartz maps

**`Space.continuous_schwartzMap_slice_integral`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L237).

```lean
lemma continuous_schwartzMap_slice_integral {d} (i : Fin d.succ) (η : 𝓢(Space d.succ, ℝ)) :
    Continuous (fun x : Space d => ∫ r : ℝ, η ((slice i).symm (r, x)))
```

### A.4. Derivative of integrations of slices of Schwartz maps

**`Space.schwartzMap_slice_integral_hasFDerivAt`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L258).

```lean
lemma schwartzMap_slice_integral_hasFDerivAt {d : ℕ} (η : 𝓢(Space d.succ, ℝ)) (i : Fin d.succ)
    (x₀ : Space d) :
    HasFDerivAt (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x)))
      (∫ (r : ℝ), fderiv ℝ (fun x : Space d => η ((slice i).symm (r, x))) x₀) x₀
```

### A.5. Differentiability as a slices of Schwartz maps

**`Space.schwartzMap_slice_integral_differentiable`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L318).

```lean
lemma schwartzMap_slice_integral_differentiable {d : ℕ} (η : 𝓢(Space d.succ, ℝ))
    (i : Fin d.succ) :
    Differentiable ℝ (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x)))
```

### A.6. Smoothness as slices of Schwartz maps

**`Space.schwartzMap_slice_integral_contDiff`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L329).

```lean
lemma schwartzMap_slice_integral_contDiff {d : ℕ} (n : ℕ) (η : 𝓢(Space d.succ, ℝ))
    (i : Fin d.succ) :
    ContDiff ℝ n (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x)))
```

### A.7. Iterated derivatives of integrations of slices of Schwartz maps

**`Space.schwartzMap_slice_integral_iteratedFDeriv_apply`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L375).

```lean
lemma schwartzMap_slice_integral_iteratedFDeriv_apply {d : ℕ} (n : ℕ) (η : 𝓢(Space d.succ, ℝ))
    (i : Fin d.succ) :
    ∀ x, ∀ y, iteratedFDeriv ℝ n (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x))) x y =
      ∫ (r : ℝ), (iteratedFDeriv ℝ n η ((slice i).symm (r, x)))
      (fun j => (slice i).symm (0, y j))
```

**`Space.schwartzMap_slice_integral_iteratedFDeriv`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L432).

```lean
lemma schwartzMap_slice_integral_iteratedFDeriv {d : ℕ} (n : ℕ) (η : 𝓢(Space d.succ, ℝ))
    (i : Fin d.succ) (x : Space d) :
    iteratedFDeriv ℝ n (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x))) x
    = (∫ (r : ℝ), iteratedFDeriv ℝ n η ((slice i).symm (r, x))).compContinuousLinearMap
      (fun _ => (slice i).symm.toContinuousLinearMap.comp
      (ContinuousLinearMap.prod (0 : Space d →L[ℝ] ℝ) (ContinuousLinearMap.id ℝ (Space d))))
```

**`Space.schwartzMap_slice_integral_iteratedFDeriv_norm_le`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L443).

```lean
lemma schwartzMap_slice_integral_iteratedFDeriv_norm_le {d : ℕ} (n : ℕ) (η : 𝓢(Space d.succ, ℝ))
    (i : Fin d.succ) (x : Space d) :
    ‖iteratedFDeriv ℝ n (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x))) x‖ ≤
        (∫ (r : ℝ), ‖iteratedFDeriv ℝ n η ((slice i).symm (r, x))‖) *
        ‖(slice i).symm.toContinuousLinearMap.comp
          (ContinuousLinearMap.prod (0 : Space d →L[ℝ] ℝ)
          (ContinuousLinearMap.id ℝ (Space d)))‖ ^ n
```

**`Space.schwartzMap_mul_pow_slice_integral_iteratedFDeriv_norm_le`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L456).

```lean
lemma schwartzMap_mul_pow_slice_integral_iteratedFDeriv_norm_le {d : ℕ} (n m : ℕ) (i : Fin d.succ) :
    ∃ rt, ∀ (η : 𝓢(Space d.succ, ℝ)),∀ (x : Space d),
    Integrable (fun x : ℝ => ‖((1 + ‖x‖) ^ rt)⁻¹‖) volume ∧
    ‖x‖ ^ m * ‖iteratedFDeriv ℝ n (fun x => ∫ (r : ℝ), η ((slice i).symm (r, x))) x‖ ≤
        ((∫ (r : ℝ), ‖((1 + ‖r‖) ^ rt)⁻¹‖) *
        ‖(slice i).symm.toContinuousLinearMap.comp
          (ContinuousLinearMap.prod (0 : Space d →L[ℝ] ℝ)
          (ContinuousLinearMap.id ℝ (Space d)))‖ ^ n)
        * (2 ^ (rt + m, n).1 * ((Finset.Iic (rt + m, n)).sup
          fun m => SchwartzMap.seminorm ℝ m.1 m.2) η)
```

### A.8. The map integrating over one component of a Schwartz map

**`Space.sliceSchwartz`**, a def, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L520).

> The continuous linear map taking a Schwartz map and integrating over the `i`th component,
> to give a Schwartz map of one dimension lower.

```lean
def sliceSchwartz {d : ℕ} (i : Fin d.succ) :
    𝓢(Space d.succ, ℝ) →L[ℝ] 𝓢(Space d, ℝ)
```

**`Space.sliceSchwartz_apply`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L553).

```lean
lemma sliceSchwartz_apply {d : ℕ} (i : Fin d.succ) (η : 𝓢(Space d.succ, ℝ)) (x : Space d) :
    sliceSchwartz i η x = ∫ (r : ℝ), η ((slice i).symm (r, x))
```

## B. Constant slice distribution

**`Space.constantSliceDist`**, a def, [line 564](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L564).

> Distributions on `Space d.succ` from distributions on `Space d` given a
> direction `i`.
> These distributions are constant on slices in the `i` direction..

```lean
def constantSliceDist {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M] {d : ℕ} (i : Fin d.succ) :
    ((Space d) →d[ℝ] M) →ₗ[ℝ] (Space d.succ) →d[ℝ] M
```

**`Space.constantSliceDist_apply`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L574).

```lean
lemma constantSliceDist_apply {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {d : ℕ} (i : Fin d.succ) (f : (Space d) →d[ℝ] M) (η : 𝓢(Space d.succ, ℝ)) :
    constantSliceDist i f η = f (sliceSchwartz i η)
```

### B.1. Derivative of constant slice distributions

**`Space.distDeriv_constantSliceDist_same`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L585).

```lean
lemma distDeriv_constantSliceDist_same {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {d : ℕ} (i : Fin d.succ) (f : (Space d) →d[ℝ] M) :
    distDeriv i (constantSliceDist i f) = 0
```

**`Space.distDeriv_constantSliceDist_succAbove`**, a lemma, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean#L615).

```lean
lemma distDeriv_constantSliceDist_succAbove {M : Type} [NormedAddCommGroup M] [NormedSpace ℝ M]
    {d : ℕ} (i : Fin d.succ) (j : Fin d) (f : (Space d) →d[ℝ] M) :
    distDeriv (i.succAbove j) (constantSliceDist i f) =
    constantSliceDist i (distDeriv j f)
```

## Depends on

- [Derivatives on Space](derivatives-basic.md)
- [Slices of space](slice.md)

## Sources

- [Physlib/SpaceAndTime/Space/ConstantSliceDist.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/ConstantSliceDist.lean)
