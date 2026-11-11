---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.asgGenerator, MathlibExt.Biology.PopulationGenetics.Diffusion.generator_one_sub_pow, MathlibExt.Biology.PopulationGenetics.Diffusion.generator_one_sub_pow_eq_asgGenerator, MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary, MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary_detailed_balance, MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary_global_balance, MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary_nonneg, MathlibExt.Biology.PopulationGenetics.Diffusion.hasSum_asgStationary_mul_pow
statement: formalized
proof: formalized
---

# Selection duality and general one-dimensional diffusions

56 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html).

## Ancestral selection graph duality

## Generator of the ancestral selection graph line-counting process

The generator of the line-counting process of the ancestral selection graph with scaled
selection coefficient `σ` (time in units of `2N` generations, the scaling of `generator`):
from `n` lines, branching `n → n + 1` at rate `n σ` and coalescence `n → n - 1` at rate
`C(n, 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.asgGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#asg-generator).

## Selection duality (Mano 2009)

**Selection duality (Mano 2009)** at generator level, with the line-counting process of the
ancestral selection graph (Krone–Neuhauser 1997) as the dual: the
Wright–Fisher generator with genic selection maps `y ↦ (1 - y) ^ n` to
`C(n, 2) ((1 - x)^(n-1) - (1 - x)^n) + n σ ((1 - x)^(n+1) - (1 - x)^n)`. This identity holds for
every real `σ`; the dual is a Markov chain only for `σ ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_one_sub_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#generator-one-sub-pow).

## Selection duality in operator form

The selection duality in operator form: `L_σ` applied to `y ↦ (1 - y) ^ n` equals the
ancestral-selection-graph generator applied to `k ↦ (1 - x) ^ k` at `n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_one_sub_pow_eq_asgGenerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#generator-one-sub-pow-eq-asg-generator).

## Stationary law of the ancestral selection graph line counts

The stationary law of the ancestral-selection-graph line-counting process with `σ > 0`:
`π_k = (2σ)^k / k! / (e^{2σ} - 1)` for `k ≥ 1` and `π_0 = 0`, a Poisson`(2σ)` law conditioned
to be positive. For `σ = 0` the stationary law is `δ₁`: branching vanishes, coalescence
reaches state `1`, and state `1` is absorbing, so `π_1 = 1` and `π_k = 0` otherwise (the
limit of the `σ > 0` formula as `σ → 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#asg-stationary).

## Detailed balance

**Detailed balance** of the ancestral-selection-graph chain:
`π_k · (k σ) = π_{k+1} · C(k + 1, 2)` for every `k` (the flux `k → k + 1` equals the flux
`k + 1 → k`). This is an identity for every real `σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary_detailed_balance`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#asg-stationary-detailed-balance).

## Global balance

**Global balance** (stationarity `π Q = 0`) of the ancestral-selection-graph chain at
state `k + 1`: the outflow `π_{k+1} ((k + 1) σ + C(k + 1, 2))` equals the inflow
`π_k (k σ) + π_{k+2} C(k + 2, 2)` (for `k = 0` the inflow from the unreachable state `0`
vanishes).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary_global_balance`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#asg-stationary-global-balance).

## Stationary weights under selection are nonnegative

For `σ > 0` the stationary weights are nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.asgStationary_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#asg-stationary-nonneg).

## Generating function of the stationary law under selection

The probability generating function of the stationary law: for `σ > 0` and every real `y`,
`∑ₖ π_k y^k = (e^{2σy} - 1) / (e^{2σ} - 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasSum_asgStationary_mul_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-sum-asg-stationary-mul-pow).

## Stationary weights under selection sum to one

For `σ > 0` the stationary weights sum to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasSum_asgStationary`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-sum-asg-stationary).

## Neutral stationary law is the point mass at one

The neutral stationary law is `δ₁`: its generating function is `y`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasSum_asgStationary_mul_pow_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-sum-asg-stationary-mul-pow-zero).

## Neutral stationary weights sum to one

The neutral stationary weights sum to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasSum_asgStationary_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-sum-asg-stationary-zero).

## Loss probability in Kimura's fixation formula

The loss probability in Kimura's formula, written with positive exponents: for `σ ≠ 0`,
`1 - kimuraFixation σ x = (e^{2σ(1 - x)} - 1) / (e^{2σ} - 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.one_sub_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#one-sub-kimura-fixation).

## Loss probability from the stationary ancestral selection graph

**Loss probability from the stationary ancestral selection graph** (Mano 2009): for
`σ > 0`, `∑ₖ π_k (1 - x)^k = 1 - kimuraFixation σ x`, i.e. the loss
probability of the favoured allele at frequency `x` is the probability that all lines of the
stationary ancestral selection graph carry the unfavoured allele. Only the series identity is
formalized; the sampling interpretation is not.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasSum_asgStationary_mul_one_sub_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-sum-asg-stationary-mul-one-sub-pow).

## Backward generator of a one-dimensional diffusion

The backward generator of a one-dimensional diffusion with drift `b` and infinitesimal
variance `a`: `(L u)(x) = a(x) / 2 · u''(x) + b(x) · u'(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.diffusionGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#diffusion-generator).

## Scale density of a one-dimensional diffusion

The scale density `ψ(y) = exp (-∫₀^y 2 b(z) / a(z) dz)` of the diffusion with drift `b`
and variance `a` (Karlin–Taylor 1981, Chapter 15).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.scaleDensity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#scale-density).

## Scale function of a one-dimensional diffusion

The scale function `S(p) = ∫₀^p ψ(y) dy`, normalized by `S(0) = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.scaleFunction`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#scale-function).

## Dirichlet ratio $S(p)/S(1)$ of the scale function

The analytic Dirichlet ratio `S(p) / S(1)` for drift `b` and variance `a` (Kimura 1962;
Ewens 2004, Chapter 4). This is the solution of the backward boundary-value problem
`L u = 0`, `u(0) = 0`, `u(1) = 1` (see `eq_fixationProb_of_diffusionGenerator_eq_zero`).
It is the hitting probability `P_p(hit 1 before 0)` only when both boundaries are
Feller-accessible; that is not implied by `IsRegularDiffusion` (see the module docstring for
the `a x = x² (1 - x)²` counterexample).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.fixationProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#fixation-prob).

## Dirichlet Green's function of a one-dimensional diffusion

The Green's function (analytic Green kernel) of `-L` with Dirichlet conditions at `0` and `1`
(Ewens 2004, Chapter 4; Karlin–Taylor 1981, Chapter 15):
`G(p, x) = 2 S(min p x) (S(1) - S(max p x)) / (S(1) a(x) ψ(x))`. In the diffusion reading (which requires Feller-accessible boundaries), `G(p, x) dx` is the expected time
spent in `(x, x + dx)` before absorption.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.greenFunction`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#green-function).

## Standing regularity hypotheses for a diffusion on $(0, 1)$

Regularity hypotheses for a diffusion on `(0, 1)` with drift `b` and variance `a`: `a` is
positive and continuous on `(0, 1)`, `b / a` is continuous on `(0, 1)` and integrable on
`[0, 1]` (so the scale function is finite up to both boundaries). The values of `b` and `a` at
`0` and `1` are irrelevant. These are standing hypotheses for this file, not Feller's
classification of regular boundaries: they do **not** imply that either endpoint is
accessible (finite scale–speed integrals), so the hitting-probability reading of
`fixationProb` needs that extra hypothesis.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion`, a structure declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#is-regular-diffusion).

## Positivity of the scale density

The scale density is positive.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.scaleDensity_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#scale-density-pos).

## Scale function vanishes at zero

The scale function vanishes at `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.scaleFunction_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#scale-function-zero).

## Continuity of the scale density on $(0, 1)$

The scale density is continuous on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.continuousOn_scaleDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#continuous-on-scale-density).

## Derivative of the scale density

`ψ' = -(2 b / a) ψ` inside the interval.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.hasDerivAt_scaleDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-deriv-at-scale-density).

## Derivative of the scale function is the scale density

`S' = ψ` inside the interval.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.hasDerivAt_scaleFunction`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#has-deriv-at-scale-function).

## Continuity of the scale function on $(0, 1)$

The scale function is continuous on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.continuousOn_scaleFunction`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#continuous-on-scale-function).

## Scale function is strictly increasing

The scale function is strictly increasing on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.strictMonoOn_scaleFunction`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 463](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L463). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#strict-mono-on-scale-function).

## Scale function is positive at one

`S(1) > 0`, so the scale-function ratio and the Green's function have a positive
denominator.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.scaleFunction_one_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#scale-function-one-pos).

## Dirichlet ratio equals one at $p = 1$

A fixed allele stays fixed.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.fixationProb_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#fixation-prob-one).

## Dirichlet ratio lies in $(0, 1)$

The scale-function ratio lies in `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.IsRegularDiffusion.fixationProb_mem_Icc`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#fixation-prob-mem-icc).

## Dirichlet ratio vanishes at $p = 0$

An absent allele is never fixed (for every `b`, `a`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.fixationProb_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#fixation-prob-zero).

## Kimura (1962)

The scale-function ratio `S / S(1)` solves the backward equation
`a / 2 · u'' + b · u' = 0` on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.diffusionGenerator_fixationProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#diffusion-generator-fixation-prob).

## Solutions of `L u = 0`

If `u` is continuous on `[0, 1]`, differentiable on `(0, 1)`
with derivative differentiable on `(0, 1)`, and `L u = 0` on `(0, 1)`, then
`u = u(0) + (u(1) - u(0)) · S / S(1)` on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.eq_of_diffusionGenerator_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#eq-of-diffusion-generator-eq-zero).

## Uniqueness of the scale-function ratio (Kimura 1962)

A function continuous on
`[0, 1]`, differentiable on `(0, 1)` with derivative differentiable on `(0, 1)`, solving
`L u = 0` on `(0, 1)` with `u(0) = 0` and `u(1) = 1` equals `S / S(1)` on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.eq_fixationProb_of_diffusionGenerator_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#eq-fixation-prob-of-diffusion-generator).

## Uniqueness for the Dirichlet problem

Two functions continuous on `[0, 1]`,
differentiable on `(0, 1)` with derivatives differentiable on `(0, 1)`, with `L u = L v` on
`(0, 1)` and the same values at `0` and `1`, agree on `[0, 1]`. Together with
`diffusionGenerator_integral_greenFunction` this identifies the Green integral as the solution
of `L v = -g`, `v(0) = v(1) = 0` whenever it has this regularity.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.eq_of_diffusionGenerator_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#eq-of-diffusion-generator-eq).

## Green's representation (Ewens 2004, Chapter 4; Karlin–Taylor 1981, Chapter 15)

Let `g` be
continuous on `(0, 1)` and assume the two halves of the Green integral are integrable away from
the opposite boundary: `S g / (a ψ)` on `[0, q]` and `(S(1) - S) g / (a ψ)` on `[q, 1]` for every
`q ∈ (0, 1)` (true for every `g` continuous on `[0, 1]` under genic selection, where
`S / (a ψ)` is bounded near `0` and `(S(1) - S) / (a ψ)` near `1`). Then
`v(q) = ∫₀¹ G(q, x) g(x) dx` solves `L v = -g` on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.diffusionGenerator_integral_greenFunction`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#diffusion-generator-integral-green-funct).

## Dirichlet condition of the Green's function at zero

Dirichlet condition at `0`: `∫₀¹ G(0, x) g(x) dx = 0` (for every `b`, `a`, `g`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_greenFunction_zero_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 722](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L722). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#integral-green-function-zero-left).

## Dirichlet condition of the Green's function at one

Dirichlet condition at `1`: `∫₀¹ G(1, x) g(x) dx = 0` (for every `b`, `a`, `g`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_greenFunction_one_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#integral-green-function-one-left).

## Wright–Fisher generator with genic selection as a general diffusion

The general generator with drift `σ x (1 - x)` and variance `x (1 - x)` is the Wright–Fisher
generator with genic selection.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.diffusionGenerator_wrightFisher`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#diffusion-generator-wright-fisher).

## Wright–Fisher diffusion with genic selection is regular

The Wright–Fisher diffusion with genic selection is regular.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.isRegularDiffusion_wrightFisher`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#is-regular-diffusion-wright-fisher).

## Scale density of the Wright–Fisher diffusion with genic selection

The scale density of the Wright–Fisher diffusion with genic selection is `e^{-2σy}` on
`[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.scaleDensity_wrightFisher`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 762](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#scale-density-wright-fisher).

## Kimura's formula as a corollary

For genic selection the general scale-function ratio
is `kimuraFixation σ p` on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.fixationProb_wrightFisher`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 776](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L776). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#fixation-prob-wright-fisher).

## General Green's function agrees with the neutral Wright–Fisher one

The general Green's function of the neutral Wright–Fisher diffusion (`b = 0`,
`a = x (1 - x)`) is the neutral Green's function of `Sojourn.lean` for `x ∈ (0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.greenFunction_neutral`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 793](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L793). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#green-function-neutral).

## Drift of an allele under selection with dominance

The drift `2 c x (1 - x) (h + (1 - 2h) x)` of an allele at frequency `x` with genotype
fitnesses `1`, `1 + h s`, `1 + s` (for zero, one and two copies), `c = N s`, time in units of
`2N` generations (Kimura 1962). For `h = 1/2` it is genic selection with `σ = c`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.dominanceDrift`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#dominance-drift).

## Diffusion with dominance is regular

The diffusion with dominance is regular.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.isRegularDiffusion_dominance`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 816](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#is-regular-diffusion-dominance).

## Kimura's scale-function ratio with dominance (Kimura 1962)

With `D = 2h - 1`, for
`p ∈ [0, 1]`,
`u(p) = ∫₀^p e^{-2cDx(1-x) - 2cx} dx / ∫₀¹ e^{-2cDx(1-x) - 2cx} dx`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.fixationProb_dominance`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 837](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L837). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#fixation-prob-dominance).

## Sojourn density conditioned on fixation

The sojourn density conditioned on fixation, the Doob `h`-transform of the Green's function
by the fixation probability `u`: `G(p, x) u(x) / u(p)` (Kimura–Ohta 1969; Ewens 2004, Chapter 4).
At `p = 0` it is the junk value `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.conditionalGreen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 878](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L878). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#conditional-green).

## Conditional mean time to fixation, backward equation

Under the hypotheses of
`diffusionGenerator_integral_greenFunction` for `g = u` (the fixation probability), the
function `w(q) = u(q) · ∫₀¹ G*(q, x) dx`, with `G*` the conditional sojourn density, solves
`L w = -u` on `(0, 1)` (Ewens 2004, Chapter 4).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.diffusionGenerator_mul_integral_conditionalGreen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 885](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L885). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#diffusion-generator-mul-integral-conditi).

## Neutral conditional mean time to fixation

The neutral conditional mean time to fixation `t̄₁(p) = -2 (1 - p) log (1 - p) / p`, in
units of `2N` generations (Kimura–Ohta 1969). It is meaningful for `p ∈ (0, 1)`; at `p = 0`
the division gives the junk value `0` (the limit is `2`, see
`tendsto_neutralFixationTime_zero`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.neutralFixationTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 912](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L912). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#neutral-fixation-time).

## Neutral conditional mean time to loss

The neutral conditional mean time to loss `t̄₀(p) = -2 p log p / (1 - p)`, in units of
`2N` generations (Kimura–Ohta 1969). It is meaningful for `p ∈ (0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.neutralLossTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 917](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L917). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#neutral-loss-time).

## Neutral loss time equals fixation time at $1 - p$

Loss of an allele at frequency `p` is fixation of the other allele at `1 - p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.neutralLossTime_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 921](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L921). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#neutral-loss-time-eq).

## Neutral conditional fixation time as an `h`-transformed sojourn integral

For
`p ∈ (0, 1)`, `∫₀¹ G(p, x) · x / p dx = -2 (1 - p) log (1 - p) / p`, with `G` the neutral
Green's function and `u(x) = x` the neutral fixation probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen_mul_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#integral-neutral-green-mul-div).

## Neutral conditional loss time

For `p ∈ (0, 1)`,
`∫₀¹ G(p, x) · (1 - x) / (1 - p) dx = -2 p log p / (1 - p)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen_mul_one_sub_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 999](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L999). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#integral-neutral-green-mul-one-sub-div).

## The general `h`-transform specializes to Kimura–Ohta

For the neutral Wright–Fisher
diffusion (`b = 0`, `a = x (1 - x)`) and `p ∈ (0, 1)`, the total conditional sojourn time
`∫₀¹ G(p, x) u(x) / u(p) dx` is `-2 (1 - p) log (1 - p) / p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_conditionalGreen_neutral`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 1017](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L1017). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#integral-conditional-green-neutral).

## Backward equation for the neutral conditional fixation time

The neutral conditional fixation time satisfies the conditioned backward equation
`L_0 (p · t̄₁(p)) = -p` on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_mul_neutralFixationTime`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 1043](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L1043). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#generator-mul-neutral-fixation-time).

## `t̄₁(0⁺) = 2`

A new neutral mutation that is destined to fix takes on average `2`
units (`4N` generations) to do so (Kimura–Ohta 1969).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_neutralFixationTime_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 1066](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L1066). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#tendsto-neutral-fixation-time-zero).

## Total expectation

For `p ∈ (0, 1)`,
`p · t̄₁(p) + (1 - p) · t̄₀(p) = -2 (p log p + (1 - p) log (1 - p))`, the unconditional mean
absorption time.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.mul_neutralFixationTime_add_mul_neutralLossTime`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean, line 1085](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/GeneralDiffusion.lean#L1085). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html#mul-neutral-fixation-time-add-mul-neutra).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Selection duality and general one-dimensional diffusions](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/selection-duality-and-general-one-dimensional-di)
