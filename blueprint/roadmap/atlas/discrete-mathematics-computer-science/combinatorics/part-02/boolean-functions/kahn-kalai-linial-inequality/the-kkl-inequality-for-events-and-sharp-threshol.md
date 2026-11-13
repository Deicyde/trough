---
declaration: section
origin: cited
lean: StatMech.TwoDim.kklw_weight_eq, StatMech.TwoDim.kklw_prob_eq_expect, StatMech.TwoDim.kklw_influence_eq_infl, StatMech.TwoDim.kklw_var_eq, StatMech.TwoDim.kklw_logMaxInfl, StatMech.TwoDim.kklw_hkkl_of_hypercontractive, StatMech.TwoDim.kklw_hkkl_half, StatMech.TwoDim.kklw_hkkl
statement: formalized
proof: formalized
---

# The KKL inequality for events, and sharp thresholds

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html).

## OSSS Bernoulli weight equals the configuration weight

The OSSS Bernoulli weight of a configuration is `StatMech.configWeight`.

Formalized by `StatMech.TwoDim.kklw_weight_eq`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-weight-eq).

## Event probability as the OSSS expectation of its indicator

`StatMech.prob p A` is the OSSS expectation of the indicator of `A`.

Formalized by `StatMech.TwoDim.kklw_prob_eq_expect`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-prob-eq-expect).

## Pivotal-probability influence as the OSSS influence of an indicator

`StatMech.BeffaraDC.influence` is the OSSS influence of the indicator of `A`.

Formalized by `StatMech.TwoDim.kklw_influence_eq_infl`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-influence-eq-infl).

## Variance of an event indicator is $P(A)(1 - P(A))$

The variance of the indicator of `A` is `P(A)(1 - P(A))`.

Formalized by `StatMech.TwoDim.kklw_var_eq`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-var-eq).

## Logarithm of the reciprocal maximal influence of an event

`log (1 / maxₑ Infₑ(A))` under the Bernoulli(`p`) product measure.

Formalized by `StatMech.TwoDim.kklw_logMaxInfl`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-log-max-infl).

## KKL inequality with constant 2 at $p$ implies its event form

The KKL inequality `KKLHypercontractive p 2` for an event: `2 · P_p(A)(1 - P_p(A)) · log (1 /
 maxₑ Infₑ(A)) ≤ ∑ₑ Infₑ(A)`.

Formalized by `StatMech.TwoDim.kklw_hkkl_of_hypercontractive`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-hkkl-of-hypercontractive).

## Kahn–Kalai–Linial inequality

**Kahn–Kalai–Linial inequality** for events under the uniform measure (J. Kahn, G. Kalai, N.
 Linial, *The influence of variables on Boolean functions*, FOCS 1988), with constant `2`: `2 ·
 P(A)(1 - P(A)) · log (1 / maxₑ Infₑ(A)) ≤ ∑ₑ Infₑ(A)`, where `Infₑ(A)` is the probability that
 `e` is pivotal for `A`.

Formalized by `StatMech.TwoDim.kklw_hkkl_half`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-hkkl-half).

## KKL on the interior of $(1/2, q)$ implies its event form there

`kklw_hkkl_of_hypercontractive` at every `p` in the interior of `[1/2, q]`.

Formalized by `StatMech.TwoDim.kklw_hkkl`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-hkkl).

## Sharp-threshold bound assuming the KKL inequality on $(1/2, q)$

Sharp-threshold bound: for an increasing event with `P_{1/2}(A) = 1/2`, if the KKL inequality
 holds for all `p ∈ (1/2, q)` and there `P_p(A)(1 - P_p(A)) ≥ v₀` and `log (1 / maxₑ Infₑ(A)) ≥
 L`, then `P_q(A) ≥ 1/2 + 2 v₀ L (q - 1/2)`.

Formalized by `StatMech.TwoDim.kklw_sharpThreshold`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-sharp-threshold).

## Sharp-threshold window bound assuming the KKL inequality on $(1/2, q)$

Window form of `kklw_sharpThreshold`: under the same hypotheses, if `P_q(A) ≤ 1 - ε` then `q -
 1/2 ≤ (1/2 - ε) / (2 v₀ L)`.

Formalized by `StatMech.TwoDim.kklw_sharpThreshold_window`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLEvents.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html#kklw-sharp-threshold-window).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The KKL inequality for events, and sharp thresholds](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-for-events-and-sharp-threshol)
