---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes, MathlibExt.Biology.PopulationGenetics.Coalescent.skylineLogLik, MathlibExt.Biology.PopulationGenetics.Coalescent.skylineLogLik_le, MathlibExt.Biology.PopulationGenetics.Coalescent.skylineLogLik_eq_iff, MathlibExt.Biology.PopulationGenetics.Coalescent.sum_skylineLogLik_le, MathlibExt.Biology.PopulationGenetics.Coalescent.sum_skylineLogLik_eq_iff, MathlibExt.Biology.PopulationGenetics.Coalescent.skylineEstimate, MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes.integral_skylineEstimate
statement: formalized
proof: formalized
---

# Skyline plot estimates of population size

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html).

## Coalescent

## Coalescent intervals under the classic skyline model

The coalescent intervals of a sample of `n` genes under the classic skyline model with
piecewise-constant population-size parameter `θ k` while there are `k` lineages: `T k` is
exponential with rate `C(k, 2) / θ k`, independently over `2 ≤ k ≤ n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes`, a structure declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#skyline-times).

## Log-likelihood of one coalescent interval in the skyline model

The log-likelihood of `θ` for one coalescent interval of length `w` with `c = C(k, 2)`
pairs of lineages: the log-density `log (c / θ) - c w / θ` of `Exp(c / θ)` at `w`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.skylineLogLik`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#skyline-log-lik).

## The skyline estimate maximizes the interval likelihood

**The skyline estimate maximizes the interval likelihood** (Pybus, Rambaut & Harvey 2000):
for `c, w, θ > 0`, `ℓ(θ) ≤ ℓ(c w)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.skylineLogLik_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#skyline-log-lik-le).

## Uniqueness of the skyline maximizer

For `c, w, θ > 0`, `ℓ(θ) = ℓ(c w)` iff
`θ = c w`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.skylineLogLik_eq_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#skyline-log-lik-eq-iff).

## The skyline estimates jointly maximize the likelihood

For positive `c i`, `w i`,
`θ i` over a finite set of intervals, `∑ ℓ_i(θ_i) ≤ ∑ ℓ_i(c_i w_i)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_skylineLogLik_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#sum-skyline-log-lik-le).

## Uniqueness of the joint maximizer

Equality in `sum_skylineLogLik_le` holds iff
`θ i = c i w i` for every interval.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.sum_skylineLogLik_eq_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#sum-skyline-log-lik-eq-iff).

## Classic skyline estimate of population size

The classic skyline estimate `θ̂_k = C(k, 2) w_k` for the interval with `k` lineages.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.skylineEstimate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#skyline-estimate).

## The skyline estimate is unbiased

`E[C(k, 2) T k] = θ k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes.integral_skylineEstimate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#integral-skyline-estimate).

## Variance of the skyline estimate

`Var[C(k, 2) T k] = θ k²`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes.variance_skylineEstimate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#variance-skyline-estimate).

## The skyline estimates are independent

**The skyline estimates are independent** across intervals.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes.iIndepFun_skylineEstimate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#i-indep-fun-skyline-estimate).

## Canonical probability space for the skyline model

The canonical probability space for the skyline model: the product of the exponential laws
`Exp(C(k, 2) / θ k)`, `2 ≤ k ≤ n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.skylinePiMeasure`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#skyline-pi-measure).

## Coordinate projections form a skyline model

The coordinate projections of `skylinePiMeasure n θ` form a skyline model whenever the
`θ k` are positive; in particular `SkylineTimes` is inhabited.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SkylineTimes.ofPi`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/Skyline.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html#of-pi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Skyline plot estimates of population size](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/skyline-plot-estimates-of-population-size)
