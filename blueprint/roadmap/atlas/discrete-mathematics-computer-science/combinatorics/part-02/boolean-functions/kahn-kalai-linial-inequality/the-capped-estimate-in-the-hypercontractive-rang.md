---
declaration: section
origin: cited
lean: StatMech.Probability.frh_perCoordWeight, StatMech.Probability.frh_lhs_eq, StatMech.Probability.frh_at_zero, StatMech.Probability.frh_capped_martingale, StatMech.Probability.frh_capped_param, StatMech.Probability.frh_openResidue, StatMech.Probability.frh_endpoint_one, StatMech.Probability.frh_martingaleHC_of_openResidue
statement: formalized
proof: formalized
---

# The capped estimate in the hypercontractive range

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html).

## Per-coordinate damped weight

The per-coordinate damped weight `Dₑ(u) = ∑_{S ∋ e} (1-u)^{|S|-1} (f̂(S)/√(p(1-p)))²` under
 `μ_p`.

Formalized by `StatMech.Probability.frh_perCoordWeight`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-per-coord-weight).

## Damped total weight as a sum of per-coordinate weights

The damped total weight is `4p(1-p) ∑ₑ Dₑ(u)`.

Formalized by `StatMech.Probability.frh_lhs_eq`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-lhs-eq).

## Damped total weight at $u = 0$ is at most the total influence

At `u = 0` the damped total weight is at most the total influence.

Formalized by `StatMech.Probability.frh_at_zero`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-at-zero).

## Capped estimate in the hypercontractive range

The capped estimate in the hypercontractive range: if `1 - u = 4p(1-p)(q'-1)` with `1 ≤ q' ≤ 2`,
 then `∑_S 4 |S| (1-u)^{|S|-1} f̂(S)² ≤ 4p(1-p) * δ^{2/q'-1} ∑ₑ Infₑ`.

Formalized by `StatMech.Probability.frh_capped_martingale`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-capped-martingale).

## Parametrization of the hypercontractive range by $q' \in (1, 2)$

Every `u ∈ [1 - 4p(1-p), 1]` has the form `1 - u = 4p(1-p)(q'-1)` with `q' ∈ [1, 2]`.

Formalized by `StatMech.Probability.frh_capped_param`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-capped-param).

## Open-interval residual case of the capped estimate

The capped estimate `∑_S 4 |S| (1-u)^{|S|-1} f̂(S)² ≤ δ^{u/(2-u)} ∑ₑ Infₑ` for all `p ∈ (1/2,
 q)` with `p < 1` and all `u ∈ (0, 1)`.

Formalized by `StatMech.Probability.frh_openResidue`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-open-residue).

## Capped estimate at the endpoint $u = 1$

At `u = 1` the capped estimate holds.

Formalized by `StatMech.Probability.frh_endpoint_one`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-endpoint-one).

## Open-interval case implies the full capped estimate on $(1/2, q)$

`frh_openResidue q` implies `mxd_martingaleHC_statement q`, by adding the endpoints.

Formalized by `StatMech.Probability.frh_martingaleHC_of_openResidue`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-martingale-hc-of-open-residue).

## Hypercontractive range misses an interval near $u = 0$

For `p > 1/2` the hypercontractive range `u ≥ 1 - 4p(1-p)` excludes a nonempty interval near `u
 = 0`.

Formalized by `StatMech.Probability.frh_lowNoise_range_nonempty`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/Hypercontractivity/FullRangeHC.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html#frh-low-noise-range-nonempty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The capped estimate in the hypercontractive range](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-capped-estimate-in-the-hypercontractive-rang)
