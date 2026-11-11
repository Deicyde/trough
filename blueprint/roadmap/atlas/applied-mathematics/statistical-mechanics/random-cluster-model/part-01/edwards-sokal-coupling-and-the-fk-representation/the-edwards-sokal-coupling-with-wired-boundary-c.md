---
declaration: section
origin: cited
lean: StatMech.IsingFK.BoundaryFixed, StatMech.IsingFK.pottsWeightWired, StatMech.IsingFK.pottsZWired, StatMech.IsingFK.pottsProbWired, StatMech.IsingFK.esWeightWired, StatMech.IsingFK.esZWired, StatMech.IsingFK.esWiredFirstMarginal, StatMech.IsingFK.wiredSub
statement: formalized
proof: formalized
---

# The Edwards–Sokal coupling with wired boundary conditions

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html).

## A. The Potts model with boundary color `b`

## Coloring fixed to a color on the boundary

The coloring `σ` equals `b` on every boundary vertex.

Formalized by `StatMech.IsingFK.BoundaryFixed`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#boundary-fixed).

## Potts weight with fixed boundary color

The Potts weight restricted to colorings with boundary color `b`.

Formalized by `StatMech.IsingFK.pottsWeightWired`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#potts-weight-wired).

## Potts partition function with fixed boundary color

The partition function of the Potts model with boundary color `b`.

Formalized by `StatMech.IsingFK.pottsZWired`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#potts-zwired).

## Potts Gibbs probability with fixed boundary color

The Gibbs probability of the Potts model with boundary color `b`.

Formalized by `StatMech.IsingFK.pottsProbWired`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#potts-prob-wired).

## Edwards–Sokal weight with fixed boundary color

The Edwards–Sokal weight restricted to colorings with boundary color `b`.

Formalized by `StatMech.IsingFK.esWeightWired`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#es-weight-wired).

## Total wired Edwards–Sokal weight

The total wired Edwards–Sokal weight.

Formalized by `StatMech.IsingFK.esZWired`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#es-zwired).

## Spin marginal of the wired Edwards–Sokal measure

The spin marginal of the wired Edwards–Sokal measure.

Formalized by `StatMech.IsingFK.esWiredFirstMarginal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#es-wired-first-marginal).

## Open-edge graph with a boundary clique

The graph of open edges of `ω` together with a clique on the boundary vertices.

Formalized by `StatMech.IsingFK.wiredSub`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#wired-sub).

## Coloring constant on the wired graph

The coloring `σ` is constant along the edges of `wiredSub`.

Formalized by `StatMech.IsingFK.ConstOnWired`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#const-on-wired).

## Colorings constant on wired clusters as cluster colorings

Colorings constant on the clusters of `wiredSub` correspond to colorings of those clusters.

Formalized by `StatMech.IsingFK.constOnWiredEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#const-on-wired-equiv).

## Functions pinned at a point as functions on its complement

Functions to `Fin q` taking the value `b` at `c₀` correspond to functions on the complement of
`c₀`. See also `Equiv.piSplitAt`.

Formalized by `StatMech.IsingFK.pinnedFunEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#pinned-fun-equiv).

## Bond marginal of the wired Edwards–Sokal measure

The bond marginal of the wired Edwards–Sokal measure.

Formalized by `StatMech.IsingFK.esWiredSecondMarginal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/EsWired.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html#es-wired-second-marginal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Edwards–Sokal coupling with wired boundary conditions](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-edwards-sokal-coupling-with-wired-boundary-c)
