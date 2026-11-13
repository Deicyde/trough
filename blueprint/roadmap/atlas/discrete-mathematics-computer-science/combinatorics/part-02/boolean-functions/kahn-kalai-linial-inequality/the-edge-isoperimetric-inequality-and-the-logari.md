---
declaration: section
origin: cited
lean: StatMech.Probability.klo_one_sub_pow_le, StatMech.Probability.klo_master_le, StatMech.Probability.klo_edge_isoperimetric, StatMech.Probability.klo_DeltaUpgrade, StatMech.Probability.klo_deltaUpgrade_zero, StatMech.Probability.klo_logOptimisation_of_deltaUpgrade, StatMech.Probability.klo_logOptimisation
statement: formalized
proof: formalized
---

# The edge-isoperimetric inequality and the logarithmic KKL reduction

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html).

## Bernoulli's inequality $1 - x^k \le k(1 - x)$

Bernoulli's inequality in the form `1 - x^k ≤ k (1 - x)` for `0 ≤ x` (the hypothesis
`x ≤ 1` is not needed). See also `one_add_mul_le_pow`.

Formalized by `StatMech.Probability.klo_one_sub_pow_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-one-sub-pow-le).

## Bound on $m - m^{2/(1+\rho^2)}$ by total influence

For an event of uniform measure `m` and total influence `I = ∑_S 4 |S| f̂(S)²`, `m -
 m^{2/(1+ρ²)} ≤ (1 - ρ²) I / 4` for `0 ≤ ρ ≤ 1`.

Formalized by `StatMech.Probability.klo_master_le`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-master-le).

## Edge-isoperimetric inequality

**Edge-isoperimetric inequality** on the discrete cube (S. Hart, *A note on the edges of the
 n-cube*, Discrete Math. 1976): an event of uniform measure `m > 0` has total influence at least
 `2 m log (1 / m)`. Here `log` is the natural logarithm, so this is weaker by the factor `log 2`
 than the sharp bound `2 m log₂ (1 / m)`.

Formalized by `StatMech.Probability.klo_edge_isoperimetric`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-edge-isoperimetric).

## Fourier-form KKL inequality given the measure–influence bound

The KKL inequality at `p = 1/2` in Fourier form, with the bound `m - m^{2/(1+ρ²)} ≤ (1 - ρ²) I /
 4` (for all `ρ ∈ [0, 1]`) as a hypothesis, where `m` is the measure and `I` the total influence
 of `φ`. The hypothesis always holds (`klo_master_le`).

Formalized by `StatMech.Probability.klo_DeltaUpgrade`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-delta-upgrade).

## Measure–influence form of KKL with constant 0 holds trivially

`klo_DeltaUpgrade 0` holds trivially.

Formalized by `StatMech.Probability.klo_deltaUpgrade_zero`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-delta-upgrade-zero).

## Measure–influence form of KKL implies the indicator-bound form

`klo_DeltaUpgrade c` implies `kls_LogOptimisation c`.

Formalized by `StatMech.Probability.klo_logOptimisation_of_deltaUpgrade`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-log-optimisation-of-delta-upgrade).

## Measure–influence form of KKL implies the KKL inequality at $p = 1/2$

`klo_DeltaUpgrade c` implies the KKL inequality `KKLHypercontractive (1/2) c`.

Formalized by `StatMech.Probability.klo_logOptimisation`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogOptimisation.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html#klo-log-optimisation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The edge-isoperimetric inequality and the logarithmic KKL reduction](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-edge-isoperimetric-inequality-and-the-logari)
