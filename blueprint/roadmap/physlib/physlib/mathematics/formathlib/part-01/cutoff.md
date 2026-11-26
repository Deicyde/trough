---
declaration: module
origin: cited
lean: IsCompact.exists_cutoff, contDiff_smul_of_cutoff
statement: formalized
proof: formalized
---

# Cutoff functions

The module `Physlib.Mathematics.ForMathlib.Cutoff`, [Physlib/Mathematics/ForMathlib/Cutoff.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Cutoff.lean): 2 declarations, 2 with a docstring.

> Smooth cutoffs around a compact set.

## i. Overview

> A compact subset of an open set in a finite-dimensional space has a smooth cutoff, `1` on a
> neighbourhood of the subset and `0` near every point outside the open set.

## ii. Key results

> - `IsCompact.exists_cutoff`
> - `contDiff_smul_of_cutoff`

## iv. References

> * None.

## A. Cutoff functions

**`IsCompact.exists_cutoff`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Cutoff.lean#L45).

> A smooth cutoff which is `1` on a neighbourhood `N` of a compact set `K` inside an open set `U`
> and has topological support inside `U`.

```lean
lemma IsCompact.exists_cutoff {X : Type*} [NormedAddCommGroup X] [NormedSpace ℝ X]
    [FiniteDimensional ℝ X]
    {K U : Set X} (hK : IsCompact K) (hU : IsOpen U) (hKU : K ⊆ U) :
    ∃ (χ : X → ℝ) (N : Set X), ContDiff ℝ ∞ χ ∧ IsOpen N ∧ K ⊆ N ∧ N ⊆ U ∧
      (∀ y ∈ N, χ y = 1) ∧ tsupport χ ⊆ U
```

**`contDiff_smul_of_cutoff`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Cutoff.lean#L63).

> `ρ • f` is smooth if `tsupport ρ ⊆ W` and `f` is smooth on `W`.

```lean
lemma contDiff_smul_of_cutoff {Y F : Type*} [NormedAddCommGroup Y] [NormedSpace ℝ Y]
    [NormedAddCommGroup F] [NormedSpace ℝ F] {ρ : Y → ℝ} (hρ : ContDiff ℝ ∞ ρ) {W : Set Y}
    (hρ0 : tsupport ρ ⊆ W) {f : Y → F} (hf : ∀ y ∈ W, ContDiffAt ℝ ∞ f y) :
    ContDiff ℝ ∞ fun y ↦ ρ y • f y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Cutoff.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/Cutoff.lean)
