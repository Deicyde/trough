---
declaration: def
origin: cited
lean: FiniteGraphFreeGroup.graphTopologicalFundamentalGroupEquiv
statement: formalized
---

# Fundamental groups of finite connected graphs

> Constructs the standard interval-cell realization of a finite connected directed multigraph and proves that its topological fundamental group is a free group of rank E - V + 1. The proof uses an explicit spanning-tree basis and develops a verified path-lifting cover, a contraction of the covering tree, root-change equivalences, the tree/triviality criterion, and the corresponding free-abelian result.

*Quoted from the card [LeanPool/projects/finite-graph-fundamental-group.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/finite-graph-fundamental-group.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FiniteGraphFreeGroup.graphTopologicalFundamentalGroupEquiv`](https://leanpool.github.io/lean-pool/LeanPool/FiniteGraphFundamentalGroup/TopologicalComparison.html#FiniteGraphFreeGroup.graphTopologicalFundamentalGroupEquiv) (def; a main declaration), declared in [LeanPool/FiniteGraphFundamentalGroup/TopologicalComparison.lean, line 1747](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup/TopologicalComparison.lean#L1747): “For a finite weakly connected directed multigraph, the topological fundamental group of its interval-cell quotient realization at any vertex is explicitly isomorphic to the free group on E + 1 - V generators.”
- [`FiniteGraphFreeGroup.graphCombinatorialToTopologicalEquiv`](https://leanpool.github.io/lean-pool/LeanPool/FiniteGraphFundamentalGroup/TopologicalComparison.html#FiniteGraphFreeGroup.graphCombinatorialToTopologicalEquiv) (def), declared in [LeanPool/FiniteGraphFundamentalGroup/TopologicalComparison.lean, line 1738](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup/TopologicalComparison.lean#L1738): “The endomorphism group at a vertex in the graph's free groupoid is explicitly isomorphic to the topological fundamental group of the interval-cell realization.”
- [`FiniteGraphFreeGroup.graphCoverProjection_isCovering`](https://leanpool.github.io/lean-pool/LeanPool/FiniteGraphFundamentalGroup/Cover.html#FiniteGraphFreeGroup.graphCoverProjection_isCovering) (theorem), declared in [LeanPool/FiniteGraphFundamentalGroup/Cover.lean, line 135](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup/Cover.lean#L135): “The canonical path-lifting projection from rooted free-groupoid paths to graph vertices is a quiver covering, with bijective maps on every incoming and outgoing edge star.”
- [`FiniteGraphFreeGroup.graphRealization_tree_simplyConnected`](https://leanpool.github.io/lean-pool/LeanPool/FiniteGraphFundamentalGroup/TreeContraction.html#FiniteGraphFreeGroup.graphRealization_tree_simplyConnected) (theorem), declared in [LeanPool/FiniteGraphFundamentalGroup/TreeContraction.lean, line 402](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup/TreeContraction.lean#L402): “The interval-cell realization of a directed arborescence is simply connected, via an explicit continuous contraction to its root.”
- [`FiniteGraphFreeGroup.graphFundamentalGroup_subsingleton_iff_cycleRank_zero`](https://leanpool.github.io/lean-pool/LeanPool/FiniteGraphFundamentalGroup/Consequences.html#FiniteGraphFreeGroup.graphFundamentalGroup_subsingleton_iff_cycleRank_zero) (theorem), declared in [LeanPool/FiniteGraphFundamentalGroup/Consequences.lean, line 160](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup/Consequences.lean#L160): “The combinatorial fundamental group is trivial exactly when the graph's cycle rank E + 1 - V is zero.”
- [`FiniteGraphFreeGroup.graphFundamentalGroupFreeAbelianizationEquiv`](https://leanpool.github.io/lean-pool/LeanPool/FiniteGraphFundamentalGroup/Consequences.html#FiniteGraphFreeGroup.graphFundamentalGroupFreeAbelianizationEquiv) (def), declared in [LeanPool/FiniteGraphFundamentalGroup/Consequences.lean, line 197](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup/Consequences.lean#L197): “The additive abelianization of the graph fundamental group is the free abelian group on E + 1 - V generators.”

## Project

- Authors: Arthur Freitas Ramos, David Hulak, Ruy de Queiroz.
- Source: *Algebraic Topology, Additional Topic 1.A: Graphs and Free Groups* by Allen Hatcher, [https://pi.math.cornell.edu/~hatcher/AT/AT.pdf](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
- Project repository: [Arthur742Ramos/finite-graph-fundamental-group](https://github.com/Arthur742Ramos/finite-graph-fundamental-group), at commit [dd57e3ab](https://github.com/Arthur742Ramos/finite-graph-fundamental-group/tree/dd57e3ab8bc5a7042fcc5498e778b008d87ac032).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C25, 55Q05, 20F65.
- In Lean Pool: [LeanPool/FiniteGraphFundamentalGroup](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup), from the card [LeanPool/projects/finite-graph-fundamental-group.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/finite-graph-fundamental-group.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/finite-graph-fundamental-group.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/finite-graph-fundamental-group.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FiniteGraphFundamentalGroup](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FiniteGraphFundamentalGroup)
