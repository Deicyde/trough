---
declaration: section
origin: cited
lean: StatMech.Probability.fsm2_dampWeight, StatMech.Probability.fsm2_dampWeight_one, StatMech.Probability.fsm2_dampWeight_le_hc, StatMech.Probability.fsm2_dampWeight_le_infl, StatMech.Probability.fsm2_logSum_gain, StatMech.Probability.fsm2_logGain_capped
statement: formalized
proof: formalized
---

# Log-sum estimates for damped influences under p-biased measures

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html).

## Damped influence of a coordinate

The damped influence `Dₑ(ρ) = ∑_{S ∋ e} ρ^{2|S \ {e}|} (f̂(S) / √(p(1-p)))²` of coordinate `e`
 on the Boolean function `φ` under `μ_p`.

Formalized by `StatMech.Probability.fsm2_dampWeight`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html#fsm2-damp-weight).

## Damped influence at $\rho = 1$ is the influence

At `ρ = 1` the damped influence is the influence.

Formalized by `StatMech.Probability.fsm2_dampWeight_one`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html#fsm2-damp-weight-one).

## Hypercontractive bound on the damped influence

Hypercontractive bound on the damped influence: `Dₑ(ρ) ≤ Infₑ^{2/q}` when `ρ² = 4p(1-p)(q-1)`
 and `1 ≤ q ≤ 2`.

Formalized by `StatMech.Probability.fsm2_dampWeight_le_hc`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html#fsm2-damp-weight-le-hc).

## Damped influence is at most the influence

The damped influence is at most the influence.

Formalized by `StatMech.Probability.fsm2_dampWeight_le_infl`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html#fsm2-damp-weight-le-infl).

## Log-sum inequality for influences against damped influences

The log-sum inequality for the influences against the damped influences, over the coordinates of
 positive influence.

Formalized by `StatMech.Probability.fsm2_logSum_gain`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html#fsm2-log-sum-gain).

## Capped log-sum estimate for damped influences

The capped log-sum estimate: `(∑ₑ Infₑ) · (2/q - 1) · log (1 / δ) ≤ ∑ₑ Infₑ · log (Infₑ /
 Dₑ(ρ))` (over coordinates of positive influence), with `δ = maxₑ Infₑ ∈ (0, 1)`.

Formalized by `StatMech.Probability.fsm2_logGain_capped`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSMartingale.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html#fsm2-log-gain-capped).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Log-sum estimates for damped influences under p-biased measures](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/log-sum-estimates-for-damped-influences-under-p)
