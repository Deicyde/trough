---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_pos, MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_lt_one, MathlibExt.Biology.PopulationGenetics.Diffusion.selectionGreen, MathlibExt.Biology.PopulationGenetics.Diffusion.selectionGreen_zero, MathlibExt.Biology.PopulationGenetics.Diffusion.greenFunction_eq_selectionGreen, MathlibExt.Biology.PopulationGenetics.Diffusion.generator_integral_selectionGreen, MathlibExt.Biology.PopulationGenetics.Diffusion.integral_selectionGreen_left, MathlibExt.Biology.PopulationGenetics.Diffusion.integral_selectionGreen_right
statement: formalized
---

# Allele age and the Maruyama effect

45 results, 43 proved and 2 without a declaration, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html).

## Positivity of the slope constant in Kimura's formula

The slope constant of Kimura's formula is positive.

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#kimura-slope-pos).

## Kimura's fixation probability is strictly increasing

Kimura's fixation probability is strictly increasing in the initial frequency.

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#strict-mono-kimura-fixation).

## Positivity of Kimura's fixation probability

An allele present at positive frequency has positive fixation probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#kimura-fixation-pos).

## Kimura's fixation probability is less than one

An allele at frequency below `1` is lost with positive probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_lt_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#kimura-fixation-lt-one).

## Sojourn density of the Wright–Fisher diffusion with selection

The sojourn density (Green's function) of the Wright–Fisher diffusion with genic selection,
time in units of `2N` generations, `σ = 2Ns`. With `u = kimuraFixation σ` and
`u'(x) = kimuraSlope σ · e^{-2σx}`,

`Ψ(p, x) = 2 u(min p x) (1 - u(max p x)) / (x (1 - x) u'(x))`,

which is `2 S(min p x) (S(1) - S(max p x)) / (S(1) x (1 - x) e^{-2σx})` in terms of the scale
function `S(y) = (1 - e^{-2σy}) / (2σ)` (`S(y) = y` if `σ = 0`). The neutral case is handled by
the neutral branches of `kimuraFixation` and `kimuraSlope` (`selectionGreen_zero`). It is
meaningful for `0 < x < 1`; at `x = 0, 1` the denominator vanishes and division by `0` gives `0`
(a null set for integrals in `x`). In the diffusion reading, `Ψ(p, x) dx`
is the expected time an allele started at frequency `p` spends in `(x, x + dx)` before loss or
fixation (Ewens 2004, Chapter 4; the paper's `Ψ(p, x)` divided by `2N`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.selectionGreen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#selection-green).

## Neutral case of the sojourn density

For `σ = 0` and `0 < x < 1` the sojourn density is the neutral Green's function.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.selectionGreen_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#selection-green-zero).

## The general Green kernel specializes to Kimura's sojourn density

For genic selection
`b x = σ x (1 - x)`, `a x = x (1 - x)`, the general Green's function `greenFunction` is
`selectionGreen σ` on `[0, 1] × (0, 1)`. The scale function is `S(y) = u(y) / u'(0)` with
`u = kimuraFixation σ` and `u'(0) = kimuraSlope σ`, since both have derivative `ψ(y) = e^{-2σy}`
and vanish at `0`; substituting that and `S(1) = 1 / u'(0)` into `greenFunction` gives
`selectionGreen`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.greenFunction_eq_selectionGreen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#green-function-eq-selection-green).

## Green's representation with selection

**Green's representation with selection** (Ewens 2004, Chapter 4; the integrated form of the
paper's `-δ(x - p) = s p (1 - p) ∂Ψ/∂p + p (1 - p) / (4N) ∂²Ψ/∂p²`). For continuous `g` and
`p ∈ (0, 1)`, `v(q) = ∫₀¹ Ψ(q, x) g(x) dx` solves `L_σ v = -g` at `p`; with
`integral_selectionGreen_left` and `integral_selectionGreen_right` (`v(0) = v(1) = 0`) this
generalizes `generator_integral_neutralGreen` to `σ ≠ 0`. In the diffusion reading, `v(p)` is the expected value of `∫₀^T g(X_t) dt` up to absorption.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_integral_selectionGreen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#generator-integral-selection-green).

## Sojourn density from frequency zero vanishes

Boundary value at `0`: an absent allele spends no time in `(0, 1)`, so
`∫₀¹ Ψ(0, x) g(x) dx = 0` for every `g`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_selectionGreen_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#integral-selection-green-left).

## Sojourn density from frequency one vanishes

Boundary value at `1`: a fixed allele spends no time in `(0, 1)`, so
`∫₀¹ Ψ(1, x) g(x) dx = 0` for every `g`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_selectionGreen_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#integral-selection-green-right).

## Sojourn density solves the backward equation below the target

Below the target frequency the sojourn density solves the homogeneous backward equation in
its first argument: `L_σ Ψ(·, x) = 0` at every `p < x` (pointwise form of the paper's
`-δ(x - p) = L_σ Ψ(·, x)`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_selectionGreen_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#generator-selection-green-of-lt).

## Sojourn density solves the backward equation above the target

Above the target frequency: `L_σ Ψ(·, x) = 0` at every `p > x`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_selectionGreen_of_gt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#generator-selection-green-of-gt).

## Continuity of the sojourn density in the starting frequency

The sojourn density is continuous in the starting frequency (in particular at `p = x`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.continuous_selectionGreen_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#continuous-selection-green-left).

## Left derivative of the sojourn density at the diagonal

Left derivative at the diagonal: `∂_p Ψ(x⁻, x) = 2 (1 - u(x)) / (x (1 - x))`. Together with
`hasDerivWithinAt_selectionGreen_Ici` this gives the jump `-2 / (x (1 - x))` of `∂_p Ψ` at
`p = x`, i.e. `L_σ Ψ(·, x) = -δ_x` in the distributional sense.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasDerivWithinAt_selectionGreen_Iic`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#has-deriv-within-at-selection-green-iic).

## Right derivative of the sojourn density at the diagonal

Right derivative at the diagonal: `∂_p Ψ(x⁺, x) = -2 u(x) / (x (1 - x))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasDerivWithinAt_selectionGreen_Ici`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#has-deriv-within-at-selection-green-ici).

## Maruyama–Kimura conditional sojourn density

The Maruyama–Kimura conditional sojourn density (the paper's `Ψ_z(p, z)`): given the initial
frequency `p` and the current frequency `x`, the density of mean time spent at frequency `z`
along the path, `Ψ(p, z) Ψ(z, x) / Ψ(p, x)` (Maruyama and Kimura 1975; Kiezun et al. 2013,
Methods). Time in units of `2N` generations.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ageDensity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#age-density).

## Closed-form sojourn density below the current frequency

The paper's closed form `Ψ₁(z)` for `0 < z < x` (Kiezun et al. 2013, Methods), in units of
`2N` generations with `σ = 2Ns`:
`(e^{-2σ(1-z)} - 1)(e^{-2σz} - 1) / (σ z (1 - z) (1 - e^{-2σ}))`, and its continuous extension
`2` for `σ = 0`. It does not depend on the current frequency `x`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 519](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L519). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below).

## Closed-form sojourn density above the current frequency

The paper's closed form `Ψ₂(z)` for `x < z < 1` (Kiezun et al. 2013, Methods), in units of
`2N` generations with `σ = 2Ns`:
`(e^{-2σ(1-z)} - 1)(e^{2σ(1-z)} - 1)(1 - e^{2σx}) /
(σ z (1 - z)(e^{-2σ(1-x)} - 1)(1 - e^{2σ}))`, and its continuous extension
`2 x (1 - z) / ((1 - x) z)` for `σ = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above).

## Mean age of an allele at a given frequency

The mean age of an allele at current frequency `x` (the paper's `a(x)`), in units of `2N`
generations: `∫₀^x Ψ₁(z) dz + ∫_x^1 Ψ₂(z) dz`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAge`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#mean-age).

## Sojourn density below the current frequency via fixation probability

`Ψ₁` through Kimura's fixation probability: `Ψ₁(z) = 2 u(z)(1 - u(z)) / (z (1 - z) u'(z))`
on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-eq).

## Sojourn density above the current frequency via fixation probability

`Ψ₂` through Kimura's fixation probability:
`Ψ₂(z) = 2 u(x)(1 - u(z))² / ((1 - u(x)) z (1 - z) u'(z))` on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-eq).

## Closed form below the current frequency

For `0 < p ≤ z ≤ x < 1` the conditional sojourn
density is the paper's `Ψ₁(z)`; it depends neither on `p` nor on `x`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ageDensity_of_le_of_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 611](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L611). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#age-density-of-le-of-le).

## Closed form above the current frequency

For `0 < p ≤ x ≤ z < 1` the conditional sojourn
density is the paper's `Ψ₂(z)`; it does not depend on `p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.ageDensity_of_le_of_ge`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#age-density-of-le-of-ge).

## Paper units

With `N` diploid individuals, selection coefficient `s ≠ 0` and time in
generations, the paper prints `Ψ₁(z) = (e^{-γ(1-z)} - 1)(e^{-γz} - 1) / (s z (1 - z)(1 - e^{-γ}))`
with `γ = 4Ns`; it equals `2N · maruyamaBelow (2Ns) z`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_generations`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-generations).

## Paper units

The paper's
`Ψ₂(z) = (e^{-γ(1-z)} - 1)(e^{γ(1-z)} - 1)(1 - e^{γx}) / (s z (1 - z)(e^{-γ(1-x)} - 1)(1 - e^{γ}))`,
`γ = 4Ns`, equals `2N · maruyamaAbove (2Ns) x z`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_generations`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-generations).

## Kimura and Ohta (1973)

The mean age of a neutral allele at frequency `x ∈ (0, 1)` is
`-2 x log x / (1 - x)` in units of `2N` generations (`-4N x ln x / (1 - x)` generations).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAge_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 677](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L677). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#mean-age-zero).

## Hyperbolic form of the sojourn density below the current frequency

`Ψ₁` in hyperbolic form: `2 sinh(σz) sinh(σ(1 - z)) / (σ z (1 - z) sinh σ)` for `σ ≠ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_eq_sinh`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 712](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L712). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-eq-sinh).

## Hyperbolic form of the sojourn density above the current frequency

`Ψ₂` in hyperbolic form:
`2 sinh(σ(1 - z))² sinh(σx) / (σ sinh σ sinh(σ(1 - x)) z (1 - z))` for `σ ≠ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_eq_sinh`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 732](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L732). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-eq-sinh).

## Symmetry

`Ψ₁` is the same for `σ` and `-σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_neg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 765](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L765). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-neg).

## Symmetry

`Ψ₂` is the same for `σ` and `-σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_neg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 774](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L774). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-neg).

## Positivity of the sojourn density below the current frequency

`Ψ₁` is positive on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-pos).

## Maruyama effect, below the current frequency

For `σ ≠ 0`, `Ψ₁(z) < 2`, its neutral
value, for every `z ∈ (0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 842](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L842). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-lt).

## Maruyama effect, above the current frequency

For `σ ≠ 0` and `0 < x < z < 1`,
`Ψ₂(z)` is strictly below its neutral value `2 x (1 - z) / ((1 - x) z)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 878](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L878). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-lt).

## Positivity of the sojourn density above the current frequency

`Ψ₂` is positive for `0 < x < z < 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-pos).

## Sojourn density above the current frequency vanishes at one

At `z = 1` the closed form `Ψ₂` vanishes (a null set for the integral).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_one_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 909](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L909). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-one-right).

## Integrability of the sojourn density below the current frequency

`Ψ₁` is integrable on `[0, x]` (it is bounded by `2`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.intervalIntegrable_maruyamaBelow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#interval-integrable-maruyama-below).

## Integrability of the sojourn density above the current frequency

`Ψ₂` is integrable on `[x, 1]` for `x ∈ (0, 1)` (it is bounded by `2 / (1 - x)`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.intervalIntegrable_maruyamaAbove`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 943](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L943). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#interval-integrable-maruyama-above).

## Symmetry

The mean age is the same for `σ` and `-σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAge_neg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 965](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L965). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#mean-age-neg).

## The Maruyama effect (Kiezun et al. 2013)

For `σ ≠ 0` and `x ∈ (0, 1)`, an allele under
selection, advantageous or deleterious, is on average strictly younger than a neutral allele at
the same frequency.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAge_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 980](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L980). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#mean-age-lt).

## Mean age as the limit of conditional sojourn times

**Mean age as the limit of conditional sojourn times** (Maruyama 1974; Kiezun et al. 2013,
Methods): for `x ∈ (0, 1)`, the total conditional sojourn time `∫₀¹ Ψ_z(p, z) dz` of a path
from initial frequency `p` to current frequency `x` tends to the mean age `a(x)` as `p → 0⁺`
(an allele arises at frequency close to `0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_integral_ageDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 1076](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L1076). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#tendsto-integral-age-density).

## Stronger selection, smaller `Ψ₁`

For `0 ≤ σ < τ` and `z ∈ (0, 1)`,
`Ψ₁` at `τ` is strictly below `Ψ₁` at `σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaBelow_lt_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 1286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L1286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-below-lt-of-lt).

## Stronger selection, smaller `Ψ₂`

For `0 ≤ σ < τ` and `0 < x < z < 1`,
`Ψ₂` at `τ` is strictly below `Ψ₂` at `σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.maruyamaAbove_lt_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 1299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L1299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#maruyama-above-lt-of-lt).

## Stronger selection, younger alleles

At a fixed frequency `x ∈ (0, 1)`, the mean age is
strictly decreasing in `σ ≥ 0`. Kiezun et al. (2013, Figure 1b) show this numerically from the
closed forms; here it is proved.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAge_lt_meanAge_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 1313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L1313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#mean-age-lt-mean-age-of-lt).

## Stronger selection, younger alleles

**Stronger selection, younger alleles**, for either sign of selection: if `|σ| < |τ|` then
an allele at frequency `x ∈ (0, 1)` under selection `τ` is on average strictly younger than one
under selection `σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAge_lt_meanAge_of_abs_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 1331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L1331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#mean-age-lt-mean-age-of-abs-lt).

## Mean time as a sum of sojourn times

**Mean time as a sum of sojourn times** (the identity behind Maruyama and Kimura 1975). For
a jointly measurable family of transition densities `w p x t ≥ 0` on `(0, 1)` satisfying the
Chapman–Kolmogorov equation for positive times,
`∫₀^∞ t w(p, x, t) dt = ∫₀¹ Ψ(p, y) Ψ(y, x) dy` with `Ψ(p, x) = ∫₀^∞ w(p, x, t) dt`, in
`ℝ≥0∞`. Dividing by `Ψ(p, x)` reads `∫₀¹ Ψ(p, y) Ψ(y, x) / Ψ(p, x) dy` (the integral of
`ageDensity` when `Ψ = selectionGreen σ`) as a mean time. The statement is abstract: no
diffusion is constructed, and `w` is not required to be the Wright–Fisher transition density.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.lintegral_mul_eq_lintegral_sojourn_mul`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean, line 1395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/AlleleAge.lean#L1395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html#lintegral-mul-eq-lintegral-sojourn-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Allele age and the Maruyama effect](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/allele-age-and-the-maruyama-effect)
