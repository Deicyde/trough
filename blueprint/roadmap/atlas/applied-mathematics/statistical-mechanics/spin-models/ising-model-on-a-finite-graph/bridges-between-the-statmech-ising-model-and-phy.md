---
declaration: section
origin: cited
lean: StatMech.Ising.spinB_eq_isingModelSpin, StatMech.Ising.two_mul_sum_bond, StatMech.Ising.hamiltonian_eq_energy, StatMech.Ising.canonicalEnsemble, StatMech.Ising.isingZ_eq_mathematicalPartitionFunction, StatMech.Ising.isingProb_eq_probability, StatMech.natAbs_sum_eq_one_iff, StatMech.hypercubicLatticeIsoCrystal
statement: formalized
proof: formalized
---

# Bridges between the StatMech Ising model and Physlib

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html).

## A. The Hamiltonian as Physlib's Ising energy

## Boolean spin agrees with Physlib's Ising spin

The Boolean spin value `spinB` is Physlib's `CondensedMatter.IsingModel.spin`.

Formalized by `StatMech.Ising.spinB_eq_isingModelSpin`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#spin-b-eq-ising-model-spin).

## Edge bond sum is half the sum over ordered adjacent pairs

The edge sum of `bond s` is half the sum of `σ_x σ_y` over ordered adjacent pairs.

Formalized by `StatMech.Ising.two_mul_sum_bond`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#two-mul-sum-bond).

## Hamiltonian agrees with Physlib's Ising energy

The Hamiltonian `hamiltonian G h` is Physlib's Ising energy
`CondensedMatter.IsingModel.energy` of the model with coupling `J = 1` and field `h`, on the region
of all vertices.

Formalized by `StatMech.Ising.hamiltonian_eq_energy`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#hamiltonian-eq-energy).

## Ising model as a Physlib canonical ensemble

The Ising model on a finite graph `G` with field `h`, as Physlib's finite canonical ensemble:
microstates are spin configurations, the energy is `hamiltonian G h`, and the measure is the
counting measure.

Formalized by `StatMech.Ising.canonicalEnsemble`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#canonical-ensemble).

## Ising partition function agrees with Physlib's partition function

The Ising partition function at inverse temperature `T.β` is Physlib's mathematical partition
function of `canonicalEnsemble G h` at temperature `T`.

Formalized by `StatMech.Ising.isingZ_eq_mathematicalPartitionFunction`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#ising-z-eq-mathematical-partition-functi).

## Ising Gibbs probability agrees with Physlib's canonical probability

The Ising Gibbs probability at inverse temperature `T.β` is Physlib's canonical probability of
`canonicalEnsemble G h` at temperature `T`.

Formalized by `StatMech.Ising.isingProb_eq_probability`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#ising-prob-eq-probability).

## Sites at $\ell^1$ distance one are those differing by a unit vector

Two sites of `ℤ^d` are at `ℓ¹` distance one exactly when they differ by a unit vector.

Formalized by `StatMech.natAbs_sum_eq_one_iff`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#nat-abs-sum-eq-one-iff).

## Isomorphism of the hypercubic lattice with Physlib's crystal graph

The nearest-neighbour graph `hypercubicLattice d` on `ℤ^d` is isomorphic to the bond graph of
Physlib's hypercubic crystal `CondensedMatter.Crystal.hypercubicGraph d`, by sending `x` to the
site in cell `x`.

Formalized by `StatMech.hypercubicLatticeIsoCrystal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PhyslibBridge.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html#hypercubic-lattice-iso-crystal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bridges between the StatMech Ising model and Physlib](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/bridges-between-the-statmech-ising-model-and-phy)
