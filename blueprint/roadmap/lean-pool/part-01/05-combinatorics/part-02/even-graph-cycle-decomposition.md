---
declaration: theorem
origin: cited
lean: Finset.exists_cycleDecomp, Finset.exists_edge_pairing_of_even
statement: formalized
proof: formalized
---

# Even graphs are edge-disjoint unions of cycles

> Decomposes every finite loopless edge set with even degree at each vertex into edge-disjoint simple cycles and derives a simultaneous fixed-point-free pairing of incident edges.

*Quoted from the card [LeanPool/projects/even-graph-cycle-decomposition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/even-graph-cycle-decomposition.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Finset.exists_cycleDecomp`](https://leanpool.github.io/lean-pool/LeanPool/EvenGraphCycles.html#Finset.exists_cycleDecomp) (theorem; a main declaration), declared in [LeanPool/EvenGraphCycles.lean, line 592](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EvenGraphCycles.lean#L592): “Every finite loopless edge set whose degree is even at every vertex is the edge-disjoint union of simple cycles of length at least three.”
- [`Finset.exists_edge_pairing_of_even`](https://leanpool.github.io/lean-pool/LeanPool/EvenGraphCycles.html#Finset.exists_edge_pairing_of_even) (theorem; a main declaration), declared in [LeanPool/EvenGraphCycles.lean, line 725](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EvenGraphCycles.lean#L725): “If every vertex has even degree, then the incident edges at every vertex admit a simultaneous fixed-point-free involutive pairing.”

## Project

- Authors: Juan Pablo Traverso Gianini, Aristotle.
- Source: *Reusable even-graph cycle decomposition accompanying Linear-Error Clique Partitions of Split Graphs via Structured Triangle Packing* by Juan Pablo Traverso Gianini, [https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/b3423f3e8c8db7c2d1b279673293ef3079faf903/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/EvenGraphCycles.lean](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/b3423f3e8c8db7c2d1b279673293ef3079faf903/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/EvenGraphCycles.lean).
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C45.
- In Lean Pool: [LeanPool/EvenGraphCycles](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EvenGraphCycles), from the card [LeanPool/projects/even-graph-cycle-decomposition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/even-graph-cycle-decomposition.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/even-graph-cycle-decomposition.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/even-graph-cycle-decomposition.yaml)
- [Lean Pool at 2b205bf9: LeanPool/EvenGraphCycles](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EvenGraphCycles)
