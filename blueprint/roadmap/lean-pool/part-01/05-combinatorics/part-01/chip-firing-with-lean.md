---
declaration: theorem
origin: cited
lean: ChipFiring.Propositions.riemann_roch, ChipFiring.Propositions.clifford
statement: formalized
proof: formalized
---

# Chip-Firing with Lean 4

> A Lean 4 / Mathlib formalization of Baker and Norine's Riemann-Roch theorem for finite graphs. Chip configurations on a finite graph, modulo chip-firing moves, form an abelian group analogous to the group of line bundles on a compact Riemann surface. Each class can be assigned a rank, analogous to the dimension of a linear series. These ranks then satisfy a formula of the form r(D) - r(K-D) = deg D + 1 - g, in exact analogy to Riemann surfaces. This formula is formalized, along with the analog of Clifford's theorem for finite graphs.

*Quoted from the card [LeanPool/projects/chip-firing-with-lean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/chip-firing-with-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ChipFiring.Propositions.riemann_roch`](https://leanpool.github.io/lean-pool/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.html#ChipFiring.Propositions.riemann_roch) (theorem; a main declaration), declared in [LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean, line 29](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean#L29): “For a finite connected graph, the ranks of a divisor and its canonical complement satisfy the graph Riemann–Roch formula.”
- [`ChipFiring.Propositions.clifford`](https://leanpool.github.io/lean-pool/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.html#ChipFiring.Propositions.clifford) (theorem; a main declaration), declared in [LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean, line 40](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ChipFiring/ChipFiringWithLean/PalomarSolution.lean#L40): “For a special divisor on a finite connected graph, its rank is at most half its degree.”

## Project

- Authors: Dhyey Dharmendrakumar Mavani, Nathan Pflueger.
- Project repository: [dhyeymavani2003/chip-firing-with-lean](https://github.com/dhyeymavani2003/chip-firing-with-lean), at commit [5b422d85](https://github.com/dhyeymavani2003/chip-firing-with-lean/tree/5b422d855c02af60591121ba7c11b5e8242542b8).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C57, 14T20.
- In Lean Pool: [LeanPool/ChipFiring](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ChipFiring), from the card [LeanPool/projects/chip-firing-with-lean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/chip-firing-with-lean.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/chip-firing-with-lean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/chip-firing-with-lean.yaml)
- [Lean Pool at 701389c0: LeanPool/ChipFiring](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/ChipFiring)
