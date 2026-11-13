---
declaration: module
origin: cited
lean: SmoothDistance.smoothDist, SmoothDistance.smoothDist_pos, SmoothDistance.norm_sub_le_smoothDist, SmoothDistance.continuous_smoothDist, SmoothDistance.hasFDerivAt_smoothDist, SmoothDistance.deriv_expNegInvGlue_nonneg, SmoothDistance.deriv_expNegInvGlue_of_nonpos, SmoothDistance.continuous_deriv_expNegInvGlue
statement: formalized
proof: formalized
---

# A smooth substitute for the distance

The module `PhyslibAlpha.Mathematics.Calculus.SmoothDistance`, [PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean): 9 declarations, 1 with a docstring.

> The function `sqrt (ε^2 + ‖x - x₀‖^2)` is smooth and bounds the distance.

## i. Overview

> The function `sqrt (ε^2 + ‖x - x₀‖^2)` is smooth and bounds the distance. The derivative of
> `expNegInvGlue` is continuous.

## ii. Key results

> - `smoothDist` : The smooth distance `√(ε² + ‖x - x₀‖²)`.
> - `smoothDist_pos`
> - `norm_sub_le_smoothDist`
> - `continuous_smoothDist`

## iv. References

> None.

## A. The cone weight

> - `smoothDist` : The smooth distance `√(ε² + ‖x - x₀‖²)`.
>
> Lemmas: `smoothDist_pos`, `norm_sub_le_smoothDist`, `continuous_smoothDist`,
> `hasFDerivAt_smoothDist`, `deriv_expNegInvGlue_nonneg`, `deriv_expNegInvGlue_of_nonpos`,
> `continuous_deriv_expNegInvGlue`, `hasDerivAt_expNegInvGlue`.

**`SmoothDistance.smoothDist`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L62).

> The smooth distance `√(ε² + ‖x - x₀‖²)`.

```lean
def smoothDist (ε : ℝ) (x₀ x : E) : ℝ
```

**`SmoothDistance.smoothDist_pos`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L65).

```lean
lemma smoothDist_pos {ε : ℝ} (hε : 0 < ε) (x₀ x : E) : 0 < smoothDist ε x₀ x
```

**`SmoothDistance.norm_sub_le_smoothDist`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L69).

```lean
lemma norm_sub_le_smoothDist (ε : ℝ) (x₀ x : E) : ‖x - x₀‖ ≤ smoothDist ε x₀ x
```

**`SmoothDistance.continuous_smoothDist`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L74).

```lean
lemma continuous_smoothDist (ε : ℝ) (x₀ : E) : Continuous (smoothDist ε x₀)
```

**`SmoothDistance.hasFDerivAt_smoothDist`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L77).

```lean
lemma hasFDerivAt_smoothDist {ε : ℝ} (hε : 0 < ε) (x₀ x : E) :
    HasFDerivAt (smoothDist ε x₀) ((1 / smoothDist ε x₀ x) • innerSL ℝ (x - x₀)) x
```

**`SmoothDistance.deriv_expNegInvGlue_nonneg`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L92).

```lean
lemma deriv_expNegInvGlue_nonneg (r : ℝ) : 0 ≤ deriv expNegInvGlue r
```

**`SmoothDistance.deriv_expNegInvGlue_of_nonpos`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L95).

```lean
lemma deriv_expNegInvGlue_of_nonpos {r : ℝ} (hr : r ≤ 0) : deriv expNegInvGlue r = 0
```

**`SmoothDistance.continuous_deriv_expNegInvGlue`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L107).

```lean
lemma continuous_deriv_expNegInvGlue : Continuous (deriv expNegInvGlue)
```

**`SmoothDistance.hasDerivAt_expNegInvGlue`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean#L110).

```lean
lemma hasDerivAt_expNegInvGlue (r : ℝ) : HasDerivAt expNegInvGlue (deriv expNegInvGlue r) r
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/SmoothDistance.lean)
