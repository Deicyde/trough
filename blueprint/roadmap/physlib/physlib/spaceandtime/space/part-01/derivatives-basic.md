---
declaration: module
origin: cited
lean: Space.deriv, Space.deriv_eq, Space.deriv_eq_fderiv_fun, Space.deriv_eq_fderiv_basis, Space.fderiv_eq_sum_deriv, Space.deriv_eq_mfderiv, Space.mdifferentiable_manifoldStructure_iff_differentiable, Space.deriv_eq_mfderiv_manifoldStructure
statement: formalized
proof: formalized
---

# Derivatives on Space

The module `Physlib.SpaceAndTime.Space.Derivatives.Basic`, [Physlib/SpaceAndTime/Space/Derivatives/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean): 40 declarations, 13 with a docstring.

## i. Overview

> In this module we define derivatives of functions and distributions on space `Space d`,
> in the standard directions.

## ii. Key results

> - `deriv` : The derivative of a function on space in a given direction.
> - `distDeriv` : The derivative of a distribution on space in a given direction.

## iv. References

> * None.

## A. Derivatives of functions on `Space d`

**`Space.deriv`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L69).

> Given a function `f : Space d → M` the derivative of `f` in direction `μ`.

```lean
noncomputable def deriv {M d} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (μ : Fin d) (f : Space d → M) : Space d → M
```

### A.1. Basic equalities

**`Space.deriv_eq`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L82).

```lean
lemma deriv_eq [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (μ : Fin d) (f : Space d → M) (x : Space d) :
    deriv μ f x = fderiv ℝ f x (basis μ)
```

**`Space.deriv_eq_fderiv_fun`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L86).

```lean
lemma deriv_eq_fderiv_fun [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (μ : Fin d) (f : Space d → M) :
    deriv μ f = fun x => fderiv ℝ (fun x => f x) x (basis μ)
```

**`Space.deriv_eq_fderiv_basis`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L90).

```lean
lemma deriv_eq_fderiv_basis [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (μ : Fin d) (f : Space d → M) (x : Space d) :
    deriv μ f x = fderiv ℝ f x (basis μ)
```

**`Space.fderiv_eq_sum_deriv`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L94).

```lean
lemma fderiv_eq_sum_deriv {M d} [AddCommGroup M] [Module ℝ M] [TopologicalSpace M]
    (f : Space d → M) (x y : Space d) :
    fderiv ℝ f x y = ∑ i : Fin d, y i • ∂[i] f x
```

**`Space.deriv_eq_mfderiv`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L103).

> The spatial-derivative in terms of the derivative of functions between
> manifolds.

```lean
lemma deriv_eq_mfderiv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin d) (f : Space d → M) (x : Space d) :
    deriv μ f x = mfderiv 𝓘(ℝ, Space d) 𝓘(ℝ, M) f x (basis μ)
```

**`Space.mdifferentiable_manifoldStructure_iff_differentiable`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L110).

```lean
lemma mdifferentiable_manifoldStructure_iff_differentiable {M d} [NormedAddCommGroup M]
    [NormedSpace ℝ M] {f : Space d → M} {x : Space d} :
    MDifferentiableAt (𝓡 d) 𝓘(ℝ, M) f x ↔ DifferentiableAt ℝ f x
```

**`Space.deriv_eq_mfderiv_manifoldStructure`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L126).

> The spatial-derivative in terms of the derivative of functions between
> manifolds with the manifold structure `Space.manifoldStructure d`.

```lean
lemma deriv_eq_mfderiv_manifoldStructure {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin d) (f : Space d → M) (x : Space d) :
    deriv μ f x = mfderiv (𝓡 d) 𝓘(ℝ, M) f x (EuclideanSpace.single μ 1)
```

### A.2. Derivative of the constant function

**`Space.deriv_const`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L151).

```lean
lemma deriv_const [NormedAddCommGroup M] [NormedSpace ℝ M] (m : M) (μ : Fin d) :
    deriv μ (fun _ => m) t = 0
```

### A.3. Derivative distributes over addition and subtraction

**`Space.deriv_add`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L163).

> Derivatives on space distribute over addition.

```lean
lemma deriv_add [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f1 f2 : Space d → M) (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    ∂[u] (f1 + f2) = ∂[u] f1 + ∂[u] f2
```

**`Space.deriv_coord_add`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L170).

> Derivatives on space distribute coordinate-wise over addition.

```lean
lemma deriv_coord_add (f1 f2 : Space d → EuclideanSpace ℝ (Fin d))
    (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    (∂[u] (fun x => f1 x i + f2 x i)) =
      (∂[u] (fun x => f1 x i)) + (∂[u] (fun x => f2 x i))
```

**`Space.deriv_sub`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L178).

> Derivatives on space distribute over subtraction.

```lean
lemma deriv_sub [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f1 f2 : Space d → M) (hf1 : Differentiable ℝ f1) (hf2 : Differentiable ℝ f2) :
    ∂[u] (f1 - f2) = ∂[u] f1 - ∂[u] f2
```

### A.4. Derivative distributes over scalar multiplication

**`Space.deriv_smul`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L191).

> Space derivatives on scalar product of functions.

```lean
lemma deriv_smul [NormedAddCommGroup M] [NormedSpace ℝ M] [NontriviallyNormedField 𝕜]
    [NormedAlgebra ℝ 𝕜] [NormedSpace 𝕜 M] {c : Space d → 𝕜} {f : Space d → M}
    (hc : DifferentiableAt ℝ c x) (hf : DifferentiableAt ℝ f x) :
    ∂[u] (c • f) x = c x • ∂[u] f x + ∂[u] c x • f x
```

**`Space.deriv_const_smul`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L198).

> Space derivatives on scalar times function.

```lean
lemma deriv_const_smul [NormedAddCommGroup M] [NormedSpace ℝ M] [Semiring R]
    [Module R M] [SMulCommClass ℝ R M] [ContinuousConstSMul R M] {f : Space d → M} (c : R)
    (h : Differentiable ℝ f) : ∂[u] (c • f) = c • ∂[u] f
```

**`Space.deriv_coord_smul`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L205).

> Coordinate-wise scalar multiplication on space derivatives.

```lean
lemma deriv_coord_smul (f : Space d → EuclideanSpace ℝ (Fin d)) (k : ℝ)
    (hf : Differentiable ℝ f) :
    ∂[u] (fun x => k * f x i) x = k * ∂[u] (fun x => f x i) x
```

### A.5. Two spatial derivatives commute

**`Space.deriv_commute`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L217).

> Derivatives on space commute with one another.

```lean
lemma deriv_commute [NormedAddCommGroup M] [NormedSpace ℝ M]
    (f : Space d → M) (hf : ContDiff ℝ 2 f) : ∂[u] (∂[v] f) = ∂[v] (∂[u] f)
```

### A.6. Derivative of a component

**`Space.deriv_component_same`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L234).

```lean
lemma deriv_component_same (μ : Fin d) (x : Space d) :
    ∂[μ] (fun x => x μ) x = 1
```

**`Space.deriv_component_diff`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L240).

```lean
lemma deriv_component_diff (μ ν : Fin d) (x : Space d) (h : μ ≠ ν) :
    (deriv μ (fun x => x ν) x) = 0
```

**`Space.deriv_component`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L246).

```lean
lemma deriv_component (μ ν : Fin d) (x : Space d) :
    (deriv ν (fun x => x μ) x) = if ν = μ then 1 else 0
```

### A.7. Derivative of a component squared

**`Space.deriv_component_sq`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L258).

```lean
lemma deriv_component_sq {d : ℕ} {ν μ : Fin d} (x : Space d) :
    (deriv ν (fun x => (x μ) ^ 2) x) = if ν = μ then 2 * x μ else 0
```

### A.8. Derivative of a product of functions of single coordinates

**`Space.deriv_prod_coord`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L271).

> The derivative in direction `μ` of `x ↦ ∏ⱼ gⱼ (xⱼ)`, a product of differentiable functions
> of one coordinate each, is `gμ' (xμ)` times the product of the other factors.

```lean
lemma deriv_prod_coord {d : ℕ} (g : Fin d → ℝ → ℂ) (hg : ∀ j, Differentiable ℝ (g j))
    (μ : Fin d) (x : Space d) :
    ∂[μ] (fun x : Space d => ∏ j, g j (x j)) x =
      _root_.deriv (g μ) (x μ) * ∏ j ∈ Finset.univ.erase μ, g j (x j)
```

### A.8. Derivivatives of components

**`Space.deriv_euclid`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L299).

```lean
lemma deriv_euclid {d ν μ} {f : Space d → EuclideanSpace ℝ (Fin n)}
    (hf : Differentiable ℝ f) (x : Space d) :
    deriv ν (fun x => f x μ) x = deriv ν (fun x => f x) x μ
```

**`Space.deriv_lorentz_vector`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L307).

```lean
lemma deriv_lorentz_vector {d ν μ} {f : Space d → Lorentz.Vector d}
    (hf : Differentiable ℝ f) (x : Space d) :
    deriv ν (fun x => f x μ) x = deriv ν (fun x => f x) x μ
```

### A.9. Derivative of a norm squared

#### A.9.1. Differentiability of the norm squared function

**`Space.norm_sq_differentiable`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L327).

```lean
lemma norm_sq_differentiable : Differentiable ℝ (fun x : Space d => ‖x‖ ^ 2)
```

#### A.9.2. Derivative of the norm squared function

**`Space.deriv_norm_sq`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L336).

```lean
lemma deriv_norm_sq (x : Space d) (i : Fin d) :
    deriv i (fun x => ‖x‖ ^ 2) x = 2 * x i
```

### A.10. Derivative of the inner product

#### A.10.1. Differentiability of the inner product function

**`Space.inner_differentiable`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L356).

> The inner product is differentiable.

```lean
lemma inner_differentiable {d : ℕ} :
    Differentiable ℝ (fun y : Space d => ⟪y, y⟫_ℝ)
```

**`Space.inner_differentiableAt`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L361).

```lean
lemma inner_differentiableAt {d : ℕ} (x : Space d) :
    DifferentiableAt ℝ (fun y : Space d => ⟪y, y⟫_ℝ) x
```

**`Space.inner_apply_differentiableAt`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L366).

```lean
lemma inner_apply_differentiableAt {d : ℕ} [NormedAddCommGroup M]
    [NormedSpace ℝ M]
    {f : M → Space d} {g : M → Space d} (x : M)
    (hf : DifferentiableAt ℝ f x) (hg : DifferentiableAt ℝ g x) :
    DifferentiableAt ℝ (fun y : M => ⟪f y, g y⟫_ℝ) x
```

**`Space.inner_apply_differentiable`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L374).

```lean
lemma inner_apply_differentiable {d : ℕ} [NormedAddCommGroup M]
    [NormedSpace ℝ M]
    {f : M → Space d} {g : M → Space d}
    (hf : Differentiable ℝ f) (hg : Differentiable ℝ g) :
    Differentiable ℝ (fun y : M => ⟪f y, g y⟫_ℝ)
```

**`Space.inner_contDiff`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L381).

```lean
lemma inner_contDiff {n : WithTop ℕ∞} {d : ℕ} :
    ContDiff ℝ n (fun y : Space d => ⟪y, y⟫_ℝ)
```

**`Space.inner_apply_contDiff`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L386).

```lean
lemma inner_apply_contDiff {n : WithTop ℕ∞} {d : ℕ} [NormedAddCommGroup M]
    [NormedSpace ℝ M]
    {f : M → Space d} {g : M → Space d}
    (hf : ContDiff ℝ n f) (hg : ContDiff ℝ n g) :
    ContDiff ℝ n (fun y : M => ⟪f y, g y⟫_ℝ)
```

#### A.10.2. Derivative of the inner product function

**`Space.deriv_eq_inner_self`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L398).

```lean
lemma deriv_eq_inner_self (x : Space d) (i : Fin d) :
    deriv i (fun x => ⟪x, x⟫_ℝ) x = 2 * x i
```

#### A.10.3. Derivative of the inner product on one side

**`Space.deriv_inner_left`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L409).

```lean
lemma deriv_inner_left {d} (x1 x2 : Space d) (i : Fin d) :
    deriv i (fun x => ⟪x, x2⟫_ℝ) x1 = x2 i
```

**`Space.deriv_inner_right`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L414).

```lean
lemma deriv_inner_right {d} (x1 x2 : Space d) (i : Fin d) :
    deriv i (fun x => ⟪x1, x⟫_ℝ) x2 = x1 i
```

### A.11. Differentiability of derivatives

**`Space.deriv_differentiable`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L424).

```lean
lemma deriv_differentiable {M} [NormedAddCommGroup M]
    [NormedSpace ℝ M] {d : ℕ} {f : Space d → M}
    (hf : ContDiff ℝ 2 f) (i : Fin d) :
    Differentiable ℝ (deriv i f)
```

**`Space.deriv_contDiff`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L433).

```lean
lemma deriv_contDiff {d} {f : Space d → ℝ} (hf : ContDiff ℝ (n + 1) f) :
    ContDiff ℝ n fun x i => deriv i f x
```

## B. Derivatives of distributions on `Space d`

### B.1. The definition

**`Space.distDeriv`**, a def, [line 453](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L453).

> Given a distribution (function) `f : Space d →d[ℝ] M` the derivative
> of `f` in direction `μ`.

```lean
noncomputable def distDeriv {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin d) : ((Space d) →d[ℝ] M) →ₗ[ℝ] (Space d) →d[ℝ] M
```

### B.2. Basic equality

**`Space.distDeriv_apply`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L477).

```lean
lemma distDeriv_apply {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ : Fin d) (f : (Space d) →d[ℝ] M) (ε : 𝓢(Space d, ℝ)) :
    (∂ᵈ[μ] f) ε = fderivD ℝ f ε (basis μ)
```

### B.3. Commutation of derivatives

**`Space.schwartMap_fderiv_comm`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L488).

```lean
lemma schwartMap_fderiv_comm {d}
    (μ ν : Fin d) (x : Space d) (η : 𝓢(Space d, ℝ)) :
    ((SchwartzMap.evalCLM ℝ (Space d) ℝ (basis μ))
      ((fderivCLM ℝ (Space d) ℝ) ((SchwartzMap.evalCLM ℝ (Space d) ℝ (basis ν))
      ((fderivCLM ℝ (Space d) ℝ) η)))) x =
    ((SchwartzMap.evalCLM ℝ (Space d) ℝ (basis ν))
      ((fderivCLM ℝ (Space d) ℝ) ((SchwartzMap.evalCLM ℝ (Space d) ℝ (basis μ))
      ((fderivCLM ℝ (Space d) ℝ) η)))) x
```

**`Space.distDeriv_commute`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean#L499).

```lean
lemma distDeriv_commute {M d} [NormedAddCommGroup M] [NormedSpace ℝ M]
    (μ ν : Fin d) (f : (Space d) →d[ℝ] M) :
    (∂ᵈ[ν] (∂ᵈ[μ] f)) = (∂ᵈ[μ] (∂ᵈ[ν] f))
```

## Depends on

- [Distributions](../../../mathematics/distribution/tempereddistribution.md)
- [Lorentz Vectors](../../../relativity/tensors/part-03/realtensor-vector-basic.md)
- [The structure of a module on Space](module.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Basic.lean)
