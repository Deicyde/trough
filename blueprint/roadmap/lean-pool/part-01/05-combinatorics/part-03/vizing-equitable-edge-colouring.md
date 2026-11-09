---
declaration: theorem
origin: cited
lean: LeanPool.Vizing.exists_equitable_edge_colouring
statement: formalized
proof: formalized
---

# Vizing's theorem and equitable edge colourings

> Proves the maximum-degree-plus-one edge-colouring bound for finite simple graphs by fans and Kempe exchanges. A separate component-swapping argument equitably rebalances any finite proper edge colouring on its original palette. Together they give equitable proper edge colourings on any palette of at least maximum degree plus one colours, with every class bounded by the ceiling of the average class size. Extracted from the published Paper IV formalization; these are classical colouring results, not a claim to new mathematics or to the paper's clique-partition bound.

*Quoted from the card [LeanPool/projects/vizing-equitable-edge-colouring.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/vizing-equitable-edge-colouring.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.Vizing.lineGraph_colorable`](https://leanpool.github.io/lean-pool/LeanPool/Vizing/Main.html#LeanPool.Vizing.lineGraph_colorable) (theorem), declared in [LeanPool/Vizing/Main.lean, line 140](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vizing/Main.lean#L140): “The line graph of a finite simple graph G is colourable with maximum degree of G plus one colours.” Its source, as the card gives it: “Vizing's theorem for finite simple graphs; Vizing (1964).”
- [`SimpleGraph.lineGraph_chromaticNumber_le_maxDegree_succ`](https://leanpool.github.io/lean-pool/LeanPool/Vizing/Main.html#SimpleGraph.lineGraph_chromaticNumber_le_maxDegree_succ) (theorem), declared in [LeanPool/Vizing/Main.lean, line 153](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vizing/Main.lean#L153): “The chromatic number of the line graph of a finite simple graph G is at most maximum degree of G plus one.”
- [`LeanPool.Vizing.Equitable.exists_equitable_colouring`](https://leanpool.github.io/lean-pool/LeanPool/Vizing/Equitable.html#LeanPool.Vizing.Equitable.exists_equitable_colouring) (theorem), declared in [LeanPool/Vizing/Equitable.lean, line 751](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vizing/Equitable.lean#L751): “Every proper edge colouring of a finite simple graph with a finite palette admits a proper recolouring on the same palette in which any two colour classes differ in size by at most one.”
- [`LeanPool.Vizing.exists_equitable_edge_colouring`](https://leanpool.github.io/lean-pool/LeanPool/Vizing/Corollaries.html#LeanPool.Vizing.exists_equitable_edge_colouring) (theorem; a main declaration), declared in [LeanPool/Vizing/Corollaries.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vizing/Corollaries.lean#L26): “For every finite simple graph G and natural c at least maximum degree of G plus one, there is an equitable proper edge colouring with c colours; each colour class has at most ceiling(|E(G)|/c) edges.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *Vizing and equitable edge-colouring modules in the published Paper IV freeze* by Juan Pablo Traverso Gianini.
- Project repository: [jtraverso/erdos-81-chordal-clique-partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions), at commit [ff2019f5](https://github.com/jtraverso/erdos-81-chordal-clique-partitions/tree/ff2019f56a50cf300a6531c9f8d4a8fb1a541e3d).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15.
- In Lean Pool: [LeanPool/Vizing](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vizing), from the card [LeanPool/projects/vizing-equitable-edge-colouring.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/vizing-equitable-edge-colouring.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/vizing-equitable-edge-colouring.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/vizing-equitable-edge-colouring.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Vizing](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vizing)
