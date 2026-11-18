---
declaration: module
origin: cited
lean: fderiv_apply_scaleUnit, fderiv_isDimensionallyCorrect, fderiv_dimension_const_direction
statement: formalized
proof: formalized
---

# Dimensional invariance of fderiv

The module `Physlib.Units.FDeriv`, [Physlib/Units/FDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/FDeriv.lean): 3 declarations, 2 with a docstring.

> In this module we prove that the derivative is dimensionally correct.
> That is to say for a function `f : M1 → M2` where `M1` carries dimensions `d1` and `M2` carries
> dimension `d2` such that `f` has the correct dimension, then
> `fderiv ℝ f : M1 → M1 →L[ℝ] M2` has the correct dimensions.
>
> To give an explicit example let us say `M1` has dimension `L𝓭` and `M2` has dimension
> `L𝓭 * L𝓭` and `f : M1 → M2 : x ↦ x ^ 2`, this is dimensionally correct.
> The `fderiv` of this `fderiv ℝ f : M1 → M1 →L[ℝ] M2` takes
> `x dx ↦ dx • (2 * x)` which is still dimensionally correct. Here `dx` is the direction
> in which the derivative is taken.

**`fderiv_apply_scaleUnit`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/FDeriv.lean#L38).

```lean
lemma fderiv_apply_scaleUnit (u1 u2 : LTMCTUnitChoices) (x dm : M1)
    (f : M1 → M2) (hf : IsDimensionallyCorrect f) (f_diff : Differentiable ℝ f) :
    fderiv ℝ f (scaleUnit u2 u1 x) dm =
    u2.dimScale u1 (dim M2) • u1.dimScale u2 (dim M1) • fderiv ℝ f x dm
```

**`fderiv_isDimensionallyCorrect`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/FDeriv.lean#L51).

> If a function is dimensionally valid then so is it's derivative.

```lean
lemma fderiv_isDimensionallyCorrect (f : M1 → M2) (hf : IsDimensionallyCorrect f)
    (f_diff : Differentiable ℝ f) :
    IsDimensionallyCorrect (fderiv ℝ f)
```

**`fderiv_dimension_const_direction`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/FDeriv.lean#L67).

> The expression `fderiv ℝ f x dm = v.1` for a fixed `dm` and for
> `v` with dimension `d M2 * (d M1)⁻¹` is dimensionally correct. This is the
> ordinary manifestation of dimensions of a derivative, usually `dm` is taken as e.g. `1`.
>
> This result also shows that dimensional correctness does depend on what
> quantities are considered dimensionful.

```lean
lemma fderiv_dimension_const_direction (dm : M1) (f : M1 → M2) (hf : IsDimensionallyCorrect f)
    (f_diff : Differentiable ℝ f) :
    IsDimensionallyCorrect (fun x (v : WithDim (dim M2 * (dim M1)⁻¹) M2) =>
      fderiv ℝ f x dm = v.1)
```

## Depends on

- [Physlib.Units.WithDim.Basic](withdim/basic.md)

## Sources

- [Physlib/Units/FDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/FDeriv.lean)
