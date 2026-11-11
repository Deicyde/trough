---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.abs_expectedSFS_le, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeDensity, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.integrable_expectedSFS, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_eq_integral_dfeDensity, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_dirac, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_add_measure, MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_smul_measure
statement: formalized
proof: formalized
---

# Distribution of fitness effects

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html).

## A bound on the expected spectrum

## Uniform bound on the expected site-frequency spectrum

The expected number of sites with `i` derived copies in a sample of `n`, `1 ≤ i < n`, is
bounded uniformly in the selection coefficient: `|E ξ_i(σ)| ≤ |θ| C(n, i)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.abs_expectedSFS_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#abs-expected-sfs-le).

## Site-frequency spectrum under a distribution of fitness effects

The expected unfolded site-frequency spectrum under the distribution of fitness effects
`μ` (a law on the scaled selection coefficient `σ = 2Ns`): `∫ E ξ_i(σ) dμ(σ)`, where each new
mutation draws its own `σ` from `μ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS`, a definition declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-sfs).

## Frequency density averaged over a distribution of fitness effects

The Poisson-random-field frequency density averaged over the distribution of fitness
effects `μ`: `∫ φ_σ(x) dμ(σ)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeDensity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-density).

## Integrability of the expected spectrum in the selection coefficient

For `1 ≤ i < n`, the expected spectrum `E ξ_i(σ)` is integrable in `σ` against every
finite measure.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.integrable_expectedSFS`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#integrable-expected-sfs).

## Mixture identity

For a finite measure `μ` of selection coefficients and a segregating
class `1 ≤ i < n`, the DFE-averaged spectrum is the binomial sampling integral of the
DFE-averaged frequency density:
`∫ E ξ_i(σ) dμ(σ) = ∫₀¹ C(n, i) x ^ i (1 - x) ^ (n - i) (∫ φ_σ(x) dμ(σ)) dx`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_eq_integral_dfeDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-sfs-eq-integral-dfe-density).

## Spectrum under a point-mass DFE is the single-selection spectrum

A DFE concentrated on one selection coefficient gives the single-`σ` spectrum.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_dirac`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-sfs-dirac).

## DFE spectrum is additive in the measure

The spectrum is additive in the (finite) DFE.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_add_measure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-sfs-add-measure).

## DFE spectrum is homogeneous in the measure

The spectrum is homogeneous in the DFE.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_smul_measure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-sfs-smul-measure).

## Gamma distribution of fitness effects

The gamma distribution of fitness effects (Boyko et al. 2008): the scaled selection
coefficient is `σ = -T` with `T ~ Gamma(a, r)`, shape `a > 0` and rate `r > 0` (scale `1 / r`),
so new mutations are deleterious with mean strength `a / r`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.gammaDFE`, a definition declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#gamma-dfe).

## Gamma DFE is a probability measure

The gamma DFE is a probability law.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.isProbabilityMeasure_gammaDFE`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#is-probability-measure-gamma-dfe).

## No mutation is beneficial under the gamma DFE

Under the gamma DFE no mutation is beneficial.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.gammaDFE_Ioi_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#gamma-dfe-ioi-zero).

## Mean selection coefficient under the gamma DFE

The mean scaled selection coefficient under the gamma DFE is `-a / r`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.integral_id_gammaDFE`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#integral-id-gamma-dfe).

## Variance of the selection coefficient under the gamma DFE

The variance of the scaled selection coefficient under the gamma DFE is `a / r ^ 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.variance_id_gammaDFE`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#variance-id-gamma-dfe).

## Rescaling a gamma DFE divides its rate

Rescaling a gamma DFE by `c > 0` (for example from `s` to `σ = 2Ns`, `c = 2N`) keeps the
shape and divides the rate by `c`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.gammaDFE_map_const_mul`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#gamma-dfe-map-const-mul).

## Fraction of strongly deleterious mutations

Under the gamma DFE the fraction of new
mutations with `σ < -c`, `c ≥ 0`, is the gamma tail `Γ(a, r c) / Γ(a)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.gammaDFE_real_Iio`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#gamma-dfe-real-iio).

## Fraction of mutations in a strength interval under the gamma DFE

The fraction of new mutations whose strength `-σ` lies in `(c₁, c₂]`, `0 ≤ c₁ ≤ c₂`, is
`(Γ(a, r c₁) - Γ(a, r c₂)) / Γ(a)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.gammaDFE_real_Ico`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#gamma-dfe-real-ico).

## Site-frequency spectrum under the gamma DFE

The spectrum under the gamma DFE as an integral against the gamma law of the strength.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.dfeSFS_gammaDFE`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#dfe-sfs-gamma-dfe).

## Poisson log-likelihood of counts

The Poisson log-likelihood `∑ (k_i log E_i - E_i - log k_i!)` of counts `k_i` with means
`E_i`. Meaningful for `E_i > 0`; at `E_i = 0` Lean's `log 0 = 0` gives a junk value.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.poissonLogLik`, a definition declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#poisson-log-lik).

## Probability of a count vector under independent Poisson laws

The joint law of independent Poisson counts with means `E_i` gives the count vector `k`
the probability `∏ e^{-E_i} E_i ^ {k_i} / (k_i!)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.pi_poissonMeasure_real_singleton`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#pi-poisson-measure-real-singleton).

## The Poisson-random-field log-likelihood

For independent Poisson counts with positive
means `E_i`, the log-probability of the observed counts `k` is `poissonLogLik E k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.log_pi_poissonMeasure_real_singleton`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#log-pi-poisson-measure-real-singleton).

## Derivative of the Poisson log-likelihood

The derivative of the log-likelihood in the parameter `ψ`, when the means `E_i(ψ)` are
positive and differentiable at `ψ`: `∑ (k_i / E_i(ψ) - 1) · DE_i(ψ)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.hasFDerivAt_poissonLogLik`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#has-fderiv-at-poisson-log-lik).

## Score equations

If `ψ` maximizes the Poisson log-likelihood over a parameter set `S`
that is a neighborhood of `ψ`, and the means are positive and differentiable at `ψ`, then
`∑ (k_i / E_i(ψ) - 1) · DE_i(ψ) = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.score_eq_zero_of_isMaxOn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#score-eq-zero-of-is-max-on).

## Profile maximum in `θ`

With means `E_i = θ f_i` linear in the mutation parameter,
positive `f_i` and at least one count, every `θ > 0` has likelihood at most that of
`θ̂ = ∑ k_i / ∑ f_i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.DistributionOfFitnessEffects.poissonLogLik_le_profile`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/DistributionOfFitnessEffects.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html#poisson-log-lik-le-profile).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distribution of fitness effects](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/distribution-of-fitness-effects/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/detecting-selection/distribution-of-fitness-effects)
