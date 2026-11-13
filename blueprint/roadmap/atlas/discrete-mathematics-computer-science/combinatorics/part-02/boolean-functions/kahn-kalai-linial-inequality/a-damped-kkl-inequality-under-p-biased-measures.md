---
declaration: section
origin: cited
lean: StatMech.Probability.fpe_integral_lhs, StatMech.Probability.fpe_master_sub, StatMech.Probability.fpe_dampedVarLogGain, StatMech.Probability.fpe_Q_eq_var_at_half, StatMech.Probability.fpe_kklGain_at_half
statement: formalized
proof: formalized
---

# A damped KKL inequality under p-biased measures

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html).

## Integrating damped total-influence weights over the noise parameter

Integrating the damped total-influence weights over the noise parameter, with the `p`-biased
 scaling `A = 4p(1-p)`.

Formalized by `StatMech.Probability.fpe_integral_lhs`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html#fpe-integral-lhs).

## Capped $p$-biased per-coordinate estimate in the variable $u$

The capped per-coordinate estimate under `μ_p` in the variable `u`, with `ρ² = A (1 - u)` and `A
 = 4p(1-p)`.

Formalized by `StatMech.Probability.fpe_master_sub`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html#fpe-master-sub).

## Damped KKL inequality under the $p$-biased measure

Damped KKL inequality under the Bernoulli(`p`) measure, `0 < p < 1`: with `A = 4p(1-p)`, `2 ·
 (∑_{S ≠ ∅} (A^{|S|-1} / A) f̂(S)²) · log (1 / maxₑ Infₑ) ≤ ∑ₑ Infₑ`.

Formalized by `StatMech.Probability.fpe_dampedVarLogGain`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html#fpe-damped-var-log-gain).

## Damped variance equals the variance at $p = 1/2$

At `p = 1/2` the damped variance is the variance.

Formalized by `StatMech.Probability.fpe_Q_eq_var_at_half`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html#fpe-q-eq-var-at-half).

## KKL inequality with constant $2$ at $p = 1/2$

The KKL inequality with constant `2` at `p = 1/2`, obtained from `fpe_dampedVarLogGain`. The
 same statement is `kkl_inequality_total fsr_pbiased_endpoint`, proved there by the
 uniform-cube argument.

Formalized by `StatMech.Probability.fpe_kklGain_at_half`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSPerEdge.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html#fpe-kkl-gain-at-half).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A damped KKL inequality under p-biased measures](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/a-damped-kkl-inequality-under-p-biased-measures)
