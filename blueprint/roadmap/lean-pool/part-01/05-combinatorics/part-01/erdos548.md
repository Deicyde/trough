---
declaration: theorem
origin: cited
lean: Erdos548.erdos_548
statement: formalized
proof: formalized
---

# The Erdős–Sós conjecture (Erdős Problem 548)

> Proves the Erdős–Sós conjecture (1962), Erdős Problem 548: every graph on n ≥ k+1 vertices with at least (k−1)n/2 + 1 edges contains every tree on k+1 vertices as a (not necessarily induced) subgraph. The headline statement is the FrontierMath Erdős benchmark statement, reviewed by Thomas Bloom and carried verbatim by Google DeepMind's Formal Conjectures; the proof was found autonomously by GPT-6 Astra. It is a finite double counting over permutation words of the host vertices: rotating the first qualifying prefix of a cut word gives a gluing inequality for two rooted branches, and reversing the two blocks of a cut moves the root to a newly attached leaf. A strong induction on the order t of the tree bounds the adjacency-marked cut words by the rooted-copy count plus (t−2)·n!, so a tree-free host on n vertices has at most (t−2)n/2 edges, the sharp classical bound.

*Quoted from the card [LeanPool/projects/erdos548.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos548.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Erdos548.erdos_548`](https://leanpool.github.io/lean-pool/LeanPool/Erdos548/Main.html#Erdos548.erdos_548) (theorem; a main declaration), declared in [LeanPool/Erdos548/Main.lean, line 135](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos548/Main.lean#L135): “Let n ≥ k+1. Every simple graph on n vertices with at least (k−1)n/2 + 1 edges contains every tree on k+1 vertices as a subgraph (an injective graph homomorphism). This is Erdős Problem 548, the Erdős–Sós conjecture, in the benchmark phrasing.”
- [`Erdos548.tree_free_edge_bound`](https://leanpool.github.io/lean-pool/LeanPool/Erdos548/Main.html#Erdos548.tree_free_edge_bound) (lemma), declared in [LeanPool/Erdos548/Main.lean, line 103](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos548/Main.lean#L103): “If a tree T on t ≥ 2 vertices is not contained in a graph G on n ≥ 1 vertices, then 2·|E(G)| ≤ (t−2)·n. This is the classical sharp form of the Erdős–Sós bound.”
- [`Erdos548.rooted_word_tree_bound`](https://leanpool.github.io/lean-pool/LeanPool/Erdos548/RootedTrees.html#Erdos548.rooted_word_tree_bound) (lemma), declared in [LeanPool/Erdos548/RootedTrees.lean, line 542](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos548/RootedTrees.lean#L542): “For a tree T on t ≥ 2 vertices rooted at r, a host graph G and a nonempty repetition-free host word of length n, the number of cut permutation words of that word whose cut ends at a neighbour of the first letter is at most the number supporting a rooted copy of T on the prefix plus (t−2)·n!.”
- [`Erdos548.marked_word_gluing_count`](https://leanpool.github.io/lean-pool/LeanPool/Erdos548/Words.html#Erdos548.marked_word_gluing_count) (lemma), declared in [LeanPool/Erdos548/Words.lean, line 203](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos548/Words.lean#L203): “For a permutation-closed family W of repetition-free words, all of the same length m, and families A, B, C of letter sets with C ⊆ A and A R ∧ B X → C (R ∪ X) for disjoint R, X, the marked cuts (l, k) with l ∈ W and k ≤ m qualifying for A plus those qualifying for B number at most the allowed cuts plus those qualifying for C.”

## Project

- Authors: Tom Adamczewski.
- Source: *Erdős problem \#548 (Erdős–Sós conjecture): proof* by Tom Adamczewski.
- Project repository: [tadamcz/erdos548](https://github.com/tadamcz/erdos548), at commit [c02708a6](https://github.com/tadamcz/erdos548/tree/c02708a6956d7b953c2e889c8bc24a0c97796313).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C35, 05C05.
- In Lean Pool: [LeanPool/Erdos548](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos548), from the card [LeanPool/projects/erdos548.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos548.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/erdos548.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/erdos548.yaml)
- [Lean Pool at 701389c0: LeanPool/Erdos548](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Erdos548)
