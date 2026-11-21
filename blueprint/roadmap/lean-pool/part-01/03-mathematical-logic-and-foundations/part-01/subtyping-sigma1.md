---
declaration: def
origin: cited
lean: DeciSigma1.decideBooleanSentence, DeciSigma1.booleanSentence_regular_iff, DeciSigma1.decideBooleanSentenceTopFree, DeciSigma1.exists_small_hole, DeciSigma1.smallHoleBound_le
statement: formalized
---

# Decidability of the Sigma-one theory of non-structural subtyping

> Computable decision procedures for Boolean combinations of existential and universal non-structural subtype sentences, with one constructor of arbitrary finite arity and variance, over finite, regular, and arbitrary trees. Includes disjunctive entailment, finite-countermodel transfer under finite satisfiability, automata, word compression, and an elementary total-length bound for holes of finite-state structural readers over finite alphabets.

*Quoted from the card [LeanPool/projects/subtyping-sigma1.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/subtyping-sigma1.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DeciSigma1.decideBooleanSentence`](https://leanpool.github.io/lean-pool/LeanPool/DeciSigma1/Main.html#DeciSigma1.decideBooleanSentence) (def; a main declaration), declared in [LeanPool/DeciSigma1/Main.lean, line 168](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1/Main.lean#L168): “Decides Boolean combinations of existential and universal subtype sentences for every finite constructor arity and variance over finite, regular, or arbitrary trees with bottom and top.”
- [`DeciSigma1.booleanSentence_regular_iff`](https://leanpool.github.io/lean-pool/LeanPool/DeciSigma1/Main.html#DeciSigma1.booleanSentence_regular_iff) (theorem; a main declaration), declared in [LeanPool/DeciSigma1/Main.lean, line 180](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1/Main.lean#L180): “Regular and arbitrary trees have the same Boolean existential theory.”
- [`DeciSigma1.decideBooleanSentenceTopFree`](https://leanpool.github.io/lean-pool/LeanPool/DeciSigma1/Main.html#DeciSigma1.decideBooleanSentenceTopFree) (def; a main declaration), declared in [LeanPool/DeciSigma1/Main.lean, line 186](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1/Main.lean#L186): “Decides the corresponding theory without top for a covariant constructor over finite, regular, or arbitrary trees.”
- [`DeciSigma1.exists_small_hole`](https://leanpool.github.io/lean-pool/LeanPool/DeciSigma1/Main.html#DeciSigma1.exists_small_hole) (theorem; a main declaration), declared in [LeanPool/DeciSigma1/Main.lean, line 400](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1/Main.lean#L400): “Every finite-state structural reader over a finite alphabet, with decidable equality, that has a hole has one whose total word length satisfies a computable bound.”
- [`DeciSigma1.smallHoleBound_le`](https://leanpool.github.io/lean-pool/LeanPool/DeciSigma1/Main.html#DeciSigma1.smallHoleBound_le) (theorem; a main declaration), declared in [LeanPool/DeciSigma1/Main.lean, line 344](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1/Main.lean#L344): “The hole-length bound is bounded by four iterated exponentials.”

## Project

- Authors: Yaoyu Zhao.
- Source: *Decidability of the Sigma-one theory of non-structural subtyping*.
- Project repository: [noti0na1/deci-sigma1](https://github.com/noti0na1/deci-sigma1), at commit [4d1702fd](https://github.com/noti0na1/deci-sigma1/tree/4d1702fd657be4d7bb3203e2e7302856353124c7).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 03B25, 68N18, 68Q45.
- In Lean Pool: [LeanPool/DeciSigma1](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1), from the card [LeanPool/projects/subtyping-sigma1.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/subtyping-sigma1.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/subtyping-sigma1.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/subtyping-sigma1.yaml)
- [Lean Pool at 307e3125: LeanPool/DeciSigma1](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/DeciSigma1)
