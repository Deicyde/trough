---
declaration: theorem
origin: cited
lean: Erdos111.countably_colorable_of_linear
statement: formalized
proof: formalized
---

# Linear finite bipartization costs force countable graph colourings

> A graph whose every finite subgraph on m vertices can be made bipartite by deleting at most C m edges has a proper colouring by natural numbers. Consequently the maximum finite-subgraph bipartization cost h_G(n), divided by n, tends to infinity for every graph that is not countably colourable, including every graph with chromatic cardinal aleph-one. The development preserves finite edge costs, rooted-pattern extension costs, closure chains, probability laws on Boolean products, finite minimax, Hilbert-space classes, and colouring along well-founded orders. It answers the limit question of Erdős Problem 111; it does not determine the exact growth of h_G.

*Quoted from the card [LeanPool/projects/erdos111-bipartization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos111-bipartization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Erdos111.countably_colorable_of_linear`](https://leanpool.github.io/lean-pool/LeanPool/Erdos111.html#Erdos111.countably_colorable_of_linear) (theorem; a main declaration), declared in [LeanPool/Erdos111.lean, line 42](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos111.lean#L42): “For any real C, if each finite subgraph H of G has bipartization number at most C times its number of vertices, G admits a proper colouring by natural numbers. Vertex types may inhabit any universe.”
- [`Erdos111.tendsto_of_not_countably_colorable`](https://leanpool.github.io/lean-pool/LeanPool/Erdos111.html#Erdos111.tendsto_of_not_countably_colorable) (theorem), declared in [LeanPool/Erdos111.lean, line 49](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos111.lean#L49): “If G has no proper colouring by natural numbers, h_G(n)/n tends to positive infinity along the whole natural-number sequence.”
- [`Erdos111.erdos_111`](https://leanpool.github.io/lean-pool/LeanPool/Erdos111.html#Erdos111.erdos_111) (theorem), declared in [LeanPool/Erdos111.lean, line 55](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos111.lean#L55): “For every graph of chromatic cardinal aleph-one, h_G(n)/n tends to positive infinity. Here h_G(n) is the largest number of edge deletions needed to bipartize a subgraph on n vertices.”
- [`Erdos111.exists_unitVector_classes`](https://leanpool.github.io/lean-pool/LeanPool/Erdos111/HilbertClasses.html#Erdos111.exists_unitVector_classes) (theorem), declared in [LeanPool/Erdos111/HilbertClasses.lean, line 85](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos111/HilbertClasses.lean#L85): “In any real Hilbert space, unit vectors can be partitioned into countably many classes, each with a positive lower bound for one plus the inner product of any two vectors in that class.”

## Project

- Authors: Jacob Parish.
- Source: *Graphs whose finite subgraphs have linear bipartization cost are countably colorable* by Plasma AI, [proof](https://github.com/plasma-ai/erdos-111/blob/de72caf0e388c729697b6813f4ea90bfe1617c7b/blueprint/proof.md), [problem](https://www.erdosproblems.com/111).
- Project repository: [plasma-ai/erdos-111](https://github.com/plasma-ai/erdos-111), at commit [de72caf0](https://github.com/plasma-ai/erdos-111/tree/de72caf0e388c729697b6813f4ea90bfe1617c7b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15, 05C63, 03E05.
- In Lean Pool: [LeanPool/Erdos111](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos111), from the card [LeanPool/projects/erdos111-bipartization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos111-bipartization.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/erdos111-bipartization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/erdos111-bipartization.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Erdos111](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Erdos111)
