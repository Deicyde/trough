---
declaration: theorem
origin: cited
lean: GoldbergSeymour.goldbergSeymour, GoldbergSeymour.GeneralHighIndexElementary
statement: formalized
proof: formalized
---

# The Goldberg–Seymour edge-coloring theorem

> Proves the Goldberg–Seymour bound for every finite loopless multigraph, with distinct identities for parallel edges: the chromatic index is at most the maximum of the maximum degree plus one and the ceiling of the odd-set density. Preserves proper partial edge colorings, Kempe components, critical subgraphs, Tashkinov trees, extension sequences, and good hierarchies. An incidence-preserving bridge supports Mathlib graphs on their actual vertex and edge sets, including isolated vertices and independently identified parallel edges. The import contains the dependency closure of the full theorem; it does not claim an executable edge-coloring algorithm or its polynomial running time.

*Quoted from the card [LeanPool/projects/goldberg-seymour.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/goldberg-seymour.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`GoldbergSeymour.goldbergSeymour`](https://leanpool.github.io/lean-pool/LeanPool/GoldbergSeymour.html#GoldbergSeymour.goldbergSeymour) (theorem; a main declaration), declared in [LeanPool/GoldbergSeymour.lean, line 34](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GoldbergSeymour.lean#L34): “Every finite loopless multigraph G has chromatic index at most max(Delta(G) + 1, ceil(Gamma(G))), where Delta is the maximum vertex degree and Gamma is the maximum of zero and 2|E(U)|/(|U| - 1) over odd vertex sets U of size at least three. E(U) contains every edge whose two endpoints lie in U, including parallel edges separately.”
- [`GoldbergSeymour.GeneralHighIndexElementary`](https://leanpool.github.io/lean-pool/LeanPool/GoldbergSeymour/GeneralHighIndexElementary.html#GoldbergSeymour.GeneralHighIndexElementary) (theorem; a main declaration), declared in [LeanPool/GoldbergSeymour/GeneralHighIndexElementary.lean, line 25](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GoldbergSeymour/GeneralHighIndexElementary.lean#L25): “If a finite loopless multigraph has chromatic index at least its maximum degree plus two, its chromatic index equals the ceiling of its odd-set density.”

## Project

- Authors: Wesley Pegden.
- Source: *Proof of the Goldberg-Seymour Conjecture on Edge-Colorings of Multigraphs* by Guantao Chen, Guangming Jing, Wenan Zang, [arXiv:1901.10316v2](https://arxiv.org/abs/1901.10316v2).
- Project repository: [wpegden/goldberg_seymour](https://github.com/wpegden/goldberg_seymour), at commit [88d98c1d](https://github.com/wpegden/goldberg_seymour/tree/88d98c1d1a59d1f1bf7c4eb58e73f3945f6daf12).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15.
- In Lean Pool: [LeanPool/GoldbergSeymour](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GoldbergSeymour), from the card [LeanPool/projects/goldberg-seymour.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/goldberg-seymour.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/goldberg-seymour.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/goldberg-seymour.yaml)
- [Lean Pool at 307e3125: LeanPool/GoldbergSeymour](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GoldbergSeymour)
