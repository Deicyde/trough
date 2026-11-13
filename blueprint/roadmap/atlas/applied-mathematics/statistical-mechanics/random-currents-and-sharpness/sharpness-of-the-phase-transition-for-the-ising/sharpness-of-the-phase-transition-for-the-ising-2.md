---
declaration: section
origin: cited
lean: StatMech.Sharpness.IsingSharp.ising_sharpness
statement: formalized
proof: formalized
---

# Sharpness of the phase transition for the Ising model: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/index.html).

## Abstract form of the sharpness theorem

Abstract form of the sharpness theorem: a magnetization satisfying the mean-field differential
inequality above `β_c` obeys `m(β) ≥ √(1 - (β_c/β)²)`, and correlations satisfying Simon's
self-consistent bound with `φ < 1` are summable with sum at most `|S|/(1 - φ)`. The hypotheses are
inputs; the unconditional statement is `ising_sharp_phase_transition`.

Formalized by `StatMech.Sharpness.IsingSharp.ising_sharpness`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/AbstractSharpness.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/AbstractSharpness.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/index.html#ising-sharpness).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sharpness of the phase transition for the Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/sharpness-of-the-phase-transition-for-the-ising)
