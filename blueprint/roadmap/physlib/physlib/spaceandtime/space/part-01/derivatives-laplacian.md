---
declaration: module
origin: cited
lean: Space.laplacian, Space.laplacian_eq_sum_snd_deriv, Space.laplacianVec, Space.distLaplacian, Space.distLaplacian_const, Space.distLaplacian_apply, Space.laplacian_comp_linearIsometryEquiv, Space.laplacianVec_comp_linearIsometryEquiv
statement: formalized
proof: formalized
---

# The Laplacian operator on `Space d`

The module `Physlib.SpaceAndTime.Space.Derivatives.Laplacian`, [Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean): 8 declarations, 6 with a docstring.

## i. Overview

> In this module we define the Laplacian operator on functions and vector-valued
> functions defined on `Space d`.

## ii. Key results

> - `laplacian` : The Laplacian operator on scalar functions on `Space d`.
> - `laplacianVec` : The Laplacian operator on vector-valued functions on `Space d`.
> - `distLaplacian` : The Laplacian operator on distributions on `Space d`.
> - `distLaplacian_apply` : The Laplacian of a distribution on a test function,
>   `(Δᵈ T) η = T (Δ η)`.
> - `laplacian_comp_linearIsometryEquiv` : The Laplacian commutes with composition by a linear
>   isometry of `Space d`.
> - `laplacianVec_comp_linearIsometryEquiv` : The vector Laplacian commutes with composition by a
>   linear isometry of `Space d`.

## iv. References

> * None.

## A. Laplacian on functions to ℝ

**`Space.laplacian`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L56).

> The scalar `laplacian` operator.

```lean
noncomputable def laplacian {d} (f : Space d → ℝ) : Space d → ℝ
```

### A.1. Relation between laplacian and divergence of gradient

**`Space.laplacian_eq_sum_snd_deriv`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L68).

```lean
lemma laplacian_eq_sum_snd_deriv {d} (f : Space d → ℝ) :
    Δ f = fun x => ∑ i, ∂[i] (∂[i] f) x
```

## B. Laplacian on vector valued functions

**`Space.laplacianVec`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L80).

> The vector `laplacianVec` operator.

```lean
noncomputable def laplacianVec {d} (f : Space d → EuclideanSpace ℝ (Fin d)) :
    Space d → EuclideanSpace ℝ (Fin d)
```

## C. Laplacian of distributions

**`Space.distLaplacian`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L97).

> The distributional `distLaplacian` operator.

```lean
noncomputable def distLaplacian {d} :
    ((Space d) →d[ℝ] ℝ) →ₗ[ℝ] (Space d) →d[ℝ] ℝ
```

### C.1. Laplacian of constant distributions

**`Space.distLaplacian_const`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L111).

```lean
lemma distLaplacian_const {d : ℕ} (c : ℝ) :
    Δᵈ (Distribution.const ℝ (Space d) c) = 0
```

### C.2. The Laplacian of a distribution on a test function

**`Space.distLaplacian_apply`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L124).

> The distributional Laplacian acts on a test function through the Laplacian of the test
> function: `(Δᵈ T) η = T (Δ η)`.

```lean
lemma distLaplacian_apply {d : ℕ} (T : (Space d) →d[ℝ] ℝ) (η : 𝓢(Space d, ℝ)) :
    (Δᵈ T) η = T (Laplacian.laplacian η)
```

## D. Composition with a linear isometry

**`Space.laplacian_comp_linearIsometryEquiv`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L141).

> The Laplacian of `f ∘ R` at `x` is the Laplacian of `f` at `R x`, for a linear isometry `R`
> of space.

```lean
lemma laplacian_comp_linearIsometryEquiv {d : ℕ} (f : Space d → ℝ) (R : Space d ≃ₗᵢ[ℝ] Space d)
    (x : Space d) (hf : DifferentiableAt ℝ (fderiv ℝ f) (R x)) :
    Δ (fun y => f (R y)) x = Δ f (R x)
```

**`Space.laplacianVec_comp_linearIsometryEquiv`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L179).

> The vector Laplacian of `f ∘ R` at `x` is the vector Laplacian of `f` at `R x`, for a linear
> isometry `R` of space.

```lean
lemma laplacianVec_comp_linearIsometryEquiv {d : ℕ} (f : Space d → EuclideanSpace ℝ (Fin d))
    (R : Space d ≃ₗᵢ[ℝ] Space d) (x : Space d)
    (hf : ∀ i, DifferentiableAt ℝ (fderiv ℝ (fun y => f y i)) (R x)) :
    Δᵥ (fun y => f (R y)) x = Δᵥ f (R x)
```

## Depends on

- [Divergence on Space](derivatives-div.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean)
