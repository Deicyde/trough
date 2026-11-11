---
declaration: section
origin: cited
lean: StatMech.Ising.isingCfgEquiv, StatMech.Ising.isingSumConfigEquiv
statement: formalized
proof: formalized
---

# Ising model on a finite graph: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/index.html).

## Configuration equivalence induced by a vertex relabeling

The equivalence of configuration spaces induced by a vertex equivalence `σ : V ≃ W`: `ω ↦ ω ∘
σ`.

Formalized by `StatMech.Ising.isingCfgEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FiniteVolumeRelabel.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FiniteVolumeRelabel.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/index.html#ising-cfg-equiv).

## Configurations on a disjoint union as pairs of configurations

The equivalence between configurations on `V ⊕ W` and pairs of configurations on `V` and `W`.

Formalized by `StatMech.Ising.isingSumConfigEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FiniteVolumeSum.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/FiniteVolumeSum.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/index.html#ising-sum-config-equiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ising model on a finite graph](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/spin-models/ising-model-on-a-finite-graph)
