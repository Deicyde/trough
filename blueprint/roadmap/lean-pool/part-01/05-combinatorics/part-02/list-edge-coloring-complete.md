---
declaration: theorem
origin: cited
lean: LeanPool.ListEdgeColoringComplete.exists_listEdgeColoring_complete
statement: formalized
proof: formalized
---

# Häggkvist–Janssen list edge colouring of complete graphs

> Proves that arbitrary lists of at least n colours on the edges of a complete graph with n vertices admit a proper list edge colouring. The proof constructs and proves uniqueness of the local rank certificate, identifies a nonzero extended-star polynomial coefficient, and applies Mathlib's combinatorial Nullstellensatz. This is an alternative proof presentation, not a literal translation of the article's argument. The conclusion uses Mathlib's actual edge type and line-graph colouring, with no certificate hypothesis and no restriction on the colour universe. This formalizes a classical theorem, not a new bound or a solution of the general list-edge conjecture.

*Quoted from the card [LeanPool/projects/list-edge-coloring-complete.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/list-edge-coloring-complete.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.ListEdgeColoringComplete.exists_listEdgeColoring_complete`](https://leanpool.github.io/lean-pool/LeanPool/ListEdgeColoringComplete/Main.html#LeanPool.ListEdgeColoringComplete.exists_listEdgeColoring_complete) (theorem; a main declaration), declared in [LeanPool/ListEdgeColoringComplete/Main.lean, line 80](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ListEdgeColoringComplete/Main.lean#L80): “For every finite vertex type V, arbitrary colour type and finite list on each edge of the complete graph, if every list has cardinality at least the number of vertices, there is a proper colouring of the line graph choosing a colour from each list. This includes orders zero and one.” Its source, as the card gives it: “Häggkvist–Janssen (1997), Theorems 1.1 and 3.1, complete-graph case.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *New Bounds on the List-Chromatic Index of the Complete Graph and Other Simple Graphs* by Roland Häggkvist, Jeannette Janssen, [doi:10.1017/S0963548397002927](https://doi.org/10.1017/S0963548397002927).
- Project repository: [jtraverso/haggkvist-janssen](https://github.com/jtraverso/haggkvist-janssen), at commit [26d7b2ee](https://github.com/jtraverso/haggkvist-janssen/tree/26d7b2ee0e14813f0e42c3f8628d6b216327c8df).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15.
- In Lean Pool: [LeanPool/ListEdgeColoringComplete](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ListEdgeColoringComplete), from the card [LeanPool/projects/list-edge-coloring-complete.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/list-edge-coloring-complete.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/list-edge-coloring-complete.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/list-edge-coloring-complete.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ListEdgeColoringComplete](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ListEdgeColoringComplete)
