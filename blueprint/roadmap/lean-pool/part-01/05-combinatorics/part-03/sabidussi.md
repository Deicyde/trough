---
declaration: theorem
origin: cited
lean: Sabidussi.LoopMultigraph.loop_sabidussi_compatibility_ordinary
statement: formalized
proof: formalized
---

# Sabidussi's compatibility conjecture for Eulerian multigraphs

> Formalizes Sabidussi's compatibility conjecture for finite labelled endpoint multigraphs with loops and parallel edges, where a loop contributes two half-edge incidences to the degree of its vertex. Given an Euler tour and minimum degree at least four, the main theorem constructs a partition of all edges into nonempty, edge-connected, 2-regular ordinary circuits such that consecutive edges of the Euler tour never lie in the same circuit. The proof runs a four-colour (F_2^2) algebra over the cyclic transition word, uses an odd balancing parity lemma to choose compatible local frames, and transports the resulting colouring back to a compatible ordinary circuit decomposition.

*Quoted from the card [LeanPool/projects/sabidussi.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sabidussi.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Sabidussi.LoopMultigraph.loop_sabidussi_compatibility_ordinary`](https://leanpool.github.io/lean-pool/LeanPool/Sabidussi/OrdinaryCircuit.html#Sabidussi.LoopMultigraph.loop_sabidussi_compatibility_ordinary) (theorem; a main declaration), declared in [LeanPool/Sabidussi/OrdinaryCircuit.lean, line 451](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sabidussi/OrdinaryCircuit.lean#L451): “For any finite endpoint multigraph with an Euler tour and minimum degree at least four, the edges partition into ordinary, nonempty, connected, 2-regular circuits that are compatible with the tour: no circuit contains two consecutive tour edges.”
- [`Sabidussi.LoopMultigraph.loop_sabidussi_compatibility`](https://leanpool.github.io/lean-pool/LeanPool/Sabidussi/LoopGraphBridge.html#Sabidussi.LoopMultigraph.loop_sabidussi_compatibility) (theorem), declared in [LeanPool/Sabidussi/LoopGraphBridge.lean, line 133](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sabidussi/LoopGraphBridge.lean#L133): “The same compatibility statement phrased with the intrinsic even-edge-set circuit decomposition, from which the ordinary-circuit form is derived.”

## Project

- Authors: Nikolay Ulyanov.
- Source: *Graph Puzzles III.1: A proof of Sabidussi's compatibility conjecture* by Nikolay Ulyanov, [https://github.com/gexahedron/sabidussi-lean/blob/032e640df0cc41d4d3d217f7c68628ab19cb3767/sabidussi_proof.pdf](https://github.com/gexahedron/sabidussi-lean/blob/032e640df0cc41d4d3d217f7c68628ab19cb3767/sabidussi_proof.pdf).
- Project repository: [gexahedron/sabidussi-lean](https://github.com/gexahedron/sabidussi-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C45.
- In Lean Pool: [LeanPool/Sabidussi](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sabidussi), from the card [LeanPool/projects/sabidussi.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sabidussi.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sabidussi.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sabidussi.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Sabidussi](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sabidussi)
