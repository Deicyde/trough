---
declaration: section
origin: cited
lean: StatMech.IsingFK.toIsing, StatMech.IsingFK.betaOfP, StatMech.IsingFK.pOfBeta
statement: formalized
proof: formalized
---

# The Ising model as the two-state Potts model

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-as-the-two-state-potts-model/index.html).

## A. Ising configurations as two-state Potts colorings

## Ising configuration of a two-state Potts coloring

The Ising configuration of a two-state Potts coloring, via `Fin 2 ≃ Bool`.

Formalized by `StatMech.IsingFK.toIsing`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Q2.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Q2.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-as-the-two-state-potts-model/index.html#to-ising).

## Ising inverse temperature of an FK edge parameter

The Ising inverse temperature `-(1/2) log (1 - p)` corresponding to the FK edge parameter `p`.
See also `pToBeta` for general `q` (`pToBeta_two_eq_betaOfP`).

Formalized by `StatMech.IsingFK.betaOfP`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Q2.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Q2.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-as-the-two-state-potts-model/index.html#beta-of-p).

## FK edge parameter of an Ising inverse temperature

The FK edge parameter `p = 1 - e^{-2β}` of the Ising model at inverse temperature `β`. See also
`betaToP` for general `q` (`betaToP_two_eq_pOfBeta`).

Formalized by `StatMech.IsingFK.pOfBeta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Q2.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Q2.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-as-the-two-state-potts-model/index.html#p-of-beta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Ising model as the two-state Potts model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-as-the-two-state-potts-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-as-the-two-state-potts-model)
