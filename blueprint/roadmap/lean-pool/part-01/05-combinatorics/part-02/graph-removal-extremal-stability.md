---
declaration: theorem
origin: cited
lean: TuranStability.stability, RemovalLemma.graph_removal
statement: formalized
proof: formalized
---

# Graph removal and extremal stability

> Formalizes the graph removal lemma for every fixed graph, Füredi's sharp stability inequality and Erdős–Simonovits stability for colourable forbidden graphs. A bridge theorem shows that near-extremal graphs with few labelled forbidden copies are close to a complete multipartite graph.

*Quoted from the card [LeanPool/projects/graph-removal-extremal-stability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/graph-removal-extremal-stability.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`TuranStability.furedi`](https://leanpool.github.io/lean-pool/LeanPool/RemovalExtremalStability/TuranStability.html#TuranStability.furedi) (theorem), declared in [LeanPool/RemovalExtremalStability/TuranStability.lean, line 48](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RemovalExtremalStability/TuranStability.lean#L48): “A clique-free graph near Turán's edge bound has a large colourable subgraph.” Its source, as the card gives it: “Füredi's stability theorem.”
- [`TuranStability.stability`](https://leanpool.github.io/lean-pool/LeanPool/RemovalExtremalStability/TuranStability.html#TuranStability.stability) (theorem; a main declaration), declared in [LeanPool/RemovalExtremalStability/TuranStability.lean, line 192](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RemovalExtremalStability/TuranStability.lean#L192): “An L-free graph near the Turán density for a (p+1)-colourable L is close in edit distance to a complete p-partite graph.” Its source, as the card gives it: “Erdős–Simonovits stability theorem.”
- [`RemovalLemma.graph_removal`](https://leanpool.github.io/lean-pool/LeanPool/RemovalExtremalStability/GraphRemoval.html#RemovalLemma.graph_removal) (theorem; a main declaration), declared in [LeanPool/RemovalExtremalStability/GraphRemoval.lean, line 66](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RemovalExtremalStability/GraphRemoval.lean#L66): “Few labelled copies of any fixed graph H can be destroyed by deleting few edges.” Its source, as the card gives it: “Conlon–Fox, Graph removal lemmas, Theorem 1.1 (https://arxiv.org/pdf/1211.3487v1); Erdős–Frankl–Rödl (1986), Theorems 1.5 and 1.5′, are related precursors; formal source https://github.com/jtraverso/graph-removal-lemma/tree/589cf03ef1e4c80ea8cdd6be77778232c62dd37c.”
- [`RemovalExtremalStability.stability_of_few_copies`](https://leanpool.github.io/lean-pool/LeanPool/RemovalExtremalStability/FewCopiesStability.html#RemovalExtremalStability.stability_of_few_copies) (theorem), declared in [LeanPool/RemovalExtremalStability/FewCopiesStability.lean, line 26](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RemovalExtremalStability/FewCopiesStability.lean#L26): “A graph near the Turán density with few labelled L copies is close in edit distance to a complete multipartite graph.”

## Project

- Authors: Juan Pablo Traverso Gianini.
- Source: *Füredi and Erdős–Simonovits stability; general graph removal lemma* by Juan Pablo Traverso Gianini.
- Project repository: [jtraverso/turan-stability](https://github.com/jtraverso/turan-stability), at commit [3eb99033](https://github.com/jtraverso/turan-stability/tree/3eb99033cc931add291781f77b7446dcba8f5f9d).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C35.
- In Lean Pool: [LeanPool/RemovalExtremalStability](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RemovalExtremalStability), from the card [LeanPool/projects/graph-removal-extremal-stability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/graph-removal-extremal-stability.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/graph-removal-extremal-stability.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/graph-removal-extremal-stability.yaml)
- [Lean Pool at 2b205bf9: LeanPool/RemovalExtremalStability](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RemovalExtremalStability)
