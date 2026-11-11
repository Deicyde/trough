---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.PolyPhen.profileScore, MathlibExt.Biology.StatisticalGenetics.PolyPhen.sum_profileScore_eq_log_likelihood_ratio, MathlibExt.Biology.StatisticalGenetics.PolyPhen.sum_mul_profileScore_nonneg, MathlibExt.Biology.StatisticalGenetics.PolyPhen.sum_mul_profileScore_nonpos, MathlibExt.Biology.StatisticalGenetics.PolyPhen.psicDifference, MathlibExt.Biology.StatisticalGenetics.PolyPhen.psicDifference_eq_log, MathlibExt.Biology.StatisticalGenetics.PolyPhen.psicDifference_pos_iff, MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes
statement: formalized
proof: formalized
---

# Profile scores for amino acid substitutions

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html).

## Profile log-odds scores

## Profile log-odds score of a residue

The profile log-odds score `log (p a / q a)` of residue `a`: `p` is the position-specific
profile probability (estimated from aligned homologs), `q` the background probability.
Meaningful for `p a, q a > 0`; otherwise Lean's `log 0 = 0` and `x / 0 = 0` give junk.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.profileScore`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#profile-score).

## The score is a log-likelihood ratio

For a sequence `s` over independent positions with
profiles `p j` and background `q` (all positive), the summed profile score is the log of the
likelihood ratio `∏ p_j(s_j) / ∏ q(s_j)` of the profile model against the background.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.sum_profileScore_eq_log_likelihood_ratio`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#sum-profile-score-eq-log-likelihood-rati).

## Gibbs' inequality for the profile score

If `p` and `q` are probability vectors and
`q` is positive, the expected score under the profile, `∑ p a log (p a / q a)` (the
Kullback–Leibler divergence), is nonnegative.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.sum_mul_profileScore_nonneg`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#sum-mul-profile-score-nonneg).

## Expected profile score under the background is nonpositive

If `p` and `q` are probability vectors and `p` is positive, the expected score under the
background, `∑ q a log (p a / q a)`, is nonpositive.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.sum_mul_profileScore_nonpos`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#sum-mul-profile-score-nonpos).

## PSIC score difference of a substitution

The PSIC score difference of a substitution from the wild-type residue `wt` to the mutant
residue `mt`: `profileScore p q wt - profileScore p q mt`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.psicDifference`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#psic-difference).

## PSIC difference as a log ratio of likelihood ratios

The PSIC difference is the log of the ratio of the two residues' likelihood ratios.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.psicDifference_eq_log`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#psic-difference-eq-log).

## Positivity criterion for the PSIC difference

The PSIC difference is positive iff the wild type is more enriched in the profile, relative
to background, than the mutant.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.psicDifference_pos_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#psic-difference-pos-iff).

## Two-class naive Bayes model

A two-class naive Bayes model: class *damaging* has prior `prior ∈ (0, 1)`, class *benign*
the complement; each feature `j` takes values in the finite type `X j` with class-conditional
probabilities `damaging j` and `benign j`, assumed positive; features are conditionally
independent given the class. The tables are estimated from training data.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes`, a structure declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#naive-bayes).

## Joint probability of class and features in naive Bayes

The joint probability of class `c` (`true` = damaging) and feature values `x`:
`π ∏ P_D(x_j)` or `(1 - π) ∏ P_B(x_j)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.joint`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#joint).

## Naive Bayes joint law is a probability law

The joint law of class and features is a probability law.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.sum_joint`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#sum-joint).

## Naive Bayes posterior probability of damage

The posterior probability that the variant is damaging given feature values `x`
(Bayes' rule on the joint law).

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.posterior`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#posterior).

## Log-likelihood ratio of a feature value

The log-likelihood ratio `log (P_D(v) / P_B(v))` of value `v` of feature `j`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.logLikelihoodRatio`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#log-likelihood-ratio).

## Naive Bayes score

The naive-Bayes score: prior log-odds plus the features' log-likelihood ratios.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.score`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#score).

## Naive-Bayes posterior

The posterior probability of *damaging* is the logistic function
of the score.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.posterior_eq_sigmoid`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#posterior-eq-sigmoid).

## Naive Bayes posterior is strictly monotone in the score

The posterior is strictly monotone in the score.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.posterior_lt_posterior_iff`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#posterior-lt-posterior-iff).

## Monotonicity in a feature value

Let feature `j` carry a numerical value `g v` (for
example a PSIC-difference bin) such that its likelihood ratio `P_D(v) / P_B(v)` is monotone in
`g v`. With the other features fixed, the posterior is monotone in `g`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.PolyPhen.NaiveBayes.posterior_update_le_of_monotone`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/PolyPhen.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html#posterior-update-le-of-monotone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Profile scores for amino acid substitutions](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/profile-scores-for-amino-acid-substitutions)
