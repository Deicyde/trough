---
declaration: theorem
origin: cited
lean: NashWilliamsTutte.tree_packing, NashWilliamsTutte.arboricity
statement: formalized
proof: formalized
---

# Nash-Williams–Tutte tree packing and arboricity

> A finite simple graph on a nonempty vertex type has k edge-disjoint spanning trees exactly when every partition into m nonempty parts has at least k(m − 1) crossing edges. The development also proves the Nash-Williams characterization of covering the edges by k forests, and that every finite nonempty 2k-edge-connected simple graph has k edge-disjoint spanning trees. It preserves the general forest exchange lemma and supporting reachability and edge-counting infrastructure, using Mathlib's graph definitions.

*Quoted from the card [LeanPool/projects/nash-williams-tutte.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nash-williams-tutte.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`NashWilliamsTutte.tree_packing`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliamsTutte/Theorems.html#NashWilliamsTutte.tree_packing) (theorem; a main declaration), declared in [LeanPool/NashWilliamsTutte/Theorems.lean, line 42](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliamsTutte/Theorems.lean#L42): “A finite simple graph on a nonempty vertex type has k pairwise edge-disjoint spanning trees if and only if every vertex partition into m nonempty parts has at least k(m − 1) crossing edges.”
- [`NashWilliamsTutte.arboricity`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliamsTutte/Theorems.html#NashWilliamsTutte.arboricity) (theorem; a main declaration), declared in [LeanPool/NashWilliamsTutte/Theorems.lean, line 116](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliamsTutte/Theorems.lean#L116): “A finite simple graph is the union of k forests if and only if every nonempty finite vertex set S induces at most k(|S| − 1) edges.”
- [`NashWilliamsTutte.exists_trees_of_isEdgeConnected`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliamsTutte/Theorems.html#NashWilliamsTutte.exists_trees_of_isEdgeConnected) (theorem), declared in [LeanPool/NashWilliamsTutte/Theorems.lean, line 191](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliamsTutte/Theorems.lean#L191): “Every finite simple graph on a nonempty vertex type that remains connected after deletion of fewer than 2k edges has k pairwise edge-disjoint spanning trees.”
- [`NashWilliamsTutte.exists_forests_core`](https://leanpool.github.io/lean-pool/LeanPool/NashWilliamsTutte/Auxiliary.html#NashWilliamsTutte.exists_forests_core) (theorem), declared in [LeanPool/NashWilliamsTutte/Auxiliary.lean, line 407](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliamsTutte/Auxiliary.lean#L407): “Every finite simple graph G contains k pairwise edge-disjoint forests and a subgraph H such that intersecting each forest with H preserves the connected components of H, and the forests cover every edge of G outside H.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *Edge-disjoint spanning trees of finite graphs*, [doi:10.1112/jlms/s1-36.1.445](https://doi.org/10.1112/jlms/s1-36.1.445), [https://github.com/jtraverso/nash-williams-trees/tree/101e48847a929dd8102521f57723e2137989ce2e](https://github.com/jtraverso/nash-williams-trees/tree/101e48847a929dd8102521f57723e2137989ce2e).
- Project repository: [jtraverso/nash-williams-trees](https://github.com/jtraverso/nash-williams-trees), at commit [101e4884](https://github.com/jtraverso/nash-williams-trees/tree/101e48847a929dd8102521f57723e2137989ce2e).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C05, 05C70, 05C40.
- In Lean Pool: [LeanPool/NashWilliamsTutte](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliamsTutte), from the card [LeanPool/projects/nash-williams-tutte.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nash-williams-tutte.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/nash-williams-tutte.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/nash-williams-tutte.yaml)
- [Lean Pool at 2b205bf9: LeanPool/NashWilliamsTutte](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/NashWilliamsTutte)
