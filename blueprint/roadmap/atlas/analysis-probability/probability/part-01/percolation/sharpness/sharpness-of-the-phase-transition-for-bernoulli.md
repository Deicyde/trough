---
declaration: section
origin: cited
lean: StatMech.Percolation.tildePc_pos, StatMech.Percolation.lineWord, StatMech.Percolation.crossProb_exp_decay_of_mem_tildePcSet, StatMech.Percolation.sharp_phase_transition
statement: formalized
proof: formalized
---

# Sharpness of the phase transition for Bernoulli bond percolation on ℤ^d

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli/index.html).

## Positivity of the Duminil-Copin–Tassion threshold

`p̃_c(d) > 0` for `d ≥ 1`: at `p = 1/(4d + 1)`, `φ_p({0}) ≤ 2dp < 1`.

Formalized by `StatMech.Percolation.tildePc_pos`, a theorem declared in [MathlibExt/Probability/Percolation/SharpnessTheorem.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessTheorem.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli/index.html#tilde-pc-pos).

## Straight path along the first coordinate axis

The direction sequence of the straight path from the origin along the first coordinate axis.

Formalized by `StatMech.Percolation.lineWord`, a definition declared in [MathlibExt/Probability/Percolation/SharpnessTheorem.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessTheorem.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli/index.html#line-word).

## Exponential decay of the one-arm probability below the threshold

Exponential decay of the one-arm probability for every `p ∈ tildePcSet d`, i.e. every `p`
admitting a finite `S ∋ 0` with `φ_p(S) < 1`.

Formalized by `StatMech.Percolation.crossProb_exp_decay_of_mem_tildePcSet`, a theorem declared in [MathlibExt/Probability/Percolation/SharpnessTheorem.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessTheorem.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli/index.html#cross-prob-exp-decay-of-mem-tilde-pc-set).

## Sharpness of the phase transition

**Sharpness of the phase transition** for Bernoulli bond percolation on `ℤ^d`, `d ≥ 1`
(Duminil-Copin–Tassion 2016; Aizenman–Barsky 1987; Menshikov 1986):

1. `p̃_c = p_c`;
2. for every `p ∈ tildePcSet d` (a finite `S ∋ 0` has `φ_p(S) < 1`),
   `ℙ_p(0 ↔ ℤ^d \ Λ_{n-1}) ≤ C e^{-cn}` for some `c, C > 0`;
3. `θ(q) ≥ (q - p̃_c)/(q(1 - p̃_c))` for `p̃_c < q < 1`.

Scope of the items:
* Item 2 is stated on `tildePcSet d`, not on `[0, p_c)`: passing from `p < p̃_c` to
  `p ∈ tildePcSet d` needs monotonicity of `p ↦ φ_p(S)`, and passing from `p < p_c` to `θ(p) = 0`
  needs monotonicity of `θ`; neither is proved in MathlibExt (θ monotonicity is
  `theta_mono_parameter` in PhyslibExt `RandomCluster/PcUpperViaFK`).
* Item 3 is informative only when `p̃_c < 1`. This file does not prove that for any `d`; at `d = 1`
  it fails (`p̃_c = p_c = 1`) and item 3 is vacuous. For `d = 2`, `p_c < 1` is proved in PhyslibExt
  (`StatMech.Percolation.pc_two_lt_one_via_fk`), which with item 1 makes item 3 non-vacuous
  there.

Formalized by `StatMech.Percolation.sharp_phase_transition`, a theorem declared in [MathlibExt/Probability/Percolation/SharpnessTheorem.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessTheorem.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli/index.html#sharp-phase-transition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sharpness of the phase transition for Bernoulli bond percolation on ℤ^d](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-for-bernoulli)
