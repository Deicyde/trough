---
declaration: lemma
origin: cited
---

# circuitlib: a circuit verification library for Lean 4

> A categorical semantics framework for digital circuits over Belnap's four-valued logic, following Ghica-Kaye-Sprunger. Its main theorems prove that combinational circuits (monotone functions on wire vectors) and sequential circuits (causal monotone stream functions) form symmetric monoidal categories, with a verified full adder as demonstration.

*Quoted from the card [LeanPool/projects/circuitlib.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/circuitlib.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- `Circuit.SequentialCircuitCategory.instSymmetricCategory`, a main declaration that the scan does not find declared in the project's files at this commit: “The category of sequential circuits, whose morphisms are causal monotone stream functions as in Ghica-Kaye-Sprunger's denotational semantics, is symmetric monoidal, with all coherence laws (pentagon, triangle, hexagons, symmetry) proven.”
- `Circuit.CombinationalCircuitCategory.instSymmetricCategory`, which the scan does not find declared in the project's files at this commit: “The category of combinational circuits, with wire counts as objects and monotone wire-vector functions as morphisms, is symmetric monoidal under juxtaposition of wire bundles.”
- [`Circuit.SequentialCircuitCategory.tensorHom_causal`](https://leanpool.github.io/lean-pool/LeanPool/Circuitlib/Circuit/Category/Sequential.html#Circuit.SequentialCircuitCategory.tensorHom_causal) (lemma), declared in [LeanPool/Circuitlib/Circuit/Category/Sequential.lean, line 205](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Circuitlib/Circuit/Category/Sequential.lean#L205): “Causality is preserved by parallel composition, the key lemma making sequential circuits closed under the tensor product.”
- `Circuit.BelnapLevel.instSemilatticeSup`, which the scan does not find declared in the project's files at this commit: “Belnap's four truth values under the information order form a join-semilattice, the wire-value semantics in which every circuit denotes a monotone function.”
- [`Circuit.CombinationalCircuit.adder_def`](https://leanpool.github.io/lean-pool/LeanPool/Circuitlib/Circuit/Combinational.html#Circuit.CombinationalCircuit.adder_def) (lemma), declared in [LeanPool/Circuitlib/Circuit/Combinational.lean, line 115](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Circuitlib/Circuit/Combinational.lean#L115): “Correctness of a full adder assembled categorically from two half adders, gates, braidings, and whiskerings, computing the Boolean sum and carry bits; a demonstration of the framework.”

## Project

- Authors: Matt Hunzinger.
- Source: [arXiv:2201.10456](https://arxiv.org/abs/2201.10456).
- Project repository: [matthunz/circuitlib](https://github.com/matthunz/circuitlib).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 18M05, 68Q60, 94C11.
- In Lean Pool: [LeanPool/Circuitlib](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Circuitlib), from the card [LeanPool/projects/circuitlib.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/circuitlib.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/circuitlib.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/circuitlib.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Circuitlib](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Circuitlib)
