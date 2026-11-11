---
declaration: section
origin: cited
lean: StatMech.Probability.hcq_exponent_le, StatMech.Probability.hcq_gap_closedForm, StatMech.Probability.hcq_gap_le, StatMech.Probability.hcq_capped_full, StatMech.Probability.hcq_dom_of_threshold, StatMech.Probability.hcq_star_of_dominates, StatMech.Probability.hcq_star_capped_threshold, StatMech.Probability.hcq_smallDelta_p_half
statement: formalized
proof: formalized
---

# The capped estimate in the hypercontractive range with a gap condition

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html).

## Hypercontractive exponent is at most the target exponent

In the hypercontractive range the exponent `2/q' - 1` is at most the target exponent `u/(2-u)`.

Formalized by `StatMech.Probability.hcq_exponent_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-exponent-le).

## Closed form of the exponent gap

Closed form of the exponent gap `u/(2-u) - (2/q' - 1)`.

Formalized by `StatMech.Probability.hcq_gap_closedForm`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-gap-closed-form).

## Upper bound on the exponent gap

Upper bound on the exponent gap.

Formalized by `StatMech.Probability.hcq_gap_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-gap-le).

## Capped estimate in the hypercontractive range with matching $q'$

The capped estimate in the hypercontractive range, with the matching `q'`.

Formalized by `StatMech.Probability.hcq_capped_full`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-capped-full).

## Under the gap condition the hypercontractive bound is dominated

If `δ^{gap} ≥ 4p(1-p)`, the bound with exponent `2/q' - 1` and factor `4p(1-p)` is at most
 `δ^{u/(2-u)}`.

Formalized by `StatMech.Probability.hcq_dom_of_threshold`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-dom-of-threshold).

## Target-exponent capped estimate from a domination bound

The capped estimate with exponent `u/(2-u)` from a domination of the hypercontractive bound.

Formalized by `StatMech.Probability.hcq_star_of_dominates`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-star-of-dominates).

## Target-exponent capped estimate under the gap condition

The capped estimate with exponent `u/(2-u)` in the hypercontractive range, under the gap
 condition `δ^{gap} ≥ 4p(1-p)`.

Formalized by `StatMech.Probability.hcq_star_capped_threshold`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-star-capped-threshold).

## Capped estimate at $p = 1/2$ for all $u \in (0, 1)$

At `p = 1/2` the capped estimate `∑_S 4 |S| (1-u)^{|S|-1} f̂(S)² ≤ δ^{u/(2-u)} ∑ₑ Infₑ` holds
 for all `u ∈ (0, 1)`.

Formalized by `StatMech.Probability.hcq_smallDelta_p_half`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-small-delta-p-half).

## Low-range residual case of the capped estimate

The capped estimate for all `p ∈ (1/2, q)` with `p < 1`, `δ < e^{-1}`, and `u ∈ (0, 1)` either
 below the hypercontractive range or failing the gap condition.

Formalized by `StatMech.Probability.hcq_lowRangeResidue`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-low-range-residue).

## Low-range case implies the small-influence case

`hcq_lowRangeResidue q` implies `cvg_smallDeltaResidue q`.

Formalized by `StatMech.Probability.hcq_smallDelta_of_lowRange`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-small-delta-of-low-range).

## Low-range case implies the full capped estimate on $(1/2, q)$

`hcq_lowRangeResidue q` implies `mxd_martingaleHC_statement q`.

Formalized by `StatMech.Probability.hcq_martingaleHC_of_lowRange`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-martingale-hc-of-low-range).

## Gap condition holds at $u = 1$

At `u = 1` (`q' = 1`) the gap condition holds.

Formalized by `StatMech.Probability.hcq_dominated_nonempty`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-dominated-nonempty).

## Power bound $s \le \delta^g$ from a logarithmic exponent bound

`s ≤ δ^g` when `g ≤ log (1/s) / log (1/δ)`.

Formalized by `StatMech.Probability.hcq_threshold_of_gap_small`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-threshold-of-gap-small).

## Gap condition holds at some $u < 1$ in the hypercontractive range

For `p > 1/2` and `0 < δ < 1`, some `u ∈ (0, 1)` lies in the hypercontractive range and
 satisfies the gap condition.

Formalized by `StatMech.Probability.hcq_residue_proper`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-residue-proper).

## Low-range case condition fails for some $u$

For `p > 1/2` and `0 < δ < 1`, the case condition in `hcq_lowRangeResidue` fails for some `u ∈
 (0, 1)`.

Formalized by `StatMech.Probability.hcq_antecedent_not_tautology`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-antecedent-not-tautology).

## Right side of the capped estimate is nonnegative

The right side `δ^{u/(2-u)} ∑ₑ Infₑ` of the capped estimate is nonnegative.

Formalized by `StatMech.Probability.hcq_lowRange_nonvacuous`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/CappedExponentGap.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html#hcq-low-range-nonvacuous).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The capped estimate in the hypercontractive range with a gap condition](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang-2)
