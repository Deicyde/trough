---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_Z, StatMech.Onsager.ons_X, StatMech.Onsager.ons_hte
statement: formalized
proof: formalized
---

# High-temperature expansion of the Ising partition function

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/high-temperature-expansion-of-the-ising-partitio/index.html).

## Zero-field Ising partition function with unit couplings

The zero-field Ising partition function of `G` with unit couplings at inverse temperature `β`.

Formalized by `StatMech.Onsager.ons_Z`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/HighTemp.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/HighTemp.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/high-temperature-expansion-of-the-ising-partitio/index.html#ons-z).

## Even-subgraph generating function of a graph

The even-subgraph generating function `∑_F x^|F|` of `G`, over edge sets `F` in which every
vertex has even degree.

Formalized by `StatMech.Onsager.ons_X`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/HighTemp.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/HighTemp.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/high-temperature-expansion-of-the-ising-partitio/index.html#ons-x).

## High-temperature expansion

**High-temperature expansion** (van der Waerden 1941). `Z(β) = 2^|V| (cosh β)^|E| X(tanh β)` for
the zero-field Ising model on a finite graph (B. L. van der Waerden, *Die lange Reichweite der
regelmässigen Atomanordnung in Mischkristallen*, 1941).

Formalized by `StatMech.Onsager.ons_hte`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/HighTemp.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Onsager/HighTemp.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/high-temperature-expansion-of-the-ising-partitio/index.html#ons-hte).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: High-temperature expansion of the Ising partition function](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/high-temperature-expansion-of-the-ising-partitio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/high-temperature-expansion-of-the-ising-partitio)
