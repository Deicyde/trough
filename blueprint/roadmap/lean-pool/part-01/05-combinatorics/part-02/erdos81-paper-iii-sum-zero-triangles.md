---
declaration: theorem
origin: cited
lean: SumZeroTriangles.exists_simpleGraph_triangle_packing
statement: formalized
proof: formalized
---

# Near-perfect triangle packings from sum-zero triples

> Records a reusable formalization byproduct accompanying Paper III: pairwise edge-disjoint triangles in any finite complete graph such that every vertex is incident to at most three uncovered edges, using a cyclic-group sum-zero triple system, with a bridge to Mathlib's SimpleGraph API.

*Quoted from the card [LeanPool/projects/erdos81-paper-iii-sum-zero-triangles.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos81-paper-iii-sum-zero-triangles.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`SumZeroTriangles.exists_simpleGraph_triangle_packing`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIIContrib/SimpleGraph.html#SumZeroTriangles.exists_simpleGraph_triangle_packing) (theorem; a main declaration), declared in [LeanPool/Erdos81PaperIIIContrib/SimpleGraph.lean, line 98](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIIContrib/SimpleGraph.lean#L98): “For every finite vertex type, its complete simple graph has a family of pairwise edge-disjoint triangle graphs whose uncovered graph has degree at most three at every vertex.”
- [`SumZeroTriangles.exists_triangle_packing_clique`](https://leanpool.github.io/lean-pool/LeanPool/Erdos81PaperIIIContrib/SumZeroTriangles.html#SumZeroTriangles.exists_triangle_packing_clique) (theorem), declared in [LeanPool/Erdos81PaperIIIContrib/SumZeroTriangles.lean, line 374](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIIContrib/SumZeroTriangles.lean#L374): “Every finite complete graph has a family of pairwise edge-disjoint triangles leaving uncovered degree at most three at every vertex.”

## Project

- Authors: Juan Pablo Traverso Gianini, Aristotle, Vasily Ilin.
- Source: *SumZeroTriangles.lean, a reusable formalization byproduct accompanying Linear-Error Clique Partitions of Split Graphs via Structured Triangle Packing* by Aristotle, [https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/main/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/SumZeroTriangles.lean](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/blob/main/preprints/PAPER_III/05_formalization/lean_v1.4_freeze/Contrib/SumZeroTriangles.lean).
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05B07, 05C70.
- In Lean Pool: [LeanPool/Erdos81PaperIIIContrib](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIIContrib), from the card [LeanPool/projects/erdos81-paper-iii-sum-zero-triangles.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos81-paper-iii-sum-zero-triangles.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos81-paper-iii-sum-zero-triangles.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos81-paper-iii-sum-zero-triangles.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos81PaperIIIContrib](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos81PaperIIIContrib)
