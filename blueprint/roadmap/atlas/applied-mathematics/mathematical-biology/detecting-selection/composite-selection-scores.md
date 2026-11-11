---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.bayesFactor, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.cms, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.posterior, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.bayesFactor_pos, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.cms_eq_div, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.posterior_odds, MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.log_posterior_odds
statement: formalized
proof: formalized
---

# Composite selection scores

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html).

## The composite of multiple signals

## Composite selection score model

A composite-score model (Grossman et al. 2010): a prior probability `prior` that the site
is under selection, and for each of the `k` component statistics a positive score function
`sel` under selection and `neut` under neutrality (unnormalized densities: only positivity is
assumed). Conditionally on the hypothesis the components are independent, which is what
makes the joint scores the products below. The Bayes/posterior reading of `posterior`
requires the additional normalization hypothesis of `sum_joint_eq_one`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel`, a structure declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#composite-model).

## Bayes factor of a component statistic

The Bayes factor of component `i` at the observed value: the ratio of its score
function under selection to its score function under neutrality.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.bayesFactor`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#bayes-factor).

## Composite of multiple signals (CMS) score

The CMS score: the product of the component Bayes factors.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.cms`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#cms).

## Normalized composite score

The normalized composite score: the normalized ratio of the products of the
component score functions. This is the posterior probability of selection given the
observed component values when the score functions are normalized densities
(see `sum_joint_eq_one` for the normalization hypothesis).

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.posterior`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#posterior).

## Positivity of component Bayes factors

Every component Bayes factor is positive.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.bayesFactor_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#bayes-factor-pos).

## CMS score as a ratio of joint densities

The CMS score is the ratio of the two joint densities.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.cms_eq_div`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#cms-eq-div).

## Posterior odds equal prior odds times the CMS score

Bayes-rule identity for conditionally independent components: the posterior odds of
selection are the prior odds times the CMS score. This is an algebraic identity for the
normalized score; it is a genuine Bayes rule only under the normalization hypothesis of
`sum_joint_eq_one`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.posterior_odds`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#posterior-odds).

## Additivity of evidence on the log-odds scale

On the log scale the evidence is additive: the log posterior odds are the log prior odds
plus the sum of the log Bayes factors of the component statistics.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.log_posterior_odds`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#log-posterior-odds).

## Posterior probability is strictly increasing in the CMS score

The posterior probability is a strictly increasing function of the CMS score, so the two
rankings of sites agree.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.posterior_lt_posterior_of_cms_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#posterior-lt-posterior-of-cms-lt).

## Normalization of the composite score model

The model is a probability model: with normalised component score functions (each a
density with respect to a common base measure), the joint distribution of the
observations sums to one. This is the validity hypothesis that makes `posterior` a
genuine Bayes posterior.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.CompositeModel.sum_joint_eq_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#sum-joint-eq-one).

## Probability of escaping a selective sweep

The probability that a lineage at position `y` escapes a sweep located at `x`, with
compound strength parameter `α > 0`: `1 - exp (-α |y - x|)` (Kim and Stephan 2002;
Nielsen et al. 2005). The parameter `α` is proportional to the recombination rate per unit
distance divided by the selection coefficient.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.escapeProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#escape-prob).

## Escape probability vanishes only at the swept site

No lineage escapes at the swept site itself, and nowhere else.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.escapeProb_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#escape-prob-eq-zero-iff).

## Escape profile determines sweep location and strength

The escape-probability profile determines the sweep location and its strength. Positivity
of one of the two strength parameters is enough: the location is the unique zero of that
profile, and the strengths then agree by injectivity of `exp`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.escapeProb_inj`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#escape-prob-inj).

## Uniqueness of the mixing weight of a two-component mixture

A mixture of two distinct laws determines its mixing weight.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.mixture_weight_unique`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#mixture-weight-unique).

## Identifiability of sweep parameters from frequency spectra

Identifiability of the sweep parameters from the per-site frequency spectra. If the
neutral spectrum `f` and the post-sweep spectrum `g` differ, and two sweep parameter pairs
give the same mixture at every position, then the parameters coincide. This is what the
composite likelihood of SweepFinder maximises over.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.sweep_param_unique`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CompositeScores.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html#sweep-param-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Composite selection scores](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/composite-selection-scores/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/detecting-selection/composite-selection-scores)
