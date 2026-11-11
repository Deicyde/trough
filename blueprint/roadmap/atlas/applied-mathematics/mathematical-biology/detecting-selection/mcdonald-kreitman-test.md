---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.alphaHat, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.neutralityIndex, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.alphaHat_eq_one_sub_neutralityIndex, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EPs, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EPn, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EDs, MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EDn
statement: formalized
proof: formalized
---

# McDonald–Kreitman test

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html).

## The McDonald–Kreitman test

## Smith–Eyre-Walker estimator of adaptive substitutions

The Smith–Eyre-Walker estimator of the proportion of adaptive nonsynonymous
substitutions, `α̂ = 1 - (D_s P_n) / (D_n P_s)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.alphaHat`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#alpha-hat).

## Neutrality index

The neutrality index `NI = (P_n / P_s) / (D_n / D_s)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.neutralityIndex`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#neutrality-index).

## Adaptive proportion estimator equals one minus the neutrality index

`α̂ = 1 - NI`, for all real counts (the junk values of division agree).

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.alphaHat_eq_one_sub_neutralityIndex`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#alpha-hat-eq-one-sub-neutrality-index).

## Expected-count model of the McDonald–Kreitman table

Expected counts of the MK table without a slightly deleterious class (see the module
docstring): synonymous and nonsynonymous mutational targets `Ls`, `Ln`, neutral fraction `f₀`
of nonsynonymous mutations, polymorphisms and neutral fixed differences per unit of neutral
target `polyRate`, `divRate` (`θ_P`, `λ_D` in the module docstring), and `A` expected adaptive
substitutions.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel`, a structure declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#mkmodel).

## Expected synonymous polymorphisms

Expected synonymous polymorphisms `E P_s = θ_P L_s`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EPs`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#eps).

## Expected nonsynonymous polymorphisms

Expected nonsynonymous polymorphisms `E P_n = θ_P f₀ L_n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EPn`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#epn).

## Expected synonymous fixed differences

Expected synonymous fixed differences `E D_s = λ_D L_s`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EDs`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#eds).

## Expected nonsynonymous fixed differences

Expected nonsynonymous fixed differences `E D_n = λ_D f₀ L_n + A`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.EDn`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#edn).

## Proportion of adaptive nonsynonymous substitutions

The proportion of nonsynonymous substitutions that are adaptive, `α = A / E D_n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.alpha`, a definition declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#alpha).

## `α̂` at the expected counts is the proportion of adaptive substitutions

(Smith & Eyre-Walker 2002): `1 - (E D_s E P_n) / (E D_n E P_s) = A / E D_n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.alphaHat_expected`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#alpha-hat-expected).

## The MK null is neutrality

The proportions of nonsynonymous changes among expected
fixed differences and expected polymorphisms agree iff there are no adaptive substitutions.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.propNonsyn_eq_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#prop-nonsyn-eq-iff).

## Consistency of `α̂` over loci

Let `Dn i, Ds i, Pn i, Ps i` be the counts at locus
`i`; suppose each of the four sequences consists of pairwise independent, identically
distributed, integrable variables whose means are the expected counts of `M` (the loci are
exchangeable copies of the model). Then almost surely `α̂` computed from the counts summed over
the first `m` loci converges to `α = A / E D_n` as `m → ∞`.

Formalized by `MathlibExt.Biology.PopulationGenetics.McDonaldKreitman.MKModel.tendsto_alphaHat`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/McDonaldKreitman.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html#tendsto-alpha-hat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: McDonald–Kreitman test](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/mcdonald-kreitman-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/detecting-selection/mcdonald-kreitman-test)
