---
declaration: section
origin: cited
lean: MathlibExt.Probability.Causality.sampleMean, MathlibExt.Probability.Causality.sampleVar, MathlibExt.Probability.Causality.popMean, MathlibExt.Probability.Causality.popVar, MathlibExt.Probability.Causality.ate, MathlibExt.Probability.Causality.diffInMeans, MathlibExt.Probability.Causality.neymanVar, MathlibExt.Probability.Causality.randExp
statement: formalized
proof: formalized
---

# Potential outcomes and causal identification

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html).

## Finite-population randomization inference (Neyman 1923)

## Sample mean over a set of units

The mean of `y` over a set of units `S`, `(1/|S|) ∑_{i ∈ S} yᵢ` (the junk value `0` for
`S = ∅`).

Formalized by `MathlibExt.Probability.Causality.sampleMean`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#sample-mean).

## Sample variance over a set of units

The sample variance of `y` over `S` with divisor `|S| - 1`; meaningful for `|S| ≥ 2` (for
`|S| ≤ 1` it is the junk value `0`).

Formalized by `MathlibExt.Probability.Causality.sampleVar`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#sample-var).

## Mean of a finite population

The mean of a finite population of `N = Fintype.card ι` units, `(1/N) ∑ᵢ yᵢ`.

Formalized by `MathlibExt.Probability.Causality.popMean`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#pop-mean).

## Variance of a finite population

The variance of a finite population with divisor `N - 1`, `S² = ∑ᵢ (yᵢ - ȳ)² / (N - 1)`;
meaningful for `N ≥ 2`.

Formalized by `MathlibExt.Probability.Causality.popVar`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#pop-var).

## Finite-population average treatment effect

The finite-population average treatment effect `(1/N) ∑ᵢ (y₁ᵢ - y₀ᵢ)`.

Formalized by `MathlibExt.Probability.Causality.ate`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#ate).

## Difference-in-means estimator

The difference in means for the treated set `S`: the mean of the treated outcomes `y₁` over
`S` minus the mean of the control outcomes `y₀` over the complement.

Formalized by `MathlibExt.Probability.Causality.diffInMeans`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#diff-in-means).

## Neyman's variance estimator

Neyman's variance estimator `s₁² / n₁ + s₀² / n₀` for the treated set `S`.

Formalized by `MathlibExt.Probability.Causality.neymanVar`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#neyman-var).

## Expectation of a statistic under complete randomization

The expectation of a statistic `f` of the treated set under complete randomization: the
treated set is uniform among the `(N choose n₁)` sets of `n₁` units (`n₁ ≤ N`; for `n₁ > N`
there is no such set and the value is `0`).

Formalized by `MathlibExt.Probability.Causality.randExp`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#rand-exp).

## Neyman (1923)

Under complete randomization with `n₁ ≥ 1` treated and `n₀ ≥ 1` control
units, the difference in means is unbiased for the finite-population average treatment
effect.

Formalized by `MathlibExt.Probability.Causality.randExp_diffInMeans`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#rand-exp-diff-in-means).

## Neyman (1923)

The variance of the difference in means under complete randomization is
`S₁²/n₁ + S₀²/n₀ - S_τ²/N`, where `S_τ²` is the population variance of the unit-level effects
`τᵢ = y₁ᵢ - y₀ᵢ` and `n₀ = N - n₁`.

Formalized by `MathlibExt.Probability.Causality.randExp_sq_diffInMeans_sub_ate`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#rand-exp-sq-diff-in-means-sub-ate).

## Expectation of Neyman's variance estimator under complete randomization

The expectation of Neyman's variance estimator under complete randomization with at least
two treated and two control units is `S₁²/n₁ + S₀²/n₀` (the sample variances are unbiased for
the population variances under sampling without replacement).

Formalized by `MathlibExt.Probability.Causality.randExp_neymanVar`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#rand-exp-neyman-var).

## Neyman's variance estimator is conservative

Its expectation under complete
randomization is at least the variance of the difference in means, with equality exactly when
the treatment effect `y₁ᵢ - y₀ᵢ` is the same for all units.

Formalized by `MathlibExt.Probability.Causality.randVar_le_randExp_neymanVar`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#rand-var-le-rand-exp-neyman-var).

## Observed outcome from potential outcomes

The observed outcome: `Y₁` on the treated event `T`, `Y₀` off it (consistency).

Formalized by `MathlibExt.Probability.Causality.observed`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#observed).

## Propensity score

The propensity of the event `T` given `W = w`, `P(T ∩ {W = w}) / P(W = w)`. Meaningful for
`P(W = w) > 0`; it is `0` (a junk value) when `P(W = w) = 0`.

Formalized by `MathlibExt.Probability.Causality.propensity`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#propensity).

## Conditional independence given a discrete variable

The event `T` is conditionally independent of `V` given `W`, stated through the values of
`W`: `P(T, V ∈ B, W = w) P(W = w) = P(T, W = w) P(V ∈ B, W = w)` for all measurable `B` and all
`w`. For a `W` with countably many values this is the conditional independence of the indicator
of `T` and `V` given `W`.

Formalized by `MathlibExt.Probability.Causality.CondIndepDiscrete`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#cond-indep-discrete).

## Strong ignorability

**Strong ignorability** of the treatment `T` given `W` for the potential outcomes `V`
(Rosenbaum & Rubin 1983): `T ⊥ V | W` and overlap, `0 < P(T | W = w) < 1` for every value `w`
of positive probability.

Formalized by `MathlibExt.Probability.Causality.StronglyIgnorable`, a definition declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 529](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L529). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#strongly-ignorable).

## Strong ignorability passes to functions of the potential outcomes

Strong ignorability is inherited by measurable functions of the potential outcomes.

Formalized by `MathlibExt.Probability.Causality.StronglyIgnorable.comp`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#comp).

## Rosenbaum & Rubin (1983), Theorem 1

The propensity score `e(X) = P(T | X)` is a
balancing score: given `e(X)`, the treatment is conditionally independent of the covariate
`X`.

Formalized by `MathlibExt.Probability.Causality.condIndepDiscrete_propensity`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#cond-indep-discrete-propensity).

## Calibration of the propensity score

The propensity score is calibrated: among units with score `c` (an event of positive
probability), the proportion treated is `c`.

Formalized by `MathlibExt.Probability.Causality.propensity_propensity`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#propensity-propensity).

## Rosenbaum & Rubin (1983), Theorem 2

A function `b(X)` of the covariate is a balancing
score (`T ⊥ X | b(X)`) if and only if it is finer than the propensity score: covariate values
of positive probability with the same `b` have the same propensity. (Theorem 1 is the case
`b = e`.)

Formalized by `MathlibExt.Probability.Causality.condIndepDiscrete_comp_iff`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#cond-indep-discrete-comp-iff).

## Rosenbaum & Rubin (1983), Theorem 3

If treatment assignment is strongly ignorable given
the covariate `X`, it is strongly ignorable given any balancing score `b(X)`.

Formalized by `MathlibExt.Probability.Causality.StronglyIgnorable.comp_of_balancing`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 786](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L786). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#comp-of-balancing).

## Rosenbaum & Rubin (1983), Theorem 3

**Rosenbaum & Rubin (1983), Theorem 3** for the propensity score: if treatment assignment
is strongly ignorable given the covariate `X`, it is strongly ignorable given `e(X)`.

Formalized by `MathlibExt.Probability.Causality.stronglyIgnorable_propensity`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 843](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L843). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#strongly-ignorable-propensity).

## Inverse probability weighting

**Inverse probability weighting** (Horvitz & Thompson 1952; Rosenbaum 1987): under
strong ignorability of `T` given a finitely-valued covariate `X` for the treated potential
outcome `Y₁`, `E[1_T Y / e(X)] = E[Y₁]`, where `Y` is the observed outcome.

Formalized by `MathlibExt.Probability.Causality.integral_ipw_treated`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 886](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L886). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#integral-ipw-treated).

## Inverse probability weighting

**Inverse probability weighting**, control arm: under strong ignorability of `T` given `X`
for `Y₀`, `E[1_{Tᶜ} Y / (1 - e(X))] = E[Y₀]`.

Formalized by `MathlibExt.Probability.Causality.integral_ipw_control`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#integral-ipw-control).

## Identification of the average treatment effect by inverse probability weighting

Under
strong ignorability of `T` given a finitely-valued `X` for the pair `(Y₀, Y₁)`,
`E[1_T Y / e(X) - 1_{Tᶜ} Y / (1 - e(X))] = E[Y₁ - Y₀]`.

Formalized by `MathlibExt.Probability.Causality.integral_ipw_ate`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 905](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L905). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#integral-ipw-ate).

## Inverse probability weighting with a general covariate

Let the covariate information be
a sub-σ-algebra `m` (for example the one generated by `X`), and `e = P(T | m)` the propensity
score. If `Y₁` is integrable, the treatment is mean-ignorable for `Y₁`,
`E[1_T Y₁ | m] = e E[Y₁ | m]` (implied by `Y₁ ⊥ T | m`), and overlap holds in the strong form
`e ≥ ε > 0`, then `E[1_T Y / e] = E[Y₁]` for the observed outcome `Y`.

Formalized by `MathlibExt.Probability.Causality.integral_ipw_treated_condExp`, a theorem declared in [MathlibExt/Probability/Causality/CausalIdentification.lean, line 929](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Causality/CausalIdentification.lean#L929). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html#integral-ipw-treated-cond-exp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Potential outcomes and causal identification](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/nonparametric-survival/potential-outcomes-and-causal-identification)
