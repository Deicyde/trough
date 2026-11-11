---
declaration: section
origin: cited
lean: StatMech.IsingFK.isingBond, StatMech.IsingFK.isingWiredWeight, StatMech.IsingFK.isingWiredZ, StatMech.IsingFK.isingWiredOnePoint, StatMech.IsingFK.bToF, StatMech.IsingFK.latToBox
statement: formalized
proof: formalized
---

# The Ising model in a box as a wired two-state Potts model

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html).

## A. The wired Ising model on a graph

## Ising bond variable of a two-state coloring

The Ising bond `σ_x σ_y` of a two-state coloring, with color `0` as spin `+1`. See also
`Ising.bond` for Boolean configurations.

Formalized by `StatMech.IsingFK.isingBond`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html#ising-bond).

## Ising weight of a coloring with plus boundary

The Ising weight `exp (β ∑_e σ_x σ_y)` of a two-state coloring with boundary color `0`, and `0`
otherwise.

Formalized by `StatMech.IsingFK.isingWiredWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html#ising-wired-weight).

## Plus-boundary Ising partition function on a graph

The partition function of the Ising model with `+` boundary condition on a graph.

Formalized by `StatMech.IsingFK.isingWiredZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html#ising-wired-z).

## Plus-boundary Ising one-point function on a graph

The one-point function `⟨σ_x⟩⁺` of the Ising model with `+` boundary condition on a graph.

Formalized by `StatMech.IsingFK.isingWiredOnePoint`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html#ising-wired-one-point).

## Two-state color of a Boolean spin

The two-state color of a Boolean spin: `true ↦ 0`, `false ↦ 1`.

Formalized by `StatMech.IsingFK.bToF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html#b-to-f).

## Box configuration as a coloring of the next larger box

A configuration in the box `Λ_n` as a two-state coloring of `Λ_{n+1}`, with color `0` (spin `+`)
outside `Λ_n`.

Formalized by `StatMech.IsingFK.latToBox`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/IsingBoxEncoding.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html#lat-to-box).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Ising model in a box as a wired two-state Potts model](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-ising-model-in-a-box-as-a-wired-two-state-po)
