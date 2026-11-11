---
declaration: section
origin: cited
lean: MathlibExt.Probability.StableDistribution.convPow_gaussianReal, MathlibExt.Probability.StableDistribution.IsStable, MathlibExt.Probability.StableDistribution.isStable_dirac, MathlibExt.Probability.StableDistribution.isStable_gaussianReal, MathlibExt.Probability.StableDistribution.not_isStable_gaussianReal_one, MathlibExt.Probability.StableDistribution.IsNondegenerate, MathlibExt.Probability.StableDistribution.isNondegenerate_gaussianReal, MathlibExt.Probability.StableDistribution.not_isNondegenerate_dirac
statement: formalized
proof: formalized
---

# Stable distributions and domains of attraction

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html).

## Convolution powers

## Convolution powers of a Gaussian are Gaussian

The convolution power of a Gaussian is Gaussian with the mean and the
variance multiplied by `n`: the law of the sum of `n` i.i.d.
`N(μ, v)` variables is `N(nμ, nv)`.

Formalized by `MathlibExt.Probability.StableDistribution.convPow_gaussianReal`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#conv-pow-gaussian-real).

## Stable distribution of a given index

Indexed stability fixes the positive-n dilation to `n^(1/α)` and allows
arbitrary centering. Degenerate Dirac identities may satisfy several indices.

Formalized by `MathlibExt.Probability.StableDistribution.IsStable`, a definition declared in [MathlibExt/Probability/StableDistribution.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#is-stable).

## Dirac measures are stable of every index

A Dirac law satisfies the fixed-dilation identity at every admissible index.
These are degenerate rescaling identities, with centering `na - n^(1/α)a`.

Formalized by `MathlibExt.Probability.StableDistribution.isStable_dirac`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#is-stable-dirac).

## Gaussian measures are stable of index 2

Every real Gaussian measure is stable of index `2`: the sum of `n`
i.i.d. `N(μ, v)` variables is `N(nμ, nv)`, which is the pushforward of
`N(μ, v)` under `x ↦ √n · x + (n - √n) μ`.

Formalized by `MathlibExt.Probability.StableDistribution.isStable_gaussianReal`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#is-stable-gaussian-real).

## Nondegenerate Gaussian is not stable of index 1

A nondegenerate Gaussian cannot have fixed stability index one. The n=4
convolution variance is `4v`, while every such affine dilation has variance `16v`.

Formalized by `MathlibExt.Probability.StableDistribution.not_isStable_gaussianReal_one`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#not-is-stable-gaussian-real-one).

## Nondegenerate measure on the real line

A measure `μ` on `ℝ` is *nondegenerate* if it is not a point mass
`δ_a` for any `a`.

Formalized by `MathlibExt.Probability.StableDistribution.IsNondegenerate`, a definition declared in [MathlibExt/Probability/StableDistribution.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#is-nondegenerate).

## Gaussian with nonzero variance is nondegenerate

A Gaussian with nonzero variance is nondegenerate: it gives mass `0`
to every singleton, while `δ_a` gives mass `1` to `{a}`.

Formalized by `MathlibExt.Probability.StableDistribution.isNondegenerate_gaussianReal`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#is-nondegenerate-gaussian-real).

## Dirac measure is degenerate

A Dirac measure is degenerate, by definition.

Formalized by `MathlibExt.Probability.StableDistribution.not_isNondegenerate_dirac`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#not-is-nondegenerate-dirac).

## Domain of attraction

The probability measure `μ` is *in the domain of attraction* of `G`
if there exist sequences of normalizing constants `a n > 0` and
centering constants `b n` such that the law of `(S_n - b n) / a n`
(where `S_n` has law `μ^{*n}`) converges weakly to `G`, expressed here
as integration against arbitrary bounded continuous functions.

Formalized by `MathlibExt.Probability.StableDistribution.InDomainOfAttraction`, a definition declared in [MathlibExt/Probability/StableDistribution.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#in-domain-of-attraction).

## Stable law lies in its own domain of attraction

A stable law is a normalized weak limit of its own convolution powers.
The positive-n inverse affine identity is exact; order zero uses normalizer one.

Formalized by `MathlibExt.Probability.StableDistribution.IsStable.inDomainOfAttraction_self`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#in-domain-of-attraction-self).

## Domain of attraction of a given index

Indexed attraction requires a nondegenerate stable limit of that index.
The general normalized weak-limit relation alone does not assign an index.

Formalized by `MathlibExt.Probability.StableDistribution.InDomainOfAttractionIndex`, a definition declared in [MathlibExt/Probability/StableDistribution.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#in-domain-of-attraction-index).

## Dirac measure lies in its own domain of attraction

The Dirac measure is in its own domain of attraction: with
`a n = 1` and `b n = (n - 1) a`, the normalized law of `S_n` is
`δ_a` for every `n`.

Formalized by `MathlibExt.Probability.StableDistribution.inDomainOfAttraction_dirac`, a theorem declared in [MathlibExt/Probability/StableDistribution.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/StableDistribution.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html#in-domain-of-attraction-dirac).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stable distributions and domains of attraction](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/infinite-divisibility-regular-variation/stable-distributions-and-domains-of-attraction)
