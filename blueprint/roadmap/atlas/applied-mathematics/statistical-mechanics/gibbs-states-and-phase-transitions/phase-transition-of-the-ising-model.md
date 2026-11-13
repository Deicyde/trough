---
declaration: section
origin: cited
lean: StatMech.Ising.spinBCF, StatMech.Ising.measurable_spin, StatMech.Ising.integrable_spin, StatMech.Ising.magnetization, StatMech.Ising.positiveMagnetizationSet, StatMech.Ising.betaC, StatMech.IsingFK.pup_exists_positive_magnetization, StatMech.FK.fkPc_lt_one_of_two_le
statement: formalized
proof: formalized
---

# Phase transition of the Ising model

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html).

## Spin at a site as a bounded continuous function

The spin at `x` as a bounded continuous real function on the configuration space.

Formalized by `StatMech.Ising.spinBCF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/MagNonneg.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/MagNonneg.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#spin-bcf).

## Measurability of the spin at a site

The spin at a site is a measurable function of the configuration.

Formalized by `StatMech.Ising.measurable_spin`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#measurable-spin).

## Integrability of the spin at a site under finite measures

The spin at a site is integrable for every finite measure.

Formalized by `StatMech.Ising.integrable_spin`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#integrable-spin).

## Spontaneous magnetization of the Ising model

The spontaneous magnetization `m*(β) = ⟨σ_0⟩⁺_β`: the expected spin at the origin under the
zero-field plus state.

Formalized by `StatMech.Ising.magnetization`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#magnetization).

## Inverse temperatures with positive spontaneous magnetization

The set of inverse temperatures `β ≥ 0` at which the spontaneous magnetization is positive.

Formalized by `StatMech.Ising.positiveMagnetizationSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#positive-magnetization-set).

## Critical inverse temperature from spontaneous magnetization

The critical inverse temperature `β_c(d) = inf {β ≥ 0 | m*(β) > 0}` (equal to `0` if the set is
empty, by the convention `sInf ∅ = 0`).

Formalized by `StatMech.Ising.betaC`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Magnetization.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#beta-c).

## Peierls' theorem

The two-dimensional Ising model has positive spontaneous magnetization at
some inverse temperature (Peierls, *On Ising's model of ferromagnetism*, 1936; Griffiths, Phys.
Rev. 136 (1964)).

Formalized by `StatMech.IsingFK.pup_exists_positive_magnetization`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperPeierls.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperPeierls.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#pup-exists-positive-magnetization).

## FK critical point is less than one for $d \ge 2$, $q \ge 1$

The FK critical point satisfies `p_c(d, q) < 1` for `d ≥ 2` and `q ≥ 1` (Grimmett, *The
Random-Cluster Model*, Theorem 5.5).

Formalized by `StatMech.FK.fkPc_lt_one_of_two_le`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#fk-pc-lt-one-of-two-le).

## Existence of the Ising phase transition

**Existence of the Ising phase transition** in dimension `d ≥ 2`: there is `β_c > 0` such that
the spontaneous magnetization vanishes for `0 < β < β_c` and is positive for `β > β_c` (Peierls,
1936; Griffiths, Phys. Rev. 136 (1964); Duminil-Copin, *Lectures on the Ising and Potts models
on the hypercubic lattice*, 2017). The statement says nothing about `β = β_c`.

Formalized by `StatMech.IsingFK.ising_phase_transition_of_two_le`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#ising-phase-transition-of-two-le).

## Sup-based $\beta_c$ equals $-\tfrac{1}{2}\log(1 - p_c)$ for $d \ge 2$

The sup-based critical inverse temperature `IsingFK.betaC (magnetization d)` in dimension
`d ≥ 2` is `-(1/2) log (1 - p_c(d, 2))`, the image of the FK critical point. This is the
supremum of the zero-magnetization inverse temperatures, not yet the public
`Ising.betaC d` (see `ising_betaC_eq_sup_betaC_of_two_le` for the bridge).

Formalized by `StatMech.IsingFK.isingFK_betaC_eq_fkPc_of_two_le`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#ising-fk-beta-c-eq-fk-pc-of-two-le).

## Inf-based and sup-based Ising critical points agree for $d \ge 2$

Bridge between the two critical-point definitions: the public
`Ising.betaC d = sInf {β ≥ 0 | m*(β) > 0}` equals the sup-based
`IsingFK.betaC (magnetization d) = sSup {β > 0 | m*(β) = 0}` in dimension `d ≥ 2`.
The `β = 0` case is not covered by the phase-transition statement (which only speaks
about `β > 0`), so it is settled separately: `φ_0({0}) = tanh 0 * … = 0 < 1`, hence
the plus-state two-point function at `β = 0` is summable, hence `m*(0) = 0`.

Formalized by `StatMech.IsingFK.ising_betaC_eq_sup_betaC_of_two_le`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#ising-beta-c-eq-sup-beta-c-of-two-le).

## Inf-based $\beta_c$ equals $-\tfrac{1}{2}\log(1 - p_c)$ for $d \ge 2$

The public Ising critical inverse temperature `Ising.betaC d` in dimension `d ≥ 2` is
`-(1/2) log (1 - p_c(d, 2))`, the image of the FK critical point. This is the form
usable with `ising_sharp_phase_transition`, whose `β_c` is `Ising.betaC d`.

Formalized by `StatMech.IsingFK.isingBetaC_eq_fkPc_of_two_le`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean, line 648](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/PcUpperAllDimensions.lean#L648). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html#ising-beta-c-eq-fk-pc-of-two-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Phase transition of the Ising model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/phase-transition-of-the-ising-model)
