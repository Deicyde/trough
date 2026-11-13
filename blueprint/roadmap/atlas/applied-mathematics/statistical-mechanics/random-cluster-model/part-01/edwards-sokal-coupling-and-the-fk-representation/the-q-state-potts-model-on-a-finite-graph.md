---
declaration: section
origin: cited
lean: StatMech.Potts.monoIndicator, StatMech.Potts.agreement, StatMech.Potts.pottsWeight, StatMech.Potts.pottsZ, StatMech.Potts.pottsProb, StatMech.Potts.pottsPMF
statement: formalized
proof: formalized
---

# The q-state Potts model on a finite graph

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html).

## A. Monochromatic edges

## Monochromatic-edge indicator

The indicator of a monochromatic edge: `𝟙[σ x = σ y]` on the unordered pair `s(x, y)`.

Formalized by `StatMech.Potts.monoIndicator`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html#mono-indicator).

## Agreement count of a spin configuration

The agreement count: the number of edges of `G` whose endpoints carry the same spin.

Formalized by `StatMech.Potts.agreement`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html#agreement).

## Potts Boltzmann weight

The Potts Boltzmann weight `exp (β J · agreement G σ)`.

Formalized by `StatMech.Potts.pottsWeight`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html#potts-weight).

## Potts partition function

The Potts partition function `Z = ∑_σ exp (β J · agreement G σ)`.

Formalized by `StatMech.Potts.pottsZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html#potts-z).

## Potts probability of a spin configuration

The Potts probability of the spin configuration `σ`.

Formalized by `StatMech.Potts.pottsProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html#potts-prob).

## Potts Gibbs measure as a probability mass function

The Potts Gibbs measure on `V → Fin q` as a probability mass function.

Formalized by `StatMech.Potts.pottsPMF`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/Potts.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html#potts-pmf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The q-state Potts model on a finite graph](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-q-state-potts-model-on-a-finite-graph)
