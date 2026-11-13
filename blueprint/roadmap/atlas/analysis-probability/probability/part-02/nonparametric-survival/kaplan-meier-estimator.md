---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.KaplanMeier.CensoredData, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.size, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.atRisk, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmFactor, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmSurvival, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMass, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmTail, MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMeasure
statement: formalized
proof: formalized
---

# Kaplan–Meier estimator

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html).

## Kaplan Meier

## Grouped right-censored survival data

Right-censored survival data grouped at `k` distinct, increasing observation times: `deaths j`
subjects die and `censored j` subjects are censored at `time j`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData`, a structure declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#censored-data).

## Sample size of censored survival data

The number of subjects in the sample.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.size`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#size).

## Number at risk at an observation time

The number at risk at `time j`: subjects whose observation time is at least `time j`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.atRisk`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#at-risk).

## Kaplan–Meier factor

The Kaplan–Meier factor `1 - dⱼ / nⱼ` at `time j` (it is `1` if nobody is at risk, where
also `dⱼ = 0`).

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmFactor`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-factor).

## Kaplan–Meier survival estimate

The Kaplan–Meier estimate `Ŝ(t) = ∏_{tⱼ ≤ t} (1 - dⱼ / nⱼ)` of the survival function.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmSurvival`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-survival).

## Kaplan–Meier jump at an observation time

The Kaplan–Meier jump at `time j`: `Ŝ(tⱼ₋) · dⱼ / nⱼ`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMass`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-mass).

## Kaplan–Meier mass after the last observation

The Kaplan–Meier mass left after the last observation time, `∏ⱼ (1 - dⱼ / nⱼ)`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmTail`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-tail).

## Kaplan–Meier measure

The Kaplan–Meier measure: the jumps `kmMass j` at `time j` and the leftover mass `kmTail` at
a chosen point `τ` (taken after the last observation time).

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMeasure`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-measure).

## Likelihood of right-censored data

The censored-data likelihood of a law `μ` of the survival time:
`∏ⱼ μ{tⱼ}^{dⱼ} · μ(tⱼ, ∞)^{cⱼ}`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.likelihood`, a definition declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#likelihood).

## Deaths at a time are among those at risk

The deaths at a time are among those at risk.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.deaths_le_atRisk`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#deaths-le-at-risk).

## Kaplan–Meier factor is at most one

The Kaplan–Meier factor is at most `1`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmFactor_le_one`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-factor-le-one).

## Kaplan–Meier factor is nonnegative

The Kaplan–Meier factor is non-negative.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmFactor_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-factor-nonneg).

## Kaplan–Meier jumps are nonnegative

The Kaplan–Meier jumps are non-negative.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMass_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-mass-nonneg).

## Leftover Kaplan–Meier mass is nonnegative

The leftover Kaplan–Meier mass is non-negative.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmTail_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-tail-nonneg).

## Kaplan–Meier jumps and leftover mass sum to one

The Kaplan–Meier jumps and the leftover mass add up to `1`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.sum_kmMass_add_kmTail`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#sum-km-mass-add-km-tail).

## Mass of a set under the Kaplan–Meier measure

The mass of a measurable set under the Kaplan–Meier measure.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMeasure_real_apply`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-measure-real-apply).

## Kaplan–Meier measure is a probability measure

The Kaplan–Meier measure is a probability measure.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMeasure_isProbabilityMeasure`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-measure-is-probability-measure).

## Survival function of the Kaplan–Meier measure

The survival function of the Kaplan–Meier measure is the Kaplan–Meier estimate on
`(-∞, τ)`: `P(T > t) = Ŝ(t)` for `t < τ`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmMeasure_real_Ioi`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-measure-real-ioi).

## Kaplan–Meier is the nonparametric MLE

**Kaplan–Meier is the nonparametric MLE** (Kaplan–Meier 1958): every probability measure on
`ℝ` has censored-data likelihood at most that of the Kaplan–Meier measure.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.likelihood_le_kmMeasure`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#likelihood-le-km-measure).

## Kaplan–Meier survival is positive at a censoring time

A time at which some subject is censored has positive Kaplan–Meier survival.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmSurvival_pos_of_censored_pos`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-survival-pos-of-censored-pos).

## Self-consistency

**Self-consistency** (Efron 1967, (7.4)): `n Ŝ(t)` is the number of observations exceeding
`t` plus, for each subject censored at or before `t`, the conditional survival `Ŝ(t) / Ŝ(tⱼ)`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.size_mul_kmSurvival`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#size-mul-km-survival).

## Kaplan–Meier estimate without censoring is the empirical survival

Without censoring, the Kaplan–Meier estimate is the empirical survival function: the
fraction `#{observations > t} / n = 1 - Fₙ(t)`.

Formalized by `MathlibExt.Probability.Statistics.KaplanMeier.CensoredData.kmSurvival_of_censored_eq_zero`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/KaplanMeier.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html#km-survival-of-censored-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kaplan–Meier estimator](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/nonparametric-survival/kaplan-meier-estimator)
