---
declaration: section
origin: cited
lean: StatMech.Percolation.crossProbReal, StatMech.Percolation.tildePc_eq_pc, StatMech.Percolation.sharpness
statement: formalized
proof: formalized
---

# Sharpness of the phase transition, assuming its two analytic inputs

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-assuming-its-t/index.html).

## One-arm probability as a function of a real density

The one-arm probability `crossProb d t n` as a function of a real density `t` (`0` outside
`[0, 1]`).

Formalized by `StatMech.Percolation.crossProbReal`, a definition declared in [MathlibExt/Probability/Percolation/SharpnessFromInputs.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessFromInputs.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-assuming-its-t/index.html#cross-prob-real).

## Equality of the Duminil-Copin–Tassion threshold and $p_c$

`p̃_c = p_c`, assuming exponential decay on `tildePcSet`, `θ(1) ≠ 0`, and `θ(q) > 0` for
`p̃_c < q < 1`.

Formalized by `StatMech.Percolation.tildePc_eq_pc`, a theorem declared in [MathlibExt/Probability/Percolation/SharpnessFromInputs.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessFromInputs.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-assuming-its-t/index.html#tilde-pc-eq-pc).

## Sharpness of the phase transition, conditional form

Sharpness of the phase transition, **conditional form**: from `p̃_c > 0`, `θ(1) ≠ 0`,
exponential decay of the one-arm probability on `tildePcSet`, and the Duminil-Copin–Tassion
differential inequality on `(p̃_c, q)` (with continuity and derivative hypotheses), conclude
`p̃_c = p_c`, exponential decay on `tildePcSet`, and `θ(q) ≥ (q - p̃_c)/(q(1 - p̃_c))` for
`p̃_c < q < 1`. The hypotheses are discharged in `sharp_phase_transition`.

Formalized by `StatMech.Percolation.sharpness`, a theorem declared in [MathlibExt/Probability/Percolation/SharpnessFromInputs.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/SharpnessFromInputs.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-assuming-its-t/index.html#sharpness).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sharpness of the phase transition, assuming its two analytic inputs](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-assuming-its-t/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/sharpness/sharpness-of-the-phase-transition-assuming-its-t)
