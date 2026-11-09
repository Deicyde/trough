---
declaration: theorem
origin: cited
lean: LeanPool.AsymptoticTrianglePacking.trianglePackingGap
statement: formalized
proof: formalized
---

# Finite hypergraph rounding and the asymptotic triangle-packing gap

> Formalizes a finite ceiling-carrying nibble theorem for uniform hypergraphs that are near-regular outside a small exceptional set and have suitably bounded codegrees, and derives the uniform subquadratic gap between fractional and integral triangle packing in finite graphs, together with its fractional-cover formulation.

*Quoted from the card [LeanPool/projects/asymptotic-triangle-packing.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/asymptotic-triangle-packing.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.AsymptoticTrianglePacking.nearRegularNibbleTheorem`](https://leanpool.github.io/lean-pool/LeanPool/AsymptoticTrianglePacking/Main.html#LeanPool.AsymptoticTrianglePacking.nearRegularNibbleTheorem) (theorem), declared in [LeanPool/AsymptoticTrianglePacking/Main.lean, line 1722](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AsymptoticTrianglePacking/Main.lean#L1722): “For every uniformity and positive error tolerance, sufficiently large finite uniform hypergraphs with bounded codegrees, near-regular degrees outside a small exceptional set, and a global degree ceiling admit a matching covering the prescribed fraction of their vertices.” Its source, as the card gives it: “Finite near-regular hypergraph nibble theorem used in the Paper III development.”
- [`LeanPool.AsymptoticTrianglePacking.trianglePackingGap`](https://leanpool.github.io/lean-pool/LeanPool/AsymptoticTrianglePacking/Main.html#LeanPool.AsymptoticTrianglePacking.trianglePackingGap) (theorem; a main declaration), declared in [LeanPool/AsymptoticTrianglePacking/Main.lean, line 1742](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AsymptoticTrianglePacking/Main.lean#L1742): “For every positive error tolerance, all sufficiently large finite graphs have fractional triangle-packing optimum at most their integral triangle-packing optimum plus the error tolerance times the square of the number of vertices.” Its source, as the card gives it: “Paper III AX1, fractional-integral triangle-packing gap.”
- [`LeanPool.AsymptoticTrianglePacking.triangleCoverPackingGap`](https://leanpool.github.io/lean-pool/LeanPool/AsymptoticTrianglePacking/Main.html#LeanPool.AsymptoticTrianglePacking.triangleCoverPackingGap) (theorem), declared in [LeanPool/AsymptoticTrianglePacking/Main.lean, line 1752](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AsymptoticTrianglePacking/Main.lean#L1752): “For every positive error tolerance, all sufficiently large finite graphs have fractional triangle-cover optimum at most their integral triangle-packing optimum plus the error tolerance times the square of the number of vertices.” Its source, as the card gives it: “Paper III AX1, cover-side formulation.”

## Project

- Authors: Juan Pablo Traverso Gianini, Aristotle.
- Source: *Asymptotic triangle cover--packing development accompanying Linear-Error Clique Partitions of Split Graphs via Structured Triangle Packing* by Juan Pablo Traverso Gianini, [https://github.com/jtraverso/erdos-81-chordal-clique-partitions/tree/main/preprints/PAPER_III](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/tree/main/preprints/PAPER_III).
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C70, 05C35.
- In Lean Pool: [LeanPool/AsymptoticTrianglePacking](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AsymptoticTrianglePacking), from the card [LeanPool/projects/asymptotic-triangle-packing.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/asymptotic-triangle-packing.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/asymptotic-triangle-packing.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/asymptotic-triangle-packing.yaml)
- [Lean Pool at 2b205bf9: LeanPool/AsymptoticTrianglePacking](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AsymptoticTrianglePacking)
