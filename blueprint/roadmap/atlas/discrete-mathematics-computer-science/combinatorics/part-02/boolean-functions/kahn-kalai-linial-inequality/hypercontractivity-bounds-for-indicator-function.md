---
declaration: section
origin: cited
lean: StatMech.Probability.kls_fluctWeight_le_pow, StatMech.Probability.kls_var_le_W, StatMech.Probability.kls_LogOptimisation, StatMech.Probability.kls_logOptimisation_zero, StatMech.Probability.kls_logOptimisation_implies_step, StatMech.Probability.kls_logSobolevStep
statement: formalized
proof: formalized
---

# Hypercontractivity bounds for indicator functions

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html).

## Bonami–Beckner bound for indicator functions

Bonami–Beckner for an indicator of uniform measure `m`: `∑_{S ≠ ∅} ρ^{2|S|} f̂(S)² ≤
 m^{2/(1+ρ²)} - m²` for `0 ≤ ρ ≤ 1`.

Formalized by `StatMech.Probability.kls_fluctWeight_le_pow`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html#kls-fluct-weight-le-pow).

## Poincaré inequality in Fourier form

Poincaré inequality in Fourier form: `∑_{S ≠ ∅} f̂(S)² ≤ ∑_S 4 |S| f̂(S)²`.

Formalized by `StatMech.Probability.kls_var_le_W`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html#kls-var-le-w).

## Fourier-form KKL inequality given the indicator Bonami–Beckner bound

The KKL inequality at `p = 1/2` in Fourier form, with the indicator hypercontractive bound `∑_{S
 ≠ ∅} ρ^{2|S|} f̂(S)² ≤ m^{2/(1+ρ²)} - m²` (for all `ρ ∈ [0, 1]`) as a hypothesis, where `f =
 1_φ` and `m = 𝔼 f`. The hypothesis always holds (`kls_fluctWeight_le_pow`).

Formalized by `StatMech.Probability.kls_LogOptimisation`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html#kls-log-optimisation).

## Indicator-bound form of KKL with constant 0 holds trivially

`kls_LogOptimisation 0` holds trivially.

Formalized by `StatMech.Probability.kls_logOptimisation_zero`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html#kls-log-optimisation-zero).

## Indicator-bound form of KKL implies the hypercontractive form

`kls_LogOptimisation c` implies `khc_LogSobolevStep c`.

Formalized by `StatMech.Probability.kls_logOptimisation_implies_step`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html#kls-log-optimisation-implies-step).

## Indicator-bound form of KKL implies the KKL inequality at $p = 1/2$

`kls_LogOptimisation c` implies the KKL inequality `KKLHypercontractive (1/2) c`.

Formalized by `StatMech.Probability.kls_logSobolevStep`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/KKL/KKLLogSobolev.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html#kls-log-sobolev-step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypercontractivity bounds for indicator functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/hypercontractivity-bounds-for-indicator-function)
