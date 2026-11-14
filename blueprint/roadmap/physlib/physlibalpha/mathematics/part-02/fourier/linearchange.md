---
declaration: module
origin: cited
lean: Fourier.det_adjoint, Fourier.invTranspose, Fourier.invTranspose_symm_apply, Fourier.inner_invTranspose_symm, Fourier.abs_det_invTranspose, Fourier.fourier_comp_invTranspose, Fourier.fourier_eq_complex, Fourier.fourier_comp_isometry
statement: formalized
proof: formalized
---

# The Fourier transform under a linear change of variables

The module `PhyslibAlpha.Mathematics.Fourier.LinearChange`, [PhyslibAlpha/Mathematics/Fourier/LinearChange.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean): 9 declarations, 6 with a docstring.

> Composition with the inverse transpose of a linear equivalence turns into evaluation of the
> transform at the image point.

## i. Overview

> For a linear equivalence `L` of a finite dimensional inner product space the map `A = (L⁻¹)ᵀ` is
> again a linear equivalence. The Fourier transform of `f ∘ A` at `ξ` is `|det L|` times the
> transform of `f` at `L ξ`. The proof moves the integral along `A` with the Haar measure scaling
> and uses `⟨A⁻¹ y, ξ⟩ = ⟨y, L ξ⟩`.

## ii. Key results

> - `Fourier.invTranspose` : the inverse transpose of a linear equivalence.
> - `Fourier.fourier_comp_invTranspose` : the transform of `f ∘ (L⁻¹)ᵀ`.
> - `Fourier.fourier_comp_isometry` : the transform commutes with linear isometries.
> - `Fourier.fourier_comp_add_right` : the transform of a translate.

## iv. References

> None.

## A. The inverse transpose

> - `Fourier.det_adjoint` : the determinant of the adjoint.
> - `Fourier.invTranspose` : the inverse transpose of a linear equivalence.

## B. The transform

> - `Fourier.fourier_comp_invTranspose` : the transform of `f ∘ (L⁻¹)ᵀ`.

## C. Isometries

> - `Fourier.fourier_eq_complex` : the transform of a complex valued function.
> - `Fourier.fourier_comp_isometry` : the transform commutes with linear isometries.

## D. Translations

> - `Fourier.fourier_comp_add_right` : the transform of a translate.

**`Fourier.det_adjoint`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L76).

> The determinant of the adjoint.

```lean
lemma det_adjoint (f : V →ₗ[ℝ] V) : LinearMap.det (LinearMap.adjoint f) = LinearMap.det f
```

**`Fourier.invTranspose`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L83).

> The inverse transpose of a linear equivalence for the inner product.

```lean
def invTranspose (L : V ≃L[ℝ] V) : V ≃L[ℝ] V
```

**`Fourier.invTranspose_symm_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L89).

```lean
lemma invTranspose_symm_apply (L : V ≃L[ℝ] V) (x : V) :
    (invTranspose L).symm x = LinearMap.adjoint L.toLinearMap x
```

**`Fourier.inner_invTranspose_symm`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L93).

```lean
lemma inner_invTranspose_symm (L : V ≃L[ℝ] V) (x y : V) :
    inner ℝ ((invTranspose L).symm x) y = inner ℝ x (L y)
```

**`Fourier.abs_det_invTranspose`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L99).

```lean
lemma abs_det_invTranspose (L : V ≃L[ℝ] V) :
    |LinearMap.det (invTranspose L : V →ₗ[ℝ] V)| = |LinearMap.det (L : V →ₗ[ℝ] V)|⁻¹
```

**`Fourier.fourier_comp_invTranspose`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L111).

> **Fourier transform and a linear change of variables.** Composition with the inverse
> transpose of `L` turns into evaluation at `L ξ` and the factor `|det L|`.

```lean
lemma fourier_comp_invTranspose (L : V ≃L[ℝ] V) (f : V → E) (ξ : V) :
    𝓕 (f ∘ invTranspose L) ξ = |LinearMap.det (L : V →ₗ[ℝ] V)| • 𝓕 f (L ξ)
```

**`Fourier.fourier_eq_complex`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L139).

> The Fourier transform of a complex valued function is the explicit integral.

```lean
lemma fourier_eq_complex {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    [MeasurableSpace V] [BorelSpace V] [FiniteDimensional ℝ V] (f : V → ℂ) (ξ : V) :
    𝓕 f ξ = ∫ x, (𝐞 (-inner ℝ x ξ) : ℂ) • f x
```

**`Fourier.fourier_comp_isometry`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L151).

> The Fourier transform commutes with linear isometries.

```lean
lemma fourier_comp_isometry (A : V ≃ₗᵢ[ℝ] W) (f : W → ℂ) (ξ : V) :
    𝓕 (f ∘ A) ξ = 𝓕 f (A ξ)
```

**`Fourier.fourier_comp_add_right`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean#L165).

> The Fourier transform turns translation into a phase.

```lean
lemma fourier_comp_add_right (f : V → ℂ) (q ζ : V) :
    𝓕 (fun v => f (v + q)) ζ = 𝐞 (inner ℝ q ζ) • 𝓕 f ζ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Fourier/LinearChange.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Fourier/LinearChange.lean)
