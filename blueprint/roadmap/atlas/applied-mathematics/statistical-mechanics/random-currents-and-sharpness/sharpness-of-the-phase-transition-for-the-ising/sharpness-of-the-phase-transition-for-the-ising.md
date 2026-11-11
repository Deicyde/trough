---
declaration: section
origin: cited
lean: StatMech.Sharpness.tildeBetaCIsing_pos, StatMech.Sharpness.ising_sharp_phase_transition
statement: formalized
proof: formalized
---

# Sharpness of the phase transition for the Ising model on ℤ^d

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/sharpness-of-the-phase-transition-for-the-ising/index.html).

## B. The auxiliary critical point

## Auxiliary critical point $\tilde\beta_c(d)$ is positive for $d \ge 2$

For `d ≥ 2` the auxiliary critical point `β̃_c(d)` is positive: `φ_β({0}) ≤ 2dβ < 1` for small
`β`.

Formalized by `StatMech.Sharpness.tildeBetaCIsing_pos`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingSharpnessTheorem.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingSharpnessTheorem.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/sharpness-of-the-phase-transition-for-the-ising/index.html#tilde-beta-cising-pos).

## Sharpness of the Ising phase transition on $\mathbb{Z}^d$, $d \ge 2$

Sharpness of the phase transition for the Ising model on `ℤ^d`, `d ≥ 2`: for `β ≥ β_c`, `m*(β) ≥
√(1 - (β_c/β)²)`; for `0 ≤ β < β_c`, the plus-state two-point function `z ↦ ⟨σ_0σ_z⟩^+_β` is
summable and decays as `exp(-c‖z‖₁)`. Reference: H. Duminil-Copin, V. Tassion, "A new proof of the
sharpness of the phase transition for Bernoulli percolation and the Ising model", Comm. Math. Phys.
343 (2016) 725–745, Theorem 1.2; first proved in M. Aizenman, D. J. Barsky, R. Fernández, "The phase
transition in a general class of Ising-type models is sharp", J. Stat. Phys. 47 (1987) 343–374.
Scope: `β_c` is `Ising.betaC d`, the infimum of the inverse temperatures with positive spontaneous
magnetization, and distance is the `ℓ¹` distance (equivalent to the Euclidean one up to constants).
The statement does not include `0 < β_c < ∞`; positivity follows from `tildeBetaCIsing_pos` and the
identification `β_c = β̃_c` in the proof, finiteness from the Peierls transition.

Formalized by `StatMech.Sharpness.ising_sharp_phase_transition`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingSharpnessTheorem.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/IsingSharpnessTheorem.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/sharpness-of-the-phase-transition-for-the-ising/index.html#ising-sharp-phase-transition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sharpness of the phase transition for the Ising model on ℤ^d](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/sharpness-of-the-phase-transition-for-the-ising/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/sharpness-of-the-phase-transition-for-the-ising)
