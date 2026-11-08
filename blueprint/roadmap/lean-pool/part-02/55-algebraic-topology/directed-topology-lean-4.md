---
declaration: class
origin: cited
lean: DirectedSpace, Dipath, DirectedVanKampen.directed_van_kampen
statement: formalized
---

# Directed Topology in Lean 4

> Foundational library for directed topological spaces, dipaths, dihomotopy, the fundamental category functor, and a directed Van Kampen pushout theorem.

*Quoted from the card [LeanPool/projects/directed-topology-lean-4.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/directed-topology-lean-4.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`DirectedSpace`](https://leanpool.github.io/lean-pool/LeanPool/DirectedTopologyLean4/DirectedSpace.html#DirectedSpace) (class; a main declaration), declared in [LeanPool/DirectedTopologyLean4/DirectedSpace.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DirectedTopologyLean4/DirectedSpace.lean#L32): “Definition of a directed topological space as a topological space with a class of directed paths closed under constant paths, concatenation, and monotone reparametrization.”
- [`Dipath`](https://leanpool.github.io/lean-pool/LeanPool/DirectedTopologyLean4/Dipath.html#Dipath) (structure; a main declaration), declared in [LeanPool/DirectedTopologyLean4/Dipath.lean, line 36](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DirectedTopologyLean4/Dipath.lean#L36): “A directed path in a directed space.”
- [`Dipath.Dihomotopic`](https://leanpool.github.io/lean-pool/LeanPool/DirectedTopologyLean4/DirectedPathHomotopy.html#Dipath.Dihomotopic) (def), declared in [LeanPool/DirectedTopologyLean4/DirectedPathHomotopy.lean, line 553](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DirectedTopologyLean4/DirectedPathHomotopy.lean#L553): “Dihomotopy equivalence relation on dipaths between fixed endpoints.”
- [`DirectedVanKampen.directed_van_kampen`](https://leanpool.github.io/lean-pool/LeanPool/DirectedTopologyLean4/DirectedVanKampen.html#DirectedVanKampen.directed_van_kampen) (theorem; a main declaration), declared in [LeanPool/DirectedTopologyLean4/DirectedVanKampen.lean, line 1133](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DirectedTopologyLean4/DirectedVanKampen.lean#L1133): “Proves the directed Van Kampen theorem, showing that the directed fundamental category functor sends the standard open cover square to a pushout in the category of categories.”

## Project

- Authors: Dominique Lawson, Henning Basold, Peter Bruin.
- Source: [doi:10.4230/LIPIcs.ITP.2024.8](https://doi.org/10.4230/LIPIcs.ITP.2024.8), [arXiv:2312.06506](https://arxiv.org/abs/2312.06506).
- Project repository: [Dominique-Lawson/Directed-Topology-Lean-4](https://github.com/Dominique-Lawson/Directed-Topology-Lean-4).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright 2023 Dominique Lawson”.
- MSC2020: 55U40, 55Q05, 18A30.
- In Lean Pool: [LeanPool/DirectedTopologyLean4](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DirectedTopologyLean4), from the card [LeanPool/projects/directed-topology-lean-4.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/directed-topology-lean-4.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/directed-topology-lean-4.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/directed-topology-lean-4.yaml)
- [Lean Pool at 2b205bf9: LeanPool/DirectedTopologyLean4](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/DirectedTopologyLean4)
