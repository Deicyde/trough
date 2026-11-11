---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.integral_binomial_eq_bernsteinApproximation, MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_wfGenerator
statement: formalized
proof: formalized
---

# Diffusion limit of the Wright–Fisher model

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/diffusion-limit-of-the-wright-fisher-model/index.html).

## One Wright–Fisher generation as a Bernstein approximation

For `M` gene copies and
current frequency `x`, the expected value of `f` at the next frequency, `∫ k, f (k / M) ∂Bin(M, x)`,
is the `M`-th Bernstein approximation of `f` on `[0, 1]` evaluated at `x`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.integral_binomial_eq_bernsteinApproximation`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/DiffusionLimit.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/DiffusionLimit.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/diffusion-limit-of-the-wright-fisher-model/index.html#integral-binomial-eq-bernstein-approxima).

## Wright–Fisher diffusion limit, generator form (Feller 1951; Voronovskaya 1932)

For `f`
of class `C²` and `x ∈ [0, 1]`, the one-generation generator of the neutral Wright–Fisher chain
with `M` gene copies, sped up by the factor `M` (time in units of `M` generations), converges
to the neutral Wright–Fisher diffusion generator `(L_0 f)(x) = x (1 - x) / 2 · f''(x)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.tendsto_wfGenerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/DiffusionLimit.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/DiffusionLimit.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/diffusion-limit-of-the-wright-fisher-model/index.html#tendsto-wf-generator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diffusion limit of the Wright–Fisher model](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/diffusion-limit-of-the-wright-fisher-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/diffusion-limit-of-the-wright-fisher-model)
