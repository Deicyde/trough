---
declaration: module
origin: cited
lean: Time.contMDiffAt_iff_contDiffAt_vadd, Time.mdifferentiableAt_iff_differentiableAt_vadd, Time.contMDiff_iff_contDiff_vadd, Time.mdifferentiableAt_vadd_iff, Time.contDiffAt_extChartAt_comp_vadd, Time.writtenInExtChartAt_eq_vadd, Time.mfderiv_eq_deriv_vadd, Time.tangentMap_eq_deriv_vadd
statement: formalized
proof: formalized
---

# Curves over `Time`

The module `Physlib.SpaceAndTime.Time.ManifoldCurves`, [Physlib/SpaceAndTime/Time/ManifoldCurves.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean): 8 declarations, 8 with a docstring; 2 private, not shown.

> A curve `Time → F` is smooth, or has a given derivative, iff its coordinate curve does.

## i. Overview

> The charts of `Time` are translations, so the coordinate curve `τ ↦ γ (τ +ᵥ t₀)` needs no origin.

## ii. Key results

> - `Time.contMDiff_iff_contDiff_vadd`: a curve is `C^n` iff its coordinate curve is
> - `Time.mfderiv_eq_deriv_vadd`: the manifold derivative is the derivative of the coordinate curve
> - `Time.contDiffAt_extChartAt_comp_vadd`: a curve read in a chart is smooth where it lies in it
> - `Time.tangentMap_eq_deriv_vadd`: the tangent map of a curve in coordinates

## iv. References

> * None.

## A. Smoothness and differentiability of curves

**`Time.contMDiffAt_iff_contDiffAt_vadd`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L60).

> A curve into a normed space is `C^n` at `x` iff its coordinate curve is `C^n` at `0`.

```lean
lemma contMDiffAt_iff_contDiffAt_vadd (γ : Time → F) (x : Time) (n : ℕ∞ω) :
    ContMDiffAt 𝓘(ℝ, ℝ) 𝓘(ℝ, F) n γ x ↔ ContDiffAt ℝ n (fun τ : ℝ ↦ γ (τ +ᵥ x)) 0
```

**`Time.mdifferentiableAt_iff_differentiableAt_vadd`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L67).

> A curve into a normed space is differentiable at `x` iff its coordinate curve is at `0`.

```lean
lemma mdifferentiableAt_iff_differentiableAt_vadd (γ : Time → F) (x : Time) :
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, F) γ x ↔ DifferentiableAt ℝ (fun τ : ℝ ↦ γ (τ +ᵥ x)) 0
```

**`Time.contMDiff_iff_contDiff_vadd`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L80).

> A curve `γ : Time → F` into a normed space is `C^n` iff the coordinate curve
> `τ ↦ γ (τ +ᵥ t₀)` is `C^n`.

```lean
lemma contMDiff_iff_contDiff_vadd (γ : Time → F) (t₀ : Time) (n : ℕ∞ω) :
    ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, F) n γ ↔ ContDiff ℝ n (fun τ : ℝ ↦ γ (τ +ᵥ t₀))
```

**`Time.mdifferentiableAt_vadd_iff`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L94).

> A curve into a normed space is differentiable at `s +ᵥ t₀` iff its coordinate curve based
> at `t₀` is differentiable at `s`.

```lean
lemma mdifferentiableAt_vadd_iff (γ : Time → F) (t₀ : Time) (s : ℝ) :
    MDifferentiableAt 𝓘(ℝ, ℝ) 𝓘(ℝ, F) γ (s +ᵥ t₀) ↔
      DifferentiableAt ℝ (fun τ : ℝ ↦ γ (τ +ᵥ t₀)) s
```

**`Time.contDiffAt_extChartAt_comp_vadd`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L101).

> A curve in a manifold read in a chart is smooth at times at which it lies in the chart.

```lean
lemma contDiffAt_extChartAt_comp_vadd {E H M : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
    [IsManifold I ∞ M] (x : M) {γ : Time → M} (t₀ : Time) {σ : ℝ}
    (hγ : ContMDiffAt 𝓘(ℝ, ℝ) I ∞ γ (σ +ᵥ t₀)) (hσ : γ (σ +ᵥ t₀) ∈ (extChartAt I x).source) :
    ContDiffAt ℝ ∞ (fun σ' : ℝ ↦ extChartAt I x (γ (σ' +ᵥ t₀))) σ
```

## B. Derivatives of curves

**`Time.writtenInExtChartAt_eq_vadd`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L116).

> A curve read in the extended chart at `x` is its coordinate curve based at `x`.

```lean
lemma writtenInExtChartAt_eq_vadd (γ : Time → F) (x : Time) :
    writtenInExtChartAt 𝓘(ℝ, ℝ) 𝓘(ℝ, F) x γ = fun τ : ℝ ↦ γ (τ +ᵥ x)
```

**`Time.mfderiv_eq_deriv_vadd`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L122).

> The manifold derivative of a curve into a normed space at `s +ᵥ t₀` applied to `1`
> equals the ordinary derivative of the coordinate curve at `s`.

```lean
lemma mfderiv_eq_deriv_vadd (γ : Time → F) (t₀ : Time) (s : ℝ) :
    mfderiv 𝓘(ℝ, ℝ) 𝓘(ℝ, F) γ (s +ᵥ t₀) (1 : ℝ) = deriv (fun τ : ℝ ↦ γ (τ +ᵥ t₀)) s
```

**`Time.tangentMap_eq_deriv_vadd`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean#L138).

> The tangent map of a curve into a normed space sends `⟨s +ᵥ t₀, 1⟩` to the point and
> the ordinary derivative of the coordinate curve.

```lean
lemma tangentMap_eq_deriv_vadd (γ : Time → F) (t₀ : Time) (s : ℝ) :
    tangentMap 𝓘(ℝ, ℝ) 𝓘(ℝ, F) γ ⟨s +ᵥ t₀, (1 : ℝ)⟩ =
      ⟨γ (s +ᵥ t₀), deriv (fun τ : ℝ ↦ γ (τ +ᵥ t₀)) s⟩
```

## Depends on

- [Time](basic.md)

## Sources

- [Physlib/SpaceAndTime/Time/ManifoldCurves.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Time/ManifoldCurves.lean)
