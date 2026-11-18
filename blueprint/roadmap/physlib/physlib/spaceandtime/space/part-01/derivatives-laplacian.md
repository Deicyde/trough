---
declaration: module
origin: cited
lean: Space.laplacian, Space.laplacian_eq_sum_snd_deriv, Space.laplacianVec, Space.distLaplacian, Space.distLaplacian_const, Space.laplacian_comp_linearIsometryEquiv, Space.laplacianVec_comp_linearIsometryEquiv
statement: formalized
proof: formalized
---

# The Laplacian operator on `Space d`

The module `Physlib.SpaceAndTime.Space.Derivatives.Laplacian`, [Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean): 7 declarations, 5 with a docstring.

## i. Overview

> In this module we define the Laplacian operator on functions and vector-valued
> functions defined on `Space d`.

## ii. Key results

> - `laplacian` : The Laplacian operator on scalar functions on `Space d`.
> - `laplacianVec` : The Laplacian operator on vector-valued functions on `Space d`.
> - `distLaplacian` : The Laplacian operator on distributions on `Space d`.
> - `laplacian_comp_linearIsometryEquiv` : The Laplacian commutes with composition by a linear
>   isometry of `Space d`.
> - `laplacianVec_comp_linearIsometryEquiv` : The vector Laplacian commutes with composition by a
>   linear isometry of `Space d`.

## iv. References

> * None.

## A. Laplacian on functions to ℝ

**`Space.laplacian`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L53).

> The scalar `laplacian` operator.

```lean
noncomputable def laplacian {d} (f : Space d → ℝ) : Space d → ℝ
```

### A.1. Relation between laplacian and divergence of gradient

**`Space.laplacian_eq_sum_snd_deriv`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L65).

```lean
lemma laplacian_eq_sum_snd_deriv {d} (f : Space d → ℝ) :
    Δ f = fun x => ∑ i, ∂[i] (∂[i] f) x
```

## B. Laplacian on vector valued functions

**`Space.laplacianVec`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L77).

> The vector `laplacianVec` operator.

```lean
noncomputable def laplacianVec {d} (f : Space d → EuclideanSpace ℝ (Fin d)) :
    Space d → EuclideanSpace ℝ (Fin d)
```

## C. Laplacian of distributions

**`Space.distLaplacian`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L94).

> The distributional `distLaplacian` operator.

```lean
noncomputable def distLaplacian {d} :
    ((Space d) →d[ℝ] ℝ) →ₗ[ℝ] (Space d) →d[ℝ] ℝ
```

### C.1. Laplacian of constant distributions

**`Space.distLaplacian_const`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L108).

```lean
lemma distLaplacian_const {d : ℕ} (c : ℝ) :
    Δᵈ (Distribution.const ℝ (Space d) c) = 0
```

## D. Composition with a linear isometry

**`Space.laplacian_comp_linearIsometryEquiv`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L120).

> The Laplacian of `f ∘ R` at `x` is the Laplacian of `f` at `R x`, for a linear isometry `R`
> of space.

```lean
lemma laplacian_comp_linearIsometryEquiv {d : ℕ} (f : Space d → ℝ) (R : Space d ≃ₗᵢ[ℝ] Space d)
    (x : Space d) (hf : DifferentiableAt ℝ (fderiv ℝ f) (R x)) :
    Δ (fun y => f (R y)) x = Δ f (R x)
```

**`Space.laplacianVec_comp_linearIsometryEquiv`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean#L158).

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

- [Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/Laplacian.lean)
