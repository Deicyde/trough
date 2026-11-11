---
declaration: section
origin: cited
lean: StatMech.Probability.dtr_full_weight_eq, StatMech.Probability.dtr_high_part_le, StatMech.Probability.dtr_trunc_split, StatMech.Probability.dtr_qstar, StatMech.Probability.dtr_lowDegreeResidue, StatMech.Probability.dtr_lowDegree_of_residue, StatMech.Probability.dtr_smallDelta_of_residue, StatMech.Probability.dtr_martingaleHC_of_residue
statement: formalized
proof: formalized
---

# Degree truncation of the capped estimate under p-biased measures

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html).

## Fourier total weight equals $4p(1-p)$ times the total influence

The Fourier total weight under `μ_p`: `4 ∑_S |S| f̂(S)² = 4p(1-p) ∑ₑ Infₑ`.

Formalized by `StatMech.Probability.dtr_full_weight_eq`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-full-weight-eq).

## Bound on the high-degree part of the damped total weight

The Fourier part of degree greater than `k` contributes at most `4p(1-p)(1-u)^k ∑ₑ Infₑ` to the
 damped total weight.

Formalized by `StatMech.Probability.dtr_high_part_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-high-part-le).

## Capped estimate from its low-degree part

The capped estimate follows from a bound on its part of degree at most `k`.

Formalized by `StatMech.Probability.dtr_trunc_split`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-trunc-split).

## Exponent $q^{\ast}(p, u)$ paired with the damping

The exponent `q*(p, u) = 1 + (1-u)/(4p(1-p))` paired with the damping `1 - u`.

Formalized by `StatMech.Probability.dtr_qstar`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-qstar).

## Low-degree residual case of the capped estimate

The low-degree form of the capped estimate for every `p ∈ (1/2, q)` with `p < 1`, small maximal
 influence `δ < e^{-1}`, and parameters `u` outside the range handled by `CappedExponentGap`.

Formalized by `StatMech.Probability.dtr_lowDegreeResidue`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-low-degree-residue).

## Low-degree case implies the low-range case

`dtr_lowDegreeResidue q` implies `hcq_lowRangeResidue q`.

Formalized by `StatMech.Probability.dtr_lowDegree_of_residue`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-low-degree-of-residue).

## Low-degree case implies the small-influence case

`dtr_lowDegreeResidue q` implies `cvg_smallDeltaResidue q`.

Formalized by `StatMech.Probability.dtr_smallDelta_of_residue`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-small-delta-of-residue).

## Low-degree case implies the full capped estimate on $(1/2, q)$

`dtr_lowDegreeResidue q` implies `mxd_martingaleHC_statement q`.

Formalized by `StatMech.Probability.dtr_martingaleHC_of_residue`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-martingale-hc-of-residue).

## Some truncation level gives a nonnegative budget

For `δ > 0` the truncation budget `δ^{u/(2-u)} - 4p(1-p)(1-u)^k` is nonnegative for some `k`.

Formalized by `StatMech.Probability.dtr_budget_pos`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-budget-pos).

## Some truncation level makes the low-degree right side nonnegative

For `δ^{u/(2-u)} > 0` some truncation level `k` makes the right side of the low-degree bound
 in `dtr_lowDegreeResidue` nonnegative.

Formalized by `StatMech.Probability.dtr_residue_c0`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/DegreeTruncation.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html#dtr-residue-c0).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degree truncation of the capped estimate under p-biased measures](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/degree-truncation-of-the-capped-estimate-under-p)
