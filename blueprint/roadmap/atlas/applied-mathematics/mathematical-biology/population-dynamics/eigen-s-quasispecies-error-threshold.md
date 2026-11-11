---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.Quasispecies.masterField, MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium, MathlibExt.Biology.Dynamics.Quasispecies.masterField_eq, MathlibExt.Biology.Dynamics.Quasispecies.masterField_eq_zero_iff, MathlibExt.Biology.Dynamics.Quasispecies.one_sub_masterEquilibrium, MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium_pos_iff, MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium_le_one, MathlibExt.Biology.Dynamics.Quasispecies.one_lt_mul_pow_iff
statement: formalized
proof: formalized
---

# Eigen's quasispecies error threshold

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html).

## Master-sequence vector field of the single-peak quasispecies

The master-sequence vector field of the single-peak quasispecies without back mutation:
`x' = σ Q x - (σ x + (1 - x)) x`, where `σ` is the master fitness relative to the mutants and
`Q` the probability of an error-free copy. Meaningful for `σ > 1`, `0 ≤ Q ≤ 1`,
`0 ≤ x ≤ 1`; it is a polynomial and is defined for all reals.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterField`, a definition declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-field).

## Interior equilibrium of the master-sequence frequency

The interior equilibrium `x* = (σ Q - 1) / (σ - 1)` of the master frequency. For
`σ = 1` (no selective advantage) Lean's `x / 0 = 0` gives the junk value `0`; every result
below assumes `1 < σ`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium`, a definition declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-equilibrium).

## Master-sequence equation is logistic

The master-sequence equation is logistic: `x' = x ((σ Q - 1) - (σ - 1) x)`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterField_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-field-eq).

## Equilibria of the master-sequence frequency

The equilibria of the master frequency are `0` and `x* = (σ Q - 1)/(σ - 1)`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterField_eq_zero_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-field-eq-zero-iff).

## Mutant frequency at the interior equilibrium

The mutant frequency at the interior equilibrium is `1 - x* = σ (1 - Q)/(σ - 1)`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.one_sub_masterEquilibrium`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#one-sub-master-equilibrium).

## Error threshold

For `σ > 1`, the interior equilibrium is positive iff `σ Q > 1`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium_pos_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-equilibrium-pos-iff).

## Interior quasispecies equilibrium is at most 1

For `σ > 1` and `Q ≤ 1` the interior equilibrium is at most `1`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium_le_one`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-equilibrium-le-one).

## Maximal genome length

For per-site fidelity `0 < q < 1` and `σ > 0`,
`σ q ^ L > 1` iff `L < log σ / (-log q)`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.one_lt_mul_pow_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#one-lt-mul-pow-iff).

## Continuity of the interior equilibrium in the copying fidelity

The interior equilibrium depends continuously on `Q`, so any sequence of fidelities with
`Q_L → Qlim` has `x*(Q_L) → x*(Qlim)`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.tendsto_masterEquilibrium`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#tendsto-master-equilibrium).

## Fixed-`q_L` limit

With per-site fidelity `q_L = 1 - μ / L`, so that the expected number
of mutations per genome copy is `μ`, the error-free probability is `q_L ^ L → e^{-μ}` and the
master equilibrium converges to `(σ e^{-μ} - 1)/(σ - 1)`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.tendsto_masterEquilibrium_fidelity`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#tendsto-master-equilibrium-fidelity).

## Eigen's error threshold

In the fixed-`q_L` limit the master sequence persists iff `μ < log σ`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.masterEquilibrium_exp_pos_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#master-equilibrium-exp-pos-iff).

## Convergence above the threshold

If `σ > 1`, `σ Q > 1` and `x` solves the master
equation on `[0, ∞)` from a positive master frequency, then `x t → x*`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.tendsto_master_of_one_lt`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#tendsto-master-of-one-lt).

## Loss of the master at or below the threshold

If `σ > 1`, `σ Q ≤ 1` and `x` solves the
master equation on `[0, ∞)` from a positive master frequency, then `x t → 0`.

Formalized by `MathlibExt.Biology.Dynamics.Quasispecies.tendsto_master_zero_of_le_one`, a theorem declared in [MathlibExt/Biology/Dynamics/Quasispecies.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Quasispecies.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html#tendsto-master-zero-of-le-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eigen's quasispecies error threshold](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-dynamics/eigen-s-quasispecies-error-threshold)
