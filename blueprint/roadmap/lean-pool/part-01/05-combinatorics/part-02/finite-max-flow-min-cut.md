---
declaration: theorem
origin: cited
lean: Contrib.MaxFlowMinCut.maxflow_eq_mincut
statement: formalized
proof: formalized
---

# Finite max-flow / min-cut

> Develops finite networks with real nonnegative capacities, proves cut-flow weak duality and maximum-flow attainment, and derives max-flow/min-cut equality by an augmenting-path argument.

*Quoted from the card [LeanPool/projects/finite-max-flow-min-cut.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/finite-max-flow-min-cut.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Contrib.MaxFlowMinCut.maxflow_eq_mincut`](https://leanpool.github.io/lean-pool/LeanPool/MaxFlowMinCut.html#Contrib.MaxFlowMinCut.maxflow_eq_mincut) (theorem; a main declaration), declared in [LeanPool/MaxFlowMinCut.lean, line 706](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MaxFlowMinCut.lean#L706): “Every finite network with real nonnegative capacities and distinct source and sink admits a feasible flow and a source-sink cut whose flow value equals the cut capacity.”
- [`Contrib.MaxFlowMinCut.value_le_capacity`](https://leanpool.github.io/lean-pool/LeanPool/MaxFlowMinCut.html#Contrib.MaxFlowMinCut.value_le_capacity) (theorem), declared in [LeanPool/MaxFlowMinCut.lean, line 458](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MaxFlowMinCut.lean#L458): “The value of every feasible flow is at most the capacity of every source-sink cut.”
- [`Contrib.MaxFlowMinCut.max_flow_exists`](https://leanpool.github.io/lean-pool/LeanPool/MaxFlowMinCut.html#Contrib.MaxFlowMinCut.max_flow_exists) (theorem), declared in [LeanPool/MaxFlowMinCut.lean, line 575](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MaxFlowMinCut.lean#L575): “Every finite network with real nonnegative capacities admits a maximum-value feasible flow.”

## Project

- Authors: Juan Pablo Traverso Gianini, Aristotle.
- Source: *Reusable max-flow/min-cut component accompanying Linear-Error Clique Partitions of Split Graphs via Structured Triangle Packing* by Juan Pablo Traverso Gianini, [https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/b3423f3e8c8db7c2d1b279673293ef3079faf903/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/MaxFlowMinCut.lean](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/b3423f3e8c8db7c2d1b279673293ef3079faf903/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/MaxFlowMinCut.lean).
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C21, 90C35.
- In Lean Pool: [LeanPool/MaxFlowMinCut](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MaxFlowMinCut), from the card [LeanPool/projects/finite-max-flow-min-cut.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/finite-max-flow-min-cut.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/finite-max-flow-min-cut.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/finite-max-flow-min-cut.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MaxFlowMinCut](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MaxFlowMinCut)
