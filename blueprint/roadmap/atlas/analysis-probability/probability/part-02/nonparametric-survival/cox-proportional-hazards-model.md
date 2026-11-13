---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskSet, MathlibExt.Probability.Statistics.CoxPartialLikelihood.mem_riskSet, MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskSet_nonempty, MathlibExt.Probability.Statistics.CoxPartialLikelihood.partialLikelihood, MathlibExt.Probability.Statistics.CoxPartialLikelihood.logPartialLikelihood, MathlibExt.Probability.Statistics.CoxPartialLikelihood.log_partialLikelihood, MathlibExt.Probability.Statistics.CoxPartialLikelihood.concaveOn_logPartialLikelihood, MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskMean
statement: formalized
proof: formalized
---

# Cox proportional hazards model

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html).

## Risk set in survival analysis

The risk set at the observed time of subject `i`: subjects still under observation,
`{l : T_l ≥ Tᵢ}`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskSet`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#risk-set).

## A subject belongs to its own risk set

Subject `i` is in its own risk set.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.mem_riskSet`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#mem-risk-set).

## Risk sets are nonempty

The risk set of subject `i` is nonempty.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskSet_nonempty`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#risk-set-nonempty).

## Cox partial likelihood

Cox's partial likelihood `∏_{i : δᵢ} exp ⟪β, xᵢ⟫ / ∑_{l ∈ R(Tᵢ)} exp ⟪β, x_l⟫`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.partialLikelihood`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#partial-likelihood).

## Cox log partial likelihood

The log partial likelihood `∑_{i : δᵢ} (⟪β, xᵢ⟫ - log ∑_{l ∈ R(Tᵢ)} exp ⟪β, x_l⟫)`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.logPartialLikelihood`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#log-partial-likelihood).

## Log of the Cox partial likelihood is the log partial likelihood

The logarithm of the partial likelihood is the log partial likelihood.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.log_partialLikelihood`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#log-partial-likelihood-2).

## Concavity of the Cox log partial likelihood

**Concavity of the Cox log partial likelihood** on `ℝᵖ`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.concaveOn_logPartialLikelihood`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#concave-on-log-partial-likelihood).

## Weighted mean of a covariate over a risk set

The `exp (b z)`-weighted mean of a scalar covariate `z` over the risk set of subject `i`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskMean`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#risk-mean).

## Weighted variance of a covariate over a risk set

The `exp (b z)`-weighted variance of a scalar covariate over the risk set of subject `i`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.riskVar`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#risk-var).

## Cox score for a scalar covariate

The Cox score for a scalar covariate: `∑_{i : δᵢ} (zᵢ - z̄ᵢ(b))`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.coxScore`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#cox-score).

## Cox observed information for a scalar covariate

The Cox observed information for a scalar covariate: `∑_{i : δᵢ} Varᵢ(b)`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.coxInformation`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#cox-information).

## Log partial likelihood of a scalar covariate

The log partial likelihood of a scalar covariate `z` as a function of `b ∈ ℝ`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.logPartialLikelihood₁`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#log-partial-likelihood-3).

## Derivative of the log partial likelihood is the Cox score

The derivative of the scalar log partial likelihood is the Cox score.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.hasDerivAt_logPartialLikelihood`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#has-deriv-at-log-partial-likelihood).

## Derivative of the Cox score is minus the information

The derivative of the Cox score is minus the observed information.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.hasDerivAt_coxScore`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#has-deriv-at-cox-score).

## Number at risk at a subject's time

The number at risk at the time of subject `i`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.numAtRisk`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#num-at-risk).

## Number of group-1 subjects at risk

The number of group-1 subjects at risk at the time of subject `i`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.numAtRiskIn`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#num-at-risk-in).

## Group indicator covariate

The group indicator `zᵢ = 1` for group 1 (`g i = true`) and `0` otherwise.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.groupIndicator`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#group-indicator).

## Log-rank numerator: observed minus expected events

The log-rank numerator `O - E`: observed minus expected group-1 events,
`∑_{i : δᵢ} (zᵢ - n₁(Tᵢ) / n(Tᵢ))`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.observedMinusExpected`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#observed-minus-expected).

## Breslow information

The Breslow (Cox) information `∑_{i : δᵢ} n₁ n₀ / n²` at the risk sets of the events.
This is `-ℓ''(0)` for a group indicator, not the tied log-rank variance: for one tied
risk set with `n = 4`, `n₁ = 2` and `d = 2` events it gives `1 / 2`, while the
hypergeometric log-rank variance is `1 / 3`. It equals the log-rank variance only when
the event times are distinct (so each risk set contributes at most one event).

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.breslowInformation`, a definition declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#breslow-information).

## The log-rank statistic is the Cox score at `β = 0`

`ℓ'(0) = O - E`.

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.coxScore_zero`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#cox-score-zero).

## The Cox information at `β = 0` is the Breslow information

**The Cox information at `β = 0` is the Breslow information** `∑ n₁ n₀ / n²`
(not the tied log-rank variance; see `breslowInformation`).

Formalized by `MathlibExt.Probability.Statistics.CoxPartialLikelihood.coxInformation_zero`, a theorem declared in [MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/Survival/CoxPartialLikelihood.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html#cox-information-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cox proportional hazards model](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/nonparametric-survival/cox-proportional-hazards-model)
