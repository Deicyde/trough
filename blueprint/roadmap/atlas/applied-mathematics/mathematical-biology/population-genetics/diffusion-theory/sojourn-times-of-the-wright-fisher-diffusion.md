---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.neutralGreen, MathlibExt.Biology.PopulationGenetics.Diffusion.generator_integral_neutralGreen, MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen_left, MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen_right, MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen
statement: formalized
proof: formalized
---

# Sojourn times of the Wright–Fisher diffusion

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html).

## Neutral Wright–Fisher Green's function

The neutral Wright–Fisher Green's function (sojourn density), time in units of `2N`
generations (Ewens 2004, Chapter 4): `G(p, x) = 2 (1 - p) / (1 - x)` for `x ≤ p` and
`G(p, x) = 2 p / x` for `p < x`. In the diffusion reading, for
`0 < x < 1`, `G(p, x) dx` is the expected time a neutral allele started at frequency `p` spends
at frequencies in `(x, x + dx)` before loss or fixation.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.neutralGreen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html#neutral-green).

## Green's representation (Ewens 2004, Chapter 4)

For continuous `g` and `p ∈ (0, 1)`, the
function `u(q) = ∫ x in 0..1, G(q, x) g(x)` solves the neutral backward equation `L_0 u = -g`
at `p`. In the diffusion reading, `u(p)` is the expected value of
`∫₀^T g(X_t) dt` up to the absorption time `T`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.generator_integral_neutralGreen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html#generator-integral-neutral-green).

## Sojourn integral vanishes for an absent allele

Boundary value at `0`: an allele that is absent spends no time in `(0, 1)`, so
`∫ x in 0..1, G(0, x) g(x) = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen_left`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html#integral-neutral-green-left).

## Sojourn integral vanishes for a fixed allele

Boundary value at `1`: a fixed allele spends no time in `(0, 1)`, so
`∫ x in 0..1, G(1, x) g(x) = 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html#integral-neutral-green-right).

## Mean absorption time as a sojourn integral

For `p ∈ [0, 1]`, the total expected
sojourn time `∫ x in 0..1, G(p, x)` is the Kimura–Ohta mean absorption time
`-2 (p log p + (1 - p) log (1 - p))` (units of `2N` generations).

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_neutralGreen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/Sojourn.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html#integral-neutral-green).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sojourn times of the Wright–Fisher diffusion](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/sojourn-times-of-the-wright-fisher-diffusion)
