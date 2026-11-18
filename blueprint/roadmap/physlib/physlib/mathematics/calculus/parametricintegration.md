---
declaration: module
origin: cited
lean: hasFDerivAt_parametric_intervalIntegral_of_contDiff, fderiv_apply_parametric_intervalIntegral, fderiv_parametric_intervalIntegral, contDiff_one_parametric_intervalIntegral_of_contDiff, contDiff_succ_parametric_intervalIntegral_of_contDiff, contDiff_parametric_intervalIntegral_of_contDiff, hasDerivAt_intervalIntegral_of_contDiff
statement: formalized
proof: formalized
---

# Parametric Integration

The module `Physlib.Mathematics.Calculus.ParametricIntegration`, [Physlib/Mathematics/Calculus/ParametricIntegration.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean): 7 declarations, 1 with a docstring.

> In this module we give some lemmas around parametric integration in Lean.
> These extend some lemmas in Mathlib, and give them in a more physics-friendly way.

**`hasFDerivAt_parametric_intervalIntegral_of_contDiff`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L30).

```lean
lemma hasFDerivAt_parametric_intervalIntegral_of_contDiff
    {F : M → ℝ → N} (hf : ContDiff ℝ 1 ↿F) (x₀ : M) :
    HasFDerivAt (fun (x : M) => ∫ (t : ℝ) in 0..1, F x t ∂(volume))
      (∫ (t : ℝ) in 0..1, fderiv ℝ (F · t) x₀ ∂(volume)) x₀
```

**`fderiv_apply_parametric_intervalIntegral`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L59).

```lean
lemma fderiv_apply_parametric_intervalIntegral
    {F : M → ℝ → N} (hf : ContDiff ℝ 1 ↿F) (x₀ : M) (v : M) :
    fderiv ℝ (fun (x : M) => ∫ (t : ℝ) in 0..1, F x t ∂(volume)) x₀ v =
      ∫ (t : ℝ) in 0..1, fderiv ℝ (F · t) x₀ v ∂(volume)
```

**`fderiv_parametric_intervalIntegral`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L68).

```lean
lemma fderiv_parametric_intervalIntegral
    {F : M → ℝ → N} (hf : ContDiff ℝ 1 ↿F) (x₀ : M) :
    fderiv ℝ (fun (x : M) => ∫ (t : ℝ) in 0..1, F x t ∂(volume)) =
      fun x => ∫ (t : ℝ) in 0..1, fderiv ℝ (F · t) x ∂(volume)
```

**`contDiff_one_parametric_intervalIntegral_of_contDiff`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L76).

```lean
lemma contDiff_one_parametric_intervalIntegral_of_contDiff
    {F : M → ℝ → N} (hf : ContDiff ℝ 1 ↿F) :
    ContDiff ℝ 1 (fun (x : M) => ∫ (t : ℝ) in 0..1, F x t ∂(volume))
```

**`contDiff_succ_parametric_intervalIntegral_of_contDiff`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L83).

```lean
lemma contDiff_succ_parametric_intervalIntegral_of_contDiff {n : ℕ} [FiniteDimensional ℝ M]
    {F : M → ℝ → N} (hf : ContDiff ℝ (n + 1) ↿F) :
    ContDiff ℝ (n + 1) (fun (x : M) => ∫ (t : ℝ) in 0..1, F x t ∂(volume))
```

**`contDiff_parametric_intervalIntegral_of_contDiff`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L96).

```lean
lemma contDiff_parametric_intervalIntegral_of_contDiff {n : ℕ} {M : Type}
    [NormedAddCommGroup M] [NormedSpace ℝ M] [ProperSpace M] [FiniteDimensional ℝ M]
    {F : M → ℝ → N} (hf : ContDiff ℝ n ↿F) :
    ContDiff ℝ n (fun (x : M) => ∫ (t : ℝ) in 0..1, F x t ∂(volume))
```

**`hasDerivAt_intervalIntegral_of_contDiff`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean#L106).

> Differentiation under the integral sign for a `C¹` integrand.

```lean
lemma hasDerivAt_intervalIntegral_of_contDiff {F : ℝ × ℝ → N}
    (hF : ContDiff ℝ 1 F) (a b x₀ : ℝ) :
    HasDerivAt (fun x ↦ ∫ t in a..b, F (x, t))
      (∫ t in a..b, fderiv ℝ F (x₀, t) (1, 0)) x₀
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Calculus/ParametricIntegration.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/ParametricIntegration.lean)
