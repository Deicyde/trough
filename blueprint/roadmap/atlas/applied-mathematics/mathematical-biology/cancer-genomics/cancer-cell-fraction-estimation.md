---
declaration: section
origin: cited
lean: MathlibExt.Biology.CancerGenomics.CancerCellFraction.tailRatio, MathlibExt.Biology.CancerGenomics.CancerCellFraction.posteriorTail_mono_of_tp2, MathlibExt.Biology.CancerGenomics.CancerCellFraction.binomPmf_mul_le_mul, MathlibExt.Biology.CancerGenomics.CancerCellFraction.posteriorTail, MathlibExt.Biology.CancerGenomics.CancerCellFraction.IsClonal, MathlibExt.Biology.CancerGenomics.CancerCellFraction.GridModel, MathlibExt.Biology.CancerGenomics.CancerCellFraction.GridModel.normalizer_pos, MathlibExt.Biology.CancerGenomics.CancerCellFraction.posteriorTail_mono
statement: formalized
proof: formalized
---

# Cancer cell fraction estimation

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html).

## Posterior tail probability on a grid

Posterior probability that the parameter `c i` exceeds `t`, for prior weights `prior` and
likelihoods `lik i` of the observed data: `∑_{c i > t} prior i lik i / ∑_i prior i lik i`.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.tailRatio`, a definition declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#tail-ratio).

## Monotone likelihood ratio implies stochastically larger posteriors

If the kernels
`L` (data `x`) and `L'` (data `x'`) satisfy the TP2 inequality `L' i L j ≥ L i L' j` whenever
`c j ≤ c i`, then for a nonnegative prior every posterior tail `P(c > t)` is at least as large
under `L'` as under `L` (both normalizers positive).

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.posteriorTail_mono_of_tp2`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#posterior-tail-mono-of-tp2).

## The binomial family is TP2

**The binomial family is TP2** (monotone likelihood ratio in the success probability):
for `a ≤ a'` and `0 ≤ p ≤ p' ≤ 1`,
`Binom(a | n, p') Binom(a' | n, p) ≤ Binom(a' | n, p') Binom(a | n, p)`.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.binomPmf_mul_le_mul`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#binom-pmf-mul-le-mul).

## Posterior probability that the cancer cell fraction exceeds a threshold

Landau et al.'s posterior probability that the CCF exceeds `t`, given `a` of `n` reads,
purity `α`, copy number `q`, a prior `prior` on the grid points `grid k`:
`∑_{grid k > t} π_k Binom(a | n, f(grid k)) / ∑_k π_k Binom(a | n, f(grid k))`, with
`f(c) = α c / (α q + 2 (1 - α))`.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.posteriorTail`, a definition declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#posterior-tail).

## Clonal call for a mutation

Landau et al.'s clonal call: `P(CCF > t | a) > γ` (they take `t = 0.95`, `γ = 0.5`).

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.IsClonal`, a definition declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#is-clonal).

## Grid model for the cancer cell fraction

Hypotheses on the CCF grid model: purity `0 < α ≤ 1`, copy number `q > 0`, grid in
`[0, q]` and within the defining CCF bound `≤ 1`, a nonnegative prior, and one grid point
of positive prior weight whose allelic fraction lies strictly inside `(0, 1)` (this makes
every posterior well defined).

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.GridModel`, a structure declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#grid-model).

## Positivity of the grid posterior normalizer

In a grid model every posterior normalizer `∑_k π_k Binom(a | n, f(grid k))`, `a ≤ n`,
is positive.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.GridModel.normalizer_pos`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#normalizer-pos).

## The CCF posterior is stochastically increasing in the read count

**The CCF posterior is stochastically increasing in the read count** (Landau et al. 2013
with the monotone-likelihood-ratio argument): `P(CCF > t | a) ≤ P(CCF > t | a')` for
`a ≤ a' ≤ n`.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.posteriorTail_mono`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#posterior-tail-mono).

## The clonal call is upward closed in the read count

**The clonal call is upward closed in the read count.**

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.IsClonal.mono`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#mono).

## The clonal call is a read-count threshold

For every CCF threshold `t` and posterior
level `γ` there is `a₀` such that, for `a ≤ n`, the mutation is called clonal iff `a₀ ≤ a`
(`a₀ = n + 1` when no count is called clonal).

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.exists_threshold`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#exists-threshold).

## Maximum-likelihood cancer cell fraction

The continuous maximum-likelihood CCF `ĉ = min 1 (a / (n κ))` for the allelic-fraction
slope `κ = α / (α q + 2 (1 - α))`. Landau et al. (2013) use the grid posterior; this continuous
maximizer over `[0, 1]` is derived here.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.ccfMLE`, a definition declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#ccf-mle).

## The continuous CCF MLE

For `0 < α ≤ 1`, `q ≥ 1`, `a ≤ n` and `0 < n`, the likelihood
`c ↦ Binom(a | n, f(c))` on `[0, 1]` is maximized at `ĉ = min 1 (a / (n κ))`.

Formalized by `MathlibExt.Biology.CancerGenomics.CancerCellFraction.isMaxOn_ccfMLE`, a theorem declared in [MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/CancerCellFraction.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html#is-max-on-ccf-mle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cancer cell fraction estimation](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/cancer-genomics/cancer-cell-fraction-estimation)
