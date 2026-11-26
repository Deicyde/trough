---
declaration: module
origin: cited
lean: WaveVectorSpace.deriv, WaveVectorSpace.deriv_eq, WaveVectorSpace.deriv_eq_fun, WaveVectorSpace.deriv_const, WaveVectorSpace.deriv_add, WaveVectorSpace.deriv_sub, WaveVectorSpace.deriv_neg, WaveVectorSpace.deriv_smul
statement: formalized
proof: formalized
---

# Derivatives on `WaveVectorSpace`

The module `Physlib.SpaceAndTime.WaveVectorSpace.Derivatives.Basic`, [Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean): 24 declarations, 3 with a docstring.

## i. Overview

> In this module we define derivatives of functions on `WaveVectorSpace` with respect
> to the standard basis.

## ii. Key results

> - `deriv i` : The derivative of a function `f : WaveVectorSpace d → M`
>   in the direction of the `i`ᵗʰ basis vector, denoted by `∂[i] f`.

## iv. References

## A. Derivatives of functions on `WaveVectorSpace d`

**`WaveVectorSpace.deriv`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L50).

> Given a function `f : WaveVectorSpace d → M`,
> `∂[i] f` is its derivative in the direction of the `i`ᵗʰ basis vector.

```lean
noncomputable def deriv {M : Type*} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (i : Fin d) (f : WaveVectorSpace d → M) (k : WaveVectorSpace d) : M
```

**`WaveVectorSpace.deriv_eq`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L57).

```lean
lemma deriv_eq {M : Type*} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (i : Fin d) (f : WaveVectorSpace d → M) (k : WaveVectorSpace d) :
    ∂[i] f k = fderiv ℝ f k (basis i)
```

**`WaveVectorSpace.deriv_eq_fun`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L62).

```lean
lemma deriv_eq_fun {M : Type*} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (i : Fin d) (f : WaveVectorSpace d → M) :
    ∂[i] f = fun k ↦ fderiv ℝ f k (basis i)
```

### A.1. Constant functions

**`WaveVectorSpace.deriv_const`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L72).

```lean
lemma deriv_const
    {M : Type*} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M] (i : Fin d) (m : M) :
    ∂[i] (fun _ : WaveVectorSpace d ↦ m) = 0
```

### A.2. Addition and subtraction

**`WaveVectorSpace.deriv_add`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L91).

```lean
lemma deriv_add : ∂[i] (f₁ + f₂) k = ∂[i] f₁ k + ∂[i] f₂ k
```

**`WaveVectorSpace.deriv_sub`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L94).

```lean
lemma deriv_sub : ∂[i] (f₁ - f₂) k = ∂[i] f₁ k - ∂[i] f₂ k
```

### A.3. Negation / scalar multiplication

**`WaveVectorSpace.deriv_neg`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L107).

```lean
lemma deriv_neg (i : Fin d) (f : WaveVectorSpace d → M) : ∂[i] (-f) = -∂[i] f
```

**`WaveVectorSpace.deriv_smul`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L113).

> The product rule for functions on `WaveVectorSpace`.

```lean
lemma deriv_smul {𝕜 : Type*} [NontriviallyNormedField 𝕜] [NormedAlgebra ℝ 𝕜] [NormedSpace 𝕜 M]
    (i : Fin d) {c : WaveVectorSpace d → 𝕜} {f : WaveVectorSpace d → M} {k : WaveVectorSpace d}
    (hc : DifferentiableAt ℝ c k) (hf : DifferentiableAt ℝ f k) :
    ∂[i] (c • f) k = c k • ∂[i] f k + ∂[i] c k • f k
```

**`WaveVectorSpace.deriv_const_smul`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L120).

```lean
lemma deriv_const_smul
    {R : Type*} [Semiring R] [Module R M] [SMulCommClass ℝ R M] [ContinuousConstSMul R M] (c : R)
    (i : Fin d) {f : WaveVectorSpace d → M} {k : WaveVectorSpace d} (hf : DifferentiableAt ℝ f k) :
    ∂[i] (c • f) k = c • ∂[i] f k
```

### A.4. Powers

**`WaveVectorSpace.deriv_pow`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L134).

> The power rule for functions on `WaveVectorSpace`.

```lean
lemma deriv_pow {𝔸 : Type*} [NormedCommRing 𝔸] [NormedAlgebra ℝ 𝔸] (i : Fin d)
    {f : WaveVectorSpace d → 𝔸} {k : WaveVectorSpace d} (n : ℕ) (hf : DifferentiableAt ℝ f k) :
    ∂[i] (f ^ n) k = (n • f k ^ (n - 1)) • ∂[i] f k
```

### A.5. Components / coordinate functions

**`WaveVectorSpace.deriv_coordCLM`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L148).

```lean
lemma deriv_coordCLM : ∂[i] (coordCLM j) k = δ[i,j]
```

**`WaveVectorSpace.deriv_coord`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L152).

```lean
lemma deriv_coord : ∂[i] (coord j) k = δ[i,j]
```

**`WaveVectorSpace.deriv_component`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L155).

```lean
lemma deriv_component : ∂[i] (fun k ↦ k j) k = δ[i,j]
```

### A.6. Norm-squared

**`WaveVectorSpace.norm_sq_differentiable`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L164).

```lean
lemma norm_sq_differentiable : Differentiable ℝ (fun k : WaveVectorSpace d ↦ ‖k‖ ^ 2)
```

**`WaveVectorSpace.deriv_norm_sq`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L167).

```lean
lemma deriv_norm_sq (i : Fin d) (k : WaveVectorSpace d) : ∂[i] (fun k ↦ ‖k‖ ^ 2) k = 2 * k i
```

### A.7. Inner product

**`WaveVectorSpace.inner_differentiable`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L182).

```lean
lemma inner_differentiable : Differentiable ℝ (fun k : WaveVectorSpace d ↦ ⟪k, k⟫)
```

**`WaveVectorSpace.inner_differentiableAt`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L186).

```lean
lemma inner_differentiableAt : DifferentiableAt ℝ (fun k ↦ ⟪k, k⟫) k
```

**`WaveVectorSpace.inner_apply_differentiable`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L189).

```lean
lemma inner_apply_differentiable (hf : Differentiable ℝ f) (hg : Differentiable ℝ g) :
    Differentiable ℝ (fun m : M ↦ ⟪f m, g m⟫)
```

**`WaveVectorSpace.inner_apply_differentiableAt`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L194).

```lean
lemma inner_apply_differentiableAt
    {m : M} (hf : DifferentiableAt ℝ f m) (hg : DifferentiableAt ℝ g m) :
    DifferentiableAt ℝ (fun m : M ↦ ⟪f m, g m⟫) m
```

**`WaveVectorSpace.inner_contDiff`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L200).

```lean
lemma inner_contDiff {n : WithTop ℕ∞} : ContDiff ℝ n (fun k : WaveVectorSpace d ↦ ⟪k, k⟫)
```

**`WaveVectorSpace.inner_apply_contDiff`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L204).

```lean
lemma inner_apply_contDiff {n : WithTop ℕ∞} (hf : ContDiff ℝ n f) (hg : ContDiff ℝ n g) :
    ContDiff ℝ n (fun m : M ↦ ⟪f m, g m⟫)
```

**`WaveVectorSpace.deriv_inner_self`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L208).

```lean
lemma deriv_inner_self : ∂[i] (fun k ↦ ⟪k, k⟫) k = 2 * k i
```

**`WaveVectorSpace.deriv_inner_left`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L211).

```lean
lemma deriv_inner_left : ∂[i] (fun k ↦ ⟪k, k₂⟫) k₁ = k₂ i
```

**`WaveVectorSpace.deriv_inner_right`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean#L215).

```lean
lemma deriv_inner_right : ∂[i] (fun k ↦ ⟪k₁, k⟫) k₂ = k₁ i
```

## Depends on

- [Wave Vector Space](basic.md)

## Sources

- [Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/Derivatives/Basic.lean)
