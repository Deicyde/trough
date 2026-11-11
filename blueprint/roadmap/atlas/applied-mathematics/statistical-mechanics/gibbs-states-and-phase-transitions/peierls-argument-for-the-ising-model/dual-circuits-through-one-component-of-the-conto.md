---
declaration: section
origin: cited
lean: StatMech.Lattice.componentSupport, StatMech.Lattice.componentGraph, StatMech.Lattice.TightAxisCircuitData
statement: formalized
proof: formalized
---

# Dual circuits through one component of the contour

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-through-one-component-of-the-conto/index.html).

## A. The component graph of a face

## Faces of a set reachable from a face in the face-boundary graph

The faces of `T` reachable from `f` in the face-boundary graph of `K`.

Formalized by `StatMech.Lattice.componentSupport`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ComponentEulerCircuit.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Peierls/ComponentEulerCircuit.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-through-one-component-of-the-conto/index.html#component-support).

## Component of a face in the face-boundary graph

The connected component of the face `f` in the face-boundary graph of `K`, as a graph on all
faces.

Formalized by `StatMech.Lattice.componentGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ComponentEulerCircuit.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Peierls/ComponentEulerCircuit.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-through-one-component-of-the-conto/index.html#component-graph).

## Tight axis circuit data: contour edges in one axis-face component

Every realised contour of length `ℓ` in `Λ_n ⊆ ℤ²` is the contour of a cluster whose
face-boundary graph has all its edges in the component of an axis face `(j, 0)` with `j < ℓ`.

Formalized by `StatMech.Lattice.TightAxisCircuitData`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ComponentEulerCircuit.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Peierls/ComponentEulerCircuit.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-through-one-component-of-the-conto/index.html#tight-axis-circuit-data).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dual circuits through one component of the contour](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-through-one-component-of-the-conto/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-through-one-component-of-the-conto)
