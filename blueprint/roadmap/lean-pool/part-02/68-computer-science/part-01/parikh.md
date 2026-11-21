---
declaration: theorem
origin: cited
lean: Parikh.parikhImage_isSemilinear_of_isContextFree
statement: formalized
proof: formalized
---

# Parikh's theorem and a certified semilinear grammar compiler

> Proves that the letter-count image of every context-free language over a finite alphabet is semilinear, using Mathlib's language, grammar and semilinear-set definitions. Proves the converse realization by a regular language and computes exact finite semilinear representations for encoded finite grammars, with component, period, coordinate and bit-budget bounds. Preserves production-labelled derivation trees, bounded decomposition, context activation and word-block automata. The language theorem does not require a finite ambient nonterminal type.

*Quoted from the card [LeanPool/projects/parikh.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/parikh.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Parikh.parikhImage_isSemilinear_of_isContextFree`](https://leanpool.github.io/lean-pool/LeanPool/Parikh/Api.html#Parikh.parikhImage_isSemilinear_of_isContextFree) (theorem; a main declaration), declared in [LeanPool/Parikh/Api.lean, line 70](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh/Api.lean#L70): “For every context-free language over a finite alphabet, its set of letter-count vectors is semilinear in Mathlib's sense.”
- [`Parikh.exists_regularLanguage_with_parikhImage`](https://leanpool.github.io/lean-pool/LeanPool/Parikh/Api.html#Parikh.exists_regularLanguage_with_parikhImage) (theorem), declared in [LeanPool/Parikh/Api.lean, line 90](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh/Api.lean#L90): “Every semilinear set of natural-number vectors indexed by a finite alphabet is exactly the letter-count image of some regular language.”
- [`Parikh.compileGrammar_correct`](https://leanpool.github.io/lean-pool/LeanPool/Parikh/Api.html#Parikh.compileGrammar_correct) (theorem), declared in [LeanPool/Parikh/Api.lean, line 104](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh/Api.lean#L104): “For every encoded finite grammar, the compiled finite representation denotes exactly the letter-count image of its decoded Mathlib grammar language.”
- [`Parikh.compileGrammar_size_bounds`](https://leanpool.github.io/lean-pool/LeanPool/Parikh/Api.html#Parikh.compileGrammar_size_bounds) (theorem), declared in [LeanPool/Parikh/Api.lean, line 108](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh/Api.lean#L108): “The compiled representation satisfies the explicit component-count, period-count, base-norm and period-norm bounds determined by the encoded grammar's size.”
- [`Parikh.compileGrammar_bit_bound`](https://leanpool.github.io/lean-pool/LeanPool/Parikh/Api.html#Parikh.compileGrammar_bit_bound) (theorem), declared in [LeanPool/Parikh/Api.lean, line 112](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh/Api.lean#L112): “The compiled representation's numerical entries satisfy the declared total bit budget, and every base and period coordinate fits its coordinate bit width.”

## Project

- Authors: Umang Mathur.
- Source: *On Context-Free Languages* by Rohit J. Parikh, [doi:10.1145/321356.321364](https://doi.org/10.1145/321356.321364).
- Project repository: [focs-lab/parikh-theorem](https://github.com/focs-lab/parikh-theorem), at commit [9c1cde93](https://github.com/focs-lab/parikh-theorem/tree/9c1cde93f29bbaa91542e401e074ec3cd7646880).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q45, 68Q42, 03D05.
- In Lean Pool: [LeanPool/Parikh](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh), from the card [LeanPool/projects/parikh.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/parikh.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/parikh.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/parikh.yaml)
- [Lean Pool at 307e3125: LeanPool/Parikh](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/Parikh)
