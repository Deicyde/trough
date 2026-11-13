---
declaration: section
origin: cited
lean: StatMech.IsingFK.Compatible, StatMech.IsingFK.monoBool, StatMech.IsingFK.disagreeEdges, StatMech.IsingFK.coloring, StatMech.IsingFK.esJointProb
statement: formalized
proof: formalized
---

# Compatible colorings in the Edwards–Sokal coupling

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html).

## A. Compatible colorings

## Compatibility of a coloring with a bond configuration

A coloring `σ` is compatible with the bond configuration `ω` if every open edge of `G` joins
vertices of the same color. See also `FK.ConstOnOpen` (`compatible_iff_constOnOpen`).

Formalized by `StatMech.IsingFK.Compatible`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html#compatible).

## Monochromatic edge indicator

Whether an edge is monochromatic under the coloring `σ`.

Formalized by `StatMech.IsingFK.monoBool`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html#mono-bool).

## Edges with differently colored endpoints

The edges of `G` whose endpoints have different colors.

Formalized by `StatMech.IsingFK.disagreeEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html#disagree-edges).

## Vertex coloring induced by a coloring of open clusters

The coloring of the vertices obtained from a coloring `τ` of the open clusters of `ω`.

Formalized by `StatMech.IsingFK.coloring`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html#coloring).

## Edwards–Sokal joint probability

The joint Edwards–Sokal probability of the coloring `σ` and the bond configuration `ω`.

Formalized by `StatMech.IsingFK.esJointProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/Coloring.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html#es-joint-prob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Compatible colorings in the Edwards–Sokal coupling](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/compatible-colorings-in-the-edwards-sokal-coupli)
