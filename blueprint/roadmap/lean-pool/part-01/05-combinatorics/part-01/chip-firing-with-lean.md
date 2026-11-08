---
declaration: theorem
origin: cited
lean: ChipFiring.Propositions.riemann_roch, ChipFiring.Propositions.clifford
statement: formalized
proof: formalized
---

# Chip-Firing with Lean 4

> A Lean 4 / Mathlib formalization of Baker and Norine's Riemann-Roch theorem for finite graphs. Chip configurations on a finite graph, modulo chip-firing moves, form an abelian group analogous to the group of line bundles on a compact Riemann surface. Each class can be assigned a rank, analogous to the dimension of a linear series. These ranks then satisfy a formula of the form r(D) - r(K-D) = deg D + 1 - g, in exact analogy to Riemann surfaces. This formula is formalized, along with the analog of Clifford's theorem for finite graphs.

*Quoted from the card [LeanPool/projects/chip-firing-with-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chip-firing-with-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`ChipFiring.Propositions.riemann_roch`](https://leanpool.github.io/lean-pool/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.html#ChipFiring.Propositions.riemann_roch) (theorem; a main declaration), declared in [LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean, line 29](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean#L29): “For a finite connected graph, the ranks of a divisor and its canonical complement satisfy the graph Riemann–Roch formula.”
- [`ChipFiring.Propositions.clifford`](https://leanpool.github.io/lean-pool/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.html#ChipFiring.Propositions.clifford) (theorem; a main declaration), declared in [LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean#L40): “For a special divisor on a finite connected graph, its rank is at most half its degree.”

## Project

- Authors: Dhyey Dharmendrakumar Mavani, Nathan Pflueger.
- Project repository: [dhyeymavani2003/chip-firing-with-lean](https://github.com/dhyeymavani2003/chip-firing-with-lean), at commit [5b422d85](https://github.com/dhyeymavani2003/chip-firing-with-lean/tree/5b422d855c02af60591121ba7c11b5e8242542b8).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C57, 14T20.
- In Lean Pool: [LeanPool/ChipFiring](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChipFiring), from the card [LeanPool/projects/chip-firing-with-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chip-firing-with-lean.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/chip-firing-with-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/chip-firing-with-lean.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ChipFiring](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ChipFiring)
