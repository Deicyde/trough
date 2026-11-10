---
declaration: def
origin: cited
lean: SimpleGraph.lineGraphColoringEquivMatchingDecomposition
statement: formalized
---

# Line-graph colourings and matching decompositions

> Connects Mathlib line-graph colourings to palette-indexed partitions of actual graph edges into Mathlib matching subgraphs. Both conversions are inverse, preserve each matching exactly, and allow empty colours without a default colour or a finiteness assumption. An edge equivalence yields exact edge accounting: natural-number counts require only finite edges and a finite palette, while indexed cardinal counts allow arbitrary vertices, edges, and palettes. This is classical representation interoperability, not a new colouring bound or a claim of priority.

*Quoted from the card [LeanPool/projects/line-graph-colouring-matching.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/line-graph-colouring-matching.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SimpleGraph.lineGraphColoringEquivMatchingDecomposition`](https://leanpool.github.io/lean-pool/LeanPool/GraphColouringMatching/Basic.html#SimpleGraph.lineGraphColoringEquivMatchingDecomposition) (def; a main declaration), declared in [LeanPool/GraphColouringMatching/Basic.lean, line 201](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching/Basic.lean#L201): “Proper colourings of the line graph on any palette are equivalent to partitions of the original edges into matching subgraphs indexed by that palette, with empty classes permitted.” Its source, as the card gives it: “New adapter proved in GraphColouringMatching/Basic.lean, using Mathlib's existing lineGraph, Coloring and Subgraph.IsMatching.”
- [`SimpleGraph.MatchingDecomposition.edgeMatching_lineGraphColoring`](https://leanpool.github.io/lean-pool/LeanPool/GraphColouringMatching/Basic.html#SimpleGraph.MatchingDecomposition.edgeMatching_lineGraphColoring) (theorem), declared in [LeanPool/GraphColouringMatching/Basic.lean, line 163](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching/Basic.lean#L163): “Converting a matching decomposition to a colouring and extracting one colour class returns exactly its original matching subgraph.”
- [`SimpleGraph.MatchingDecomposition.edgeEquivSigma`](https://leanpool.github.io/lean-pool/LeanPool/GraphColouringMatching/Basic.html#SimpleGraph.MatchingDecomposition.edgeEquivSigma) (def), declared in [LeanPool/GraphColouringMatching/Basic.lean, line 111](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching/Basic.lean#L111): “Original graph edges are in bijection with the disjoint union of the edge types of the palette-indexed matching subgraphs.”
- [`SimpleGraph.MatchingDecomposition.card_edges_eq_sum`](https://leanpool.github.io/lean-pool/LeanPool/GraphColouringMatching/Finite.html#SimpleGraph.MatchingDecomposition.card_edges_eq_sum) (theorem), declared in [LeanPool/GraphColouringMatching/Finite.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching/Finite.lean#L26): “For a finite edge set and finite palette, the number of graph edges equals the sum of the numbers of edges in its matching classes, even when the vertex set is infinite.”
- [`SimpleGraph.MatchingDecomposition.cardinal_edges_eq_sum`](https://leanpool.github.io/lean-pool/LeanPool/GraphColouringMatching/Cardinal.html#SimpleGraph.MatchingDecomposition.cardinal_edges_eq_sum) (theorem), declared in [LeanPool/GraphColouringMatching/Cardinal.lean, line 27](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching/Cardinal.lean#L27): “Without any finiteness assumption on vertices, edges, or colours, the cardinality of the graph edge set equals the indexed cardinal sum of the matching-class edge cardinalities, with a universe lift on the graph edge cardinality when required.” Its source, as the card gives it: “Cardinal.lean applies Mathlib's indexed cardinal sum to the existing edgeEquivSigma; no infinite graph-colouring theorem is assumed.”
- [`SimpleGraph.lineGraph_colorable_iff_matchingDecomposition`](https://leanpool.github.io/lean-pool/LeanPool/GraphColouringMatching/Basic.html#SimpleGraph.lineGraph_colorable_iff_matchingDecomposition) (theorem), declared in [LeanPool/GraphColouringMatching/Basic.lean, line 215](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching/Basic.lean#L215): “The line graph is k-colourable if and only if the graph edges decompose into k matchings, allowing unused colours.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *Original Lean Pool graph-colouring and matching adapters*, [https://github.com/jtraverso/lean-pool/tree/4c1fddb73f9891afc2186f8f11066ea2a08fe4fc/LeanPool/GraphColouringMatching](https://github.com/jtraverso/lean-pool/tree/4c1fddb73f9891afc2186f8f11066ea2a08fe4fc/LeanPool/GraphColouringMatching).
- Project repository: [jtraverso/lean-pool](https://github.com/jtraverso/lean-pool), at commit [4c1fddb7](https://github.com/jtraverso/lean-pool/tree/4c1fddb73f9891afc2186f8f11066ea2a08fe4fc).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15, 05C70.
- In Lean Pool: [LeanPool/GraphColouringMatching](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching), from the card [LeanPool/projects/line-graph-colouring-matching.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/line-graph-colouring-matching.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/line-graph-colouring-matching.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/line-graph-colouring-matching.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GraphColouringMatching](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GraphColouringMatching)
