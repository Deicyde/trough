---
declaration: module
origin: cited
lean: Space.normPowerSeries, Space.normPowerSeries_eq, Space.normPowerSeries_eq_rpow, Space.normPowerSeries_differentiable, Space.normPowerSeries_tendsto, Space.normPowerSeries_inv_tendsto, Space.deriv_normPowerSeries, Space.fderiv_normPowerSeries
statement: formalized
proof: formalized
---

# The norm on space

The module `Physlib.SpaceAndTime.Space.Norm.Basic`, [Physlib/SpaceAndTime/Space/Norm/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean): 47 declarations, 6 with a docstring; 3 private, not shown.

## i. Overview

> The main content of this file is defining `Space.normPowerSeries`, a sequence of smooth
> functions which are differentiable everywhere, and which tend to the norm in the limit as `n → ∞`.
>
> We use properties of this sequence to prove various results about distributions involving norms.

## ii. Key results

> - `normPowerSeries` : A sequence of functions which are differentiable everywhere, and in the limit
>   as `n → ∞` tends to `‖x‖`.
> - `normPowerSeries_differentiable` : Each `normPowerSeries n` is differentiable everywhere.
> - `normPowerSeries_tendsto` : `normPowerSeries n` tends to the norm in the limit as `n → ∞`.
> - `distGrad_distOfFunction_norm_zpow` : The gradient of the distribution defined by a power of the
>   norm.
> - `distGrad_distOfFunction_log_norm` : The gradient of the distribution defined by the logarithm
>   of the norm.
> - `distDiv_norm_zpow_smul_repr_self_eq_smul` : The divergence of the distribution defined by
>   `x ↦ ‖x‖ ^ q • x`.
> - `distLaplacian_distOfFunction_norm_zpow` : The Laplacian of the distribution defined by a power
>   of the norm.
> - `distDiv_inv_pow_eq_dim` : The divergence of `x ↦ ‖x‖ ^ (-d) • x` equals `d * volume (ball 0 1)`
>   times the Dirac delta at the origin.
> - `distLaplacian_fundamentalSolution_norm_zpow` : The Laplacian of the power-form fundamental
>   solution `‖x‖ ^ (2 - d)`, in every dimension (trivial at `d = 0, 2`).
> - `distLaplacian_fundamentalSolution_log_norm` : The Laplacian of the two-dimensional logarithmic
>   fundamental solution `Real.log ‖x‖`.

## iv. References

> * None.

## A. The norm as a limit of smooth functions

**`Space.normPowerSeries`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L92).

> A sequence of functions which are differentiable everywhere, and in the limit
> as `n → ∞` tends to `‖x‖`.

```lean
def normPowerSeries {d} : ℕ → Space d → ℝ
```

**`Space.normPowerSeries_eq`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L95).

```lean
lemma normPowerSeries_eq (n : ℕ) :
    normPowerSeries (d := d) n = fun x => √(‖x‖ ^ 2 + 1/(n + 1))
```

**`Space.normPowerSeries_eq_rpow`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L98).

```lean
lemma normPowerSeries_eq_rpow {d} (n : ℕ) :
    normPowerSeries (d := d) n = fun x => ((‖x‖ ^ 2 + 1/(n + 1))) ^ (1/2 : ℝ)
```

### A.1. Differentiability of the smooth approximation of the norm

**`Space.normPowerSeries_differentiable`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L109).

```lean
lemma normPowerSeries_differentiable {d} (n : ℕ) :
    Differentiable ℝ (fun (x : Space d) => normPowerSeries n x)
```

### A.2. The limit of the smooth approximation of the norm

**`Space.normPowerSeries_tendsto`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L124).

```lean
lemma normPowerSeries_tendsto {d} (x : Space d) :
    Filter.Tendsto (fun n => normPowerSeries n x) Filter.atTop (𝓝 (‖x‖))
```

**`Space.normPowerSeries_inv_tendsto`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L131).

```lean
lemma normPowerSeries_inv_tendsto {d} (x : Space d) (hx : x ≠ 0) :
    Filter.Tendsto (fun n => (normPowerSeries n x)⁻¹) Filter.atTop (𝓝 (‖x‖⁻¹))
```

### A.3. The derivative of the smooth approximation of the norm

**`Space.deriv_normPowerSeries`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L142).

```lean
lemma deriv_normPowerSeries {d} (n : ℕ) (x : Space d) (i : Fin d) :
    ∂[i] (normPowerSeries n) x = x i * (normPowerSeries n x)⁻¹
```

**`Space.fderiv_normPowerSeries`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L152).

```lean
lemma fderiv_normPowerSeries {d} (n : ℕ) (x y : Space d) :
    fderiv ℝ (fun (x : Space d) => normPowerSeries n x) x y =
      ⟪y, x⟫_ℝ * (normPowerSeries n x)⁻¹
```

### A.4. Limits of the derivative of the smooth approximation

**`Space.deriv_normPowerSeries_tendsto`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L165).

> The coordinate derivatives of `normPowerSeries` converge pointwise, including at zero.

```lean
lemma deriv_normPowerSeries_tendsto {d} (x : Space d) (i : Fin d) :
    Filter.Tendsto (fun n => ∂[i] (normPowerSeries n) x) Filter.atTop (𝓝 (x i * (‖x‖)⁻¹))
```

**`Space.fderiv_normPowerSeries_tendsto`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L174).

> For every fixed direction, the derivatives of `normPowerSeries` converge pointwise,
> including at zero.

```lean
lemma fderiv_normPowerSeries_tendsto {d} (x y : Space d) :
    Filter.Tendsto (fun n => fderiv ℝ (fun (x : Space d) => normPowerSeries n x) x y)
      Filter.atTop (𝓝 (⟪y, x⟫_ℝ * (‖x‖)⁻¹))
```

### A.5. The smooth approximation is AEStronglyMeasurable

**`Space.normPowerSeries_aestronglyMeasurable`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L189).

```lean
lemma normPowerSeries_aestronglyMeasurable {d} (n : ℕ) :
    AEStronglyMeasurable (normPowerSeries n : Space d → ℝ) volume
```

### A.6. Bounds on the smooth approximation of the norm

**`Space.normPowerSeries_nonneg`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L200).

```lean
lemma normPowerSeries_nonneg {d} (n : ℕ) (x : Space d) :
    0 ≤ normPowerSeries n x
```

**`Space.normPowerSeries_pos`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L205).

```lean
lemma normPowerSeries_pos {d} (n : ℕ) (x : Space d) :
    0 < normPowerSeries n x
```

**`Space.normPowerSeries_ne_zero`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L210).

```lean
lemma normPowerSeries_ne_zero {d} (n : ℕ) (x : Space d) :
    normPowerSeries n x ≠ 0
```

**`Space.normPowerSeries_le_norm_sq_add_one`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L214).

```lean
lemma normPowerSeries_le_norm_sq_add_one {d} (n : ℕ) (x : Space d) :
    normPowerSeries n x ≤ ‖x‖ + 1
```

**`Space.norm_lt_normPowerSeries`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L222).

```lean
lemma norm_lt_normPowerSeries {d} (n : ℕ) (x : Space d) :
    ‖x‖ < normPowerSeries n x
```

**`Space.norm_le_normPowerSeries`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L226).

```lean
lemma norm_le_normPowerSeries {d} (n : ℕ) (x : Space d) :
    ‖x‖ ≤ normPowerSeries n x
```

**`Space.normPowerSeries_zpow_le_norm_sq_add_one`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L230).

```lean
lemma normPowerSeries_zpow_le_norm_sq_add_one {d} (n : ℕ) (m : ℤ) (x : Space d)
    (hx : x ≠ 0) :
    (normPowerSeries n x) ^ m ≤ (‖x‖ + 1) ^ m + ‖x‖ ^ m
```

**`Space.normPowerSeries_inv_le`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L242).

```lean
lemma normPowerSeries_inv_le {d} (n : ℕ) (x : Space d) (hx : x ≠ 0) :
    (normPowerSeries n x)⁻¹ ≤ ‖x‖⁻¹
```

**`Space.normPowerSeries_log_le_normPowerSeries`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L246).

```lean
lemma normPowerSeries_log_le_normPowerSeries {d} (n : ℕ) (x : Space d) :
    |Real.log (normPowerSeries n x)| ≤ (normPowerSeries n x)⁻¹ + (normPowerSeries n x)
```

**`Space.normPowerSeries_log_le`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L252).

```lean
lemma normPowerSeries_log_le {d} (n : ℕ) (x : Space d) (hx : x ≠ 0) :
    |Real.log (normPowerSeries n x)| ≤ ‖x‖⁻¹ + (‖x‖ + 1)
```

### A.7. The `IsDistBounded` property of the smooth approximation of the norm

**`Space.IsDistBounded.normPowerSeries_zpow`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L264).

```lean
lemma IsDistBounded.normPowerSeries_zpow {d : ℕ} {n : ℕ} (m : ℤ) :
    IsDistBounded (d := d) (fun x => (normPowerSeries n x) ^ m)
```

**`Space.IsDistBounded.normPowerSeries_single`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L290).

```lean
lemma IsDistBounded.normPowerSeries_single {d : ℕ} {n : ℕ} :
    IsDistBounded (d := d) (fun x => (normPowerSeries n x))
```

**`Space.IsDistBounded.normPowerSeries_inv`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L295).

```lean
lemma IsDistBounded.normPowerSeries_inv {d : ℕ} {n : ℕ} :
    IsDistBounded (d := d) (fun x => (normPowerSeries n x)⁻¹)
```

**`Space.IsDistBounded.normPowerSeries_deriv`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L300).

```lean
lemma IsDistBounded.normPowerSeries_deriv {d : ℕ} (n : ℕ) (i : Fin d) :
    IsDistBounded (d := d) (fun x => ∂[i] (normPowerSeries n) x)
```

**`Space.IsDistBounded.normPowerSeries_fderiv`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L306).

```lean
lemma IsDistBounded.normPowerSeries_fderiv {d : ℕ} (n : ℕ) (y : Space d) :
    IsDistBounded (d := d) (fun x => fderiv ℝ (fun (x : Space d) => normPowerSeries n x) x y)
```

**`Space.IsDistBounded.normPowerSeries_log`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L312).

```lean
lemma IsDistBounded.normPowerSeries_log {d : ℕ} (n : ℕ) :
    IsDistBounded (d := d) (fun x => Real.log (normPowerSeries n x))
```

### A.8. Differentiability of functions

**`Space.differentiable_normPowerSeries_zpow`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L327).

```lean
lemma differentiable_normPowerSeries_zpow {d : ℕ} {n : ℕ} (m : ℤ) :
    Differentiable ℝ (fun x : Space d => (normPowerSeries n x) ^ m)
```

**`Space.differentiable_normPowerSeries_inv`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L332).

```lean
lemma differentiable_normPowerSeries_inv {d : ℕ} {n : ℕ} :
    Differentiable ℝ (fun x : Space d => (normPowerSeries n x)⁻¹)
```

**`Space.differentiable_log_normPowerSeries`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L337).

```lean
lemma differentiable_log_normPowerSeries {d : ℕ} {n : ℕ} :
    Differentiable ℝ (fun x : Space d => Real.log (normPowerSeries n x))
```

### A.9. Derivatives of functions

**`Space.deriv_normPowerSeries_zpow`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L346).

```lean
lemma deriv_normPowerSeries_zpow {d : ℕ} {n : ℕ} (m : ℤ) (x : Space d) (i : Fin d) :
    ∂[i] (fun x : Space d => (normPowerSeries n x) ^ m) x =
      m * x i * (normPowerSeries n x) ^ (m - 2)
```

**`Space.fderiv_normPowerSeries_zpow`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L359).

```lean
lemma fderiv_normPowerSeries_zpow {d : ℕ} {n : ℕ} (m : ℤ) (x y : Space d) :
    fderiv ℝ (fun x : Space d => (normPowerSeries n x) ^ m) x y =
      m * ⟪y, x⟫_ℝ * (normPowerSeries n x) ^ (m - 2)
```

**`Space.deriv_log_normPowerSeries`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L366).

```lean
lemma deriv_log_normPowerSeries {d : ℕ} {n : ℕ} (x : Space d) (i : Fin d) :
    ∂[i] (fun x : Space d => Real.log (normPowerSeries n x)) x =
      x i * (normPowerSeries n x) ^ (-2 : ℤ)
```

**`Space.fderiv_log_normPowerSeries`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L379).

```lean
lemma fderiv_log_normPowerSeries {d : ℕ} {n : ℕ} (x y : Space d) :
    fderiv ℝ (fun x : Space d => Real.log (normPowerSeries n x)) x y =
      ⟪y, x⟫_ℝ * (normPowerSeries n x) ^ (-2 : ℤ)
```

### A.10. Gradients of distributions based on powers

**`Space.gradient_dist_normPowerSeries_zpow`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L391).

```lean
lemma gradient_dist_normPowerSeries_zpow {d : ℕ} {n : ℕ} (m : ℤ) :
    ∇ᵈ (distOfFunction (fun x : Space d => (normPowerSeries n x) ^ m) (by fun_prop)) =
    distOfFunction (fun x : Space d => (m * (normPowerSeries n x) ^ (m - 2)) • basis.repr x)
    (by fun_prop)
```

#### A.10.1. The limits of gradients of distributions based on powers

**`Space.gradient_dist_normPowerSeries_zpow_tendsTo_distGrad_norm`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L427).

```lean
lemma gradient_dist_normPowerSeries_zpow_tendsTo_distGrad_norm {d : ℕ} [NeZero d] (m : ℤ)
    (hm : - (d - 1 : ℕ) ≤ m) (η : 𝓢(Space d, ℝ))
    (y : EuclideanSpace ℝ (Fin d)) :
    Filter.Tendsto (fun n =>
    ⟪(∇ᵈ (distOfFunction
    (fun x : Space d => (normPowerSeries n x) ^ m) (by fun_prop))) η, y⟫_ℝ)
    Filter.atTop
    (𝓝 (⟪∇ᵈ (distOfFunction (fun x : Space d => ‖x‖ ^ m)
    (IsDistBounded.pow m hm)) η, y⟫_ℝ))
```

**`Space.gradient_dist_normPowerSeries_zpow_tendsTo`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L462).

```lean
lemma gradient_dist_normPowerSeries_zpow_tendsTo {d : ℕ} [NeZero d] (m : ℤ)
    (hm : - (d - 1 : ℕ) + 1 ≤ m)
    (η : 𝓢(Space d, ℝ)) (y : EuclideanSpace ℝ (Fin d)) :
    Filter.Tendsto (fun n =>
    ⟪(∇ᵈ (distOfFunction (fun x : Space d => (normPowerSeries n x) ^ m)
    (by fun_prop))) η, y⟫_ℝ)
    Filter.atTop
    (𝓝 (⟪distOfFunction (fun x : Space d => (m * ‖x‖ ^ (m - 2)) • basis.repr x) (by
    simp [← smul_smul]
    refine IsDistBounded.const_fun_smul ?_ ↑m
    apply IsDistBounded.zpow_smul_repr_self
    omega) η, y⟫_ℝ))
```

### A.11. Gradients of distributions based on logs

**`Space.gradient_dist_normPowerSeries_log`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L541).

```lean
lemma gradient_dist_normPowerSeries_log {d : ℕ} {n : ℕ} :
    ∇ᵈ (distOfFunction (fun x : Space d => Real.log (normPowerSeries n x)) (by fun_prop)) =
    distOfFunction (fun x : Space d => ((normPowerSeries n x) ^ (- 2 : ℤ)) • basis.repr x)
    (by fun_prop)
```

#### A.11.1. The limits of gradients of distributions based on logs

**`Space.gradient_dist_normPowerSeries_log_tendsTo_distGrad_norm`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L577).

```lean
lemma gradient_dist_normPowerSeries_log_tendsTo_distGrad_norm {d : ℕ} (hd : 2 ≤ d)
    (η : 𝓢(Space d, ℝ)) (y : EuclideanSpace ℝ (Fin d)) :
    Filter.Tendsto (fun n =>
    ⟪(∇ᵈ (distOfFunction
    (fun x : Space d => Real.log (normPowerSeries n x)) (by fun_prop))) η, y⟫_ℝ)
    Filter.atTop
    (𝓝 (⟪∇ᵈ (distOfFunction (fun x : Space d => Real.log ‖x‖)
    (IsDistBounded.log_norm)) η, y⟫_ℝ))
```

**`Space.gradient_dist_normPowerSeries_log_tendsTo`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L611).

```lean
lemma gradient_dist_normPowerSeries_log_tendsTo {d : ℕ} (hd : 2 ≤ d)
    (η : 𝓢(Space d, ℝ)) (y : EuclideanSpace ℝ (Fin d)) :
    Filter.Tendsto (fun n =>
    ⟪(∇ᵈ (distOfFunction (fun x : Space d => Real.log (normPowerSeries n x))
    (by fun_prop))) η, y⟫_ℝ)
    Filter.atTop
    (𝓝 (⟪distOfFunction (fun x : Space d => (‖x‖ ^ (- 2 : ℤ)) • basis.repr x) (by
    refine (IsDistBounded.zpow_smul_repr_self _ ?_)
    omega) η, y⟫_ℝ))
```

## B. Distributions involving norms

### B.1. The gradient of distributions based on powers

**`Space.distGrad_distOfFunction_norm_zpow`**, a lemma, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L675).

```lean
lemma distGrad_distOfFunction_norm_zpow {d : ℕ} [NeZero d]
    (m : ℤ) (hm : - (d - 1 : ℕ) + 1 ≤ m) :
    ∇ᵈ (distOfFunction (fun x : Space d => ‖x‖ ^ m)
      (IsDistBounded.pow m (by omega)))
    = distOfFunction (fun x : Space d => (m * ‖x‖ ^ (m - 2)) • basis.repr x) (by
      simp [← smul_smul]
      refine IsDistBounded.const_fun_smul ?_ ↑m
      apply IsDistBounded.zpow_smul_repr_self
      omega)
```

### B.2. The gradient of distributions based on logs

**`Space.distGrad_distOfFunction_log_norm`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L695).

```lean
lemma distGrad_distOfFunction_log_norm {d : ℕ} (hd : 2 ≤ d := by omega) :
    ∇ᵈ (distOfFunction (fun x : Space d => Real.log ‖x‖)
      (IsDistBounded.log_norm))
    = distOfFunction (fun x : Space d => (‖x‖ ^ (- 2 : ℤ)) • basis.repr x) (by
      refine (IsDistBounded.zpow_smul_repr_self _ ?_)
      omega)
```

### B.3. Divergence of radial norm-power distributions

**`Space.distDiv_norm_zpow_smul_repr_self_eq_smul`**, a lemma, [line 877](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L877).

```lean
lemma distDiv_norm_zpow_smul_repr_self_eq_smul
    {d : ℕ} [NeZero d] (q : ℤ) (hq : 0 < q + (d : ℤ)) :
    ∇ᵈ ⬝ (distOfFunction (fun x : Space d => ‖x‖ ^ q • basis.repr x)
      (IsDistBounded.zpow_smul_repr_self q (by omega))) =
      (((q + d : ℤ) : ℝ) •
        distOfFunction (fun x : Space d => ‖x‖ ^ q)
          (IsDistBounded.pow q (by omega)))
```

### B.4. The Laplacian of distributions based on powers

**`Space.distLaplacian_distOfFunction_norm_zpow`**, a lemma, [line 925](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L925).

```lean
lemma distLaplacian_distOfFunction_norm_zpow {d : ℕ} [NeZero d] (m : ℤ)
    (hdiv : 0 < m - 2 + (d : ℤ)) :
    Δᵈ (distOfFunction (fun x : Space d => ‖x‖ ^ m)
      (IsDistBounded.pow m (by omega))) =
      (((m : ℝ) * (((m - 2 + d : ℤ) : ℝ))) •
        distOfFunction (fun x : Space d => ‖x‖ ^ (m - 2))
          (IsDistBounded.pow (m - 2) (by omega)))
```

### B.5. Divergence equal dirac delta

> We show that the divergence of `x ↦ ‖x‖ ^ (- d) • x` is equal to a multiple of the Dirac delta
> at `0`.

**`Space.distDiv_inv_pow_eq_dim`**, a lemma, [line 964](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L964).

> The distributional divergence of the radial field `x ↦ ‖x‖ ^ (-d) • x` (i.e. `x / ‖x‖ ^ d`)
> equals `d * volume (Metric.ball 0 1)` — the surface area of the unit sphere `S^{d-1}` — times the
> Dirac delta at the origin. This is the Gauss-law identity underlying the fundamental solution of
> the Laplacian: away from `0` the field is divergence-free, and all of its flux concentrates at the
> origin.

```lean
lemma distDiv_inv_pow_eq_dim {d : ℕ} [NeZero d] :
    ∇ᵈ ⬝ (distOfFunction (fun x : Space d => ‖x‖ ^ (- d : ℤ) • basis.repr x)
      (IsDistBounded.zpow_smul_repr_self (- d : ℤ) (by omega))) =
      (d * (volume (α := Space d)).real (Metric.ball 0 1)) • diracDelta ℝ 0
```

### B.6. The Laplacian of the fundamental solution

**`Space.distLaplacian_fundamentalSolution_norm_zpow`**, a lemma, [line 1094](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L1094).

> The distributional Laplacian of `‖x‖ ^ (2 - d)` is `(2 - d) * d * volume (Metric.ball 0 1)`
> times the Dirac delta at the origin. For `d ≥ 3` this `‖x‖ ^ (2 - d)` is the (singular)
> fundamental solution of the Laplacian, and for `d = 1` it is `‖x‖`. When `d = 2` the exponent
> vanishes, so the identity collapses to the trivial `Δᵈ 1 = 0`; the genuine two-dimensional
> fundamental solution is the logarithm, proved in `distLaplacian_fundamentalSolution_log_norm`.
> The statement also holds vacuously for `d = 0`, where the space is trivial.

```lean
lemma distLaplacian_fundamentalSolution_norm_zpow {d : ℕ} :
    Δᵈ (distOfFunction (fun x : Space d => ‖x‖ ^ (- ((d : ℤ) - 2)))
      (IsDistBounded.pow _ (by omega))) =
      ((- ((d : ℝ) - 2)) * d *
        (volume (α := Space d)).real (Metric.ball 0 1)) • diracDelta ℝ 0
```

**`Space.distLaplacian_fundamentalSolution_log_norm`**, a lemma, [line 1146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean#L1146).

> In dimension two the fundamental solution of the Laplacian is the logarithm: the
> distributional Laplacian of `Real.log ‖x‖` is `2 * volume (Metric.ball 0 1)` times the Dirac
> delta at the origin.

```lean
lemma distLaplacian_fundamentalSolution_log_norm :
    Δᵈ (distOfFunction (fun x : Space 2 => Real.log ‖x‖) IsDistBounded.log_norm) =
      (2 * (volume (α := Space 2)).real (Metric.ball 0 1)) • diracDelta ℝ 0
```

## Depends on

- [The Laplacian operator on `Space d`](../part-01/derivatives-laplacian.md)

## Proof depends on

- [Physlib.Mathematics.Distribution.PowMul](../../../mathematics/distribution/powmul.md)
- [Integrability of norm powers on subsets of Space](integrals-normpow.md)

## Sources

- [Physlib/SpaceAndTime/Space/Norm/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Norm/Basic.lean)
