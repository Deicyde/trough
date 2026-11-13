---
declaration: section
origin: cited
lean: StatMech.Ising.spin, StatMech.Ising.bond, StatMech.Ising.bond_eq_pm, StatMech.Ising.hamiltonian, StatMech.Ising.isingWeight, StatMech.Ising.isingZ, StatMech.Ising.isingZ_pos, StatMech.Ising.isingProb
statement: formalized
proof: formalized
---

# The finite-volume Ising Gibbs measure

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html).

## A. Spins and bonds

## Spin of a configuration at a site

The spin `σ_x ∈ {1, -1}` of the configuration `s` at `x`: `1` for `true`, `-1` for `false`.

Formalized by `StatMech.Ising.spin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#spin).

## Bond variable of an unordered pair

The bond variable `σ_x σ_y` of an unordered pair `e = {x, y}`.

Formalized by `StatMech.Ising.bond`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#bond).

## Bond variable takes values $\pm 1$

A bond variable is `1` or `-1`.

Formalized by `StatMech.Ising.bond_eq_pm`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#bond-eq-pm).

## Ising Hamiltonian on a finite graph

The Ising Hamiltonian `H(s) = -∑_{xy ∈ E(G)} σ_x σ_y - h ∑_x σ_x` on a finite graph `G` with
unit coupling and external field `h`. See also `CondensedMatter.IsingModel.energy` and
`StatMech.Ising.hamiltonian_eq_energy`.

Formalized by `StatMech.Ising.hamiltonian`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#hamiltonian).

## Boltzmann weight of an Ising configuration

The Boltzmann weight `exp (-β H(s))` of a configuration at inverse temperature `β`.

Formalized by `StatMech.Ising.isingWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#ising-weight).

## Ising partition function

The partition function `Z = ∑_s exp (-β H(s))`. See also
`CanonicalEnsemble.mathematicalPartitionFunction` and
`StatMech.Ising.isingZ_eq_mathematicalPartitionFunction`.

Formalized by `StatMech.Ising.isingZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#ising-z).

## Positivity of the Ising partition function

The partition function is positive.

Formalized by `StatMech.Ising.isingZ_pos`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#ising-z-pos).

## Gibbs probability of an Ising configuration

The Gibbs probability `exp (-β H(s)) / Z` of a configuration. See also
`CanonicalEnsemble.probability` and `StatMech.Ising.isingProb_eq_probability`.

Formalized by `StatMech.Ising.isingProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#ising-prob).

## Ising Gibbs probabilities sum to one

The Gibbs probabilities sum to one.

Formalized by `StatMech.Ising.isingProb_sum_eq_one`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#ising-prob-sum-eq-one).

## Finite-volume Ising Gibbs probability mass function

The finite-volume Ising Gibbs distribution as a probability mass function on configurations.

Formalized by `StatMech.Ising.isingPMF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Gibbs.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html#ising-pmf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The finite-volume Ising Gibbs measure](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/the-finite-volume-ising-gibbs-measure)
