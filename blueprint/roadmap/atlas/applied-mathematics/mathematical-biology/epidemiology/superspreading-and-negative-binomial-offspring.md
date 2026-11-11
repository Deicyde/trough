---
declaration: section
origin: cited
lean: MathlibExt.Biology.Epidemiology.Superspreading.nbPmf, MathlibExt.Biology.Epidemiology.Superspreading.nbPgf, MathlibExt.Biology.Epidemiology.Superspreading.nbOffspring, MathlibExt.Biology.Epidemiology.Superspreading.nbPmf_nonneg, MathlibExt.Biology.Epidemiology.Superspreading.hasSum_nbPmf_mul_pow, MathlibExt.Biology.Epidemiology.Superspreading.isProbabilityMeasure_nbOffspring, MathlibExt.Biology.Epidemiology.Superspreading.pgf_nbOffspring, MathlibExt.Biology.Epidemiology.Superspreading.nbPgf_antitone
statement: formalized
proof: formalized
---

# Superspreading and negative-binomial offspring

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html).

## Negative-binomial offspring probabilities

The **negative-binomial offspring probability** with mean `R` and dispersion `k`:
`P(Z = n) = C(k + n - 1, n) p^k (1 - p)^n` with `p = k / (k + R)` (Lloyd-Smith et al. 2005).
Meaningful for `k > 0`, `R ≥ 0`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.nbPmf`, a definition declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#nb-pmf).

## Negative-binomial probability generating function

The **negative-binomial generating function** `G_k(s) = (1 + (R / k) (1 - s))^{-k}`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.nbPgf`, a definition declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#nb-pgf).

## Negative-binomial offspring distribution

The negative-binomial offspring law as a measure on `ℕ`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.nbOffspring`, a definition declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#nb-offspring).

## Nonnegativity of the negative-binomial probabilities

The negative-binomial probabilities are nonnegative for `k > 0`, `R ≥ 0`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.nbPmf_nonneg`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#nb-pmf-nonneg).

## Generating-function identity

For `k > 0`, `R ≥ 0` and `s ∈ [0, 1]`,
`∑ₙ P(Z = n) sⁿ = (1 + (R / k) (1 - s))^{-k}`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.hasSum_nbPmf_mul_pow`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#has-sum-nb-pmf-mul-pow).

## Negative-binomial offspring law is a probability measure

The negative-binomial offspring law is a probability measure (`k > 0`, `R ≥ 0`).

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.isProbabilityMeasure_nbOffspring`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#is-probability-measure-nb-offspring).

## Generating function of the negative-binomial law in closed form

The generating function of the negative-binomial offspring law is `nbPgf` on `[0, 1]`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.pgf_nbOffspring`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#pgf-nb-offspring).

## Monotonicity in the dispersion

For `R ≥ 0`, `s ∈ [0, 1]` and `0 < k₁ ≤ k₂`,
`G_{k₂}(s) ≤ G_{k₁}(s)`; equivalently `k ↦ k log (1 + x / k)` is nondecreasing for `x ≥ 0`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.nbPgf_antitone`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#nb-pgf-antitone).

## Negative-binomial law with dispersion one is geometric

`k = 1` is the geometric offspring law: `G_1(s) = 1 / (1 + R (1 - s))`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.nbPgf_one_dispersion`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#nb-pgf-one-dispersion).

## Poisson limit

As `k → ∞`, `G_k(s) → e^{-R (1 - s)}` (for all real `R`, `s`).

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.tendsto_nbPgf_atTop`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#tendsto-nb-pgf-at-top).

## Comparison principle for Galton–Watson extinction

If the offspring generating
functions satisfy `f₂ ≤ f₁` on `[0, 1]`, then the extinction probabilities satisfy
`q₂ ≤ q₁`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.extinctionProb_le_of_pgf_le`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#extinction-prob-le-of-pgf-le).

## Negative-binomial extinction probability is the least fixed point

The extinction probability of the negative-binomial epidemic is the least fixed point of
`G_k` in `[0, 1]`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.isLeast_extinctionProb_nbOffspring`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#is-least-extinction-prob-nb-offspring).

## Superspreading raises the extinction probability

**Superspreading raises the extinction probability** (Lloyd-Smith et al. 2005): at a
fixed mean `R ≥ 0`, the probability `q_k` that the outbreak started by one case goes extinct
is nonincreasing in the dispersion `k > 0`.

Formalized by `MathlibExt.Biology.Epidemiology.Superspreading.extinctionProb_nbOffspring_antitone`, a theorem declared in [MathlibExt/Biology/Epidemiology/Superspreading.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/Superspreading.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html#extinction-prob-nb-offspring-antitone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Superspreading and negative-binomial offspring](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/epidemiology/superspreading-and-negative-binomial-offspring)
