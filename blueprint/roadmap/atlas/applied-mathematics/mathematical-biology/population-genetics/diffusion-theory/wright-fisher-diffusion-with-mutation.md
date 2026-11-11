---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.mutationGenerator, MathlibExt.Biology.PopulationGenetics.Diffusion.mutationGenerator_zero_zero, MathlibExt.Biology.PopulationGenetics.Diffusion.betaPDFReal_eq_wrightDensity, MathlibExt.Biology.PopulationGenetics.Diffusion.contDiffOn_betaPDFReal, MathlibExt.Biology.PopulationGenetics.Diffusion.flux_betaPDFReal, MathlibExt.Biology.PopulationGenetics.Diffusion.forwardEquation_betaPDFReal, MathlibExt.Biology.PopulationGenetics.Diffusion.intervalIntegrable_mutationGenerator_mul_betaPDFReal, MathlibExt.Biology.PopulationGenetics.Diffusion.integral_mutationGenerator_mul_betaPDFReal
statement: formalized
proof: formalized
---

# Wright–Fisher diffusion with mutation

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html).

## Wright–Fisher generator with two-way mutation

The backward generator of the Wright–Fisher diffusion with two-way mutation, time in units of
`2N` generations and scaled mutation rates `θ₁ = 4N u₁` (towards the allele) and `θ₂ = 4N u₂`
(away from it): `(L f)(x) = x (1 - x) / 2 · f''(x) + (θ₁ (1 - x) - θ₂ x) / 2 · f'(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.mutationGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#mutation-generator).

## Mutation generator without mutation is the neutral generator

Without mutation the generator is the neutral Wright–Fisher generator `generator 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.mutationGenerator_zero_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#mutation-generator-zero-zero).

## Beta density as Wright's stationary density

On `(0, 1)` the Beta`(θ₁, θ₂)` density is Wright's unnormalized density in the scaled rates
`α = θ₁ / 2`, `β = θ₂ / 2`, divided by the Beta function `B(θ₁, θ₂)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.betaPDFReal_eq_wrightDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#beta-pdfreal-eq-wright-density).

## Smoothness of the Beta density on the open unit interval

The Beta`(θ₁, θ₂)` density is analytic (`C^ω`), in particular smooth, on `(0, 1)`, so the
derivatives in `flux_betaPDFReal` and `forwardEquation_betaPDFReal` exist.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.contDiffOn_betaPDFReal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#cont-diff-on-beta-pdfreal).

## Zero probability flux (Wright 1931)

On `(0, 1)` the Beta`(θ₁, θ₂)` density `π`
satisfies `½ (x (1 - x) π)' - (θ₁ (1 - x) - θ₂ x) / 2 · π = 0`. The identity holds for all real
`θ₁, θ₂` (it is linear in `π`; Mathlib's density is identically `0` when `B(θ₁, θ₂) = 0`);
`π` is a probability density when `θ₁, θ₂ > 0` (`isProbabilityMeasureBeta`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.flux_betaPDFReal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#flux-beta-pdfreal).

## Stationary forward equation (Wright 1931)

On `(0, 1)` the Beta`(θ₁, θ₂)` density `π`
solves the stationary Fokker–Planck equation `½ (a π)'' - (b π)' = 0` with `a(x) = x (1 - x)` and
`b(x) = (θ₁ (1 - x) - θ₂ x) / 2`. Holds for all real `θ₁, θ₂` (see `flux_betaPDFReal`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.forwardEquation_betaPDFReal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#forward-equation-beta-pdfreal).

## Integrability of the mutation generator against the Beta density

For `θ₁, θ₂ > 0` and `f` twice continuously differentiable on `[0, 1]`, `L f · π` is
integrable on `[0, 1]`, so the integral in `integral_mutationGenerator_mul_betaPDFReal` is a
genuine (not junk) value.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.intervalIntegrable_mutationGenerator_mul_betaPDFReal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#interval-integrable-mutation-generator-m).

## Weak stationarity of Wright's law (density form)

For `θ₁, θ₂ > 0` and every `f` twice
continuously differentiable on `[0, 1]`, `∫₀¹ (L f)(x) π(x) dx = 0` for the Beta`(θ₁, θ₂)`
density `π`. (`L f` uses `deriv`, which agrees with the one-sided derivatives inside `(0, 1)`;
its values at the endpoints do not affect the integral.) The proof is integration by parts:
`L f · π = (x ^ θ₁ (1 - x) ^ θ₂ f' / (2 B(θ₁, θ₂)))'` on `(0, 1)` because the flux vanishes, and
this boundary term is `0` at both endpoints since `θ₁, θ₂ > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_mutationGenerator_mul_betaPDFReal`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#integral-mutation-generator-mul-beta-pdf).

## Integrability of the mutation generator under Wright's stationary law

For `θ₁, θ₂ > 0` and `f` twice continuously differentiable on `[0, 1]`, `L f` is integrable
against Wright's stationary law `Beta(θ₁, θ₂)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integrable_mutationGenerator_betaMeasure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#integrable-mutation-generator-beta-measu).

## Weak stationarity of Wright's law (Wright 1931; Ewens 2004, ch. 4)

For `θ₁, θ₂ > 0`
and every `f` twice continuously differentiable on `[0, 1]`, `∫ L f d(Beta(θ₁, θ₂)) = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_mutationGenerator_betaMeasure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#integral-mutation-generator-beta-measure).

## Mutation generator applied to the allele frequency

The generator applied to the frequency itself is the mutation drift:
`L x = (θ₁ (1 - x) - θ₂ x) / 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.mutationGenerator_id`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#mutation-generator-id).

## Mutation generator applied to heterozygosity

The generator applied to the heterozygosity `H(x) = 2x (1 - x)`:
`L H = -2x (1 - x) + (θ₁ (1 - x) - θ₂ x) (1 - 2x)` (drift decreases `H` at rate `1`, mutation
restores it).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.mutationGenerator_heterozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#mutation-generator-heterozygosity).

## Allele frequency after one generation of two-way mutation

Allele frequency after one generation of two-way mutation, before random sampling: an `a`
copy mutates to `A` with probability `u₁` and an `A` copy to `a` with probability `u₂`, so the
frequency `x` of `A` becomes `(1 - u₂) x + u₁ (1 - x) ∈ [0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.mutatedFreq`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#mutated-freq).

## Drift of the Wright–Fisher chain with mutation (Ewens 2004, ch. 4)

One generation of the
Wright–Fisher chain on `M` gene copies (`M = 2N`): mutation moves the frequency `x` to
`p' = mutatedFreq u₁ u₂ x`, then the new count is `Binomial(M, p')`. With `u₁ = θ₁ / (2M)`,
`u₂ = θ₂ / (2M)` (`θᵢ = 4N uᵢ`), the expected change of frequency per `2N = M` generations is
exactly the drift coefficient of `mutationGenerator`:
`M · (E[k / M] - x) = (θ₁ (1 - x) - θ₂ x) / 2`, for every `M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_binomial_mutatedFreq_drift`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#integral-binomial-mutated-freq-drift).

## Infinitesimal variance of the Wright–Fisher chain with mutation

In the setting of
`integral_binomial_mutatedFreq_drift`, the scaled second moment of the frequency change is
`M · E[(k / M - x) ^ 2] = p' (1 - p') + (θ₁ (1 - x) - θ₂ x) ^ 2 / (4M)` with
`p' = mutatedFreq u₁ u₂ x = x + (θ₁ (1 - x) - θ₂ x) / (2M)`. As `M → ∞` with `θ₁, θ₂, x` fixed
this tends to `x (1 - x)`, the diffusion coefficient of `mutationGenerator` (the limit itself is
not stated here).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_binomial_mutatedFreq_sq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Mutation.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html#integral-binomial-mutated-freq-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wright–Fisher diffusion with mutation](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion-with-mutation)
