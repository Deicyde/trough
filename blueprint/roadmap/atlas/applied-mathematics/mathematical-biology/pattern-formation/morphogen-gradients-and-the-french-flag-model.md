---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.MorphogenGradient.decayLength, MathlibExt.Biology.Dynamics.MorphogenGradient.profile, MathlibExt.Biology.Dynamics.MorphogenGradient.thresholdPosition, MathlibExt.Biology.Dynamics.MorphogenGradient.IsSteadyState, MathlibExt.Biology.Dynamics.MorphogenGradient.decayLength_pos, MathlibExt.Biology.Dynamics.MorphogenGradient.div_decayLength_sq, MathlibExt.Biology.Dynamics.MorphogenGradient.sqrt_mul_eq, MathlibExt.Biology.Dynamics.MorphogenGradient.hasDerivAt_profile
statement: formalized
proof: formalized
---

# Morphogen gradients and the French flag model

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html).

## Decay length of a morphogen gradient

The decay length `λ = √(D / k)` of a morphogen with diffusion coefficient `D` and linear
degradation rate `k` (both positive in the model).

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.decayLength`, a definition declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#decay-length).

## Steady-state exponential morphogen profile

The steady-state gradient `c(x) = (j / √(D k)) e^{-x/λ}`, `λ = √(D / k)`, for source flux
`j` at `x = 0`. Meaningful for `D, k > 0`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.profile`, a definition declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#profile).

## French-flag boundary position for a threshold

The French-flag boundary for threshold `θ`: `x_θ = λ log(c(0) / θ)`, where
`c(0) = j / √(D k)`. Meaningful for `D, k, j, θ > 0`; it is negative when `θ > c(0)` (no cell
is above threshold).

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.thresholdPosition`, a definition declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#threshold-position).

## Bounded steady state of the synthesis–diffusion–degradation model

A bounded steady state of the synthesis–diffusion–degradation model on `[0, ∞)`, with
`c' = dc/dx`: `D c'' = k c` for `x > 0`, `c` and `c'` continuous up to the source, source flux
`-D c'(0) = j`, and `c` bounded on `[0, ∞)`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.IsSteadyState`, a structure declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#is-steady-state).

## Positivity of the decay length

The decay length is positive for positive `D` and `k`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.decayLength_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#decay-length-pos).

## Diffusion coefficient over squared decay length equals degradation rate

`D / λ² = k`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.div_decayLength_sq`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#div-decay-length-sq).

## Source amplitude in terms of the decay length

`√(D k) = D / λ`, so the source amplitude is `c(0) = j λ / D`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.sqrt_mul_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#sqrt-mul-eq).

## Slope of the morphogen profile

The profile has slope `c'(x) = -c(x)/λ`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.hasDerivAt_profile`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#has-deriv-at-profile).

## Exponential profile is a bounded steady state

The exponential profile is a bounded steady state with source flux `j`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.isSteadyState_profile`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#is-steady-state-profile).

## Uniqueness

Every bounded steady state with source flux `j` is the exponential
profile on `[0, ∞)`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.eq_profile_of_isSteadyState`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#eq-profile-of-is-steady-state).

## Morphogen profile is strictly decreasing

The profile is strictly decreasing in `x` for a positive source.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.profile_strictAnti`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#profile-strict-anti).

## Profile equals the threshold at the French-flag boundary

The profile equals `θ` at the boundary `x_θ`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.profile_thresholdPosition`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#profile-threshold-position).

## French-flag boundary

For positive parameters and threshold `θ`, `c(x) = θ` exactly at
`x = x_θ = λ log(c(0)/θ)`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.profile_eq_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#profile-eq-iff).

## French-flag regions

A cell at `x` is at or above threshold `θ` iff it lies within the
boundary `x_θ`: `θ ≤ c(x) ↔ x ≤ x_θ`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.le_profile_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#le-profile-iff).

## Boundary shift

Scaling the source flux by `a > 0` moves every French-flag boundary by
`λ log a`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.thresholdPosition_mul`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#threshold-position-mul).

## Doubling the source flux shifts boundaries by $\lambda \log 2$

Doubling the source flux shifts every French-flag boundary away from the source by exactly
`λ log 2`.

Formalized by `MathlibExt.Biology.Dynamics.MorphogenGradient.thresholdPosition_two_mul`, a theorem declared in [MathlibExt/Biology/Dynamics/MorphogenGradient.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/MorphogenGradient.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html#threshold-position-two-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Morphogen gradients and the French flag model](https://deicyde.github.io/atlas-lean/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/pattern-formation/morphogen-gradients-and-the-french-flag-model)
