---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.generator, MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation, MathlibExt.Biology.PopulationGenetics.Diffusion.meanAbsorptionTime, MathlibExt.Biology.PopulationGenetics.Diffusion.wrightDensity, MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraSlope, MathlibExt.Biology.PopulationGenetics.Diffusion.one_sub_exp_ne_zero, MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_zero_right, MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_one_right
statement: formalized
proof: formalized
---

# Wright–Fisher diffusion

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html).

## Backward generator of the Wright–Fisher diffusion with selection

The backward generator of the Wright–Fisher diffusion with genic selection, time in units
of `2N` generations and scaled selection coefficient `σ = 2Ns`:
`(L_σ u)(x) = x (1 - x) / 2 · u''(x) + σ x (1 - x) · u'(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#generator).

## Kimura's fixation probability

Kimura's fixation probability of an allele at initial frequency `x` with scaled selection
coefficient `σ = 2Ns`: `(1 - e^{-2σx}) / (1 - e^{-2σ})`, and `x` in the neutral case.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation).

## Kimura–Ohta mean absorption time of a neutral allele

Kimura–Ohta mean time to absorption (loss or fixation) of a neutral allele at frequency `x`,
in units of `2N` generations: `-2 (x log x + (1 - x) log (1 - x))`. In generations this is
`-4N (x ln x + (1 - x) ln (1 - x))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAbsorptionTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#mean-absorption-time).

## Wright's stationary density of the Wright–Fisher diffusion

Wright's (unnormalized) stationary density of the Wright–Fisher diffusion with scaled
mutation rates `α` (towards the allele) and `β` (away from it):
`x ^ (2α - 1) (1 - x) ^ (2β - 1)` (real powers).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.wrightDensity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#wright-density).

## Slope constant of Kimura's fixation probability

The constant `K σ` such that `(kimuraFixation σ)' x = K σ · e^{-2σx}`:
`1` if `σ = 0`, and `2σ / (1 - e^{-2σ})` otherwise.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraSlope`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-slope).

## Denominator of Kimura's formula is nonzero

For `σ ≠ 0` the denominator `1 - e^{-2σ}` of Kimura's formula does not vanish.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.one_sub_exp_ne_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#one-sub-exp-ne-zero).

## Kimura's fixation probability vanishes at frequency zero

An allele that is absent is never fixed.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_zero_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation-zero-right).

## Kimura's fixation probability equals one at frequency one

An allele that is already fixed stays fixed.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_one_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation-one-right).

## Neutral fixation probability equals the initial frequency

Neutral case: the fixation probability equals the initial frequency.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_neutral`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation-neutral).

## Slope constant of Kimura's formula is nonzero

The slope constant of Kimura's formula never vanishes.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraSlope_ne_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-slope-ne-zero).

## Derivative of Kimura's fixation probability at a point

The derivative of Kimura's fixation probability: `u'(x) = K σ · e^{-2σx}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasDerivAt_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#has-deriv-at-kimura-fixation).

## Continuity of Kimura's fixation probability

Kimura's fixation probability is continuous in the initial frequency.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.continuous_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#continuous-kimura-fixation).

## Derivative of Kimura's fixation probability as a function

The derivative of Kimura's fixation probability, as a function.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.deriv_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#deriv-kimura-fixation).

## Kimura (1962)

The fixation probability solves the backward equation
`x (1 - x) / 2 · u'' + σ x (1 - x) · u' = 0` (everywhere).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#generator-kimura-fixation).

## Uniqueness of the fixation probability (Kimura 1962)

If `u` is continuous on `[0, 1]`,
differentiable on `(0, 1)` with derivative `u'` differentiable on `(0, 1)`, solves the backward
equation `L_σ u = 0` on `(0, 1)`, and satisfies `u 0 = 0`, `u 1 = 1`, then `u` is Kimura's
fixation probability on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.eq_kimuraFixation_of_generator_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#eq-kimura-fixation-of-generator-eq-zero).

## Uniqueness of the fixation probability

**Uniqueness of the fixation probability**, `C²` form: a function continuous on `[0, 1]`,
`C²` on `(0, 1)`, solving `L_σ u = 0` on `(0, 1)` with `u 0 = 0`, `u 1 = 1` equals Kimura's
fixation probability on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.eq_kimuraFixation_of_contDiffOn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#eq-kimura-fixation-of-cont-diff-on).

## Nonnegativity of Kimura's fixation probability

Kimura's fixation probability is nonnegative at nonnegative frequencies, for every
selection coefficient `σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation-nonneg).

## Kimura's fixation probability is at most one

Kimura's fixation probability is at most `1` at frequencies `y ≤ 1`, for every selection
coefficient `σ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_le_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation-le-one).

## Kimura's fixation probability lies in the unit interval

Kimura's fixation probability is a probability on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.kimuraFixation_mem_Icc`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#kimura-fixation-mem-icc).

## Advantageous alleles fix more often than their initial frequency

Advantageous alleles (`σ > 0`) are fixed with probability strictly larger than their
initial frequency `x ∈ (0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.lt_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#lt-kimura-fixation).

## Neutral mean absorption time vanishes at frequency zero

The neutral mean absorption time vanishes at `x = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAbsorptionTime_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#mean-absorption-time-zero).

## Neutral mean absorption time vanishes at frequency one

The neutral mean absorption time vanishes at `x = 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.meanAbsorptionTime_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#mean-absorption-time-one).

## Derivative of the neutral mean absorption time

On `(0, 1)`, `T'(x) = -2 (log x - log (1 - x))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.hasDerivAt_meanAbsorptionTime`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#has-deriv-at-mean-absorption-time).

## Kimura–Ohta (1969)

The neutral mean absorption time solves `L_0 T = -1` on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_meanAbsorptionTime`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#generator-mean-absorption-time).

## Decay of heterozygosity

`H(x) = 2x(1 - x)` is an eigenfunction of the neutral
generator with eigenvalue `-1`, so `E[H_t] = H_0 e^{-t}` (time in units of `2N` generations).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_heterozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#generator-heterozygosity).

## Moment duality with Kingman's coalescent

**Moment duality with Kingman's coalescent** at generator level: the neutral generator maps
`y ↦ y ^ n` to `C(n, 2) (x ^ (n - 1) - x ^ n)`, which is the generator of the block-counting
process (jumps `n → n - 1` at rate `C(n, 2)`) applied to `n ↦ x ^ n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#generator-pow).

## Wright's stationary density (zero-flux form)

On `(0, 1)`, with infinitesimal variance
`a(x) = x (1 - x)` and mutation drift `b(x) = α (1 - x) - β x`, Wright's density
`π(x) = x ^ (2α - 1) (1 - x) ^ (2β - 1)` satisfies `(a π)' = 2 b π`, i.e. the stationary
forward (Fokker–Planck) equation `½ (a π)' - b π = 0` with zero probability flux.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.deriv_flux_wrightDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#deriv-flux-wright-density).

## Normalization of Wright's density

For `α, β > 0` the stationary density integrates to
the Beta function `B(2α, 2β) = Γ(2α) Γ(2β) / Γ(2α + 2β)`, so
`wrightDensity α β x / B(2α, 2β)` is the Beta`(2α, 2β)` probability density on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_wrightDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#integral-wright-density).

## Wright's density has finite positive total mass

For `α, β > 0` Wright's density has a finite, positive total mass on `(0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_wrightDensity_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#integral-wright-density-pos).

## Integrability of Wright's density on the unit interval

For `α, β > 0` Wright's density is integrable on `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.intervalIntegrable_wrightDensity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#interval-integrable-wright-density).

## Heterozygosity decay in one Wright–Fisher generation

If the number `X` of copies of an
allele among `M` gene copies (`M = 2N` for diploids) is `Binomial(M, x)`, then the new frequency
`p' = X / M` satisfies `E[2 p' (1 - p')] = (1 - 1/M) · 2x(1 - x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_binomial_heterozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/WrightFisher.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html#integral-binomial-heterozygosity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wright–Fisher diffusion](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/wright-fisher-diffusion)
