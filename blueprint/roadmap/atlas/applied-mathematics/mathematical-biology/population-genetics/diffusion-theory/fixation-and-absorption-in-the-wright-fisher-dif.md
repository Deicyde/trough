---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.IsWrightFisherSolution, MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.absorptionTime, MathlibExt.Biology.PopulationGenetics.Diffusion.contDiff_kimuraFixation, MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.ae_exists_absorbed, MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.measureReal_fixation, MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.integral_absorptionTime
statement: formalized
---

# Fixation and absorption in the Wright–Fisher diffusion

8 results, 6 proved and 2 without a declaration, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html).

## Martingale problem for the Wright–Fisher diffusion

`X` solves the **martingale problem for the Wright–Fisher diffusion** with scaled genic
selection coefficient `σ = 2Ns` (time in units of `2N` generations) with respect to the
filtration `ℱ` and the measure `μ`: `X` takes values in `[0, 1]`, has continuous paths, is
adapted to `ℱ`, and for every `C²` function `f` the process
`f (X t) - f (X 0) - ∫₀ᵗ generator σ f (X s) ds` is an `ℱ`-martingale.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.IsWrightFisherSolution`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#is-wright-fisher-solution).

## Absorption time of a frequency path

The absorption time of a `[0, 1]`-valued path: the first time it is at `0` or `1`
(the infimum of the empty set is `0` in `ℝ≥0`; the path is absorbed almost surely, see
`ae_exists_absorbed`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.absorptionTime`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#absorption-time).

## Kimura's fixation probability is twice continuously differentiable

Kimura's fixation probability is a `C²` function of the initial frequency on all of `ℝ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.contDiff_kimuraFixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#cont-diff-kimura-fixation).

## Positivity of Kimura's slope constant

The slope constant of Kimura's formula is positive.

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#kimura-slope-pos).

## Strict monotonicity of Kimura's fixation probability

Kimura's fixation probability is strictly increasing in the initial frequency.

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#strict-mono-kimura-fixation).

## Absorption in finite time

A solution of the Wright–Fisher martingale problem is
almost surely absorbed: from some time on it is constantly `0` or constantly `1`.

## Sources

- Ethier & Kurtz (1986), ch. 10; Karlin & Taylor (1981), ch. 15. Proves the deferred entry `ae_exists_absorbed`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.ae_exists_absorbed`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean, line 842](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean#L842). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#ae-exists-absorbed).

## Kimura's fixation probability, process form

For a solution of the Wright–Fisher
martingale problem with scaled selection coefficient `σ = 2Ns` started at frequency `x`, the
probability that the allele is eventually fixed is `(1 - e^{-2σx}) / (1 - e^{-2σ})` (`x` when
`σ = 0`).

## Sources

- Kimura (1962); Ewens (2004), ch. 4. Proves the deferred entry `measureReal_fixation`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.measureReal_fixation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean, line 858](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean#L858). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#measure-real-fixation).

## Kimura–Ohta mean absorption time, process form

For a solution of the neutral
Wright–Fisher martingale problem started at frequency `x`, the expected time to loss or
fixation, in units of `2N` generations, is `-2 (x log x + (1 - x) log (1 - x))`.

## Sources

- Kimura & Ohta (1969); Ewens (2004), ch. 4. Proves the deferred entry `integral_absorptionTime`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.KimuraFixationProcess.integral_absorptionTime`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean, line 935](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/KimuraFixationProcess.lean#L935). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html#integral-absorption-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixation and absorption in the Wright–Fisher diffusion](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/fixation-and-absorption-in-the-wright-fisher-dif)
