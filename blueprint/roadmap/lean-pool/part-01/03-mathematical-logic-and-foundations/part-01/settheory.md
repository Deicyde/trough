---
declaration: theorem
origin: cited
lean: SetTheory.kunen_inconsistency_V, NontrivialElementaryEmbedding
statement: formalized
---

# The Kunen inconsistency theorem

> Formalizes elementary embeddings of models of ZF set theory and proves the Kunen inconsistency theorem, that there is no nontrivial elementary embedding of the set-theoretic universe into itself.

*Quoted from the card [LeanPool/projects/settheory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/settheory.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SetTheory.kunen_inconsistency_V`](https://leanpool.github.io/lean-pool/LeanPool/SetTheory/KunenInconsistency.html#SetTheory.kunen_inconsistency_V) (theorem; a main declaration), declared in [LeanPool/SetTheory/KunenInconsistency.lean, line 374](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SetTheory/KunenInconsistency.lean#L374): “Proves the Kunen inconsistency theorem, that every elementary embedding of the von Neumann universe V into itself is the identity.”
- [`SetTheory.kunen_inconsistency_vonNeumann`](https://leanpool.github.io/lean-pool/LeanPool/SetTheory/KunenInconsistency.html#SetTheory.kunen_inconsistency_vonNeumann) (theorem), declared in [LeanPool/SetTheory/KunenInconsistency.lean, line 348](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SetTheory/KunenInconsistency.lean#L348): “Proves the Kunen inconsistency theorem for von Neumann levels V_μ at a successor-limit ordinal, computing the supremum of the critical-point iterates.”
- [`SetTheory.crit`](https://leanpool.github.io/lean-pool/LeanPool/SetTheory/ElementaryEmbedding.html#SetTheory.crit) (def), declared in [LeanPool/SetTheory/ElementaryEmbedding.lean, line 112](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SetTheory/ElementaryEmbedding.lean#L112): “Defines the critical point of a nontrivial elementary embedding as the least ordinal it moves.”
- [`NontrivialElementaryEmbedding`](https://leanpool.github.io/lean-pool/LeanPool/SetTheory/ElementaryEmbedding.html#NontrivialElementaryEmbedding) (class; a main declaration), declared in [LeanPool/SetTheory/ElementaryEmbedding.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SetTheory/ElementaryEmbedding.lean#L28): “Defines a nontrivial elementary embedding of a model of ZF into itself.”

## Project

- Authors: Shuhao Song.
- Source: *Elementary embeddings and infinitary combinatorics* by Kenneth Kunen, [doi:10.2307/2269948](https://doi.org/10.2307/2269948).
- Project repository: [znssong/SetTheory](https://github.com/znssong/SetTheory).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 03E55, 03C90.
- In Lean Pool: [LeanPool/SetTheory](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SetTheory), from the card [LeanPool/projects/settheory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/settheory.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/settheory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/settheory.yaml)
- [Lean Pool at 701389c0: LeanPool/SetTheory](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/SetTheory)
