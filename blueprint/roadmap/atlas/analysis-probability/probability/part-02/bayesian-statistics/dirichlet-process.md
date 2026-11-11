---
declaration: section
origin: cited
lean: ProbabilityTheory.stickRemainder, ProbabilityTheory.stickWeight, ProbabilityTheory.stickBreakingMeasure, ProbabilityTheory.sum_range_stickWeight_add_stickRemainder, ProbabilityTheory.stickRemainder_mem_Icc, ProbabilityTheory.stickWeight_nonneg, ProbabilityTheory.antitone_stickRemainder, ProbabilityTheory.hasSum_stickWeight_iff
statement: formalized
---

# Dirichlet process

56 results, 53 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html).

## Leftover stick in stick breaking

The stick left after breaking off the first `k` pieces at proportions `b`:
`∏_{j<k} (1 - bⱼ)`.

Formalized by `ProbabilityTheory.stickRemainder`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-remainder).

## Stick-breaking weights

The `k`-th piece of a stick broken at proportions `b`: `bₖ ∏_{j<k} (1 - bⱼ)`.

Formalized by `ProbabilityTheory.stickWeight`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-weight).

## Stick-breaking measure

The discrete measure `∑ₖ πₖ δ_{θₖ}` with the stick-breaking weights `πₖ = stickWeight b k`
(negative weights, which do not occur for proportions in `[0, 1]`, are read as `0`).

Formalized by `ProbabilityTheory.stickBreakingMeasure`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-breaking-measure).

## Stick-breaking pieces and leftover make up the whole stick

The first `n` pieces and the leftover stick make up the whole stick. Holds for all real
`b`.

Formalized by `ProbabilityTheory.sum_range_stickWeight_add_stickRemainder`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#sum-range-stick-weight-add-stick-remaind).

## Leftover stick lies in the unit interval

The leftover stick is in `[0, 1]` for proportions in `[0, 1]`.

Formalized by `ProbabilityTheory.stickRemainder_mem_Icc`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-remainder-mem-icc).

## Nonnegativity of stick-breaking weights

The pieces are nonnegative for proportions in `[0, 1]`.

Formalized by `ProbabilityTheory.stickWeight_nonneg`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-weight-nonneg).

## Leftover stick is decreasing

The leftover stick shrinks for proportions in `[0, 1]`.

Formalized by `ProbabilityTheory.antitone_stickRemainder`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#antitone-stick-remainder).

## Stick-breaking weights sum to one iff the leftover stick tends to zero

For proportions in `[0, 1]`, the pieces sum to `1` iff the leftover stick tends to `0`.

Formalized by `ProbabilityTheory.hasSum_stickWeight_iff`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#has-sum-stick-weight-iff).

## Mass of a set under the stick-breaking measure

The mass of a measurable set under the stick-breaking measure.

Formalized by `ProbabilityTheory.stickBreakingMeasure_apply`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-breaking-measure-apply).

## Stick-breaking measure is a probability measure

The stick-breaking measure is a probability measure when the pieces sum to `1`.

Formalized by `ProbabilityTheory.isProbabilityMeasure_stickBreakingMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#is-probability-measure-stick-breaking-me).

## Stick-breaking measure has total mass at most one

The stick-breaking measure has total mass at most `1` for proportions in `[0, 1]`.

Formalized by `ProbabilityTheory.stickBreakingMeasure_apply_le_one`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-breaking-measure-apply-le-one).

## Measurability of the stick-breaking measure in its parameters

The stick-breaking measure depends measurably (for the Giry σ-algebra on `Measure X`) on
the proportions and the atoms.

Formalized by `ProbabilityTheory.measurable_stickBreakingMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#measurable-stick-breaking-measure).

## Stick-breaking process

A **stick-breaking process** on the probability space `(Ω, μ)`: independent proportions
`βₖ ∈ [0, 1]` (almost surely, with arbitrary laws), i.i.d. atoms `atom k` with law `H`, and the
proportion sequence independent of the atom sequence. Ishwaran–James (2001) take
`βₖ ∼ Beta(aₖ, bₖ)`; Sethuraman's Dirichlet process is `IsDirichlet`.

Formalized by `ProbabilityTheory.StickBreakingProcess`, a structure declared in [MathlibExt/Probability/DirichletProcess.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#stick-breaking-process).

## Random stick-breaking weight

The random piece `πₖ = βₖ ∏_{j<k} (1 - βⱼ)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.weight`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#weight).

## Random leftover stick

The random leftover stick `∏_{j<k} (1 - βⱼ)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.remainder`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#remainder).

## Random measure of a stick-breaking process

The random measure `G = ∑ₖ πₖ δ_{θₖ}`.

Formalized by `ProbabilityTheory.StickBreakingProcess.G`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#g).

## Expected sum of squared stick-breaking weights

`∑ₖ E[πₖ²]`: given `G`, two independent draws from `G` pick the same piece `k` with
probability `∑ₖ πₖ²`. For an atomless base measure the atoms are almost surely distinct, so this
is also the probability that the two draws coincide (not used here).

Formalized by `ProbabilityTheory.StickBreakingProcess.sumSqWeight`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#sum-sq-weight).

## Measurability of the random stick-breaking weights

The pieces are measurable.

Formalized by `ProbabilityTheory.StickBreakingProcess.measurable_weight`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#measurable-weight).

## Stick-breaking proportions lie in the unit interval almost surely

Almost surely every proportion is in `[0, 1]`.

Formalized by `ProbabilityTheory.StickBreakingProcess.ae_forall_mem_Icc`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-forall-mem-icc).

## Random stick-breaking weights lie in the unit interval almost surely

Almost surely every piece is in `[0, 1]`.

Formalized by `ProbabilityTheory.StickBreakingProcess.ae_weight_mem_Icc`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-weight-mem-icc).

## Measurability of the random stick-breaking measure

The random measure depends measurably on `ω`.

Formalized by `ProbabilityTheory.StickBreakingProcess.measurable_G`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#measurable-g).

## Base measure of a stick-breaking process is a probability measure

The base measure is a probability measure.

Formalized by `ProbabilityTheory.StickBreakingProcess.isProbabilityMeasure_H`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#is-probability-measure-h).

## Expected leftover stick is the product of expected complements

`E[∏_{j<k} (1 - βⱼ)] = ∏_{j<k} (1 - E[βⱼ])`.

Formalized by `ProbabilityTheory.StickBreakingProcess.integral_remainder`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#integral-remainder).

## Mean of a stick-breaking weight

`E[πₖ] = E[βₖ] ∏_{j<k} (1 - E[βⱼ])`.

Formalized by `ProbabilityTheory.StickBreakingProcess.integral_weight`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#integral-weight).

## Second moment of a stick-breaking weight

`E[πₖ²] = E[βₖ²] ∏_{j<k} E[(1 - βⱼ)²]`.

Formalized by `ProbabilityTheory.StickBreakingProcess.integral_weight_sq`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#integral-weight-sq).

## Random stick-breaking weights sum to one almost surely

If the expected leftover stick `∏_{j<k} (1 - E[βⱼ])` tends to `0`, the pieces sum to `1`
almost surely.

Formalized by `ProbabilityTheory.StickBreakingProcess.ae_hasSum_weight`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-has-sum-weight).

## Stick-breaking random measure is almost surely a probability measure

When the pieces sum to `1` almost surely, `G` is almost surely a probability measure.

Formalized by `ProbabilityTheory.StickBreakingProcess.ae_isProbabilityMeasure_G_of_hasSum`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-is-probability-measure-g-of-has-sum).

## Mean of the random measure

If the pieces sum to `1` almost surely, then
`E[G(A)] = H(A)` for every measurable `A`.

Formalized by `ProbabilityTheory.StickBreakingProcess.lintegral_G_apply`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-g-apply).

## Mixed second moment of the random measure

If the pieces sum to `1` almost surely, then
`E[G(A) G(B)] = (1 - s) H(A) H(B) + s H(A ∩ B)` with `s = ∑ₖ E[πₖ²]` (`sumSqWeight`, at most
`1` under this hypothesis): two draws from `G` pick the same piece with probability `s`, and
otherwise land on two independent atoms.

Formalized by `ProbabilityTheory.StickBreakingProcess.lintegral_G_mul_G`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-g-mul-g).

## Sethuraman's stick-breaking representation of the Dirichlet process

**Sethuraman's stick-breaking representation of the Dirichlet process** `DP(α, H)`
(Sethuraman 1994): the proportions are `Beta(1, α)` with `α > 0`. We take this construction as
the definition of `DP(α, H)`; Sethuraman's theorem that it has Ferguson's Dirichlet marginals
is recorded in `WantedExt/Probability/DirichletProcessWanted.lean`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet`, a structure declared in [MathlibExt/Probability/DirichletProcess.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#is-dirichlet).

## Blackwell–MacQueen urn predictive law

The predictive law in the **Blackwell–MacQueen urn**: after observations `x₀, …, x_{n-1}`,
the next observation has law `(α H + ∑ᵢ δ_{xᵢ}) / (α + n)`. It is a probability measure for
`α > 0` and a probability measure `H` (`isProbabilityMeasure_polyaUrnPredictive`); outside that
domain the definition is total but meaningless (e.g. `α = n = 0` gives the zero measure).

Formalized by `ProbabilityTheory.polyaUrnPredictive`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#polya-urn-predictive).

## Predictive probability of a set in the Blackwell–MacQueen urn

The predictive probability of a measurable set: `(α H(A) + #{i | xᵢ ∈ A}) / (α + n)`.

Formalized by `ProbabilityTheory.polyaUrnPredictive_apply`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#polya-urn-predictive-apply).

## Blackwell–MacQueen predictive law is a probability measure

The predictive law is a probability measure for `α > 0` and a probability measure `H`.

Formalized by `ProbabilityTheory.isProbabilityMeasure_polyaUrnPredictive`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#is-probability-measure-polya-urn-predict).

## Beta law is concentrated on the unit interval

The Beta law is concentrated on `[0, 1]`.

Formalized by `ProbabilityTheory.ae_mem_Icc_betaMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-mem-icc-beta-measure).

## Second moment of $1 - X$ under $\mathrm{Beta}(1, \alpha)$

`E[(1 - x)²] = α / (α + 2)` under `Beta(1, α)`.

Formalized by `ProbabilityTheory.integral_one_sub_sq_betaMeasure_one`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#integral-one-sub-sq-beta-measure-one).

## Mean proportion of a Dirichlet process

The proportions of a Dirichlet process have mean `1 / (1 + α)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.integral_β`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#integral).

## Mean of a Dirichlet-process weight

**Mean of a Dirichlet-process weight** (Sethuraman 1994): `E[πₖ] = αᵏ / (1 + α)^(k+1)`
(`α^{k-1} / (1 + α)^k` for Sethuraman's `π_k`, indexed from `1`).

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.integral_weight`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#integral-weight-2).

## The Dirichlet-process weights sum to `1` almost surely

**The Dirichlet-process weights sum to `1` almost surely** (Sethuraman 1994): the leftover
stick tends to `0`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.ae_hasSum_weight`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-has-sum-weight-2).

## Dirichlet process is almost surely a probability measure

A Dirichlet process is almost surely a probability measure.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.ae_isProbabilityMeasure_G`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#ae-is-probability-measure-g).

## Mean of the Dirichlet process

**Mean of the Dirichlet process** (Ferguson 1973): `E[G(A)] = H(A)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.lintegral_G_apply`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-g-apply-2).

## Probability that two Dirichlet process draws pick the same piece

Two draws from a Dirichlet process pick the same piece with probability `1 / (1 + α)`:
`∑ₖ E[πₖ²] = 1 / (1 + α)`. This is the probability that the second customer of the Chinese
restaurant process with parameter `α` joins the first one's table.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.sumSqWeight_eq`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#sum-sq-weight-eq).

## Mixed second moment of the Dirichlet process

**Mixed second moment of the Dirichlet process** (Ferguson 1973):
`E[G(A) G(B)] = (α H(A) H(B) + H(A ∩ B)) / (α + 1)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.lintegral_G_mul_G`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 769](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L769). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-g-mul-g-2).

## The Blackwell–MacQueen urn for two draws

**The Blackwell–MacQueen urn for two draws** (Blackwell–MacQueen 1973): if `X₁, X₂` are
i.i.d. draws from a Dirichlet process `G`, then `P(X₁ ∈ A, X₂ ∈ B) = E[G(A) G(B)]` equals
`∫_A P(X₂ ∈ B | X₁ = x) dH(x)` with the predictive law
`polyaUrnPredictive α H ![x] = (α H + δₓ) / (α + 1)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.lintegral_G_mul_G_eq_predictive`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-g-mul-g-eq-predictive).

## Variance of the Dirichlet process

**Variance of the Dirichlet process** (Ferguson 1973):
`Var(G(A)) = H(A) (1 - H(A)) / (α + 1)`.

Formalized by `ProbabilityTheory.StickBreakingProcess.IsDirichlet.variance_G_apply`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 812](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L812). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#variance-g-apply).

## Sethuraman's canonical probability space

The product probability space `(ℕ → ℝ) × (ℕ → X)` carrying i.i.d. `Beta(1, α)` proportions
and, independently, i.i.d. `H` atoms.

Formalized by `ProbabilityTheory.sethuramanMeasure`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 859](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L859). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#sethuraman-measure).

## Law of the proportion coordinate of Sethuraman's space

The proportion coordinate of the canonical space has law `⊗ₖ Beta(1, α)`.

Formalized by `ProbabilityTheory.measurePreserving_fst_sethuramanMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 871](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L871). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#measure-preserving-fst-sethuraman-measur).

## Law of the atom coordinate of Sethuraman's space

The atom coordinate of the canonical space has law `⊗ₖ H`.

Formalized by `ProbabilityTheory.measurePreserving_snd_sethuramanMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 880](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L880). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#measure-preserving-snd-sethuraman-measur).

## Law of each proportion in Sethuraman's space

Each proportion of the canonical space has law `Beta(1, α)`.

Formalized by `ProbabilityTheory.hasLaw_fst_sethuramanMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 887](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#has-law-fst-sethuraman-measure).

## Law of each atom in Sethuraman's space

Each atom of the canonical space has law `H`.

Formalized by `ProbabilityTheory.hasLaw_snd_sethuramanMeasure`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#has-law-snd-sethuraman-measure).

## Sethuraman's construction

**Sethuraman's construction** on the canonical space: the coordinates of the two factors are
the proportions and the atoms.

Formalized by `ProbabilityTheory.sethuraman`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 903](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L903). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#sethuraman).

## Sethuraman's canonical model is a Dirichlet process

The canonical model is a Dirichlet process.

Formalized by `ProbabilityTheory.StickBreakingProcess.isDirichlet_sethuraman`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#is-dirichlet-sethuraman).

## Dirichlet process

The **Dirichlet process** `DP(α, H)` as a law on `Measure X`, defined as the law of
Sethuraman's (1994) stick-breaking measure with `Beta(1, α)` proportions and `H` atoms.
Ferguson's (1973) definition by Dirichlet marginals is the wanted statement
`map_dirichletProcess_partition`.

Formalized by `ProbabilityTheory.dirichletProcess`, a definition declared in [MathlibExt/Probability/DirichletProcess.lean, line 936](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L936). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#dirichlet-process).

## Mean of the Dirichlet process

**Mean of the Dirichlet process**, law form: `∫ ν(A) dDP(α, H)(ν) = H(A)`.

Formalized by `ProbabilityTheory.lintegral_dirichletProcess_apply`, a theorem declared in [MathlibExt/Probability/DirichletProcess.lean, line 947](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/DirichletProcess.lean#L947). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-dirichlet-process-apply).

## Finite-dimensional marginals of the Dirichlet process

**Finite-dimensional marginals of the Dirichlet process** (Ferguson 1973, §3; Sethuraman
1994, Theorem 3.4): on a measurable partition `A₀, …, A_m` of `X` with `H(Aᵢ) > 0`, the vector
`(G(A₀), …, G(A_m))` has the Dirichlet law `Dir(α H(A₀), …, α H(A_m))`.

Stated but not proved: `ProbabilityTheory.map_dirichletProcess_partition` is written with `theorem_wanted` in [WantedExt/Probability/DirichletProcessWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/DirichletProcessWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#map-dirichlet-process-partition).

## The moments of the Dirichlet process are the Blackwell–MacQueen urn

**The moments of the Dirichlet process are the Blackwell–MacQueen urn** (Blackwell–MacQueen
1973): `E[∏ᵢ G(Aᵢ)] = P(X₀ ∈ A₀, …, X_{n-1} ∈ A_{n-1})` for the urn's first `n` draws.

Stated but not proved: `ProbabilityTheory.lintegral_dirichletProcess_prod` is written with `theorem_wanted` in [WantedExt/Probability/DirichletProcessWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/DirichletProcessWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#lintegral-dirichlet-process-prod).

## Ferguson's conjugacy

**Ferguson's conjugacy** (Ferguson 1973, Theorem 1): given `n` observations `xs` from
`G ∼ DP(α, H)`, the posterior of `G` is `DP(α + n, (α H + ∑ᵢ δ_{xsᵢ}) / (α + n))`. Stated as
the disintegration `P(G ∈ S, X₀ ∈ A₀, …) = ∫_{∏ Aᵢ} DP(α + n, posterior base)(S) dP(xs)` over
the urn law of the observations.

Stated but not proved: `ProbabilityTheory.setLIntegral_dirichletProcess_prod` is written with `theorem_wanted` in [WantedExt/Probability/DirichletProcessWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/DirichletProcessWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html#set-lintegral-dirichlet-process-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dirichlet process](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/dirichlet-process/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/bayesian-statistics/dirichlet-process)
