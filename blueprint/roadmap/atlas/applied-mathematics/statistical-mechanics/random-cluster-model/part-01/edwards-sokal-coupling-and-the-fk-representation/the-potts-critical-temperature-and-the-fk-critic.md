---
declaration: section
origin: cited
lean: StatMech.IsingFK.pToBeta, StatMech.IsingFK.betaToP, StatMech.IsingFK.pToBeta_two_eq_betaOfP, StatMech.IsingFK.betaToP_two_eq_pOfBeta, StatMech.IsingFK.betaC, StatMech.IsingFK.isingBetaC
statement: formalized
proof: formalized
---

# The Potts critical temperature and the FK critical parameter

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html).

## A. The FK parametrization

## Potts inverse temperature of an FK edge parameter

The Potts inverse temperature `-((q - 1)/q) log (1 - p)` corresponding to the FK edge parameter
`p`.

Formalized by `StatMech.IsingFK.pToBeta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html#p-to-beta).

## FK edge parameter of a Potts inverse temperature

The FK edge parameter `1 - e^{-qβ/(q-1)}` of the `q`-state Potts model at inverse temperature
`β`.

Formalized by `StatMech.IsingFK.betaToP`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html#beta-to-p).

## Inverse-temperature map of the Potts model at $q = 2$ is the Ising map

At `q = 2` the general parametrization `pToBeta` is `betaOfP`.

Formalized by `StatMech.IsingFK.pToBeta_two_eq_betaOfP`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html#p-to-beta-two-eq-beta-of-p).

## FK edge-parameter map of the Potts model at $q = 2$ is the Ising map

At `q = 2` the general parametrization `betaToP` is `pOfBeta`.

Formalized by `StatMech.IsingFK.betaToP_two_eq_pOfBeta`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html#beta-to-p-two-eq-p-of-beta).

## Critical inverse temperature of a magnetization curve

The critical inverse temperature `sup {β > 0 : m*(β) = 0}` of a spontaneous-magnetization curve
`m*`. See also `Ising.betaC`, the infimum of the inverse temperatures with positive
magnetization.

Formalized by `StatMech.IsingFK.betaC`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html#beta-c).

## Critical inverse temperature of the $d$-dimensional Ising model

The critical inverse temperature of the `d`-dimensional Ising model, `sup {β > 0 : m*(β) =
0}`.

Formalized by `StatMech.IsingFK.isingBetaC`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/BetacPc.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html#ising-beta-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Potts critical temperature and the FK critical parameter](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-potts-critical-temperature-and-the-fk-critic)
